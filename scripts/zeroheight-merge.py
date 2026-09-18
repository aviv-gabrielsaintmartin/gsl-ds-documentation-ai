#!/usr/bin/env python3
"""Merge a regenerated Zeroheight doc into the repo's doc, section by section.

Never a replacement. Measured on `select-card-group`: the two barely compete.
Zeroheight fills the visual sections and has **nothing** for `When to use`,
`When NOT to use` or `Variant Selection Flow`, which somebody wrote here by
hand -- including a decision tree no export could produce.

The rules, in order:

  repo section empty, source has it   -> take the source's, whole
  both have it                        -> keep the repo's words, add the
                                         source's pictures
  only the repo has it                -> leave it alone
  only the source has it              -> add the section

And one rule that overrides all of them: a `zeroheight.com` link never
replaces a repo-relative one. The migration exists to retire those.

    python3 scripts/zeroheight-merge.py <component> <regenerated.md> [--write] [--keep-zh-links] [--base=<doc>] [--place="Name=Target"]

Without --write it writes a `.merged.md` next to the input and changes nothing
in the repo. Read `.claude/skills/zeroheight-merge/SKILL.md` before running it:
the traps it documents were all paid for once already.
"""
import re, shutil, sys
from pathlib import Path

REPO = Path("/Users/gabriel.saintmartin/gsl-ds-documentation-ai")
C = REPO / "components"
HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def split(lines):
    """[(level, title, body lines)] in document order; preamble is title None."""
    out, cur = [], (0, None, [])
    for l in lines:
        m = HEAD.match(l)
        if m:
            out.append(cur)
            cur = (len(m.group(1)), m.group(2).strip(), [])
        else:
            cur[2].append(l)
    out.append(cur)
    return [s for s in out if s[1] is not None or any(x.strip() for x in s[2])]


def trim(b):
    b = list(b)
    while b and not b[0].strip(): b.pop(0)
    while b and not b[-1].strip(): b.pop()
    return b


def empty(body):
    t = "\n".join(body).strip()
    return not t or t.lower().startswith(("not documented", "not applicable"))


def picture_blocks(body):
    """Contiguous runs that are a table holding images, or a bare image.

    The run itself only -- the bold line that names it is carried separately by
    `picture_groups`, because a label belongs to a group of runs, not to one.
    """
    return [b for _, b in picture_groups(body)]


LABEL = re.compile(r"^\*\*[^*]{1,40}\*\*$")


def picture_groups(body):
    """[(label, block)] -- every run, with the bold line that names its group.

    `date-picker` has ten state tables whose columns are all
    `Default | Hover | Pressed | Disabled`; the bold line above is the only
    thing telling them apart, and a group can hold more than one table.

    The label is inherited by every run under it, not just the first. Giving it
    to the first alone was worse than giving it to none: when that first run
    was dropped -- its pictures already on the page -- the run after it kept
    the label above, and a `Day — selected` table ended up standing under
    **Error**, saying something false about the component.
    """
    out, run, label = [], [], None
    for l in body + [""]:
        if l.lstrip().startswith("|") or re.match(r"^!\[[^\]]*\]\(images/", l.strip()):
            run.append(l)
            continue
        if run:
            if any("](images/" in x for x in run):
                out.append((label, trim(run)))
            run = []
        if LABEL.match(l.strip()):
            label = l.strip()
    return out


CELL_IMG = re.compile(r"!\[[^\]]*\]\(images/[^)\s]+\)")
SEP = re.compile(r"^\s*\|[\s|:-]+\|\s*$")


def cell_words(cell):
    """A cell's words, with its picture and its markup taken out."""
    t = CELL_IMG.sub(" ", cell)
    t = re.sub(r"<br\s*/?>", " ", t)
    return re.sub(r"[^a-z0-9]", "", t.lower())


def table_runs(lines):
    """[(start, end)] line ranges of each contiguous table."""
    runs, s = [], None
    for i, l in enumerate(list(lines) + [""]):
        if l.lstrip().startswith("|"):
            if s is None:
                s = i
        elif s is not None:
            runs.append((s, i))
            s = None
    return runs


def fill_cells(body, src):
    """Give the repo's table cells the source's pictures, cell by cell.

    Two faults this repairs, both measured on this batch. A repo cell can hold
    no picture where the source has one -- `button`'s DON'T cell for "Do not
    use a different size", and its DO cell for secondary buttons. And it can
    hold the WRONG one: `date-picker`'s DO cell shows a day-button screenshot,
    `media-upload`'s shows a hover state. Both came in with the old migration.

    A cell is touched only when its words already match the source's, so
    nothing written here is lost. Cells are addressed by row and column index,
    never by the image's name -- `button-card` uses one picture in seven cells,
    and replacing it as text changed all seven at once.
    """
    body = list(body)
    src_tables = [list(src[a:b]) for a, b in table_runs(src)]
    filled = 0
    for a, b in table_runs(body):
        run = body[a:b]
        h = headers(run)
        if not h:
            continue
        match = next((r for r in src_tables if headers(r) == h), None)
        if match is None:
            continue
        rows_b = [i for i in range(a, b) if not SEP.match(body[i])][1:]
        rows_s = [l for l in match if not SEP.match(l)][1:]
        for i, srow in zip(rows_b, rows_s):
            bc = body[i].strip().strip("|").split("|")
            sc = srow.strip().strip("|").split("|")
            if len(bc) != len(sc):
                continue
            touched = False
            for k in range(len(bc)):
                sm = CELL_IMG.search(sc[k])
                if not sm or cell_words(bc[k]) != cell_words(sc[k]):
                    continue
                bm = CELL_IMG.search(bc[k])
                if bm:
                    if bm.group(0) == sm.group(0):
                        continue
                    bc[k] = bc[k][:bm.start()] + sm.group(0) + bc[k][bm.end():]
                else:
                    bc[k] = " " + sm.group(0) + " " + bc[k].strip()
                filled += 1
                touched = True
            if touched:
                body[i] = "| " + " | ".join(c.strip() for c in bc) + " |"
    return body, filled


def images_in(text):
    return set(re.findall(r"\]\(images/([^)\s]+)\)", text))


def headers(block):
    """The column names of the first table in a block, lower-cased."""
    for l in block:
        if l.lstrip().startswith("|"):
            return tuple(c.strip().lower() for c in l.strip().strip("|").split("|"))
    return None


def merge(component, regen_path, write=False, keep_links=False, base=None, place=None):
    # `--base` merges against a doc other than the repo's own. It answers the
    # question a review actually asks -- "what does this look like without that
    # section?" -- without touching `components/`. Cutting a section by hand
    # after the merge is not the same thing: the source withholds any table the
    # repo already had, so a section deleted afterwards takes the source's
    # replacement down with it. `date-picker` would have lost eight pictures.
    place = {k.strip().lower(): v.strip() for k, v in (place or {}).items()}
    doc = Path(base) if base else C / component / f"{component}.md"
    repo_lines = doc.read_text().splitlines()
    new_lines = Path(regen_path).read_text().splitlines()
    # Match headings case-insensitively. Zeroheight titles some pages in lower
    # case -- `dropdown` against the repo's `Dropdown` -- and a case mismatch
    # made the merge treat the H1 as a section the repo did not have, so it
    # appended a second title with the hero under it at the end of the page.
    def hkey(lv, title):
        return (lv, re.sub(r"\s+", " ", title).strip().lower())

    # The migration exists to retire zeroheight.com links -- 43 docs still
    # carry one. A merge that brings more in is working against its own point.
    # The words are kept; only the link around them goes, because this repo has
    # no page to point at instead. `--keep-zh-links` turns it off.
    zh_stripped = 0
    if not keep_links:
        def _unlink(m):
            nonlocal zh_stripped
            zh_stripped += 1
            return m.group(1)
        new_lines = [re.sub(r"\[([^\]]+)\]\(https?://(?:www\.)?zeroheight\.com[^)]*\)",
                            _unlink, l) for l in new_lines]

    repo = split(repo_lines)
    new = {hkey(lv, t): trim(b) for lv, t, b in split(new_lines) if t}

    # A section whose own body is blank but whose sub-sections are full is NOT
    # an empty section. `date-picker` keeps its states under `Date field` and
    # `Date picker`, so the parent read as empty, the source's whole states
    # block was dropped in above them, and eight sentences appeared twice.
    has_child = set()
    for i, (lv, title, _) in enumerate(repo):
        if title is None:
            continue
        for lv2, t2, b2 in repo[i + 1:]:
            if t2 is None:
                continue
            if lv2 <= lv:
                break
            if not empty(trim(b2)):
                has_child.add(hkey(lv, title))
                break

    have = images_in("\n".join(repo_lines))
    out, report = [], []
    used = set()

    for lv, title, body in repo:
        if title is None:
            out += body
            continue
        out.append("#" * lv + " " + title)
        key = hkey(lv, title)
        src = new.get(key)
        used.add(key)
        body_t = trim(body)

        if src is None:
            out += [""] + body_t + [""]
            report.append((title, "kept — the source has no such section"))
            continue
        if empty(body_t) and not empty(src) and key not in has_child:
            out += [""] + src + [""]
            report.append((title, f"taken from the source ({len(images_in(chr(10).join(src)))} images)"))
            continue
        if empty(src):
            out += [""] + body_t + [""]
            report.append((title, "kept — empty in the source"))
            continue

        # Drop a block only when EVERY picture in it is already on the page.
        # Testing "any" threw away whole blocks for one known picture: the
        # date-picker DO/DON'T row was dropped because its DON'T was already
        # here, taking the DO picture with it.
        body_t, n_filled = fill_cells(body_t, src)
        have |= images_in("\n".join(body_t))
        groups = [(lab, p) for lab, p in picture_groups(src)
                  if not images_in("\n".join(p)) <= have]
        pics = [p for _, p in groups]

        # A table whose columns the section already has is a REPLACEMENT, not
        # an addition. `modal-bottom-sheet` ended up with two
        # `| Bottom sheet | Modal |` tables, one under the other.
        existing = {headers(b) for b in picture_blocks(body_t)}
        pics = [p for p in pics if headers(p) not in existing or headers(p) is None]

        # The H1 section holds the page hero. A hero is never added to -- the
        # source replaced the picture, so the existing line is rewritten.
        # Appending put a second hero below the separator, above `## Usage`.
        if lv == 1 and pics:
            new_hero = images_in("\n".join(pics[0]))
            if len(new_hero) == 1:
                name = new_hero.pop()
                swapped = False
                for n, l in enumerate(body_t):
                    if re.match(r"^!\[[^\]]*\]\(images/", l.strip()):
                        body_t[n] = f"![](images/{name})"
                        swapped = True
                        break
                if not swapped:
                    body_t = [f"![](images/{name})", ""] + body_t
                out += [""] + trim(body_t) + [""]
                report.append((title, "page hero replaced by the source's"))
                continue

        if pics:
            # A bare image with no name is superseded by a named table covering
            # the same sub-section. `modal-bottom-sheet` carried three loose
            # pictures under iOS that the new Phone/Tablet table replaces.
            # A loose picture goes only when the caption UNDER it is one of the
            # arriving table's column names -- then it really is the picture
            # that table replaces. Dropping every loose picture the moment any
            # table arrived cost `button` its "Proportion of emphasis" figure,
            # which has a caption of its own and no table to replace it. Same
            # family as the hero: a broad sweep eats a picture nobody replaced.
            cols = {c for p in pics for c in (headers(p) or ())}
            if cols:
                kept, k = [], 0
                while k < len(body_t):
                    s = body_t[k].strip()
                    if re.match(r"^!\[\]\(images/[^)]+\)$", s):
                        j = k + 1
                        while j < len(body_t) and not body_t[j].strip():
                            j += 1
                        cap = body_t[j].strip() if j < len(body_t) else ""
                        # The caption is bold on the page -- `**Date field**`,
                        # never `Date field`. Comparing it with its asterisks
                        # on matched nothing, so date-picker kept three stale
                        # pictures above the table that replaced them. One of
                        # the three was not even an image.
                        cap = cap.strip("*_ ").lower()
                        if cap in cols and len(cap) < 40:
                            k = j + 1                  # the picture and its caption
                            continue
                    kept.append(body_t[k])
                    k += 1
                body_t = kept
            # The label is written once per group, above the first of its runs
            # that survived the filter.
            # One unnamed picture standing for a whole section is that
            # section's picture, and the source's is the current one. Adding
            # it left `date-picker`'s `Header` showing two, the stale one
            # first. Same reasoning as the hero, one level down.
            bare = [b for b in picture_blocks(body_t) if headers(b) is None
                    and len(images_in("\n".join(b))) == 1]
            src_bare = [p for _, p in groups if headers(p) is None
                        and len(images_in("\n".join(p))) == 1]
            if len(bare) == 1 and len(src_bare) == 1 and len(groups) == 1:
                old_i = images_in("\n".join(bare[0])).pop()
                new_i = images_in("\n".join(src_bare[0])).pop()
                body_t = [l.replace(f"(images/{old_i})", f"(images/{new_i})")
                          if l.strip() == f"![](images/{old_i})" else l
                          for l in body_t]
                out += [""] + trim(body_t) + [""]
                report.append((title, "section picture replaced by the source's"
                               + (f", {n_filled} cells re-pictured" if n_filled else "")))
                continue

            merged = trim(body_t) + [""]
            shown = None
            for lab, p in groups:
                if lab and lab != shown:
                    merged += [lab, ""]
                shown = lab
                merged += p + [""]
            out += [""] + trim(merged) + [""]
            n = sum(len(images_in("\n".join(p))) for p in pics)
            report.append((title, f"repo words kept, {n} pictures added"
                                  + (f", {n_filled} cells re-pictured" if n_filled else "")))
        else:
            out += [""] + body_t + [""]
            report.append((title, f"{n_filled} cells re-pictured" if n_filled
                                  else "kept — nothing new in the source"))

    # Sections only the source has go under the heading they sit under THERE.
    # Appending them at the end put `Error` after `Accessibility`, which reads
    # as a new top-level topic rather than a state of the component.
    src_order = split(new_lines)
    last_at = {}
    parent_of = {}
    stack = []
    for lv, title, _ in src_order:
        if title is None:
            continue
        stack = [x for x in stack if x[0] < lv]
        parent_of[hkey(lv, title)] = stack[-1][1] if stack else None
        stack.append((lv, title))

    def prose(body):
        """The section's real sentences -- not headings, images or table rows."""
        out = []
        for l in body:
            s = l.strip()
            if not s or s.startswith(("#", "|", "![")):
                continue
            for part in re.split(r"(?<=[.!?])\s+", s):
                if len(part.strip()) > 40:
                    out.append(re.sub(r"[^a-z0-9]", "", part.lower())[:60])
        return out

    for lv, title, body in src_order:
        if title is None or hkey(lv, title) in used:
            continue

        # The doc may already hold this content under a heading of its own
        # choosing. `modal-bottom-sheet`'s Scrolling was moved into Touch
        # Target & Layout by hand; re-adding the section printed the same
        # paragraph twice. Then only the pictures are wanted, in the section
        # where the words already live.
        # Checking only the first sentence missed four sections whose opening
        # line was an image or a caption. Ask instead how much of the section
        # is already on the page.
        sents = prose(trim(body))
        flat = re.sub(r"[^a-z0-9]", "", "\n".join(out).lower())
        here = [s for s in sents if s in flat]

        # A section that brings pictures the page has never seen is NOT already
        # on the page, whatever its words say. `checkbox`'s three error tables
        # -- twelve pictures -- were thrown away because the one sentence at
        # the foot of the section happened to sit in `Touch Target & Layout`.
        # The page had the sentence. It had none of the error states.
        unseen = [pp for pp in picture_blocks(trim(body))
                  if not images_in("\n".join(pp)) <= have]

        if sents and len(here) >= max(1, len(sents) // 2) and not unseen:
            report.append((title, "skipped — the doc already says this, and "
                                  "the source has no new picture"))
            continue

        # The section is going in. Any paragraph of it the page already carries
        # is dropped on the way, which is what stops the same words being
        # printed twice -- the fault `modal-bottom-sheet`'s Scrolling showed.
        # Sentence by sentence, not line by line. `button`'s repo doc carries
        # the whole of the source's `Read more button` paragraph on one line,
        # reworded in the middle. The line never matched; two of its sentences
        # did, and both were printed twice.
        kept = []
        for l in trim(body):
            s = l.strip()
            if s and not s.startswith(("#", "|", "![")):
                parts = re.split(r"(?<=[.!?])\s+", s)
                flt = [re.sub(r"[^a-z0-9]", "", x.lower()) for x in parts]
                gone = [len(f) > 40 and f in flat for f in flt]
                # Once a sentence on this line has gone as a repeat, the short
                # ones beside it are repeats too. `checkbox` kept "The row
                # height is 48px." on its own, orphaned from the sentence it
                # belonged to, because 18 characters is under the threshold.
                if any(gone):
                    gone = [g or (f and f in flat) for g, f in zip(gone, flt)]
                fresh = [x for x, g in zip(parts, gone) if not g]
                if not fresh:
                    continue
                l = " ".join(fresh)
            kept.append(l)
        # `--place "Name=Target"` overrides where a source-only section lands.
        # The draft script GUESSES this and says so; there was nowhere to write
        # the answer down once a human had checked it. Children follow their
        # parent, because the parent goes in first and they look it up by name.
        placed = place.get(title.strip().lower())
        parent = placed or parent_of.get(hkey(lv, title))
        # A placed section sits one level under the heading it was placed
        # beneath. Keeping the page's own level left `media-upload` with four
        # H3s the template does not define, and `template-drift.py` only ever
        # looks at H2 and H3 -- so the depth is what decides whether a doc
        # reads as on-template or not.
        if placed:
            for l in out:
                m = HEAD.match(l)
                if m and m.group(2).strip().lower() == placed.strip().lower():
                    lv = len(m.group(1)) + 1
                    break
        block = ["#" * lv + " " + title, ""] + trim(kept) + [""]
        at = None
        if parent:
            key_p = parent.lower()
            # After the last section already placed under this parent, not
            # before it. The draft script flattens the page's levels, so a
            # child often shares its parent's level; "the end of the parent's
            # block" then means "just before the sibling I added last", and
            # `date-picker`'s width sections came out back to front.
            if key_p in last_at:
                at = last_at[key_p]
            else:
                for n, l in enumerate(out):
                    m = HEAD.match(l)
                    if m and m.group(2).strip().lower() == key_p:
                        plv = len(m.group(1))
                        at = len(out)
                        for k in range(n + 1, len(out)):
                            m2 = HEAD.match(out[k])
                            if m2 and len(m2.group(1)) <= plv:
                                at = k
                                break
                        break
        if at is None:
            out += block
        else:
            out[at:at] = block
            last_at[parent.lower()] = at + len(block)
        dropped = len(trim(body)) - len(trim(kept))
        report.append((title, f"ADDED under {parent or 'the end'} — only the "
                              f"source has it ({len(images_in(chr(10).join(kept)))} images"
                              + (f", {dropped} repeated lines dropped)" if dropped else ")")))

    # One pass over the finished page: a nameless image sitting directly above
    # a named comparison table is the picture that table replaced. Gabriel
    # spotted three of these under modal-bottom-sheet's iOS heading.
    body_starts = next((n for n, l in enumerate(out) if l.startswith("## ")), 0)
    cleaned, i = [], 0
    while i < len(out):
        line = out[i]
        # The hero lives above the first `##`, directly over the readiness
        # table, and must never be swept up by this.
        if i > body_starts and re.match(r"^!\[\]\(images/[^)]+\)\s*$", line.strip()):
            j = i + 1
            while j < len(out) and not out[j].strip():
                j += 1
            if j + 1 < len(out) and out[j].lstrip().startswith("|") \
                    and re.match(r"^\s*\|[\s|:-]+\|\s*$", out[j + 1]) \
                    and len([c for c in out[j].strip().strip("|").split("|")
                             if c.strip()]) >= 2 \
                    and images_in(line) not in [images_in(x) for x in out[j:j + 3]]:
                i += 1
                continue
        cleaned.append(line)
        i += 1
    out = cleaned

    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    text = re.sub(r"(?m)^---\s*\n\s*\n---\s*$", "---", text)      # a doubled rule
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    if zh_stripped:
        report.append(("(zeroheight.com links)",
                       f"{zh_stripped} stripped from incoming text, words kept"))
    return text, report


if __name__ == "__main__":
    comp, regen = sys.argv[1], sys.argv[2]
    write = "--write" in sys.argv
    base = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--base=")), None)
    place = dict(a.split("=", 1)[1].split("=", 1)
                 for a in sys.argv if a.startswith("--place="))
    text, report = merge(comp, regen, write,
                         keep_links="--keep-zh-links" in sys.argv, base=base, place=place)
    for title, what in report:
        print(f"   {title[:34]:36} {what}")
    src_imgs = images_in(text) - images_in((C / comp / f"{comp}.md").read_text())
    print(f"\n{len(src_imgs)} images to copy in")

    # The check that found the real damage. `checkbox` reported 42 of 42 placed
    # by the draft and still lost 12 in the merge, and nothing said so. Any
    # picture downloaded from the page and missing from the merged doc is
    # either a fault or a decision, and both need a human to see them.
    # A file can be named `.png`, sit where the doc expects it, resolve every
    # link check -- and not be a picture. 36 files across 12 components are
    # Figma node JSON saved under a `.png` name by the old migration, and each
    # renders as a broken image. Nothing in this repo was looking.
    def _is_image(path):
        try:
            head = path.open("rb").read(8)
        except OSError:
            return True
        return (head.startswith((b"\x89PNG", b"\xff\xd8\xff", b"GIF8", b"RIFF"))
                or head.lstrip()[:1] in (b"<",))
    broken = []
    for name in sorted(images_in(text)):
        for folder in (Path(regen).parent / "images", C / comp / "images"):
            f = folder / name
            if f.is_file():
                if not _is_image(f):
                    broken.append(name)
                break
    if broken:
        print(f"\n!! {len(broken)} referenced files are NOT pictures "
              f"(Figma JSON under a .png name):")
        for name in broken:
            print(f"     {name}")

    downloaded = {f.name for f in (Path(regen).parent / "images").iterdir()
                  if f.is_file() and not f.name.startswith(".")}
    unplaced = sorted(downloaded - images_in(text))
    if unplaced:
        print(f"\n!! {len(unplaced)} of {len(downloaded)} source images are NOT in "
              f"the merged doc:")
        for name in unplaced:
            print(f"     {name}")
    else:
        print(f"all {len(downloaded)} source images are in the merged doc")
    out = Path(regen).parent / f"{comp}.merged.md"
    out.write_text(text)
    print("merged draft:", out)
    if write:
        for name in src_imgs:
            src = Path(regen).parent / "images" / name
            if src.exists():
                shutil.copy(src, C / comp / "images" / name)
        (C / comp / f"{comp}.md").write_text(text)
        print("WRITTEN into components/")

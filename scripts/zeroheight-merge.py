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

    python3 scripts/zeroheight-merge.py <component> <regenerated.md> [--write]

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
    """Contiguous runs that are a table holding images, or a bare image."""
    out, run = [], []
    for l in body + [""]:
        if l.lstrip().startswith("|") or re.match(r"^!\[[^\]]*\]\(images/", l.strip()):
            run.append(l)
        else:
            if run and any("](images/" in x for x in run):
                out.append(trim(run))
            run = []
    return out


def images_in(text):
    return set(re.findall(r"\]\(images/([^)\s]+)\)", text))


def headers(block):
    """The column names of the first table in a block, lower-cased."""
    for l in block:
        if l.lstrip().startswith("|"):
            return tuple(c.strip().lower() for c in l.strip().strip("|").split("|"))
    return None


def merge(component, regen_path, write=False):
    doc = C / component / f"{component}.md"
    repo_lines = doc.read_text().splitlines()
    new_lines = Path(regen_path).read_text().splitlines()
    # Match headings case-insensitively. Zeroheight titles some pages in lower
    # case -- `dropdown` against the repo's `Dropdown` -- and a case mismatch
    # made the merge treat the H1 as a section the repo did not have, so it
    # appended a second title with the hero under it at the end of the page.
    def hkey(lv, title):
        return (lv, re.sub(r"\s+", " ", title).strip().lower())

    repo = split(repo_lines)
    new = {hkey(lv, t): trim(b) for lv, t, b in split(new_lines) if t}

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
        if empty(body_t) and not empty(src):
            out += [""] + src + [""]
            report.append((title, f"taken from the source ({len(images_in(chr(10).join(src)))} images)"))
            continue
        if empty(src):
            out += [""] + body_t + [""]
            report.append((title, "kept — empty in the source"))
            continue

        pics = [p for p in picture_blocks(src)
                if not images_in("\n".join(p)) & have]

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
            cols = {c for p in pics for c in (headers(p) or ())}
            if cols:
                kept = []
                for l in body_t:
                    s = l.strip()
                    if re.match(r"^!\[\]\(images/[^)]+\)$", s):
                        continue                       # the table replaces it
                    if s.lower() in cols and len(s) < 40:
                        continue                       # and its caption with it
                    kept.append(l)
                body_t = kept
            merged = trim(body_t) + [""]
            for p in pics:
                merged += p + [""]
            out += [""] + trim(merged) + [""]
            n = sum(len(images_in("\n".join(p))) for p in pics)
            report.append((title, f"repo words kept, {n} pictures added"))
        else:
            out += [""] + body_t + [""]
            report.append((title, "kept — nothing new in the source"))

    # Sections only the source has go under the heading they sit under THERE.
    # Appending them at the end put `Error` after `Accessibility`, which reads
    # as a new top-level topic rather than a state of the component.
    src_order = split(new_lines)
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
        sent = here[0] if here else None
        if sents and len(here) >= max(1, len(sents) // 2):
            # Same rule as above: a table the page already has, under the same
            # column names, is a replacement rather than a second copy.
            on_page = {headers(b) for b in picture_blocks(out)}
            pics = [pp for pp in picture_blocks(trim(body))
                    if not images_in("\n".join(pp)) & have
                    and (headers(pp) is None or headers(pp) not in on_page)]
            at = None
            for n, l in enumerate(out):
                if sent in re.sub(r"[^a-z0-9]", "", l.lower()):
                    at = n + 1
                    while at < len(out) and not HEAD.match(out[at]):
                        at += 1
                    break
            n_img = 0
            if pics and at is not None:
                add = []
                for pp in pics:
                    add += [""] + pp
                    n_img += len(images_in("\n".join(pp)))
                out[at:at] = add + [""]
            report.append((title, f"already in the doc under another heading — "
                                  f"section skipped, {n_img} pictures added there"))
            continue

        block = ["#" * lv + " " + title, ""] + trim(body) + [""]
        parent = parent_of.get(hkey(lv, title))
        at = None
        if parent:
            for n, l in enumerate(out):
                m = HEAD.match(l)
                if m and m.group(2).strip().lower() == parent.lower():
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
        report.append((title, f"ADDED under {parent or 'the end'} — only the "
                              f"source has it ({len(images_in(chr(10).join(body)))} images)"))

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
    return text, report


if __name__ == "__main__":
    comp, regen = sys.argv[1], sys.argv[2]
    write = "--write" in sys.argv
    text, report = merge(comp, regen, write)
    for title, what in report:
        print(f"   {title[:34]:36} {what}")
    src_imgs = images_in(text) - images_in((C / comp / f"{comp}.md").read_text())
    print(f"\n{len(src_imgs)} images to copy in")
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

#!/usr/bin/env python3
"""Turn one extracted Zeroheight page into a draft component doc.

    python3 scripts/zeroheight-draft.py <extract-dir> [--name "Floor selection"]

Reads <extract-dir>/blocks.json (written by scripts/zeroheight-extract.mjs) and
writes <extract-dir>/<slug>.md, laid out against components/component-template.md.

This is a DRAFT. Two things in it are mechanical and can be trusted: no image is
lost, and no source text is dropped. One thing is a guess and is printed as such
at the end: which template section a source heading belongs under. Read that
list before moving the file into components/.

Nothing here writes into components/.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "components" / "component-template.md"

# --- Source heading -> template section -----------------------------------
# Zeroheight pages use their own headings. These are the ones seen so far;
# a heading that is not here is kept verbatim under whatever section it fell
# in, and named in the report so a human can place it.

SECTION_OF = {
    "usage": ("## Usage", None),
    "platform": ("## Usage", "### Platform"),
    "when to use": ("## Usage", "### When to use"),
    "when not to use": ("## Usage", "### When NOT to use"),
    "related components": ("## Usage", "### Related Components"),
    "related component": ("## Usage", "### Related Components"),
    "variants": ("## Variants & Modifiers", None),
    "variants & modifiers": ("## Variants & Modifiers", None),
    "modifiers": ("## Variants & Modifiers", "### Modifiers"),
    "behaviors": ("## Behavior & Responsiveness", None),
    "behaviours": ("## Behavior & Responsiveness", None),
    "behavior": ("## Behavior & Responsiveness", None),
    "states": ("## Behavior & Responsiveness", "### Interactive States & Loading"),
    "interaction": ("## Behavior & Responsiveness", "### Interactive States & Loading"),
    "loading": ("## Behavior & Responsiveness", "### Interactive States & Loading"),
    "width": ("## Behavior & Responsiveness", "### Touch Target & Layout"),
    "height and width": ("## Behavior & Responsiveness", "### Touch Target & Layout"),
    "size": ("## Behavior & Responsiveness", "### Touch Target & Layout"),
    "responsive": ("## Behavior & Responsiveness", "### Breakpoints & Platform Adaptations"),
    "breakpoints": ("## Behavior & Responsiveness", "### Breakpoints & Platform Adaptations"),
    "content": ("## Content & UX Writing", None),
    "content & ux writing": ("## Content & UX Writing", None),
    "accessibility": ("## Accessibility (a11y)", None),
    "accessibility (a11y)": ("## Accessibility (a11y)", None),
    "a11y": ("## Accessibility (a11y)", None),
}

MAX_TABLE_COLUMNS = 5   # a wider table splits silently when published

READINESS = re.compile(r"(Figma|Web|iOS|Android)\s*:\s*([^│|]+)", re.I)


def slugify(name):
    s = re.sub(r"[()]", "", name.lower().strip())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def template_outline():
    """The template's own headings, in order: [(level, title, column or None)]."""
    lines = TEMPLATE.read_text().splitlines()
    out = []
    for i, line in enumerate(lines):
        if re.match(r"^#\s+How to use this template\s*$", line):
            break
        m = re.match(r"^(#{2,6})\s+(.*?)\s*$", line)
        if not m:
            continue
        column = None
        for ahead in lines[i + 1:i + 4]:
            c = re.match(r"^<!--\s*column:\s*(.+?)\s*-->$", ahead.strip())
            if c:
                column = c.group(1)
                break
            if ahead.strip():
                break
        title = m.group(2).strip()
        if title.startswith("["):        # the placeholder section in the template
            continue
        out.append((len(m.group(1)), title, column))
    return out


def md_escape(text):
    return text.replace("|", "\\|")


def image_md(item, alt=""):
    name = item["hash"]
    if not name.endswith(".png"):
        name += ".png"
    return f"![{alt or item.get('name') or ''}](images/{name})"


def split_evenly(items, cap=MAX_TABLE_COLUMNS):
    """Split into chunks of at most `cap`, as evenly as the count allows."""
    if len(items) <= cap:
        return [items]
    chunks = -(-len(items) // cap)          # ceil
    size = -(-len(items) // chunks)
    return [items[i:i + size] for i in range(0, len(items), size)]


def gallery_md(items):
    # One image with no name of its own is just an image. Wrapping it in a
    # single-column table with an empty header reads as a broken table.
    if len(items) == 1 and not (items[0].get("name") or "").strip():
        return [image_md(items[0]), ""]
    out = []
    for chunk in split_evenly(items):
        names = [md_escape(i.get("name") or "") or "&nbsp;" for i in chunk]
        out.append("| " + " | ".join(names) + " |")
        out.append("| " + " | ".join("---" for _ in chunk) + " |")
        out.append("| " + " | ".join(image_md(i) for i in chunk) + " |")
        out.append("")
    return out


def dosdonts_md(items):
    """Matched pairs in one table; unpaired items in their own table, by polarity."""
    def polarity(i):
        label = (i.get("label") or "").lower().replace("’", "'")
        if label.startswith("do n") or label.startswith("don't"):
            return "DON'T"
        if label.startswith("caution"):
            return "CAUTION"
        if label.startswith("do"):
            return "DO"
        return "DO"

    groups = {"DO": [], "DON'T": [], "CAUTION": []}
    for i in items:
        groups[polarity(i)].append(i)

    out, pairs = [], []
    while groups["DO"] and groups["DON'T"]:
        pairs.append((groups["DO"].pop(0), groups["DON'T"].pop(0)))

    if pairs:
        out += ["| DO | DON'T |", "| --- | --- |"]
        for do, dont in pairs:
            dont_img = image_md(dont, "DON'T")
            out.append(
                f"| {image_md(do, 'DO')}<br>**DO:** {md_escape(do['caption'])} "
                f"| {dont_img}<br>**DON'T:** {md_escape(dont['caption'])} |")
        out.append("")

    for kind in ("DO", "DON'T", "CAUTION"):
        left = groups[kind]
        if not left:
            continue
        out += [f"| {kind} |", "| --- |"]
        for i in left:
            out.append(f"| {image_md(i, kind)}<br>**{kind}:** {md_escape(i['caption'])} |")
        out.append("")
    return out


def table_md(rows):
    out = []
    width = max(len(r) for r in rows)
    for n, row in enumerate(rows):
        cells = []
        for c in row:
            text = md_escape(c["text"])
            for link in c.get("links", []):
                if link["text"] and link["text"] in text:
                    text = text.replace(link["text"], f"[{link['text']}]({link['href']})", 1)
            if c.get("image"):
                text = (image_md(c["image"]) + ("<br>" + text if text else "")).strip()
            cells.append(text or " ")
        cells += [" "] * (width - len(cells))
        out.append("| " + " | ".join(cells) + " |")
        if n == 0:
            out.append("| " + " | ".join("---" for _ in range(width)) + " |")
    out.append("")
    return out


def paragraph_md(block):
    text = md_escape(block["text"])
    for link in block.get("links", []):
        if link["text"] and link["text"] in text:
            text = text.replace(link["text"], f"[{link['text']}]({link['href']})", 1)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("extract_dir", type=Path)
    ap.add_argument("--name", help="Component name. Defaults to the page title.")
    args = ap.parse_args()

    data = json.loads((args.extract_dir / "blocks.json").read_text())
    blocks = data["blocks"]
    name = args.name or data["title"].split("·")[0].strip()
    slug = slugify(name)

    # --- the preamble: summary, hero, readiness, links --------------------
    summary, hero, readiness, links = "", None, {}, []
    body_start = 0
    for n, b in enumerate(blocks):
        if b["type"] == "heading":
            body_start = n
            break
        if b["type"] == "paragraph":
            if READINESS.search(b["text"]):
                for key, value in READINESS.findall(b["text"]):
                    readiness[key.lower()] = value.strip().rstrip("│|").strip()
            elif not summary:
                summary = paragraph_md(b)
        elif b["type"] == "image" and hero is None:
            hero = b
        elif b["type"] == "listitem":
            links += b.get("links", [])
        body_start = n + 1

    # --- route every body block to a template section ---------------------
    outline = template_outline()
    buckets = {title: [] for _, title, _ in outline}
    level_of = {title: level for level, title, _ in outline}
    unmapped, current = [], None
    extra_depth = 0

    for b in blocks[body_start:]:
        if b["type"] == "heading":
            key = b["text"].strip().lower()
            if key in SECTION_OF:
                parent, child = SECTION_OF[key]
                target = (child or parent).lstrip("# ").strip()
                current = target if target in buckets else None
                extra_depth = 0
                continue
            # Not a template heading: keep it, one level below its section.
            if not current:
                unmapped.append((b["text"], "— nothing open, dropped to Usage"))
                current = "Usage"
            else:
                unmapped.append((b["text"], current))
            depth = min(level_of.get(current, 3) + 1, 6)
            buckets[current].append(("raw", "#" * depth + " " + b["text"]))
            continue

        if current is None:
            current = "Usage"
        bucket = buckets[current]
        if b["type"] == "paragraph":
            bucket.append(("raw", paragraph_md(b)))
        elif b["type"] == "listitem":
            bucket.append(("raw", f"* {paragraph_md(b)}"))
        elif b["type"] == "image":
            bucket.append(("raw", image_md(b)))
        elif b["type"] == "gallery":
            bucket.append(("lines", gallery_md(b["items"])))
        elif b["type"] == "dosdonts":
            # Zeroheight puts these straight under Usage, with no heading of
            # their own. The template has a section for exactly this.
            target = "Usage Guidance" if current == "Usage" else current
            buckets[target].append(("lines", dosdonts_md(b["items"])))
        elif b["type"] == "table":
            bucket.append(("lines", table_md(b["rows"])))

    # --- write the doc ----------------------------------------------------
    # No source line. Zeroheight is being discontinued, so a comment pointing
    # back at it would outlive the thing it points to.
    doc = [f"# {name}", "", summary or "Not documented", ""]
    if hero:
        doc += [image_md(hero), ""]

    # Figma is not a build status. It says the component exists in a library,
    # and the Figma link below the table is the evidence for that.
    if "figma" not in readiness and any("figma.com" in l["href"] for l in links):
        readiness["figma"] = "Ready ✅"

    cols = ["Figma", "Web", "iOS", "Android"]
    doc += ["| " + " | ".join(cols) + " |",
            "| " + " | ".join("---" for _ in cols) + " |",
            "| " + " | ".join(readiness.get(c.lower(), "Not documented") for c in cols) + " |",
            ""]
    for link in links:
        doc.append(f"* [{link['text']}]({link['href']})")
    if links:
        doc.append("")
    doc += ["---", ""]

    # A parent section whose children carry the content must not say
    # "Not documented" — that reads as a gap, and marks one in the ledger.
    def children_filled(index):
        level = outline[index][0]
        for deeper_level, deeper_title, _ in outline[index + 1:]:
            if deeper_level <= level:
                break
            if buckets[deeper_title]:
                return True
        return False

    for n, (level, title, _) in enumerate(outline):
        content = buckets[title]
        if title == "Platform" and not content:
            continue                       # omitted, never "Not documented"
        doc.append("#" * level + " " + title)
        doc.append("")
        if not content:
            if not children_filled(n):
                doc += ["Not documented", ""]
            continue
        for kind, payload in content:
            if kind == "raw":
                doc += [payload, ""]
            else:
                doc += payload
    text = "\n".join(doc).rstrip() + "\n"

    out_file = args.extract_dir / f"{slug}.md"
    out_file.write_text(text)

    # --- the report -------------------------------------------------------
    on_disk = {p.name for p in (args.extract_dir / "images").glob("*.png")}
    used = set(re.findall(r"images/([A-Za-z0-9_\-]+\.png)", text))
    print(f"wrote {out_file}")
    print(f"images downloaded: {len(on_disk)} | placed in the doc: {len(used)}")
    missing = sorted(on_disk - used)
    if missing:
        print(f"NOT PLACED ({len(missing)}) — every one needs a home before this ships:")
        for m in missing:
            print("   " + m)
    empty = [t for _, t, c in outline if c and not buckets[t]]
    if empty:
        print(f"sections with nothing from the source ({len(empty)}): " + ", ".join(empty))
    if unmapped:
        print(f"headings the source has and the template does not ({len(unmapped)}) — "
              f"guessed placement, check each:")
        for h, where in unmapped:
            print(f"   {h!r} -> {where}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Generate the `references/` folder of the design skill, `skills/design/`.

The design skill is written here and run elsewhere — from the iOS repo, the
Android repo, the web repo or next to Figma. It cannot read this repo, so it
carries a copy of what it chooses from. **This script makes that copy.** Its
`SKILL.md` is written by hand and rarely changes; `references/` is regenerated
whenever the rules change, and never edited by hand.

What it copies:

| Reference | From |
| --- | --- |
| The component, token and icon rulesets | Every `-rules-ai.md` an agent generates from |
| The spec format | `specs/spec-rules-ai.md` |
| What iOS can build | The two iOS name maps |
| Each component's variants | The `## Variants & Modifiers` section of every component doc, extracted into one file |

**Only copying and extracting. Nothing is rewritten for meaning.** Three
mechanical changes, both because the copy leaves the repo:

- A link to a file that is also in `references/` points at the copy.
- Every other link keeps its text and loses its target. Outside this repo the
  target does not exist, and a dead link is worse than none.
- Images are removed. They live in each component's `images/` folder, which is
  not copied.

    python3 scripts/build-design-references.py

Re-run it after changing any file listed in SOURCES, or any component doc's
variants. It deletes and rewrites `skills/design/references/` whole.
"""

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "skills" / "design" / "references"

# Each source, copied under its own filename.
SOURCES = [
    "specs/spec-rules-ai.md",
    "components/components-rules-ai.md",
    "tokens/color/color-rules-ai.md",
    "tokens/typography/typography-rules-ai.md",
    "tokens/spacing/spacing-rules-ai.md",
    "tokens/radius/radius-rules-ai.md",
    "tokens/shadow/shadow-rules-ai.md",
    "tokens/border-width/border-width-rules-ai.md",
    "icons/icons-rules-ai.md",
    "components/components-ios-map.md",
    "tokens/tokens-ios-map.md",
]
VARIANTS_FILE = "component-variants.md"

IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")


def rewrite_links(text: str, copied: set[str]) -> str:
    """Point links at copies when they exist; otherwise keep only the text."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
        if not in_fence:
            line = IMAGE.sub("", line)

            def fix(m: re.Match) -> str:
                label, target = m.group(1), m.group(2)
                name = target.split("#")[0].split("/")[-1]
                if target.startswith("#"):
                    return m.group(0)
                if name in copied:
                    anchor = target[len(target.split("#")[0]):]
                    return f"[{label}]({name}{anchor})"
                return label

            line = LINK.sub(fix, line)
        out.append(line)
    return "\n".join(out) + "\n"


def header(source: str) -> str:
    return (
        f"<!-- Generated from `{source}` on {date.today().isoformat()} by "
        "scripts/build-design-references.py. Never edit here: edit the source "
        "and re-run the script. -->\n\n"
    )


def extract_variants() -> str:
    """One section per component: its H1 title, then its Variants & Modifiers."""
    parts = [
        "# Component variants\n\n"
        "Every component's **Variants & Modifiers** section, extracted from its "
        "own doc. A spec takes variant axes and values from here and nowhere "
        "else. Headings sit one level lower than in the source doc: an axis "
        "that is `###` there is `####` here.\n"
    ]
    for doc in sorted((ROOT / "components").glob("*/*.md")):
        if doc.stem != doc.parent.name:
            continue  # only the component's own doc, never its -figma.md
        text = doc.read_text()
        title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), doc.stem)
        m = re.search(r"^## Variants & Modifiers\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        body = m.group(1).strip() if m else "_This doc has no Variants & Modifiers section._"
        body = re.sub(r"^(#{3,5}) ", lambda h: h.group(1) + "# ", body, flags=re.M)
        parts.append(f"\n## {title}\n\n_From `{doc.relative_to(ROOT)}`._\n\n{body}\n")
    return "".join(parts)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    copied = {Path(s).name for s in SOURCES} | {VARIANTS_FILE}

    for source in SOURCES:
        text = (ROOT / source).read_text()
        (OUT / Path(source).name).write_text(header(source) + rewrite_links(text, copied))

    variants = rewrite_links(extract_variants(), copied)
    (OUT / VARIANTS_FILE).write_text(header("components/*/*.md") + variants)

    print(f"Wrote {len(SOURCES) + 1} files to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()

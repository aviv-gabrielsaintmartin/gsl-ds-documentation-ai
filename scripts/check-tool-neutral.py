#!/usr/bin/env python3
"""Check that no component doc explains a component by naming a tool.

A usage doc describes the component. It is read by agents that build for web,
iOS, Android and Figma, and by people who use none of those. **A tool name
inside the content makes the page a reference for one tool**, which is what
Gabriel ruled against: Figma, Zeroheight and Storybook are all tools, and a doc
may point at them but must not be written in terms of them.

**Confluence is stricter and has no link exemption.** Gabriel, 22 September
2026: it may not appear in a component doc at all. A Confluence link sends the
reader somewhere this repo does not control and most agents cannot open, so the
link is a finding in its own right. The word stays legal only in an `-audit`
file recording where a fact originally came from, and those are not checked here.

    python3 scripts/check-tool-neutral.py

Where a tool name is still allowed, and why:

| Allowed | Why |
| --- | --- |
| A link — `[X on Storybook](https://…)` or a bare URL | Pointing at where a component can be seen is a reference, not content. **Links are removed before the line is judged**, so a tip that happens to carry one is still caught. **Confluence is the exception — see above** |
| The readiness table's own `Figma` column header and its note | The table asks where the component exists. That question is its own task and is out of scope here |

Everything else is a finding: a tip about operating the tool, a layer name, a
note that something is or is not available in one of them, or a statement of
where a fact was read from. Those belong in the registries, in
`components-rules-ai-audit.md`, or in the backlog — never in the page someone reads to
understand the component.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ROOT / "components"

TOOLS = ("figma", "zeroheight", "storybook", "figjam")

# Confluence has no link exemption, so it is matched on the whole line rather
# than on what survives link-stripping. The host is checked too, because a bare
# attachment URL never spells the word out.
BANNED_ANYWHERE = {
    "confluence": re.compile(r"confluence|atlassian\.net", re.I),
}

# The readiness table is a separate question, with its own task. Its header row
# and the template's note explaining the Figma column are left alone.
READINESS_HEADER = re.compile(r"^\|\s*Figma\s*\|\s*Web\s*\|", re.I)
READINESS_NOTE = "Figma answers a different question"

MD_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
BARE_URL = re.compile(r"https?://\S+")


def outside_links(line: str) -> str:
    """The line with every link removed, text and address alike.

    A line can be a link **and** prose — `**Figma tip:** … [Common Picto](url)`
    is both. Treating any line that contains a URL as a link let those through,
    so the links come out first and whatever is left is judged on its own.
    """
    return BARE_URL.sub(" ", MD_LINK.sub(" ", line))


def findings(path: Path) -> list[tuple[int, str, str]]:
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        if READINESS_HEADER.match(line.strip()) or READINESS_NOTE in line:
            continue
        banned = [t for t, rx in BANNED_ANYWHERE.items() if rx.search(line)]
        if banned:
            out.append((i, banned[0], line.strip()))
            continue
        rest = outside_links(line).lower()
        named = [t for t in TOOLS if t in rest]
        if named:
            out.append((i, named[0], line.strip()))
    return out


def main() -> int:
    docs = sorted(p for p in COMPONENTS.glob("*/*.md")
                  if p.stem == p.parent.name or p.parent.name == "charts")
    hits = {p: f for p in docs if (f := findings(p))}

    total = sum(len(f) for f in hits.values())
    print(f"Checked {len(docs)} component docs for tool names in their content.\n")
    if not hits:
        print("No component doc explains itself in terms of a tool. Clean.")
        return 0

    print(f"Docs naming a tool outside a link: {len(hits)} — {total} lines\n")
    for path, found in hits.items():
        print(f"  {path.relative_to(ROOT)}  ({len(found)})")
        for line_no, tool, text in found:
            print(f"      {line_no}: [{tool}] {text[:120]}")
        print()
    print("A tool name belongs in a link, or in the registries, the audit or the")
    print("backlog. Not in the page someone reads to understand the component.")
    print("Confluence has no link exemption: remove it, do not move it into a link.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

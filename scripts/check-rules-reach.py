#!/usr/bin/env python3
"""Check that every selectable component is named by at least one rule.

`components-rules-ai.md` holds two things: the rules an agent follows, and an
inventory of all 98 entries in the four Figma libraries. A component can sit in
that inventory and be named by no rule at all. When it is, **no agent can ever
select it** -- not because it disobeyed, but because nothing routes there. The
eval cannot see this: it tests the rules that exist, never the ones missing.

This asks one question of one file, against itself:

    for every inventory entry not marked never-select,
    does any rule above the inventory name it?

    python3 scripts/check-rules-reach.py

**What counts as named.** Anywhere in the rules section -- a `Choose` row, an
`Otherwise` branch, a tier table, a prose ruling. All of those are routes an
agent can follow. Whether a component also deserves its own `Choose` row is a
different and weaker question, and `check-rules-docs.py` already reports it.

**What this does NOT check.** Whether the inventory itself is complete. If a
component exists in Figma and nobody added it to the inventory, it is invisible
here -- the file agrees with itself perfectly while missing a component. That
question belongs to `components/coverage.py`, which reads the four registries.

**What this does NOT check, second.** Whether the rule that names a component is
any good. A component named once in a parenthetical passes this check. Only the
eval asks whether a rule is reachable *in practice*.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / "components" / "components-rules-ai.md"

INVENTORY_HEADING = re.compile(r"^##\s+The inventory\s*$")
INVENTORY_ROW = re.compile(r"^\|\s*`([^`]+)`([^|]*)\|([^|]*)\|([^|]*)\|\s*$")
NEVER_SELECT = "\U0001f6ab"

# Registry spelling -> the spelling the rules use. Only where normalising cannot
# bridge the two. Source: components-rules-ai-audit.md, "Five docs cover a
# registry entry under a different name".
ALIASES = {
    "coachmark": "coach mark",
}


def norm(name: str) -> str:
    """Fold the spellings that mean one component: case, plurals, punctuation.

    A parenthetical is kept, deliberately. `Navigation Bar (App)` and
    `Navigation bar` are two components in two libraries, and folding them would
    let a rule for one vouch for the other. That exact fault was found in
    `check-rules-docs.py` on 21 September 2026.
    """
    n = name.strip().strip("`*_ ").lower()
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    if n.endswith("s") and not n.endswith("ss"):   # Feedback Messages / message
        n = n[:-1]
    return ALIASES.get(n, n)


def split_file(path: Path) -> tuple[str, list[str]]:
    """The rules text, and the inventory's lines."""
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if INVENTORY_HEADING.match(line):
            return "\n".join(lines[:i]), lines[i:]
    raise SystemExit(f"No '## The inventory' heading in {path}")


def inventory(lines: list[str], path: Path) -> list[tuple[str, bool]]:
    """Every inventory entry: (name, may an agent select it)."""
    out: list[tuple[str, bool]] = []
    for line in lines:
        m = INVENTORY_ROW.match(line)
        if m:
            name, _, purpose, _doc = m.groups()
            out.append((name.strip(), NEVER_SELECT not in purpose))
    if not out:
        raise SystemExit(f"No inventory rows found in {path}")
    return out


# A component name is short and never spans a line. Both caps matter: without
# them an unpaired `**` in prose pairs with the next one three paragraphs down
# and the span swallows the text between, which produced 71 false holes on the
# first run of this script.
SPAN = re.compile(r"\*\*([^*\n]{1,70})\*\*|`([^`\n]{1,70})`")


def candidates(span: str) -> set[str]:
    """The component names one bold or backtick span could be naming.

    The house style bolds a name, but a span often carries more than one --
    `**On web -> Pop-up**`, `**Button**, tertiary`, `**Action menu** on desktop,
    **Modal bottom sheet menu** on mobile`. Each shape is trimmed back rather
    than guessed at, and every trimming is kept, so a name is found whichever
    shape it was written in.
    """
    out = {span}
    out.add(span.split("→")[-1])          # after the last arrow
    out |= set(span.split("·"))           # middot-separated alternatives
    out.add(span.split(",")[0])                # `Button`, tertiary
    out.add(re.sub(r"\s*\(.*?\)\s*", " ", span))   # qualifier in brackets
    return {n for n in (norm(s) for s in out) if n}


def named_in_rules(text: str) -> set[str]:
    """Every component name the rules section mentions, however it mentions it."""
    out: set[str] = set()
    for m in SPAN.finditer(text):
        out |= candidates(m.group(1) or m.group(2))
    return out


def main(argv: list[str]) -> int:
    # A path argument exists so this check can be run against a deliberately
    # broken copy. A check nobody has seen fail is not a check.
    path = Path(argv[1]).resolve() if len(argv) > 1 else RULES
    rules_text, inventory_lines = split_file(path)
    named = named_in_rules(rules_text)
    entries = inventory(inventory_lines, path)

    selectable = [n for n, may_select in entries if may_select]
    unreachable = [n for n in selectable if norm(n) not in named]
    # Two names sit in two libraries each; report the name once.
    unreachable = sorted(dict.fromkeys(unreachable))

    try:
        shown = path.relative_to(ROOT)
    except ValueError:
        shown = path
    print(f"Checked {len(entries)} inventory entries against {shown}'s rules.")
    print(f"  {len(selectable)} an agent may select · "
          f"{len(entries) - len(selectable)} never-select, not checked")
    print()

    if not unreachable:
        print("Every selectable component is named by at least one rule. Clean.")
        return 0

    print(f"Selectable components no rule names: {len(unreachable)}")
    for name in unreachable:
        print(f"  - `{name}`  — in the inventory, reachable by no rule, "
              f"so no agent can select it")
    print()
    print("Each one is a hole in the ruleset, not a mistake an agent can make.")
    print("Either write a rule that routes to it, or mark it never-select with")
    print("the reason, which is a decision for Gabriel and not for this script.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

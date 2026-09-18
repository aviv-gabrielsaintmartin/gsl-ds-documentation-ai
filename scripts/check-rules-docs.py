#!/usr/bin/env python3
"""Check that each component doc and the ruleset name the same alternatives.

The doc is where a sentence is written; `components-rules-ai.md` is where the
decision is made. Both state, for one component, what to use *instead* — the doc
in its `When NOT to use` table, the ruleset in its row's `Otherwise` cell. When
those two sets disagree, one of them is sending an agent somewhere the other does
not, and nothing else in this repo notices.

This compares the two as sets of component names. It never compares prose: the
doc is meant to rephrase. Run it after editing either side.

    python3 scripts/check-rules-docs.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / "components" / "components-rules-ai.md"
COMPONENTS = ROOT / "components"

# Names that appear as alternatives but are not components, so a doc is not
# wrong for omitting them.
NOT_A_COMPONENT = {"which component", "highest tier first", "when nothing fits",
                   "platform limits", "never select", "where a chart's legend sit"}


def norm(name: str) -> str:
    """Fold the spellings that mean one component: case, plurals, punctuation."""
    n = name.strip().strip("`*_ ").lower()
    n = re.sub(r"\s*\(.*?\)\s*", " ", n)          # "Button group (single-select)"
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    if n.endswith("s") and not n.endswith("ss"):   # Feedback Messages / message
        n = n[:-1]
    return n


def bolded(cell: str) -> set[str]:
    """Component names in a cell, which the house style always bolds.

    A bold span sometimes carries more than the name — `**On web → Pop-up**`, or
    `**Button**, tertiary`. The name is what follows the last arrow. A span saying
    something is deliberately *not* a component is not a name at all.
    """
    out = set()
    for m in re.finditer(r"\*\*([^*]+)\*\*", cell):
        raw = m.group(1).split("\u2192")[-1]
        if "not a component" in raw.lower():
            continue
        n = norm(raw)
        if n and n not in {norm(x) for x in NOT_A_COMPONENT}:
            out.add(n)
    return out


def rule_rows() -> dict[str, set[str]]:
    """Every Choose row in the ruleset: component -> what it sends you to instead."""
    text = RULES.read_text(encoding="utf-8")
    text = text[: text.index("## The inventory")]
    rows: dict[str, set[str]] = {}
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[1] in ("---", "When"):
            continue
        chosen = bolded(cells[0])
        if len(chosen) != 1:
            continue
        rows[next(iter(chosen))] = bolded(cells[2])
    return rows


def doc_alternatives(path: Path) -> tuple[set[str] | None, str | None]:
    """A doc's `When NOT to use` targets, or a reason it could not be read."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^### When NOT to use\s*$(.*?)^###", text, re.M | re.S)
    if not m:
        return None, "no `When NOT to use` section"
    body = m.group(1).strip()
    if body.lower().startswith("not documented"):
        return None, "`When NOT to use` says Not documented"
    targets: set[str] = set()
    saw_table = False
    for line in body.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 2 or cells[1] in ("---", "Use"):
            continue
        saw_table = True
        targets |= bolded(cells[1])
    if not saw_table:
        return None, "`When NOT to use` is not the two-column table the template asks for"
    return targets, None


def main() -> int:
    rules = rule_rows()
    rules_text = RULES.read_text(encoding="utf-8")
    named_anywhere = {norm(m.group(1)) for m in
                      re.finditer(r"[`*]{1,2}([A-Z][^`*|]{2,40})[`*]{1,2}",
                                  rules_text[: rules_text.index("## The inventory")])}
    docs = sorted(p for p in COMPONENTS.glob("*/*.md") if p.stem == p.parent.name
                  or p.parent.name == "charts")

    disagreements: list[str] = []
    unreadable: list[str] = []
    no_rule: list[str] = []
    no_choose_row: list[str] = []

    for path in docs:
        rel = path.relative_to(ROOT)
        m = re.search(r"^### When to use\s*$\s*\*\*([^*]+)\*\*", path.read_text(encoding="utf-8"), re.M)
        name = norm(m.group(1)) if m else norm(path.stem.replace("-", " "))
        if name not in rules:
            if name in named_anywhere:
                no_choose_row.append(f"{rel}  — reachable, but no Choose row, so alternatives cannot be compared")
            else:
                no_rule.append(f"{rel}  — doc names itself '{name}', and no rule names it at all")
            continue
        targets, why = doc_alternatives(path)
        if targets is None:
            unreadable.append(f"{rel}  — {why}")
            continue
        only_doc = targets - rules[name]
        only_rules = rules[name] - targets
        if only_doc or only_rules:
            parts = []
            if only_doc:
                parts.append("doc sends you to " + ", ".join(sorted(only_doc)) + " and the ruleset does not")
            if only_rules:
                parts.append("ruleset sends you to " + ", ".join(sorted(only_rules)) + " and the doc does not")
            disagreements.append(f"{rel}\n      " + "\n      ".join(parts))

    print(f"Checked {len(docs)} component docs against {len(rules)} ruleset rows.\n")
    for title, items in (("Disagreements — one side sends an agent where the other does not", disagreements),
                         ("Docs whose `When NOT to use` could not be compared", unreadable),
                         ("Docs reachable but with no Choose row — not a fault, just not comparable", no_choose_row),
                         ("Docs no rule names at all", no_rule)):
        if items:
            print(f"{title}: {len(items)}")
            for i in items:
                print(f"  - {i}")
            print()
    if not (disagreements or unreadable or no_rule):
        print("Every doc and its ruleset row name the same alternatives. Clean.")
    return 1 if disagreements else 0


if __name__ == "__main__":
    sys.exit(main())

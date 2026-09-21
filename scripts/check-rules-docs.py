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

**One thing it still cannot do**, and it will show up as a disagreement rather
than hide: a qualifier written *inside* a bold span becomes part of the name.
`**Navigation Bar (App), mobile only**` reads as a component called "navigation
bar mobile only". Write the qualifier outside the asterisks —
`**Navigation Bar (App)** — mobile only` — and it compares correctly. Not
tested against every doc; found once, in `navigation-bar.md`, 21 September 2026.
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
    """Fold the spellings that mean one component: case, plurals, punctuation.

    **A parenthetical is kept.** It used to be stripped, which folded
    `Navigation Bar (App)` into `Navigation bar` — two components in two
    libraries, sharing one key. The second row overwrote the first and this file
    then compared a doc against the wrong row and printed a false line.
    `bare()` and `resolve()` below put the stripping back where it belongs:
    applied only when the parenthetical is a qualifier rather than part of a
    name. Fixed 21 September 2026.
    """
    n = name.strip().strip("`*_ ").lower()
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    if n.endswith("s") and not n.endswith("ss"):   # Feedback Messages / message
        n = n[:-1]
    return n


def bare(raw: str) -> str:
    """Normalise with any parenthetical dropped first.

    Takes the **raw** text, not a normalised name: `norm()` turns brackets into
    spaces, so by then there is nothing left to strip.
    """
    return norm(re.sub(r"\s*\(.*?\)\s*", " ", raw))


def resolve(raw: str, known: set[str]) -> str:
    """Pick the form that names a real component.

    Two different things wear brackets in this repo, and only one of them is a
    qualifier:

    | Written | Means |
    | --- | --- |
    | `Navigation Bar (App)` | A component whose name includes "(App)" |
    | `Button group (multi-select)` | `Button group`, used one particular way |

    Nothing distinguishes them by spelling, so this asks the ruleset instead: if
    the full form is a Choose row, it is a name and is kept. If it is not, the
    brackets were a qualifier and are dropped. When neither form is known, the
    stripped form is returned — both sides of a comparison then fold the same
    way, so a doc and its rule row still agree with each other.
    """
    full = norm(raw)
    if full in known:
        return full
    return bare(raw)


def resolve_all(raws: set[str], known: set[str]) -> set[str]:
    return {resolve(r, known) for r in raws}


def bolded(cell: str) -> set[str]:
    """Component names in a cell, which the house style always bolds.

    A bold span sometimes carries more than the name — `**On web → Pop-up**`, or
    `**Button**, tertiary`. The name is what follows the last arrow. A span saying
    something is deliberately *not* a component is not a name at all.

    **Returns raw text, not normalised names.** `resolve()` needs the brackets
    intact to tell a name from a qualifier, so every caller norms or resolves
    for itself.
    """
    out = set()
    for m in re.finditer(r"\*\*([^*]+)\*\*", cell):
        raw = m.group(1).split("\u2192")[-1]
        if "not a component" in raw.lower():
            continue
        if norm(raw) and norm(raw) not in {norm(x) for x in NOT_A_COMPONENT}:
            out.add(raw.strip())
    return out


def rule_rows() -> dict[str, set[str]]:
    """Every Choose row in the ruleset: component -> what it sends you to instead."""
    text = RULES.read_text(encoding="utf-8")
    text = text[: text.index("## The inventory")]
    raw: dict[str, set[str]] = {}
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[1] in ("---", "When"):
            continue
        chosen = bolded(cells[0])
        if len(chosen) != 1:
            continue
        raw[norm(next(iter(chosen)))] = bolded(cells[2])
    # A row's own name in column one is the canonical spelling, so those are the
    # known names every Otherwise cell is resolved against.
    known = set(raw)
    return {name: resolve_all(alts, known) for name, alts in raw.items()}


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
        name = resolve(name, set(rules))
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
        targets = resolve_all(targets, set(rules))
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

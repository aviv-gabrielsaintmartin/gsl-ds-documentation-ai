#!/usr/bin/env python3
"""Check the Figma column of every component doc's readiness table.

Every component doc opens with a `| Figma | Web | iOS | Android |` table. It is
the one place availability lives -- Gabriel's decision of 24 September 2026 --
and until this script nothing read a single cell of it. `template-drift.py`
asks only whether the table exists.

This reads the **Figma cell only**, against the four Figma registries:

    python3 scripts/check-readiness-figma.py
    python3 scripts/check-readiness-figma.py path/to/components   # a broken copy

**What Ready means here.** Gabriel's definition, 24 September 2026. A Figma cell
may say Ready only when both hold:

  1. the component has an entry in one of the four `figma/*-registry.json`, and
  2. that entry is not flagged outdated, in progress, or unverified.

**Every disagreement fails, in both directions:**

  - the cell says Ready and no registry holds the component;
  - the cell says Ready and the entry is flagged -- **for Gabriel to rule**,
    never for this script to decide;
  - a registry holds the component, unflagged, and the cell says anything
    other than Ready. A link or a note where the status should be counts here:
    an agent reading the cell cannot tell it means Ready.

**What this does NOT check.** That a registry entry is still current. The
registries are written by the `figma-sync-*` skills and are only as fresh as
their last run. A component deleted from Figma since then passes here. Nor does
it read the Web, iOS or Android cells -- those need the web code and the app
monorepo, and are separate work.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ROOT / "components"

# The registry reading lives in coverage.py -- tiers, aliases, the name-to-doc
# rule. Imported, never copied, so the two cannot disagree about which doc a
# registry entry belongs to.
_spec = importlib.util.spec_from_file_location("coverage", COMPONENTS / "coverage.py")
coverage = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(coverage)

# Registry entries that exist but may not be called Ready. **Listed by hand, on
# purpose.** The registry `status` field is free prose, and a keyword search over
# it is wrong: `Map template` and both `mapPinsV2` sets contain the word
# OUTDATED only because they name the excluded `(❌ OUTDATED) mapPins` set.
# Each reason is quoted from that entry's own `status`. Add an entry here when a
# `figma-sync-*` run flags one; remove it when a live re-read clears it.
FLAGGED = {
    ("Tab Bar", "Components"):
        "in progress — lives inside a 'Refacto' section, "
        "'likely an in-progress refactor'",
    ("Brand Logo", "Components"):
        "unverified — 'key is last-known, not live-confirmed'",
    ("Image Ratio", "Components"):
        "unverified — 'key is last-known, not live-confirmed'",
}

TABLE_HEADER = re.compile(r"^\|\s*Figma\s*\|\s*Web\s*\|\s*iOS\s*\|\s*Android\s*\|")
READY = re.compile(r"^Ready\b")


def figma_cell(doc: Path) -> str | None:
    """The first cell of the readiness table's value row, or None if no table."""
    lines = doc.read_text().splitlines()
    for i, line in enumerate(lines):
        if TABLE_HEADER.match(line) and i + 2 < len(lines):
            cells = lines[i + 2].split("|")
            return cells[1].strip() if len(cells) > 1 else ""
    return None


def main(argv: list[str]) -> int:
    base = Path(argv[1]).resolve() if len(argv) > 1 else COMPONENTS

    # Which registry entries each doc covers. `Image Ratio` and `Brand Logo` sit
    # in two libraries, so a doc can hold more than one entry.
    entries_for: dict[Path, list[tuple[str, str]]] = {}
    for name, tier in coverage.load_registry_entries():
        rel = coverage.find_doc(name)
        if rel:
            entries_for.setdefault(base / rel, []).append((name, tier))

    docs = sorted(p for p in base.rglob("*.md") if figma_cell(p) is not None)
    # The template carries the table as a blank to fill; it describes no component.
    docs = [p for p in docs if p.name != "component-template.md"]

    wrong, to_rule, clean = [], [], 0
    for doc in docs:
        cell = figma_cell(doc)
        says_ready = bool(READY.match(cell))
        entries = entries_for.get(doc, [])
        flags = [(e, FLAGGED[e]) for e in entries if e in FLAGGED]
        shown = doc.relative_to(base)

        if says_ready and not entries:
            wrong.append((shown, cell, "no Figma registry holds this component"))
        elif says_ready and flags:
            for (name, tier), why in flags:
                to_rule.append((shown, cell, f"`{name}` ({tier}) is flagged: {why}"))
        elif not says_ready and entries and not flags:
            held = ", ".join(f"`{n}` ({t})" for n, t in entries)
            wrong.append((shown, cell, f"the registry holds {held}, unflagged"))
        else:
            clean += 1

    print(f"Checked the Figma cell of {len(docs)} readiness tables "
          f"against the four Figma registries.")
    print(f"  {clean} agree · {len(wrong)} disagree · {len(to_rule)} for Gabriel to rule")
    print()

    if not wrong and not to_rule:
        print("Every Figma cell agrees with the registries. Clean.")
        return 0

    if wrong:
        print(f"Cells that disagree with the registries: {len(wrong)}")
        for shown, cell, why in wrong:
            print(f"  - {shown}  says '{cell}'  — {why}")
        print()
    if to_rule:
        print(f"Cells that say Ready on a flagged registry entry: {len(to_rule)}")
        for shown, cell, why in to_rule:
            print(f"  - {shown}  says '{cell}'  — {why}")
        print()

    print("Fix the cell, or fix the registry with a figma-sync-* run. Which one")
    print("is wrong is a judgement this script cannot make.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

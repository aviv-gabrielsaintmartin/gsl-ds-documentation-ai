# Compliance run ledger

_Append-only. **Written by the checking agent — never edit by hand.** One row per
run, scored against [compliance-scorecard.md](compliance-scorecard.md)._

_Always name a check in full — `C4 · Authorisation`, never bare `C4`._

This is the **comparison table**. Open it to see whether output is getting
better across runs without opening a single report. Open a report only when a
row looks wrong.

## Why this is not in the scorecard

The scorecard is the ruler; this is a record of what was measured. A ruler gets
rewritten whenever a rule or a threshold changes, and rewriting a file that also
holds what happened on a date reaches back and edits history. Separating them is
what lets the rules change while the evidence stays fixed — the same split as
`-rules-ai` against `-ledger` everywhere else in this repo.

## How it is used

1. Every run appends one row. **Nothing is ever rewritten or removed** — except
   the quality verdict, which is written later by Gabriel and only ever filled
   in, never changed.
2. **Record every run, including bad ones.** A log holding only good runs is a
   highlight reel, not evidence.
3. `no regression` for `C1 · Provenance` compares against **the last run with
   the same wireframe label**, and no other. Comparing a search results page
   against a form measures the difficulty of the brief, not the compliance of
   the output.
4. Full detail for any row is in that run's folder — `runs/run-NNN/`, holding
   the brief, the screenshots, the facts and the report.

## What each column means

| Column | Meaning |
| --- | --- |
| Run | Its three-digit number. Never reused, never renumbered |
| Date | When it was scored |
| Platform | Which platform produced the output — `figma`, `web`, `ios`, `android` |
| Wireframe | The comparability label. **Two runs are comparable only when this matches** |
| The five checks | Percentage, `—` where a threshold is pass/fail rather than a score, or `unavailable` where the adapter could not supply the facts. **Never `0%` for a missing fact** |
| Hard fails | How many, across all checks. A count here of anything but zero outranks every percentage in the row |
| Quality | Gabriel's one-line verdict. **Never scored.** The full wording lives in the run's report |

`C6 · Layout` has no column — it is inactive until the layout rules are verified
against real screens.

## Runs

| Run | Date | Platform | Wireframe | C1 · Prov | C2 · Tier | C3 · Token | C4 · Auth | C5 · Decl | Hard fails | Quality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | _no runs scored yet_ | — | — | — | — | — | — | — | — |

**`run-001` exists and has never been scored.** Its brief and screenshots are in
`runs/run-001/`; it has no `facts.json` and no `report.md`, because the report
had nowhere to live when it was run. It is the reason this file exists.

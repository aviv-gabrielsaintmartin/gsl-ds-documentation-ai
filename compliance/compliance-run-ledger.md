# Compliance run ledger

_Append-only. **Written by the checking agent — never edit by hand.** One row per
run, judged against [compliance-scorecard.md](compliance-scorecard.md)._

_The scorecard's questions have no codes and its steps have no numbers. A column
is named after the design step it covers, shortened only as far as the table
forces._

This is the **comparison table**. Open it to see whether output is getting
better across runs without opening a single report. Open a report only when a
row looks wrong.

## Why this is not in the scorecard

The scorecard is the ruler; this is a record of what was measured. A ruler gets
rewritten whenever a rule or a question changes, and rewriting a file that also
holds what happened on a date reaches back and edits history. Separating them is
what lets the rules change while the evidence stays fixed — the same split as
`-rules-ai` against `-ledger` everywhere else in this repo.

## How it is used

1. Every run appends one row. **Nothing is ever rewritten or removed** — except
   the quality verdict, which is written later by Gabriel and only ever filled
   in, never changed.
2. **Record every run, including bad ones.** A log holding only good runs is a
   highlight reel, not evidence.
3. **Read down one wireframe label, never across the table.** Two runs are
   comparable only when that label matches. Comparing a search results page
   against a form measures the difficulty of the brief, not the compliance of
   the output. **Nothing is gated on it** — no question in the scorecard
   compares a run against a previous one.
4. Full detail for any row is in that run's folder — `runs/run-NNN/`, holding
   the brief, the screenshots, the facts and the report.

## What each column means

| Column | Meaning |
| --- | --- |
| Run | Its three-digit number. Never reused, never renumbered |
| Date | When it was scored |
| Platform | Which platform produced the output — `figma`, `web`, `ios`, `android` |
| Wireframe | The comparability label. **Two runs are comparable only when this matches** |
| The three step columns | How many of that step's questions were answered `yes`. `ok` where none were, or `unavailable` where the adapter could not supply the facts. **Never `ok` for a missing fact** |
| Flags | How many flags the run raised. A flag is a finding, never a failure |
| Quality | Gabriel's one-line verdict. **Never scored.** The full wording lives in the run's report |

**Define the content, put them on the screen and check the content have no
column** — they have no question yet. **Place them according to the design
guidance has none** either: it is inactive until the layout rules are verified
against real screens. All four keep a row in the run's own report, so the gap
stays visible where it matters.

## Runs

| Run | Date | Platform | Wireframe | Components | What to build | Tokens | Flags | Quality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | _no runs judged yet_ | — | — | — | — | — | — |

**`run-001` exists and has never been scored.** Its brief and screenshots are in
`runs/run-001/`; it has no `facts.json` and no `report.md`, because the report
had nowhere to live when it was run. It is the reason this file exists.

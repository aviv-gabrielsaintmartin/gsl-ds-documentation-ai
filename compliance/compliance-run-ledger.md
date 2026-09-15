# Compliance run ledger

_Append-only. **Written by the checking agent — never edit by hand.** One row per
run, judged against [compliance-scorecard.md](compliance-scorecard.md)._

**This is history, not measurement.** The scorecard is the measurement. This file
exists so Gabriel can see whether output is improving across runs without opening
a single report. Open a report only when a row looks wrong.

_Recast 15 September 2026. The per-step columns were dropped and replaced by
**Failures · Findings · Flags**. **No measurement changed** — every number here
was already in the run's own report. The old columns mirrored the scorecard's
steps, so every scorecard edit made them wrong. These three are the scorecard's
three kinds of verdict, which do not change when a question does. The original
columns are in git history._

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
3. **Two runs are comparable only when they sit in the same brief folder.**
   Comparing a search results page against a form measures the difficulty of the
   brief, not the compliance of the output. **Nothing is gated on it** — no
   question in the scorecard compares a run against a previous one.
4. Full detail for any row is in that run's folder —
   `briefs/brief-NNN/run-NNN/`, holding the screenshots and the report. The
   brief itself is one level up, written once and shared by every run under it.

## What each column means

| Column | Meaning |
| --- | --- |
| Run | Its three-digit number. **Global across every brief**, never reused, never renumbered |
| Date | When it was scored |
| Platform | Which platform produced the output — `figma`, `web`, `ios`, `android` |
| Brief | The brief folder this run sits in. **Rows sharing a value ran the same brief and are comparable** |
| **Failures** | How many failing questions were answered `yes`, out of how many could fail. **This is the compliance verdict** — read it first |
| Findings | How many questions the scorecard labels a finding rather than a failure were answered `yes`. A finding is not a fault |
| Flags | How many flags the run raised — restricted or unprecedented use that a person has to look at. **Never a failure** |
| Quality | Gabriel's one-line verdict. **Never scored, and not part of the compliance measure.** The full wording lives in the run's report |

**A question nobody could answer counts in neither Failures nor Findings.** The
scorecard answers it `unavailable`, and the run's report says which one and why.
Never read a low Failures count as a clean screen without checking the report for
`unavailable`.

**Which step a failure came from is not a column.** It changes every time the
scorecard changes, and the run's report already says it. Four of the scorecard's
seven steps have no question at all, and their rows in each report keep that gap
visible where it matters.

## Runs

| Run | Date | Platform | Brief | Failures | Findings | Flags | Quality |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 002 | 14 Sep 2026 | figma | `brief-001` | **2 of 7** | 1 | 3 |  |
| 003 | 14 Sep 2026 | figma | `brief-001` | **0 of 7** | 1 | 2 |  |

**`run-001` exists and has never been scored.** Its screenshots are in
`briefs/brief-001/run-001/`; it has no report, because the report had nowhere to
live when it was run. It is the reason this file exists.

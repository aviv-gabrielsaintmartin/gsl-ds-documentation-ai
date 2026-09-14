# Compliance flag ledger

_Append-only. **Written by the checking agent — never edit by hand.** Flags
raised by [compliance-scorecard.md](compliance-scorecard.md), accumulated across
every run._

_The scorecard's questions have no codes and its steps have no numbers. Name the
design step a flag came from — `Choose the tokens`._

**Every item a person must rule on lands here — failures included, not only
flags.** One item is noise; the same item three times is evidence a ruleset is
missing a case.

## How it is used

1. Every run appends its flags here. Nothing is ever rewritten or removed.
2. **A subject seen three times is raised for a human decision** — never
   auto-promoted, never auto-dismissed. Gabriel rules on it.
3. **A ruling of `ruleset gap` does not file itself.** Gabriel decides, per
   item, whether it is fixed on the spot or becomes a backlog task. Some gaps
   close in one sentence, and a backlog round-trip costs more than the fix.
   Revised by him 14 Sep 2026, after the first scored run produced eight items.
4. **Either way it lands in `project/backlog.md`** — as a task if it is filed, as
   a row in the *Done* table if it is fixed on the spot. One destination, which
   is what the 11 Sep 2026 rule was protecting: two destinations meant two
   sessions filed the same finding in different files.
5. Doing the work writes the rule into the ruleset and the reasoning into the
   relevant `-audit.md` — `color-usage-audit.md`, `spacing-usage-audit.md`,
   `typography-usage-audit.md` or `components-audit.md`. **The audit is where
   reasoning settles, never the queue.**

| Verdict | Meaning |
| --- | --- |
| `awaiting decision` | Raised for Gabriel. Blocks nothing; accumulates until ruled on |
| `agent error` | The rulesets did cover it. The generating agent got it wrong |
| `ruleset gap` | The rulesets did not cover this case. Fix the ruleset |
| `library defect` | **The Figma library is wrong.** Not the agent, not the documentation. No doc change fixes it; it needs a library edit |
| `accepted` | Legitimate as used. No change needed |

## Flags

| Run | Step | Subject | Why raised | Times seen | Verdict |
| --- | --- | --- | --- | --- | --- |
| 002 | Choose the tokens | `Scales/Energy/Green100`, `Green200`, `Green400`, `Yellow100`, `Orange100`, `Red100`, `Red200` — 7 cells at `133:5097` | **Restricted.** Used exactly as colour's **Energy and CO2 scales** describes, including white letters on A and G only. Restricted tokens are flagged, never failed | 1 | `awaiting decision` |
| 002 | Choose the tokens | `Scales/CO2/Blue100`–`Blue700` — 7 cells at `134:5090` | **Restricted.** Used in the stated order, lowest to highest emission. The ruleset records the CO₂ ordering as never verified against code, so a live use of it is worth a human's eye | 1 | `awaiting decision` |
| 002 | Choose the tokens | `Color/Content/Constant/White/Default` on CO₂ steps D, E, F, G at `134:5090` | **Unprecedented.** The colour ruleset prescribes letter colour on the energy ladder and says nothing about the CO₂ ladder. The token exists and is not denied. The choice may be revealing a gap in the ruleset rather than an error | 1 | `awaiting decision` |


**Run 002's rows predate the rule above them.** They were written on 14 September
2026, when only flags landed here and failures did not. Its three failures and
its two uncovered findings are in
[report-run-002.md](runs/run-002/report-run-002.md) under *Decisions you need to
make* — eight items, not three. **The rows are not corrected**: this file records
what was measured on a date, and the rule changed after. Every run from 003 on
carries every item needing a ruling.
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
| 003 | Choose the tokens | `Scales/Energy/Green100`, `Green200`, `Green400`, `Yellow100`, `Orange100`, `Red100`, `Red200` — 7 cells at `152:22601` | **Restricted.** Used exactly as colour's **Energy and CO2 scales** describes, including white letters on A and G only. Restricted tokens are flagged, never failed. Run 002 ruled the identical use `accepted` | 2 | `awaiting decision` |
| 003 | Choose the tokens | `Scales/CO2/Blue100`–`Blue700` — 7 cells at `152:22657`, plus the grade callout at `152:22646` | **Restricted.** Used in the stated order, lowest to highest emission, with the letter colours the CO₂ rule prescribes. The ruleset still records the CO₂ ordering as never verified against code. Run 002 ruled the identical use `accepted` | 2 | `awaiting decision` |
| 003 | Choose the tokens | `Donut chart`'s internal `.Legend` `Alignment` set to `Vertical` at `I152:23189;2782:13323` | **Not covered.** `components-rules-ai.md` says the chart has no alignment property and not to look for one. One exists on the internal `.Legend` and was used. The sentence may mean placement beside the chart rather than how the legend's rows stack | 1 | `awaiting decision` |
| 003 | Define the components to use | Parts hidden inside the `Donut chart` instance at `152:23189` — two arcs, two legend rows, the centre total, the header subtitle, and one arc's sweep reshaped | **Not covered.** The chart exposes two booleans, `KPI` and `Legend`. The internals' own properties and direct node edits went past them, to show three data points instead of five. No styled property was changed, so no scorecard question fails it | 1 | `awaiting decision` |
| 003 | Define what needs to be built | The page frame `152:22144` and the two section stacks `152:22145`, `152:22146` carry no declaration | **Not covered.** The declaring rule says a layout container holding declared content is declared inside that content's own declaration. Each of these holds content from several declarations at once, so it fits inside none. Judged page structure and passed | 1 | `awaiting decision` |


**Run 002's rows predate the rule above them.** They were written on 14 September
2026, when only flags landed here and failures did not. Its three failures and
its two uncovered findings are in
[report-run-002.md](runs/run-002/report-run-002.md) under *Decisions you need to
make* — eight items, not three. **The rows are not corrected**: this file records
what was measured on a date, and the rule changed after. Every run from 003 on
carries every item needing a ruling.
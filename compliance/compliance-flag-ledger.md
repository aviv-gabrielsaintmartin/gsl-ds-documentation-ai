# Compliance flag ledger

_Append-only. **Written by the checking agent — never edit by hand.** Flags
raised by [compliance-scorecard.md](compliance-scorecard.md), accumulated across
every run._

_The scorecard's questions have no codes and its steps have no numbers. Name the
design step a flag came from — `Choose the tokens`._

A flag is a finding, not a failure. One flag is noise; the same flag three times
is evidence a ruleset is missing a case.

## How it is used

1. Every run appends its flags here. Nothing is ever rewritten or removed.
2. **A subject seen three times is raised for a human decision** — never
   auto-promoted, never auto-dismissed. Gabriel rules on it.
3. **If the ruling is `ruleset gap`, it becomes a task in
   [the backlog](../project/backlog.md) first.** Doing that task writes the rule
   into the ruleset and the reasoning into the relevant `-audit.md` —
   `color-usage-audit.md`, `spacing-usage-audit.md`, `typography-usage-audit.md`
   or `components-audit.md`. Decided by Gabriel, 11 Sep 2026.

| Verdict | Meaning |
| --- | --- |
| `awaiting decision` | Raised for Gabriel. Blocks nothing; accumulates until ruled on |
| `ruleset gap` | The rulesets did not cover this case. Fix the ruleset |
| `agent error` | The rulesets did cover it. The generating agent got it wrong |
| `accepted` | Legitimate as used. No change needed |

## Flags

| Run | Step | Subject | Why flagged | Times seen | Verdict |
| --- | --- | --- | --- | --- | --- |
| 002 | Choose the tokens | `Scales/Energy/Green100`, `Green200`, `Green400`, `Yellow100`, `Orange100`, `Red100`, `Red200` — 7 cells at `133:5097` | **Restricted.** Used exactly as colour's **Energy and CO2 scales** describes, including white letters on A and G only. Restricted tokens are flagged, never failed | 1 | `awaiting decision` |
| 002 | Choose the tokens | `Scales/CO2/Blue100`–`Blue700` — 7 cells at `134:5090` | **Restricted.** Used in the stated order, lowest to highest emission. The ruleset records the CO₂ ordering as never verified against code, so a live use of it is worth a human's eye | 1 | `awaiting decision` |
| 002 | Choose the tokens | `Color/Content/Constant/White/Default` on CO₂ steps D, E, F, G at `134:5090` | **Unprecedented.** The colour ruleset prescribes letter colour on the energy ladder and says nothing about the CO₂ ladder. The token exists and is not denied. The choice may be revealing a gap in the ruleset rather than an error | 1 | `awaiting decision` |

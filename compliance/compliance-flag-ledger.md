# Compliance flag ledger

_Append-only. **Written by the checking agent — never edit by hand.** Flags
raised by [compliance-scorecard.md](compliance-scorecard.md), accumulated across
every run._

_Always name a check in full — `C4 · Authorisation`, never bare `C4`._

A flag is a finding, not a failure. One flag is noise; the same flag three times
is evidence a ruleset is missing a case.

## How it is used

1. Every run appends its flags here. Nothing is ever rewritten or removed.
2. **A subject seen three times is raised for a human decision** — never
   auto-promoted, never auto-dismissed. Gabriel rules on it.
3. If the ruling is `ruleset gap`, it becomes an entry in the relevant
   `-audit.md` — `color-usage-audit.md`, `spacing-usage-audit.md`,
   `typography-usage-audit.md` or `components-audit.md`.

| Verdict | Meaning |
| --- | --- |
| `awaiting decision` | Raised for Gabriel. Blocks nothing; accumulates until ruled on |
| `ruleset gap` | The rulesets did not cover this case. Fix the ruleset |
| `agent error` | The rulesets did cover it. The generating agent got it wrong |
| `accepted` | Legitimate as used. No change needed |

## Flags

| Run | Check — number **and** name | Subject | Why flagged | Times seen | Verdict |
| --- | --- | --- | --- | --- | --- |
| — | — | _no runs yet_ | — | — | — |

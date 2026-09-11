---
paths:
  - "compliance/**"
---

# Compliance docs

How generated output is judged against the design system. Same
`-scorecard` / `-audit` / `-ledger` split the other pillars use.

| File | Role |
| --- | --- |
| `compliance-scorecard.md` | **The checks.** What is measured, what fails outright, the thresholds, and the report format. Read by a **checking** agent |
| `compliance-audit.md` | The evidence — why these checks, what was rejected, open questions. **Never read as rules** |
| `compliance-run-ledger.md` | Append-only, one row per run. The comparison table. **Written by the checking agent — never edit by hand** |
| `compliance-flag-ledger.md` | Append-only findings across runs. **Written by the checking agent — never edit by hand** |
| `runs/run-NNN/` | One folder per run: the brief, screenshots, `facts.json`, `report.md`. All four required |

## The ruler is not the measurements

`compliance-scorecard.md` is rewritten whenever a rule or a threshold changes.
The two ledgers and the run folders record what happened on a date and are
**never** rewritten. Never move a growing log back into the scorecard: editing
the rules would then reach back and edit history, and a file read before every
run would grow by a line every time a screen is generated.

## This pillar is platform-neutral

**The scorecard defines the concept and what to measure. It never defines how a
tool measures it.** No API names, no node identifiers, no framework vocabulary.
If a check cannot be stated without naming a tool, it is not yet a design-system
rule and does not belong here.

How each platform measures is an **adapter**, and adapters live in the consuming
agent's repo — one for Figma, later one each for web, iOS and Android. What this
repo owns is the *adapter contract*: the list of facts a platform must report,
stated in design-system vocabulary.

A check whose facts a platform cannot supply reports `unavailable` — never `0%`.
A zero reads as "the output failed"; the truth is that the adapter has a gap.

## Always write a check's number **and** name

`C1 · Provenance`, never bare `C1`. Six two-character codes are not memorable,
and a report using them cannot be followed by anyone who did not write it. This
holds in the scorecard, in every report, in the ledger, in audit entries, and in
conversation.

## The rule that governs this pillar

**Every check must name the rule it enforces.** A check traceable to no rule in
`components-rules-ai.md` or one of the three token rulesets does not belong in
the scorecard — delete it rather than justify it.

**The scorecard is never stricter than the ruleset it enforces.** Typography
Typography's **The eleven used styles** says *prefer* these eleven, not *only* these — so a twelfth style
is a flag, never a failure. If a gap is found this way it is a **ruleset defect**
and gets fixed in the ruleset, not worked around here.

**Never score against unverified rules.** `C6 · Layout` is defined and switched off
because spacing's **Container padding** and **Page rhythm** mark themselves unverified. A number
with no evidence under it is worse than an acknowledged gap.

## Two things not to confuse

- **`-eval` judges a ruleset. `-scorecard` judges output.** `components-eval.md`
  asks whether an agent reading the ruleset reaches the right answer. The
  scorecard asks whether a produced screen is compliant.
- **Compliance is not quality.** Compliance is arithmetic and is scored here.
  Quality is judgment, is not scored, and is recorded as a free-text human
  verdict — in full in the run's own `report.md`, in one line in
  `compliance-run-ledger.md`. Never add a quality check to the scorecard.

## When you run a check

- **A run is unfinished until its report exists.** Write it to
  `runs/run-NNN/report.md` — in this repo, never inside the Figma file or the
  prototype it judges. Keep `facts.json` too: it is what lets a later scorecard
  change be re-tested against an old run.
- Record **every** run in `compliance-run-ledger.md`, including bad ones. A log
  holding only good runs is a highlight reel, not evidence.
- Append flags to the flag ledger; never rewrite or remove one.
- A flagged subject seen **three times** is promoted to a ruleset defect, with an
  entry in the relevant `-audit.md`.

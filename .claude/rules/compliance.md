---
paths:
  - "compliance/**"
---

# Compliance docs

How generated output is judged against the design system. Same
`-scorecard` / `-audit` / `-ledger` split the other pillars use.

| File | Role |
| --- | --- |
| `compliance-scorecard.md` | **The questions.** What is asked, grouped by the design step each question guards, what a `yes` means, and the report format. Read by a **checking** agent |
| `compliance-scorecard-audit.md` | The evidence — why these questions, what was rejected, open questions. **Never read as rules** |
| `compliance-run-ledger.md` | Append-only, one row per run. The comparison table. **Written by the checking agent — never edit by hand** |
| `compliance-flag-ledger.md` | Append-only findings across runs. **Written by the checking agent — never edit by hand** |
| `briefs/brief-NNN/` | One folder per brief: `brief-NNN.md`, written once, plus every run of it. **Two runs are comparable only when they share this folder.** A changed requirement starts a new brief folder, never an edit to an existing one |
| `briefs/brief-NNN/run-NNN/` | One folder per run: screenshots and `report-run-NNN.md`, both required. **Run numbers are global across every brief**, never reused. Screenshots keep their descriptive names |

## The ruler is not the measurements

`compliance-scorecard.md` is rewritten whenever a rule or a question changes.
The two ledgers and the run folders record what happened on a date and are
**never** rewritten. Never move a growing log back into the scorecard: editing
the rules would then reach back and edit history, and a file read before every
run would grow by a line every time a screen is generated.

**One thing may be added to a run report after the fact: the ruling.** A report
is written with its ruling column empty, because the verdicts come from Gabriel
later. Filling that column is not rewriting history — it is the third author
finishing the record, and it happens **once**. Everything else in the file is
fixed the day it is written: the answers, the evidence, the declarations, the
date. **This exception is the run report's alone.** The two ledgers are never
touched, including to add a ruling.

## This pillar is platform-neutral

**The scorecard defines the concept and what to measure. It never defines how a
tool measures it.** No API names, no node identifiers, no framework vocabulary.
If a check cannot be stated without naming a tool, it is not yet a design-system
rule and does not belong here.

**The agent answering them is not platform-neutral.** It reads the output
directly — on Figma, the file the generating agent drew in. A second platform
needs a second scoring agent; the questions, the report format and the ledgers
stay as they are.

**There is no translation step and no stored facts file.** One was designed and
removed by Gabriel on 14 September 2026 as too advanced for the end-of-September
deadline. Do not reintroduce it without a deliberate decision — the cost it
buys back is being able to re-run a changed question against an old screen.

A question the scoring agent cannot answer reports `unavailable` — never `no`. A
`no` reads as "the output was clean"; the truth is that nobody could see.

**The scoring agent is never the generating agent.** It starts fresh, never sees
the generating conversation, and never asks the generating agent anything. A
generating agent knows every question in the scorecard, so anything it hands the
scorer it can shape without ever stating a falsehood.

## The questions have no codes, and never get any

They are questions, grouped into one section per step of designing a screen.
Refer to one by quoting it, or by naming its step — `Choose the tokens`.

The six checks this replaced were called `C1`–`C6`, and keeping them legible cost
a standing instruction to write the name beside every number, in the scorecard,
in every report, in both ledgers and in conversation. Removed by Gabriel,
12 September 2026. **Do not reintroduce numbering**: the step a question sits
under is what a reader needs, and it is already in its heading.

## Every question is binary

Phrased so that the compliant answer is `no`. **No percentages and no
thresholds** — every threshold this pillar ever carried was `100%` or `zero`,
which is a yes/no question wearing a percent sign. Counts belong in the reason
column, never in the verdict.

**Nothing compares a run against a previous run.** `no regression` was dropped on
12 September 2026: it answered whether this run beat the last one, which is a
question about the project rather than about the design system, and it was the
only judgment here that could not be made from a single run. The trend lives in
the run ledger, read down one brief folder.

## The rule that governs this pillar

**Every question must name the rule it enforces.** A question traceable to no
rule in `components-rules-ai.md` or one of the token rulesets does not belong in
the scorecard — delete it rather than justify it.

**The scorecard is never stricter than the ruleset it enforces.** Typography
Typography's **The eleven used styles** says *prefer* these eleven, not *only* these — so a twelfth style
is a flag, never a failure. If a gap is found this way it is a **ruleset defect**
and gets fixed in the ruleset, not worked around here.

**Never judge against unverified rules.** *Place them according to the design
guidance* is defined and switched off because spacing's **Container padding** and
**Page rhythm** mark themselves unverified. A verdict with no
evidence under it is worse than an acknowledged gap.

**A step with no question says so.** Define the content, put them on the screen
and check the content have nothing checking them. Each keeps a
section in the scorecard and a row in every report stating that. An absent step
reads as an oversight; a step that states its own emptiness reads as a known gap.

## Two things not to confuse

- **`-eval` judges a ruleset. `-scorecard` judges output.** `components-rules-ai-eval.md`
  asks whether an agent reading the ruleset reaches the right answer. The
  scorecard asks whether a produced screen is compliant. **The difference
  underneath is the answer key** — an eval's expected answers are written down,
  so two runs compare; a scorecard judges a screen that has never existed, so it
  produces a report and not a score you can trend.
- **The scorecard keeps its own name, and its audit carries the scorecard's.**
  `compliance-scorecard-audit.md` explains `compliance-scorecard.md`. The
  scorecard is not renamed to `-eval`: no file in this repo is its target, and
  it has no answer key. The naming rule is in `README.md`.
- **Compliance is not quality.** Compliance is arithmetic and is judged here.
  Quality is judgment, is not judged here, and is recorded as a free-text human
  verdict — in full in the run's own `report-run-NNN.md`, in one line in
  `compliance-run-ledger.md`. Never add a quality question to the scorecard.

## When you run a check

- **A run is unfinished until its report exists.** Write it to
  `briefs/brief-NNN/run-NNN/report-run-NNN.md` — in this repo, never inside the Figma file
  or the prototype it judges. **Write down what you found, above the answers** —
  the report is the only record of what the screen contained.
- **The report's `## Declarations` section is not yours to write.** The
  generating agent writes it before scoring; a checking agent reads it and
  answers *was anything hand-built without a complete declaration?* Never edit
  it, never add one on the agent's behalf — a declaration written after the
  verdict is not a declaration.
- Record **every** run in `compliance-run-ledger.md`, including bad ones. A log
  holding only good runs is a highlight reel, not evidence.
- Append flags to the flag ledger; never rewrite or remove one.
- A flagged subject seen **three times** is promoted to a ruleset defect, with an
  entry in the relevant `-audit.md`.

# Brief 01 — The compliance scorecard

| | |
| --- | --- |
| **Status** | Approved 2026-09-08, in progress |
| **Branch** | `docs/compliance-scorecard` |
| **Written** | 2026-09-08 |
| **Depends on** | Nothing |
| **Blocks** | **Block 4 · Figma agent** — it has no target until this exists |

---

## What this block is

**A written definition of what "design-system compliant" means, precise enough
that a machine can score it.** Not the checker itself — the definition the
checker will implement.

Two files, a new pillar:

| File | What it is |
| --- | --- |
| `compliance/compliance-scorecard.md` | The checks, how each is measured, what fails outright, and how a run is scored |
| `compliance/compliance-audit.md` | Why these checks and not others, what was rejected, what's still open |

## Why now, and not after the agent exists

Compliance was step 5 of the original plan, after building the agent. That order
is wrong: an agent built before the scorecard has nothing to aim at, and its
first output gets judged by eye — which is exactly the human bottleneck this
project exists to remove.

There is also a proven pattern to copy. `components-eval.md` scored the
component ruleset by giving a cold agent only that ruleset and marking its
answers. It worked so well that a **perfect 22/22 still surfaced four real
defects**, because the agent was also asked where it struggled. The scorecard is
the same idea pointed at generated output instead of at a ruleset.

The reason this can be automated at all: **compliance is arithmetic and quality
is judgment.** "Is every fill bound to an authorised token?" has one right
answer. "Does this feel like SeLoger?" does not. Separating them is what lets
the compliance gate run unattended while the quality bar stays yours.

## The proposed design

### Five checks

| ID | Check | What it measures | Mechanism |
| --- | --- | --- | --- |
| **C1** | **Provenance** | Is each element a real library component, or hand-drawn? | Every instance's `mainComponent.key` must appear in one of the four `figma/*-registry.json` files. Score = library instances ÷ (library instances + hand-built equivalents) |
| **C2** | **Tier ceiling** | Was a higher-tier component reinvented from lower-tier parts? | **Highest tier first**'s ten rows, using the ruleset's own *count the parts* test: a local frame reproducing **two or more** of a higher-tier component's moving parts is a violation |
| **C3** | **Token binding** | Are values bound to tokens, or hardcoded? | Every fill, stroke, corner radius, gap and text style must carry a bound variable or style. Score = bound ÷ total |
| **C4** | **Authorisation** | Are the bound tokens *allowed*, or merely *existing*? | Token names checked against the deny-lists in the three token rulesets |
| **C5** | **Declaration** | When something new was invented, was it declared? | **When nothing fits** requires stating what was built, which problem it belongs under, and which components were ruled out and why |

**C4 · Authorisation is the check the token audits paid for.** 83 of 218 colour tokens have no
consumer, `Spacing/56` has no documented purpose, and no component binds a
Display type style. Without `C4 · Authorisation`, output can be 100% "token-bound" and still be
built on values the audits rejected.

### Two kinds of failure

This distinction is the heart of the design, and it needs your agreement.

| Kind | Meaning | Effect on the score |
| --- | --- | --- |
| **Hard fail — a gate** | Something the system explicitly forbids. A `Status Bar` placed in a screen. A deny-listed token. A hand-built `Listing Card` | **Gate. Not a deduction.** The run does not pass, whatever the percentages say |
| **Deduction** | Something with no precedent, but not forbidden | Lowers the score, run can still pass |

A raw hex is a hard fail. A token that exists, isn't deny-listed, but sits
outside the "eleven styles components actually use" is a deduction — the
rulesets say *prefer these*, not *only these*, and the scorecard must not invent
a stricter rule than the ruleset it enforces.

### A sixth check, defined but switched off

**C6 · Layout.** Page composition: outer margin, section rhythm, container
padding and grid alignment per viewport tier.

Defined now, **inactive until Block 3 · Layout**. The rules exist —
spacing's **Container padding** and **Page rhythm** already cover it per
tier — but they carry an explicit warning that they are **unverified**, because
page composition lives outside the component library and could not be checked.
Scoring against unverified rules would manufacture false confidence.

## What deliberately does not change

- **No checker is built.** This block produces a specification. The runner comes
  in **Block 4 · Figma agent**, alongside the agent — you cannot debug a checker with no output to
  run it against.
- **Quality is not scored.** Not now, not by this scorecard. Every run logs your
  quality verdict alongside its compliance score, so the quality bar can later
  be written from a corpus of real judgments rather than from scratch.
- **No ruleset is edited.** The scorecard enforces the rulesets as they stand.
  If a check turns out to be unenforceable, that is a defect in the ruleset and
  gets fixed there — not worked around here.
- **No new rules are invented.** Every check traces to an existing rule. A check
  with no rule behind it is out of scope by definition.

## A naming decision I need you to confirm

The repo's grammar defines `-eval.md` as **the check on a ruleset**. This file
checks **generated output** — a different subject. Calling it
`compliance-eval.md` would blur the one distinction the grammar exists to make.

**Proposal: a sixth suffix, `-scorecard.md`** — how *output* is judged, as
against `-eval.md`, how a *ruleset* is judged. `README.md` gains the row.

The alternative is to widen `-eval` to mean "any check", accepting that its
subject varies. Cheaper, and slightly less clear.

## How we'll know it worked

| Test | Passes if |
| --- | --- |
| **The cold-agent test** | An agent given only `compliance-scorecard.md` and one generated frame produces a score, and a second agent independently produces the same score |
| **The traceability test** | Every check names the specific rule it enforces. A check with no rule behind it is out |
| **The no-false-precision test** | Nothing is scored that rests on unverified rules — which is why `C6 · Layout` ships switched off |
| **The gate test** | A screen containing a `Status Bar` fails, no matter how well it scores elsewhere |

The first is the real one. Two agents disagreeing on the same frame means the
scorecard is prose, not a specification.

## Open questions for you

Answered by Gabriel, 2026-09-08. Where his answer differed from the
recommendation, his reasoning is recorded — in two cases it was the better one.

| # | Question | Decided | Note |
| --- | --- | --- | --- |
| 1 | Does one hard fail sink the whole run, or just its own check? | **Its own check.** Extend to run-level once we know the checker works | Recommendation was run-level. His is right for a first version: a run-level gate on an unproven checker throws away a whole run's data on one false positive, and data is what we need. Mitigated by report order — hard fails print above any percentage |
| 2 | Unprecedented-but-allowed tokens — fail or flag? | **Flag, and treat the flags as findings.** "It can help us identify potential usage, then act on it" | A better reason than the one recommended. Flags therefore **accumulate into a ledger** rather than being per-run noise. Repeated reaches for the same unauthorised token are evidence a ruleset is missing a case |
| 3 | Is `C2 · Tier ceiling` reliably machine-detectable, or a heuristic? | **Machine-detectable.** New or hand-built components must be flagged | Correct, but not from the registry: `Listing Card`'s `exposedSubComponents` are private internal slots (`.listing_price_tag`), not the public components someone would reinvent it from — and only 5 of 11 Experiences record them at all. So C2 needs a **parts column on Highest tier first's ten rows**, and uses C5 as the tiebreaker for false positives |
| 4 | A passing threshold now, or report only? | **Implement now, refine after** | Refined: thresholds are **derived from the rules**, never invented. `C3 = 100%` because "never write a pixel literal" says so; `C4 = 0 deny-listed` because the *Never use* tables say so. Where no rule states a number, the threshold is **no regression** against the previous run |

## Corrected during the build

Two things were wrong in the brief above and were fixed before the block shipped.
Recorded here rather than silently edited, because the brief is a record.

| What the brief assumed | What was decided |
| --- | --- |
| The scorecard could describe how output is inspected | **It cannot.** Describing the mechanism made it a Figma checker specification in a platform-neutral repo. The scorecard now defines the concept and what to measure; an **adapter contract** lists the facts a platform must report, and each platform's adapter lives in the consuming agent's repo |
| Checks could be referred to by number | **They cannot.** Six two-character codes are not memorable. Always `C1 · Provenance`, never bare `C1` — in documents, reports, ledgers and conversation |
| Listing the facts an adapter must report was enough | **It was not.** The contract was agreeable but not implementable — nothing said what an adapter *is*, what shape the facts arrive in, or what a check concludes from them. Added: the pipeline, a who-owns-what split, a JSON example, and a worked example of two elements scored end to end |

The first correction also resolved two of the six open questions: **Highest tier first**'s parts
list is platform-neutral so it stays in the ruleset, and the checker is a *how*
so it lives with its tool.

## Risks

| Risk | Mitigation |
| --- | --- |
| **The scorecard becomes stricter than the rulesets**, and the agent gets blamed for following the documentation correctly | The traceability test: every check names its rule. A check nobody can trace gets deleted |
| **False precision.** A tidy 87% implying more rigour than the evidence supports | `C6 · Layout` ships inactive. Every check states what it cannot see |
| **It measures what is easy rather than what matters.** `C3 · Token binding` is trivial to check; `C2 · Tier ceiling` is where real compliance failures live | C2 is defined even though it needs a human confirm, rather than dropped for being awkward |
| **Scoring drifts once real runs start** and old scores stop being comparable | The scorecard carries a run log, like the eval. A scoring change is a dated entry, not a silent edit |

## Cost

Roughly a day for both files. The recurring cost is honesty: every future run
has to be recorded even when the score is bad, or the log becomes a highlight
reel and stops being evidence.

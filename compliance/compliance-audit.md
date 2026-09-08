# Compliance scorecard audit

_The evidence behind [compliance-scorecard.md](compliance-scorecard.md): why
these six checks, what was rejected, and what is still unresolved. **Never read
as rules.**_

---

## Method

The scorecard was not designed from first principles. Every check was derived by
working backwards from a rule that already exists in this repo, and any candidate
check that could not be traced to one was dropped.

That constraint did most of the design work. It is also the scorecard's own
stated test: *every check names the rule it enforces; a check with no rule behind
it does not belong here.*

The three source rulesets and their enforceable sections:

| Ruleset | Sections a checker can act on |
| --- | --- |
| `components/components-rules-ai.md` | Rule 0 tier order · Rule 3 never-select list · Rule 4 inventory · Rule 5 declaration |
| `tokens/color/color-rules-ai.md` | Rule 1 no raw colour · *Never use* (7 rows + 28 enumerated) · *Restricted* (3 cases) |
| `tokens/spacing/spacing-rules-ai.md` | Rule 0 never override component padding · Rule 1 no pixel literal · *Do not use* (7 tokens) |
| `tokens/typography/typography-rules-ai.md` | Rule 1 no hand-set font properties · Rule 3 the eleven used styles · Rule 5 no Display |

## Why the scorecard is platform-neutral, and the checkers are not

**Decided 2026-09-08 by Gabriel**, correcting the first draft.

The first version collapsed three layers into one. Its measurement rows named
Figma's plugin API directly — reading a component key, reading a bound variable,
printing a Figma node ID in the report. That made the document a Figma checker
specification, in a repo whose stated purpose is to hold **one platform-neutral
truth** that several agents consume.

The three layers, separated:

| Layer | Content | Where |
| --- | --- | --- |
| The concept | What compliance means, the six checks, hard fail vs deduction vs flag, thresholds | this repo |
| What to measure | In design-system vocabulary | this repo |
| **How** to measure it | Figma reads component keys; web reads package imports; iOS reads its view hierarchy | **the consuming agent repo, one adapter per platform** |

The mechanism is the **adapter contract**: the scorecard lists the *facts* a
platform must report, and the checks operate on the facts. A data requirement is
platform-neutral; an API call is not.

Two consequences that improved the design rather than merely relocating it:

- **It forced neutral vocabulary.** "Every element reported as a library
  component must name a component in the inventory" is a better statement of the
  rule than "read the component key", because it is true on every platform and
  names the design-system concept rather than the mechanism.
- **It exposed that platforms answer different questions.** Figma can say "this
  is an instance of a library component"; web says "this is an import from the
  design-system package". So the contract separates **required** from
  **optional** facts, and a check whose facts a platform cannot supply reports
  `unavailable`, never `0%`. A missing fact is a gap in the adapter, not a
  failure in the output.

**Cost.** The scorecard can no longer be executed by reading it — it needs an
adapter before it does anything. That is the correct trade: an unexecutable
neutral spec plus one adapter beats an executable spec that only works for one
tool.

## Why the adapter mechanism is specified, not just contracted

**Raised 2026-09-08 by Gabriel:** *"Adapter — how exactly does that work? Is
everything documented?"*

It was not. The first version of the platform split listed **which facts** an
adapter must report and stopped there. Five things were missing, and together
they made the contract agreeable but not implementable:

| Missing | Why it mattered |
| --- | --- |
| What an adapter physically is | Nothing said whether it was a script, a skill or a prompt, or that it contains no rules |
| The shape of the data | Facts were written in dot notation — `element.isLibraryComponent` — implying a structure that was never defined. Two people would have built incompatible adapters |
| A worked example | Nothing showed facts going in and a verdict coming out. This was the largest gap: the difference between a spec someone can implement and one they can only agree with |
| How the report is assembled | The format was shown; nothing said who computes scores from facts |
| Who owns which part | "The consuming repo" was never made concrete against what this repo owns |

All five are now in the scorecard, and all five are platform-neutral — a data
shape is the contract's format, not any tool's output.

**One subtlety the schema had to settle: an omitted field means `unavailable`;
`false` means "no".** `"isTokenBound": false` says the platform looked and found
a literal. Omitting the field says the platform could not look. Conflating them
would let an adapter gap read as a compliance failure, which is the exact error
the `unavailable` rule exists to prevent.

**On the JSON block.** `components-audit.md` rejected publishing the component
inventory as JSON, on the grounds that JSON in this repo is reserved for Figma
identity data written by the sync skills. That still holds: this is an **example
inside a markdown file**, not a committed data file, and no skill owns it. A
separate `adapter-facts.schema.json` was rejected for exactly the reason the
inventory was.

## Why identifiers are always written with their names

**Raised 2026-09-08 by Gabriel:** *"When explaining using C1, P1 etc., when the
document needs to be read by a human, add the full name or summary. Not possible
to remember all of them."*

Correct, and it applied to the first draft throughout, as well as to the
conversation that produced it. Six two-character codes are not memorable, and a
report using bare codes cannot be followed by anyone who did not write it.

The convention: **always `C1 · Provenance`, never bare `C1`.** In the scorecard,
in every report, in the ledger, in audit entries, and in conversation. The cost
is a few characters. The benefit is that a report is legible to someone reading
it cold, which is the only condition under which it is useful.

Recorded as a rule in `.claude/rules/compliance.md` and
`.claude/rules/project.md` rather than left as a preference.

## Why compliance is separable from quality

The whole scorecard rests on this, so it is worth stating rather than assuming.

| | Compliance | Quality |
| --- | --- | --- |
| Question | "Is every fill bound to an authorised token?" | "Does this feel like SeLoger?" |
| Answers | One | Many, and contested |
| Who can settle it | A script | A person |
| Documented? | Yes — four rulesets | No — it lives in Gabriel's head |

Mixing them produces a number nobody trusts. Keeping them apart lets the
compliance gate run unattended today while the quality bar is written later,
from a corpus of recorded verdicts rather than from scratch. That is why the run
log has a **Quality verdict** column that the scorecard itself never scores.

## Why the checks are scored independently

**Decided 2026-09-08 by Gabriel.** A hard fail fails its own check, not the run.

The alternative — one hard fail sinks the run — is more honest about what a
screen containing platform chrome is worth. It was rejected for a first version
on the grounds that a run-level gate on an unproven checker discards a whole
run's data on a single false positive, and data is currently the scarcest thing
in this project. Run-level gating is expected once the checker is proven.

The risk this creates is real: a report reading "C1 94%, C3 88%" looks broadly
fine while containing a `Status Bar`. It is mitigated by **format rather than by
scoring** — hard fails print first, by name, with node IDs, above any
percentage. A percentage never appears before a gate it could disguise.

## Why unauthorised tokens are flagged, not failed

**Decided 2026-09-08 by Gabriel**, for a better reason than the one proposed.

The recommendation was to flag because *a scorecard must not be stricter than
the ruleset it enforces* — typography Rule 3 says "prefer these eleven styles",
not "only these", so failing style twelve would blame the agent for reading the
documentation correctly.

Gabriel's reason was that the flags are **findings worth having**: an agent
reaching for an unprecedented token may be revealing a gap in the ruleset rather
than making a mistake.

That reframing changed the design. Flags are no longer per-run noise to be
skimmed — they **accumulate in a ledger**, and a flag seen three times is
promoted to a ruleset defect with an entry in the relevant `-audit.md`. This is
the same mechanism that made `components-eval.md` valuable: its 22/22 first run
still surfaced four defects, because the agent's friction was recorded rather
than discarded.

It also gives the checker a second purpose. It grades output, and it improves
the knowledge base.

## Why `C2 · Tier ceiling` needs data that does not exist yet

**Decided 2026-09-08 by Gabriel:** C2 must be machine-detectable, and hand-built
or new components must be flagged. Correct, and the mechanism took a wrong turn
first.

The initial assumption was that the Figma registries could supply each
higher-tier component's parts. They cannot:

| Problem | Detail |
| --- | --- |
| **Wrong kind of data** | `Listing Card`'s `exposedSubComponents` are private internal slots — `.listing_tags_list`, `.listing_price_tag`, `.listing_title`. A hand-built imitation would contain `Card`, `Image Slider` and `Tag`, none of which appear in that list |
| **Incomplete** | Only 5 of 11 Experiences, 10 of 21 Patterns and 18 of 61 Components record sub-components at all |
| **Inconsistent** | `Map template` mixes public (`Image Slider`, `Tag`) with private, and carries a stale entry marked `❌ … (outdated)` |

What C2 actually needs is small: **a machine-readable parts column on Rule 0's
ten rows.** The information already exists as prose in the ruleset — *"A property
summary card from Card + Image slider + Tag + Price"* — and needs only to become
data. Ten rows.

This is a dependency on the components ruleset, not on the registries, and it is
the one thing blocking C2 from running.

The false-positive problem is solved differently, and better: **C5 decides what a
detection means.** Composition detected with no declaration is a hard fail;
composition detected with a declaration naming what was ruled out is a flag for
review. The checker never has to answer "is this secretly a Listing Card?" — it
only has to answer "did the agent say what it was doing?"

## Why thresholds are derived, never invented

**Decided 2026-09-08 by Gabriel:** implement thresholds now, refine later.

The objection to setting thresholds before any run is that an invented number
acquires authority fast — write down 80% and someone optimises to 80%. That
objection does not apply where the rule already states the number:

| Threshold | Invented? |
| --- | --- |
| `C3 · Token binding` = 100% bound | No — "never write a pixel literal", "never write a raw colour" |
| `C4 · Authorisation` = 0 deny-listed | No — the *Never use* tables |
| `C5 · Declaration` = 100% declared | No — Rule 5 |
| `C2 · Tier ceiling` = 0 undeclared compositions | No — Rule 0 + Rule 5 |
| `C1 · Provenance` = no regression | Nothing to derive, so nothing invented — run 1 sets the baseline |

So every threshold in the scorecard either comes from a rule or is a ratchet.
None is a guess.

## Why `C6 · Layout` ships switched off

`spacing-rules-ai.md` Rules 6 and 7 do document page composition — container
padding, and outer margin, section gap, card-grid gap and form-field gap per
viewport tier. Six of the nine pieces a layout check needs are already there.

But the ruleset flags them itself: *"Rules 6 and 7 are unverified. They describe
product-page composition, which lives outside the component library and could not
be checked. Follow them as the documented intent, but they do not carry the same
evidence as Rules 3–5."*

Scoring against them would produce a number with no evidence under it — the exact
failure the token audits were run to prevent. C6 is therefore defined in full and
explicitly inactive, so that the gap is visible rather than silently unmeasured.

This also revised the plan. Block 3 was scoped as *write the missing layout
rules*; it is actually *verify layout rules that already exist*. Same dependency
— Gabriel naming 3–5 real product screens — but a cheaper job and a stronger
result.

## A note on the flag ledger's name

`-ledger` is defined in `README.md` as script-written and never hand-edited. The
flag ledger is written by the **checking agent** rather than by a Python script,
which stretches that definition slightly.

It is still the right suffix: the file is machine-generated, append-only, and
must never be hand-edited — which is what the suffix actually guarantees. The
alternative was `-log`, a seventh suffix for a distinction nobody would act on.

## Rejected approaches

| Rejected | Why |
| --- | --- |
| **A single overall compliance percentage** | Averaging six unrelated checks hides the one that matters. A screen at "91%" tells you nothing about whether it contains platform chrome |
| **Scoring quality alongside compliance** | Different kinds of question. A blended score would be trusted by nobody and would quietly make the human judgment look optional |
| **Deriving checks from what is easy to measure** | C3 is trivial to check and C2 is where real failures live. Building the scorecard around what a script can see easily would have measured everything except the thing that matters |
| **Letting the scorecard be stricter than the rulesets** | It would blame the agent for correctly following the documentation. Any gap found this way is a ruleset defect and gets fixed there |
| **Waiting for the Figma agent before defining compliance** | The original plan's order. An agent built first has nothing to aim at, and its first output gets judged by eye — the human bottleneck this project exists to remove |
| **Scoring C6 against Rules 6 and 7 as they stand** | They are marked unverified by their own ruleset. A number with no evidence under it is worse than an acknowledged gap |
| **Writing the scorecard as a Figma checker specification** | The first draft did this. It put plugin-API vocabulary and Figma node IDs into a repo whose purpose is one platform-neutral truth consumed by several agents. Split into a neutral scorecard plus per-platform adapters |
| **Scoring a check `0%` when a platform cannot supply its facts** | A zero reads as *the output failed*. It would blame generated output for a gap in the adapter. Such a check reports `unavailable` |
| **Referring to checks by number alone** | Six two-character codes are not memorable. A report nobody can read cold is not a report |
| **Using `exposedSubComponents` as C2's parts list** | Wrong kind of data — private internal slots, not the public components an imitation would contain — and present for fewer than half the registry entries |

## Open questions

Six questions were raised when the scorecard was drafted. **Five were answered
the same day**; the sixth moved out of this repo with the platform split.

| # | Question | Answer |
| --- | --- | --- |
| 1 | Where does Rule 0 parts list live — the ruleset, or a separate data file? | **`components-rules-ai.md` Rule 0.** `Card`, `Image Slider`, `Tag` are design-system names, so the list is platform-neutral and belongs with the rule it serves. Answered by the platform split |
| 2 | Where does the checker run? | **The consuming agent repo**, as a platform adapter. Also answered by the platform split — the checker is a *how*, and every *how* lives with its tool |
| 3 | Can a Figma file report bound values reliably enough for `C3 · Token binding`? | **No longer this repo question.** It is a Figma-adapter concern and moves out with the adapter. What stays here is the requirement that the fact be reportable at all |
| 4 | What counts as one run? | **One output** — whatever the agent produced from a single wireframe and brief, even if that is three screens. Refined during the discussion: **no-regression compares runs of the same wireframe only**, because comparing a search results page against a form measures the difficulty of the brief, not the compliance of the output |
| 5 | Should a declared invention expire? | **No, and it is never auto-promoted.** A repeatedly declared invention is flagged as *awaiting human decision* — it may be a missing component rather than a one-off, and only a person can settle that |
| 6 | Who owns a promoted flag? | **Gabriel, explicitly asked.** A subject seen three times is raised for a human decision, not auto-promoted and not auto-dismissed. An open decision blocks nothing; it accumulates until ruled on |

### Still open

1. **Nothing forces a decision to be made.** Questions 5 and 6 both resolve to
   "ask a human", and `awaiting decision` accumulates by design. If nobody ever
   rules, the ledger becomes a list of unread questions. No mechanism prevents
   that, and inventing a deadline would be arbitrary.
2. **The adapter contract is specified but unvalidated.** Its seven required
   facts, and the shape they arrive in, were derived by reasoning about what the
   six checks need — not by building an adapter. The first Figma adapter will
   almost certainly find a fact that is missing, one that no platform can supply
   cleanly, or a shape that does not survive a deep element tree. Being
   implementable is not the same as being correct.
3. **`C1 · Provenance` has no denominator until there is a run.** "Local builds
   that duplicate an existing component" requires knowing which locals duplicate
   something, which is `C2 · Tier ceiling` parts list. Until block 2 lands,
   `C1 · Provenance` can count hard fails but not produce a percentage.

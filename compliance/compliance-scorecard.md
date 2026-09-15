# Compliance scorecard

_How generated output is judged against the GSL Design System. **The questions
are platform-neutral by design** — they say *what* to measure, never *how* a
given tool measures it. The agent answering them is not: today it reads Figma.
See [what the scoring agent reads](#what-the-scoring-agent-reads)._

**Read by the scoring agent**, never by a generating agent — a generating agent
reads the `*-rules-ai.md` rulesets.

Evidence and rejected alternatives: [compliance-audit.md](compliance-audit.md).

---

## The three layers, and which one this file is

| Layer | Content | Where it lives |
| --- | --- | --- |
| **The concept** | What compliance means. The questions. What a `yes` means. Where a reason goes | **this file** |
| **What to measure** | Stated in design-system vocabulary — "every element must be an instance of a library component" | **this file** |
| **How to measure it** | Figma reads its component keys; web reads its package imports; iOS reads its view hierarchy | **the scoring agent — one per platform** |

**Nothing tool-specific belongs in this file.** No API names, no node IDs, no
framework vocabulary. If a question cannot be stated without naming a tool, it is
not yet a design-system rule and does not belong in the scorecard.

---

## What compliance means

**Reuse before invention.** Use an existing component or an authorised token
wherever one fits; create something new only when nothing does, and declare it
when you do.

Compliance is **not** quality. Compliance is arithmetic — "is every colour bound
to an authorised token?" has one right answer. Quality is judgment and is not
scored here. Every run records a human quality verdict alongside its answers, so
a quality bar can later be written from real judgments.

---

## How a run is judged

**One run = one output.** Whatever the generating agent produced from a single
wireframe and brief. If it produced three screens from one brief, that is one
run.

The scorecard asks a short list of questions, grouped by the step of designing
each one guards. **Every question is binary, and is phrased so that the
compliant answer is `no`.**

| The answer | What it means |
| --- | --- |
| **`no`** | Compliant. Nothing further is recorded |
| **`yes`** | A finding. The report states **what** and **where**, in the *Reason* column |
| **`unavailable`** | The scoring agent could not tell from the screen. **Never answer `no` in this case** — being unable to see is not the same as finding nothing |

**A `yes` is not always a failure.** One question — *was any element hand-built* —
is a finding that the next step resolves, because **When nothing fits** permits
invention as long as it is declared. Every question states what its `yes` means.

### There are no percentages, and no thresholds

Deliberate, and it is a simplification rather than a loss. Every threshold the
earlier version of this file carried was either `100%` or `zero`: *never write a
pixel literal*, *never write a raw colour*, *0 deny-listed*, *100% of inventions
declared*. A threshold of 100% is a yes/no question wearing a percent sign, and
writing it as `88%` invited a reader to treat a broken rule as a good score.

**Counts belong in the reason, not in the verdict.** *Three elements carry a
literal colour* is more use than `88%`, and it is the sentence someone can act
on.

### `no regression` is not a question here

An earlier version gated provenance on *no regression* — better than the last run
of the same wireframe. It was dropped on 12 September 2026: it answers whether
this run beat the previous one, which is a question about the project, not about
the design system, and it was the only judgment in this file that could not be
made from a single run.

The trend it measured is still readable. Open
[compliance-run-ledger.md](compliance-run-ledger.md) and read down one wireframe
label, which is what a ledger is for.

---

## The questions, by step

Designing a screen is seven steps. **Each section below is one step.** Four steps
have questions; three have none, and say so rather than being left out — an
absent step reads as an oversight, a step that states its own emptiness reads as
a known gap.

Every question names the rule it enforces. **A question traceable to no rule in
`components-rules-ai.md` or one of the token rulesets does not belong here** —
delete it rather than justify it.

---

### Define the content

**No question yet.**

Nothing here checks copy, tone, or whether the content answers the user need the
brief described. `Content & UX Writing` is empty in 15 of 57 component docs, so
there is no source to check against. Stated so the gap stays visible.

---

### Define the components to use

**Did the output use the design system, or build its own?**

| Question | A `yes` means | Enforces | What the scorer must see |
| --- | --- | --- | --- |
| Was any element hand-built instead of taken from the library? | **A finding, not a failure.** Every hand-built element is carried into **Define what needs to be built**, where the declaration question decides it | **The inventory** | Whether an element is a library instance |
| Was any never-select component used? | **Failure.** Platform chrome, brand assets, another component's internals, or a withheld component | **Never select** | Which component each instance is |
| Was any component name used that appears in no registry? | **Failure.** It came from outside GSL | **The inventory** | Which component each instance is |

**The first question is the whole of "is it using the design system".** It needs
one look per element and no lists, no parts counting and no judgment: either an
element is a library instance or it is not, and the answer is a count of the ones
that are not.

**What this step cannot see** — whether the *right* component was chosen. `Chip`
where `Tag` was correct passes completely. That is `components-eval.md`'s job,
not the scorecard's.

**And it cannot see that a hand-built element duplicates something that already
exists.** It reports that `12:3500` was hand-built; it does not report that
`12:3500` is a `Listing Card`. Naming what was rebuilt is the reason, and the
reason is investigated by a person. Removed by Gabriel, 12 September 2026 — the
parts-counting check that attempted it reached 4 of **Highest tier first**'s 10
rows and could never reach the other six.

---

### Define what needs to be built

**When something was invented, was it declared?**

| Question | A `yes` means | Enforces | What the scorer must see |
| --- | --- | --- | --- |
| Was anything hand-built without a complete declaration? | **Failure.** **When nothing fits**'s own words: *an undeclared new component is a compliance failure even when it looks right* | **When nothing fits** | Whether an element is a library instance, and the run's `## Declarations` section |

A declaration is complete only when it states all three:

1. **What was built.**
2. **Which problem from Which component it belongs under.**
3. **Which existing components were ruled out, and why.**

**A declaration missing any of the three counts as absent.** Two of the three is
not a partial pass; it is a declaration nobody can review.

**Where a declaration physically lives:** the `## Declarations` section of
`compliance/briefs/brief-<NNN>/run-<NNN>/report-run-<NNN>.md`, written by the
generating agent
before scoring. Same place on every platform — a run folder is the same whether
the output was drawn in Figma or built on web. See
[the report has two authors](#the-report-has-two-authors).

**A run that invented nothing still writes the section**, reading `_None._`. An
empty section says the agent looked; a missing one cannot be told apart from an
agent that never considered the question.

**This question is the pivot of the whole scorecard.** It is what lets
**Define the components to use** report a hand-built element without anyone
having to decide whether building it was justified. The checker never answers *"was this invention a good idea?"*,
which needs a person. It answers *"did the agent say what it was doing?"*, which
does not.

**A declared invention does not expire, and is never auto-promoted.** The same
invention declared in more than one run is flagged as *awaiting human decision* —
it may be a missing component rather than a one-off, and only a person can settle
that. An open decision blocks nothing; it accumulates until it is ruled on.

---

### Choose the tokens

**Are values bound to tokens, and are those tokens allowed?**

| Question | A `yes` means | Enforces | What the scorer must see |
| --- | --- | --- | --- |
| Was any styled value written as a literal instead of bound to a token? | **Failure** | colour's **No raw colour** · spacing's and radius's **No pixel literals** · typography's **No hand-set fonts** | Whether each styled property resolves to a token, and what is being styled |
| Was a library component's internal styling overridden? | **Failure** | **Components first**, in all six token rulesets | Whether a property belongs to a component's own internals or was set locally |
| Was any deny-listed token used? | **Failure** | the six deny-lists below | Which token each property resolves to, and what is being styled |
| Was any token used that is not in the GSL token set? | **Failure.** It came from outside GSL | [tokens-index.md](../tokens/tokens-index.md), which routes to all twelve token pages | Which token each property resolves to |

**Styled properties are colour, type style, spacing, radius, border width and
shadow.** A type property — family, size, weight, line height — set individually
rather than through a text style is a literal.

**A library component's internal properties are not examined.** They belong to
the component and are correct by construction. If the scoring agent cannot
distinguish internals from local styling, the first question reports
`unavailable`.

**A token name that resolves on no token page is not a GSL token.** This is the
token half of *was any component name used that appears in no registry*, and it
is sourced the same way: [tokens-index.md](../tokens/tokens-index.md) does for
tokens what **The inventory** does for components — it is the list of what
exists, and a name absent from it does not exist. Neither question needs a
prohibition written anywhere, because the list is the rule.

**The index, not the rulesets, answers this one.** A ruleset says which of the
existing tokens are *allowed*, which is the deny-list question above. This
question asks only whether the name is one of ours at all, so it reads the twelve
token pages the index routes to and nothing else.

#### The six deny-lists

**Every token ruleset carries one, and all six are read.** Three of them —
radius, shadow and border width — were unenforced until 12 September 2026, so a
`1.5` border or a shadow of `32` broke a written rule and was never reported.

| Ruleset | Section | Examples |
| --- | --- | --- |
| `color-rules-ai.md` | *Never use* | the symbol, native, scale and decorative-surface families, the focus border, the unreachable status leaves, the enumerated orphans |
| `spacing-rules-ai.md` | *Do not use* | `Spacing/56` |
| `typography-rules-ai.md` | **No Display** | the Display family |
| `radius-rules-ai.md` | *Do not use* | any value outside the five-token table · `Corner radius/*` per-component variables |
| `shadow-rules-ai.md` | *Do not use* | `24` and `32` · any custom shadow · the mobile bottom navigation bar's shadow |
| `border-width-rules-ai.md` | *Do not use* | any value other than `0`, `1` and `2` · `Border Width/2` for anything but active or focused · a widened border to signal an error |

#### Two things that are flagged, never failed

| Class | Source | What happens |
| --- | --- | --- |
| **Restricted** | `color-rules-ai.md` *Restricted* — allowed only as described | **Flag** → *awaiting human decision* |
| **Unprecedented** | Exists, is not deny-listed, but sits outside the preferred set — e.g. outside typography's **The eleven used styles** | **Flag, never a failure** |

**Why unprecedented is a flag.** The rulesets say *prefer these*, not *only
these*. A scorecard stricter than the ruleset it enforces blames the agent for
reading the documentation correctly. And the flags are findings in their own
right — an agent reaching for an unprecedented token may be revealing a gap in a
ruleset rather than making a mistake.

**What this step cannot see** — whether an authorised token is the *right*
authorised token. A subdued surface where a default one was meant passes.

---

### Put them on the screen

**No question yet.**

Nothing checks whether a placed component carries the content the brief asked
for — an agent can place a `Text Field` and leave its label empty, and every
question above still answers `no`.

---

### Place them according to the design guidance · **INACTIVE**

**Defined so it is not forgotten. Not asked, and not reported, until
Block 3 · Layout completes.**

| | |
| --- | --- |
| **Would enforce** | spacing's **Container padding** · **Page rhythm** per tier · `grid-tokens.md` outer margin and gutter |
| **Would ask** | Whether outer margin, section gap, card-grid gap and form-field gap match spacing's **Page rhythm** table for the output's viewport tier, and whether container padding matches **Container padding** |
| **Would need** | The output's viewport tier. A platform that cannot report it leaves this step inactive |

**Why it is switched off.** The spacing ruleset carries an explicit warning on
the two rules this would enforce: *"Rules 6 and 7 are unverified. They describe
product-page composition, which lives outside the component library and could not
be checked."*

Judging against unverified rules manufactures confidence the evidence does not
support. Block 3 · Layout verifies them against real product screens; this step
activates then, and this section says so rather than quietly judging anyway.

---

### Check the content

**No question yet.**

Nothing reads the finished screen back against the brief. The scorecard's own
blind-spot table says copy and tone are unmeasured, and this is the step where
that would be caught.

---

## What the scoring agent reads

### It reads the output directly

**The scoring agent opens the produced screen and looks.** On Figma that means
reading the file the generating agent drew in. There is no intermediate file and
no translation step.

**It also reads the `## Declarations` section of the run's report**, which the
generating agent wrote before scoring. That is the only part of a run the screen
itself cannot tell it.

### It is a different agent from the one that built the screen

**This is the rule the whole arrangement rests on.** A generating agent knows
every question in this file, so anything it hands the scorer it can shape without
ever stating a falsehood.

| Written by the **generating** agent | Written by the **scoring** agent |
| --- | --- |
| The `## Declarations` section, before scoring | Everything below it — what it found, the answers, the flags |

The scoring agent must be started fresh. It never sees the generating
conversation and never asks the generating agent anything.

### What it has to be able to determine

Each question names what it needs. Stated here in one place, in design-system
terms rather than platform terms.

| What it must determine | Used by |
| --- | --- |
| Whether an element is an instance of a design-system component, or was built by hand | *Was any element hand-built* |
| Which component an instance is, by its name in **The inventory** | *Was any never-select component used* · *appears in no registry* |
| Whether a styled property resolves through a token or is a literal value | *Was any styled value written as a literal* |
| Which token, by the name used on the token pages | *Was any deny-listed token used* · *not in the GSL token set* |
| What is being styled — colour, type style, spacing, radius, border width, shadow | the same two questions |
| Whether a property belongs to a component's own internals or was set locally | *Was a component's internal styling overridden* |

Two more it should record where it can, because they make a finding actionable
rather than merely true:

- **Where the element is**, so a finding can be pointed at rather than described.
- **What a hand-built element contains**, so the reason says *a card holding an
  image slider and a tag* and not only *something was hand-built*.

### When it cannot tell

**A question the scoring agent cannot answer reports `unavailable`, never `no`.**
A `no` reads as a clean screen. The truth is that nobody could see.

- `unavailable` is neither a compliant answer nor a failing one.
- It records that the screen could not be read on that point, and that is worth
  knowing.

### It writes down what it found

**Findings go into the report, above the answers.** Not into a separate file.

This is deliberately the cheap version. A stored, structured record of every
element would let a future rule be re-run against an old screen — worth having,
and out of scope before the end of September. The screenshots and the written
findings are the record until then.

### Names are always design-system names

`Listing Card`, `Spacing/16`, `body/16/regular` — never a local identifier from
the tool. `figma/*-registry.json` is what turns one into the other.

### This scorer is Figma-only, and that is a known limit

**The questions are written in design-system vocabulary, so they carry to web,
iOS and Android unchanged.** The agent answering them does not.

- A second platform needs a second scoring agent, written against that platform.
- The questions, the report format and the ledgers stay as they are.
- Nothing here has been designed for that yet, and nothing should be until one
  Figma run has been scored end to end.

### A worked example

Two elements from a listing page, and what each question concludes.

**A `Button` placed from the Components library**

| Question | What the scorer found | Answer |
| --- | --- | --- |
| Was any element hand-built instead of taken from the library? | a library instance, named `Button` | **no** |
| Was any never-select component used? | `Button` | **no** — not on the list |
| Was any component name used that appears in no registry? | `Button` | **no** — it is in the Components registry |
| Was anything hand-built without a complete declaration? | nothing hand-built here | **no** |
| Was any styled value written as a literal instead of bound to a token? | its colour and spacing both resolve to tokens | **no** |
| Was a library component's internal styling overridden? | nothing set locally on it | **no** |
| Was any deny-listed token used? | `Surface/Brand/Primary/default` · `Spacing/16` | **no** — neither is deny-listed |
| Was any token used that is not in the GSL token set? | both names resolve on the token pages | **no** |

**A hand-built block containing `Card`, `Image Slider` and `Tag`**

| Question | What the scorer found | Answer |
| --- | --- | --- |
| Was any element hand-built instead of taken from the library? | not a library instance | **yes** — a finding, not a failure. Carried into *define what needs to be built* |
| Was any never-select component used? | no library component to check | **no** |
| Was any component name used that appears in no registry? | no component name to check | **no** |
| Was anything hand-built without a complete declaration? | the only declaration names an agency banner, not this | **yes** — **failure** |
| Was any styled value written as a literal instead of bound to a token? | one colour is written as `#1A1A1A` | **yes** — **failure** |
| Was a library component's internal styling overridden? | not a library component, so it has no internals | **no** |
| Was any deny-listed token used? | `Radius/8` | **no** |
| Was any token used that is not in the GSL token set? | `Radius/8` resolves on the radius token page | **no** |

Note what the scorer never had to decide: whether the second block *is* a
`Listing Card`. It only reported that it was hand-built and that nothing declared
it. Naming what it duplicates is a person's job, on the reason.

---

## The report

### A report is a file

**Every run produces a report, and the report is part of the output.** A run
whose screen exists but whose report does not is an unfinished run, not a
compliant one.

It is written to:

```
compliance/briefs/brief-<NNN>/run-<NNN>/report-run-<NNN>.md
```

`<NNN>` is the next unused three-digit number. Numbers are never reused, never
reordered, and never renumbered after the fact.

**Every run file carries its run number in its own name.** The folder already
says which run it is, and the filename repeats it on purpose: a file is opened in
a tab, attached to a message, or dropped beside another run's file, and in all
three the folder is gone. Screenshots are the exception — they keep their
descriptive names, because what a screenshot shows matters more than which run
drew it.

**A report lives in this repo, never inside the output it judges.** Not in the
Figma file, not in the web prototype, not beside the skill that produced it. A
verdict stored inside the thing it judges cannot be sent to anyone on its own,
cannot be compared against another run, and is thrown away with the prototype.

### What a run folder holds

| File | Required? | Written by | What it is |
| --- | --- | --- | --- |
| the brief — `../brief-<NNN>.md` | **yes**, one level up | the person running it, **before the first run of it** | The brief every run in this folder was given. Written once and shared, so it cannot be quietly rewritten to match what came out. **A changed requirement is a new brief folder**, never an edit to this one |
| screenshots — `*.png` | **yes** | whoever ran it | What the screen actually looked like. The only human-readable proof: a Figma file changes under you, a screenshot does not |
| `report-run-<NNN>.md` | **yes** | **two authors — see below** | **Declarations**, then the answers. Template below |

### The report has two authors

**The generating agent writes the `Declarations` section. The checking agent
writes everything else.** They write at different times, into the same file.

| Written by | When | What |
| --- | --- | --- |
| The generating agent | **Before scoring**, as the last act of generating | `## Declarations` — one block per element it built by hand |
| The scoring agent | After the screen exists and the declarations are written | Every other section, and both ledger rows. It writes **above and below** `## Declarations` and **never edits it** — it reads it and answers the question |

**A declaration is written before the score is known, and is never revised
afterwards.** This is the same protection the brief already has: it is
written before the first run so it cannot be reworded to match what came out, and a declaration is written before scoring so it cannot be retrofitted to
pass. A declaration added or reworded after the verdict is not a declaration.

**The run folder is the only home a declaration has.** Not a note on the Figma
frame, not a comment in the prototype, not the agent's reply in chat — a reply
is not an artefact and is gone when the session closes.

**There is no stored record of what the scoring agent saw, beyond what it wrote
in the report.** A structured one would let a changed question be re-run against
an old screen — *would the new question have caught the old mistake?* — without
regenerating anything. Decided out of scope by Gabriel, 14 September 2026, as too
advanced for the end-of-September deadline. Until then the screenshots and the
written findings are the record, and a changed question is tested by running a
new screen.

### Who the report is for, and the order that follows from it

**The report is written for Gabriel.** It is the only thing in the pipeline a
person reads end to end. The ledgers are the machine-facing summary, and nothing
else reads a report at all.

That decides the order. **Conclusion first, decisions second, machinery last.**

| Section | Who writes it | Why it sits here |
| --- | --- | --- |
| **Verdict** | the scoring agent | The answer, in plain words. First, because it is what he opened the file for |
| **Decisions you need to make** | the scoring agent | The only part that needs him to act |
| **Answers** | the scoring agent | The scorecard question by question |
| **Declarations** | the **generating** agent | What it built by hand and why. Written first, never edited |
| **Evidence** | the scoring agent | The walk, the inventory, the locators. Last, because nobody reads it unless a line above is disputed |
| **Quality verdict** | Gabriel | Free text, never scored |

**The generating agent writes `## Declarations` into the file first.** The
scoring agent then writes the human sections **above** it and the evidence
**below** it. Writing around a declaration is allowed; editing one is not.

### Writing rules for the report

**Gabriel's personal writing rules apply to the whole file except Evidence.**
Short sentences, short paragraphs, no preamble.

**A locator is a coordinate, never part of a sentence.** A node ID, a key, a
file id — each is a way to find a thing, not a way to name it.

- Name the thing in words, then give its locator in a column or in brackets.
- **Never** write a list of bare IDs in running prose.
- Bad: *"Also undeclared: the four plain text nodes at `133:5081`, `133:5085`,
  `134:5078`, `134:5968`."*
- Good: *"Four text nodes are undeclared — two section titles, two rating
  labels."* The IDs go in the Evidence table.

**Evidence is the one section written for a machine**, and the repo's usual rule
applies there: restate a condition rather than eliding it, and give every finding
its locator.

### Every row appears, including the empty ones

**One row per question, in step order, whatever the answer.** A row reading `no`
is information. A missing row is ambiguous — the reader cannot tell whether the
question was answered or whether nobody asked it.

The same holds for the three steps with no question and for the inactive step:
they each keep a row saying so.

### Everything a person must rule on goes in one table

**A failure needs a human ruling as much as a flag does.** This was missing until
14 September 2026: flags carried four verdicts and failures carried none, so a
failure was recorded and never decided. Gabriel raised it after the first scored
run, where the clearest finding was neither the agent's fault nor the
documentation's.

Both go in **Decisions you need to make**, with the same five verdicts:

| Verdict | Meaning |
| --- | --- |
| `awaiting decision` | Not yet ruled on. Blocks nothing; accumulates until it is |
| `agent error` | The rules covered this case. The generating agent got it wrong |
| `ruleset gap` | The rules did not cover this case. **Becomes a task in the backlog** |
| `library defect` | **The Figma library is wrong.** Not the agent, not the documentation — no doc change fixes it, and it needs a library edit |
| `accepted` | Legitimate as used. No change needed |

**`library defect` exists because the first scored run produced one.**
`Donut chart` places its legend beside the chart and offers no other option. Its
own documentation allows below **or** to the left, so the library can express
only one of the two placements it is meant to support. Nothing the agent did
caused that, and no documentation change fixes it — the component needs an
alignment property it does not have. Ruled by Gabriel on 14 September 2026, from
run-002.

### The template

Markdown, so it renders anywhere and can be sent to someone on its own. Filled
in here with example values, so the shape is unambiguous.

````markdown
# Run 007 — Property listing detail, mobile

| | |
| --- | --- |
| **Date scored** | 2026-09-14 |
| **Platform** | Figma |
| **Brief** | [brief-002.md](../brief-002.md) |
| **Destination** | where the output was produced — a Figma node, a route, a screen |
| **Output** | [block-1-energy.png](block-1-energy.png) · [block-2-finance.png](block-2-finance.png) |
| **Frame judged** | `132:5052` · page `Screen` |

## Verdict

The screen is built almost entirely from the library. Two things failed.

One block was built by hand and never declared, so nobody can review whether
building it was right. One component had its internal spacing changed, which the
rules forbid outright.

Four things need your ruling, below. One of them looks like a Figma bug rather
than a mistake by the agent.

## Decisions you need to make (4)

| What | Why it needs you | Ruling |
| --- | --- | --- |
| The partner-offer block was built by hand and not declared | The rules are clear that this fails. Whether it should have been built at all is yours | _unruled_ |
| The donut chart's legend sits beside the chart, not below | The ruleset says below. The Figma component itself says beside. One of them is wrong | _unruled_ |
| The energy scale colours were used | A restricted family, used exactly as the rules describe. Restricted means a person looks | _unruled_ |
| White letters on the CO₂ ladder | No rule allows or forbids it. It may be a gap in the rules rather than a mistake | _unruled_ |

Rulings: `awaiting decision` · `agent error` · `ruleset gap` · `library defect` ·
`accepted`.

## Answers

| Step | Question | Answer | Reason |
| --- | --- | --- | --- |
| Define the content | _no question yet_ | — | — |
| Define the components to use | Was any element hand-built instead of taken from the library? | **yes** | Five things were built by hand. Three are declared, two are not |
| Define the components to use | Was any never-select component used? | no | — |
| Define the components to use | Was any component name used that appears in no registry? | no | — |
| Define what needs to be built | Was anything hand-built without a complete declaration? | **yes** | The partner-offer block, and four plain text nodes |
| Choose the tokens | Was any styled value written as a literal instead of bound to a token? | no | — |
| Choose the tokens | Was a library component's internal styling overridden? | **yes** | The donut chart's internal spacing was changed |
| Choose the tokens | Was any deny-listed token used? | no | — |
| Choose the tokens | Was any token used that is not in the GSL token set? | no | — |
| Put them on the screen | _no question yet_ | — | — |
| Place them according to the design guidance | _inactive_ | — | — |
| Check the content | _no question yet_ | — | — |

## Declarations (1)

Written by the generating agent, before scoring. Never edited afterwards. One
block per element built by hand; `_None._` if it invented nothing.

### A compact agency banner

| | |
| --- | --- |
| **What was built** | A compact agency banner — logo, agency name, and a contact action on one row |
| **Problem it belongs under** | Grouping and structuring content |
| **Ruled out** | `Card` — needs a full-bleed logo the Card padding forbids · `Listing Card` — this is an agency, not a property |

## Evidence

Written for a machine and for a dispute. Every locator lives here.

### How the screen was read

**Proved.** The frame was walked node by node. For every node the walk recorded
its type, its main component, its overridden fields, its bound variables and its
styling.

### Hand-built elements

| What | Nodes | Locator | Declared? |
| --- | --- | --- | --- |
| The partner-offer content block | 5 | `138:5263` | **no** |
| Section titles and rating labels | 4 | `133:5081` · `133:5085` · `134:5078` · `134:5968` | **no** |

## Quality verdict

_Human, free text, never scored. Not yet written._
````

**The quality verdict heading stays even when empty.** It is the only record of
the thing compliance cannot measure, and an empty heading asks to be filled
where a missing one does not.

### After writing the report

**The scoring agent appends both ledger rows itself.** It holds the findings and
the counts already; anything else re-derives them from the report, and a copy
step drifts.

| Append to | What |
| --- | --- |
| [compliance-run-ledger.md](compliance-run-ledger.md) | One row for the run — how many questions answered `yes` at each step, so runs can be compared without opening any report |
| [compliance-flag-ledger.md](compliance-flag-ledger.md) | One row per item in *Decisions you need to make* — failures included, not only flags |

Both files are append-only. Never rewrite a row, never remove one.

**A run is unfinished until both appends exist.** The first scored run wrote a
report and neither row, because two files disagreed about whose job it was.

---

## The flag ledger

**Every item a person must rule on is recorded here — failures included, not
only flags.** One item in one run is noise; the same item in three runs is
evidence a ruleset is missing a case.

Recorded in [compliance-flag-ledger.md](compliance-flag-ledger.md), appended
after every run, never rewritten.

| Column | Meaning |
| --- | --- |
| Run | Which run raised it |
| Step | Which step of designing it came from |
| Subject | Token name, component name, or element |
| Why raised | Failure · restricted · unprecedented · declared invention |
| Times seen | Cumulative across all runs |
| Verdict | `awaiting decision` · `agent error` · `ruleset gap` · `library defect` · `accepted` |

**A subject seen three times is raised for a human decision** — it is not
auto-promoted and not auto-dismissed. Gabriel rules on it, and the verdict says
which of the five it was.

**A verdict of `ruleset gap` does not file itself.** Gabriel decides, per item,
whether it is fixed on the spot or becomes a backlog task. Some gaps close in one
sentence, and a backlog round-trip costs more than the fix. Revised by him
14 Sep 2026, after the first scored run produced eight items to rule on.

**Either way it lands in [the backlog](../project/backlog.md)** — as a task if it
is filed, as a row in the *Done* table if it is fixed on the spot. One
destination, which is what the 11 Sep 2026 rule was protecting: two destinations
meant two sessions filed the same finding in different files.

Doing the work writes the rule into the ruleset and the reasoning into the
relevant `-audit.md`, exactly as the component eval's misses did — the audit is
where the reasoning settles, never the queue.

This is the mechanism by which running the checker improves the knowledge base
rather than only grading output.

---

## Runs

**The run log lives in [compliance-run-ledger.md](compliance-run-ledger.md)**,
one row per run, append-only.

It used to sit in this file, and moving it out is the point. **This file is the
ruler; a run log is a measurement.** A ruler is rewritten whenever a rule or a
question changes — and rewriting a file that also holds what happened on a date
reaches back and edits history. Keeping them apart is what lets the rules change
while the evidence stays fixed. It is the same split as `-rules-ai` against
`-ledger` everywhere else in this repo.

There is a second, duller reason: this file is read **before every run**. A log
that grows by a line each time a screen is generated does not belong inside it.

Record every run, including bad ones. A log that holds only good runs is a
highlight reel, not evidence.

---

## What this scorecard cannot see

Stated plainly so a clean report is not mistaken for a good screen.

| Blind spot | Whose job |
| --- | --- |
| Whether the **right** component was chosen | `components-eval.md` |
| Whether a hand-built element **duplicates** a component that already exists | Human, from the reason on the report |
| Whether the **right** authorised token was chosen | Nothing yet |
| Whether the screen carries the content the brief asked for | Nothing yet — **Put them on the screen** has no question |
| Whether the screen is **usable** | Human |
| Whether the screen is **good** | Human — the quality bar, undocumented by design |
| Page composition | **Place them according to the design guidance**, inactive until Block 3 · Layout |
| Copy and tone | Nothing yet — **Define the content** and **Check the content** have no question |
| Accessibility beyond token choice | Nothing yet — `Accessibility (a11y)` is empty in 51 of 59 component docs |

A screen can answer `no` to every question and still be the wrong screen, badly
written and inaccessible. That is not a flaw in the scorecard; it is the boundary
of what compliance means.

# Compliance scorecard

_How generated output is judged against the GSL Design System. **Platform-neutral
by design** — it defines *what* to measure, never *how* a given tool measures it.
Each platform implements the [adapter contract](#the-adapter-contract) in its own
repo._

**Read by a checking agent**, not by a generating agent — a generating agent
reads the `*-rules-ai.md` rulesets.

Evidence and rejected alternatives: [compliance-audit.md](compliance-audit.md).

---

## The three layers, and which one this file is

| Layer | Content | Where it lives |
| --- | --- | --- |
| **The concept** | What compliance means. The questions. What a `yes` means. Where a reason goes | **this file** |
| **What to measure** | Stated in design-system vocabulary — "every element must be an instance of a library component" | **this file** |
| **How to measure it** | Figma reads its component keys; web reads its package imports; iOS reads its view hierarchy | **the consuming agent's repo — one adapter per platform** |

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
| **`unavailable`** | The adapter could not supply the facts the question needs. **Never answer `no` in this case** — a missing fact is a gap in the adapter, not a compliant screen |

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

| Question | A `yes` means | Enforces | Facts used |
| --- | --- | --- | --- |
| Was any element hand-built instead of taken from the library? | **A finding, not a failure.** Every hand-built element is carried into **Define what needs to be built**, where the declaration question decides it | **The inventory** | `isLibraryComponent` |
| Was any never-select component used? | **Failure.** Platform chrome, brand assets, another component's internals, or a withheld component | **Never select** | `componentName` |
| Was any component name used that appears in no registry? | **Failure.** It came from outside GSL | **The inventory** | `componentName` |

**The first question is the whole of "is it using the design system".** It needs
one fact per element and no lists, no parts counting and no judgment: the adapter
says whether an element is a library instance, and the answer is a count of the
ones that are not.

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

| Question | A `yes` means | Enforces | Facts used |
| --- | --- | --- | --- |
| Was anything hand-built without a complete declaration? | **Failure.** **When nothing fits**'s own words: *an undeclared new component is a compliance failure even when it looks right* | **When nothing fits** | `isLibraryComponent` · `declarations` |

A declaration is complete only when it states all three:

1. **What was built.**
2. **Which problem from Which component it belongs under.**
3. **Which existing components were ruled out, and why.**

**A declaration missing any of the three counts as absent.** Two of the three is
not a partial pass; it is a declaration nobody can review.

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

| Question | A `yes` means | Enforces | Facts used |
| --- | --- | --- | --- |
| Was any styled value written as a literal instead of bound to a token? | **Failure** | colour's **No raw colour** · spacing's and radius's **No pixel literals** · typography's **No hand-set fonts** | `isTokenBound` · `kind` |
| Was a library component's internal styling overridden? | **Failure** | **Components first**, in all seven rulesets | `isComponentInternal` *(optional)* |
| Was any deny-listed token used? | **Failure** | the six deny-lists below | `tokenName` · `kind` |
| Was any token used that is not in the GSL token set? | **Failure.** It came from outside GSL | [tokens-index.md](../tokens/tokens-index.md), which routes to all twelve token pages | `tokenName` |

**Styled properties are colour, type style, spacing, radius, border width and
shadow.** A type property — family, size, weight, line height — set individually
rather than through a text style is a literal.

**A library component's internal properties are not examined.** They belong to
the component and are correct by construction. If the adapter cannot distinguish
internals from local styling, the first question reports `unavailable`.

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
| **Facts used** | `viewportTier` *(optional)* — a platform that cannot report it leaves this step inactive |

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

## The adapter contract

### What an adapter is

**A translator, not a checker.** An adapter reads generated output using its own
platform's mechanisms, then restates everything it found in design-system
vocabulary. After it runs, the platform is gone — the questions never see a tool.

That is what lets one scorecard judge Figma output today and web or native
output later. A new platform means a new adapter, never a new scorecard.

An adapter contains **no rules**. It never decides whether something is
compliant; it only reports what is there. Every judgment lives in the questions
above.

### The pipeline

```
1. THE AGENT generates output
        │
        ▼
2. THE ADAPTER          platform-specific · lives with the tool
   Asks the platform its own questions, then translates every
   answer into design-system names, using the Figma registries
   as the dictionary
        │
        ▼
3. THE FACTS            platform-neutral · the contract below
   "this element is a library component named Button"
   "its background is token-bound to Surface/Brand/Primary/default"
        │
        ▼
4. THE CHECKER          platform-neutral · reads only facts
   Answers the questions above against the inventory and
   the six deny-lists
        │
        ▼
5. THE REPORT           one row per question, then flags
```

### Who owns what

| Owned by **this repo** | Owned by the **consuming agent's repo** |
| --- | --- |
| The contract — which facts must be reported | The adapter — how its platform answers |
| The questions and the report format | The runner that executes them on real output |
| The design-system names the facts must use | The translation from local identifiers into those names |

A gap in an adapter is a defect in the consuming repo. A question that cannot be
expressed as a question about facts is a defect **here**.

### Required facts

A platform that cannot supply these cannot be judged.

| Fact | Meaning in design-system terms |
| --- | --- |
| `element.isLibraryComponent` | Is this element an instance of a design-system component, or was it built locally? |
| `element.componentName` | If it is a library component, which one — by the name used in the Figma registries and **The inventory** |
| `property.isTokenBound` | Is this styled property resolved through a design token, or written as a literal value? |
| `property.tokenName` | If bound, which token — by the name used on the token pages |
| `property.kind` | What is being styled: colour · type style · spacing · radius · border width · shadow |
| `output.declarations` | The declarations the generating agent produced under **When nothing fits** |

### Optional facts

A question that needs one a platform cannot supply reports `unavailable`, never
`no`.

| Fact | Used by | If missing |
| --- | --- | --- |
| `element.isComponentInternal` | *Was a library component's internal styling overridden?* | The question reports `unavailable`, and the literal-value question cannot exclude a component's own internals |
| `element.viewportTier` | **Place them according to the design guidance** | That step stays inactive on that platform |
| `element.children` | The report | A hand-built element is named but not described, so the reason says *what* was built by hand and not *what it was built from* |
| `element.locator` | The report | Findings are named but not addressable |

**`unavailable` is not a compliant answer and not a failing one.** It records
that the platform could not answer, which is a gap in the adapter, not in the
output.

**`element.children` stopped being required on 12 September 2026**, when the
parts-counting question was removed. It is still worth supplying: it is what
turns *"something was hand-built"* into *"a card containing an image slider and a
tag was hand-built"*, which is the sentence the reason column needs.

### The shape

One object per run. `elements` is flat; `children` holds locators rather than
nesting, so a deep tree stays readable.

```json
{
  "run":  { "id": "001", "date": "2026-09-08", "wireframe": "serp-v1", "platform": "figma" },
  "declarations": [
    {
      "what": "A compact agency banner",
      "problem": "Grouping and structuring content",
      "ruledOut": [
        { "component": "Card", "why": "needs a full-bleed logo the Card padding forbids" },
        { "component": "Listing Card", "why": "this is an agency, not a property" }
      ]
    }
  ],
  "elements": [
    {
      "locator": "12:3401",
      "isLibraryComponent": true,
      "componentName": "Button",
      "isComponentInternal": false,
      "children": [],
      "properties": [
        { "kind": "colour",  "isTokenBound": true, "tokenName": "Surface/Brand/Primary/default" },
        { "kind": "spacing", "isTokenBound": true, "tokenName": "Spacing/16" }
      ]
    },
    {
      "locator": "12:3500",
      "isLibraryComponent": false,
      "componentName": null,
      "children": ["12:3501", "12:3502", "12:3503"],
      "properties": [
        { "kind": "colour", "isTokenBound": false, "literalValue": "#1A1A1A" },
        { "kind": "radius", "isTokenBound": true,  "tokenName": "Radius/8" }
      ]
    }
  ]
}
```

**An omitted field means `unavailable`. `false` means "no".** They are different
answers and must never be conflated — `"isTokenBound": false` says the platform
looked and found a literal; omitting the field says the platform could not look.

`literalValue` is recorded when `isTokenBound` is `false`, so a report can name
what was hardcoded rather than only that something was.

### A worked example

The two elements above, and what each question concludes.

**`12:3401` — a library `Button`**

| Question | Facts used | Answer |
| --- | --- | --- |
| Was any element hand-built instead of taken from the library? | `isLibraryComponent` is `true`, named `Button` | **no** |
| Was any never-select component used? | `Button` | **no** — not on the list |
| Was any component name used that appears in no registry? | `Button` | **no** — it is in the Components registry |
| Was anything hand-built without a complete declaration? | nothing hand-built here | **no** |
| Was any styled value written as a literal instead of bound to a token? | both properties token-bound | **no** |
| Was a library component's internal styling overridden? | `isComponentInternal` is `false` on both | **no** |
| Was any deny-listed token used? | `Surface/Brand/Primary/default` · `Spacing/16` | **no** — neither is on a deny-list |
| Was any token used that is not in the GSL token set? | both names resolve on the token pages | **no** |

**`12:3500` — a hand-built element containing `Card`, `Image Slider` and `Tag`**

| Question | Facts used | Answer |
| --- | --- | --- |
| Was any element hand-built instead of taken from the library? | `isLibraryComponent` is `false` | **yes** — a finding, not a failure. Carried into *define what needs to be built* |
| Was any never-select component used? | `componentName` is `null` — there is no library component to check | **no** |
| Was any component name used that appears in no registry? | `componentName` is `null` | **no** |
| Was anything hand-built without a complete declaration? | the only declaration names an agency banner, not this | **yes** — **failure** |
| Was any styled value written as a literal instead of bound to a token? | one colour is `#1A1A1A` | **yes** — **failure** |
| Was a library component's internal styling overridden? | not a library component, so it has no internals | **no** |
| Was any deny-listed token used? | `Radius/8` | **no** |
| Was any token used that is not in the GSL token set? | `Radius/8` resolves on the radius token page | **no** |

Note what the checker never had to decide: whether `12:3500` *is* a `Listing
Card`. It only had to report that it was hand-built and that nothing declared it.
Naming what it duplicates is a person's job, on the reason.

### Naming, across platforms

Component and token names in the facts above are always **design-system names** —
`Listing Card`, `Spacing/16`, `body/16/regular` — never a platform's local
identifier. Translating a local identifier into a design-system name is the
adapter's job, and the reason `figma/*-registry.json` exists.

---

## The report

### A report is a file

**Every run produces a report, and the report is part of the output.** A run
whose screen exists but whose report does not is an unfinished run, not a
compliant one.

It is written to:

```
compliance/runs/run-<NNN>/report.md
```

`<NNN>` is the next unused three-digit number. Numbers are never reused, never
reordered, and never renumbered after the fact.

**A report lives in this repo, never inside the output it judges.** Not in the
Figma file, not in the web prototype, not beside the skill that produced it. A
verdict stored inside the thing it judges cannot be sent to anyone on its own,
cannot be compared against another run, and is thrown away with the prototype.

### What a run folder holds

| File | Required? | Written by | What it is |
| --- | --- | --- | --- |
| `prompt.md` | **yes** | the person running it, **before generating** | The brief the run was given. Saved first, so a brief can never be quietly rewritten to match what came out |
| screenshots — `*.png` | **yes** | whoever ran it | What the screen actually looked like. The only human-readable proof: a Figma file changes under you, a screenshot does not |
| `facts.json` | **yes** | the adapter | What the platform found, in design-system vocabulary. Shape defined in [The shape](#the-shape) |
| `report.md` | **yes** | the checking agent | The answers. Template below |

**Why `facts.json` is kept rather than discarded after judging.** When a rule or
a question changes, the checker can be re-run against a stored `facts.json` —
answering *would the new question have caught the old mistake?* without
regenerating anything. Discard it and the next scorecard edit orphans every run
before it.

### Every row appears, including the empty ones

**One row per question, in step order, whatever the answer.** A row reading `no`
is information. A missing row is ambiguous — the reader cannot tell whether the
question was answered or whether nobody asked it.

The same holds for the three steps with no question and for the inactive step:
they each keep a row saying so.

**There is no hard-fails-first section any more.** It existed because a report
opening with *"C1 94%, C3 88%"* read as broadly fine even when something
forbidden had shipped. With no percentages left, there is nothing for a failure
to hide behind — the Answer column is scanned for `yes`, and that is the whole
reading.

### The template

Markdown, so it renders anywhere and can be sent to someone on its own. Filled
in here with example values, so the shape is unambiguous.

````markdown
# Run 007 — Property listing detail, mobile

| | |
| --- | --- |
| **Date** | 2026-09-14 |
| **Platform** | Figma |
| **Wireframe** | `listing-detail-mobile` |
| **Brief** | [prompt.md](prompt.md) |
| **Output** | [block-1-energy.png](block-1-energy.png) · [block-2-finance.png](block-2-finance.png) |
| **Facts** | [facts.json](facts.json) |

The **wireframe** label is what makes two runs comparable in the ledger. It is
not gated on — nothing fails for a label that does not match a previous run.

## Answers

| Step | Question | Answer | Reason |
| --- | --- | --- | --- |
| Define the content | _no question yet_ | — | — |
| Define the components to use | Was any element hand-built instead of taken from the library? | **yes** | `12:3500` — a hand-built element containing `Card`, `Image Slider` and `Tag` |
| Define the components to use | Was any never-select component used? | **yes** | `Status Bar` at `12:3401` — **Never select** |
| Define the components to use | Was any component name used that appears in no registry? | no | — |
| Define what needs to be built | Was anything hand-built without a complete declaration? | **yes** | `12:3500` — the only declaration names an agency banner |
| Choose the tokens | Was any styled value written as a literal instead of bound to a token? | **yes** | `#1A1A1A` at `12:3500` |
| Choose the tokens | Was a library component's internal styling overridden? | no | — |
| Choose the tokens | Was any deny-listed token used? | **yes** | `Spacing/56` at `12:3500` — spacing's *Do not use* |
| Choose the tokens | Was any token used that is not in the GSL token set? | no | — |
| Put them on the screen | _no question yet_ | — | — |
| Place them according to the design guidance | _inactive_ | — | — |
| Check the content | _no question yet_ | — | — |

## Flags (1)

Findings, not failures. Also appended to
[the flag ledger](../../compliance-flag-ledger.md).

| Step | Subject | Why flagged |
| --- | --- | --- |
| Choose the tokens | `Spacing/40`, 3 elements | Unprecedented — no rule authorises or forbids it as a section gap |

## Awaiting human decision (0)

_None._

## Quality verdict

_Human, free text, never scored. Not yet written._
````

**The quality verdict heading stays even when empty.** It is the only record of
the thing compliance cannot measure, and an empty heading asks to be filled
where a missing one does not.

### After writing the report

Two appends, both to files that are never rewritten:

| Append to | What |
| --- | --- |
| [compliance-run-ledger.md](compliance-run-ledger.md) | One row for the run — how many questions answered `yes` at each step, so runs can be compared without opening any report |
| [compliance-flag-ledger.md](compliance-flag-ledger.md) | Every flag raised, so a finding seen three times can be spotted |

---

## The flag ledger

**Flags accumulate across runs.** A flag in one run is noise; the same flag in
three runs is evidence a ruleset is missing a case.

Recorded in [compliance-flag-ledger.md](compliance-flag-ledger.md), appended
after every run, never rewritten.

| Column | Meaning |
| --- | --- |
| Run | Which run raised it |
| Step | Which step of designing it came from |
| Subject | Token name, component name, or element |
| Why flagged | Restricted · unprecedented · declared invention |
| Times seen | Cumulative across all runs |
| Verdict | `awaiting decision` · `ruleset gap` · `agent error` · `accepted` |

**A subject seen three times is raised for a human decision** — it is not
auto-promoted and not auto-dismissed. Gabriel rules on it, and the verdict says
which of the four it was. **If the verdict is `ruleset gap`, it becomes a task in
[the backlog](../project/backlog.md) first.** Doing that task writes the rule
into the ruleset and the reasoning into the relevant `-audit.md`, exactly as the
component eval's misses did — the audit is where the reasoning settles, never
the queue. Decided by Gabriel, 11 Sep 2026: the backlog is the one place a
finding has to be able to land, and two destinations meant two sessions filed
the same finding in different files.

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

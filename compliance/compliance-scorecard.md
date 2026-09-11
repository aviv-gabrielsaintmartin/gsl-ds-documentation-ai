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
| **The concept** | What compliance means. The six checks. Hard fail vs deduction vs flag. Thresholds. Scoring | **this file** |
| **What to measure** | Stated in design-system vocabulary — "every element must be an instance of a library component" | **this file** |
| **How to measure it** | Figma reads its component keys; web reads its package imports; iOS reads its view hierarchy | **the consuming agent's repo — one adapter per platform** |

**Nothing tool-specific belongs in this file.** No API names, no node IDs, no
framework vocabulary. If a check cannot be stated without naming a tool, it is
not yet a design-system rule and does not belong in the scorecard.

---

## What compliance means

**Reuse before invention.** Use an existing component or an authorised token
wherever one fits; create something new only when nothing does, and declare it
when you do.

Compliance is **not** quality. Compliance is arithmetic — "is every colour bound
to an authorised token?" has one right answer. Quality is judgment and is not
scored here. Every run records a human quality verdict alongside its compliance
score, so a quality bar can later be written from real judgments.

---

## The adapter contract

### What an adapter is

**A translator, not a checker.** An adapter reads generated output using its own
platform's mechanisms, then restates everything it found in design-system
vocabulary. After it runs, the platform is gone — the checks never see a tool.

That is what lets one scorecard judge Figma output today and web or native
output later. A new platform means a new adapter, never a new scorecard.

An adapter contains **no rules**. It never decides whether something is
compliant; it only reports what is there. Every judgment lives in the checks
below.

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
   Compares the facts against the inventory, the deny-lists,
   and **Highest tier first**'s parts lists
        │
        ▼
5. THE REPORT           hard fails, then scores, then flags
```

### Who owns what

| Owned by **this repo** | Owned by the **consuming agent's repo** |
| --- | --- |
| The contract — which facts must be reported | The adapter — how its platform answers |
| The checks, thresholds and report format | The runner that executes them on real output |
| The design-system names the facts must use | The translation from local identifiers into those names |

A gap in an adapter is a defect in the consuming repo. A check that cannot be
expressed as a question about facts is a defect **here**.

### Required facts

A platform that cannot supply these cannot be scored.

| Fact | Meaning in design-system terms |
| --- | --- |
| `element.isLibraryComponent` | Is this element an instance of a design-system component, or was it built locally? |
| `element.componentName` | If it is a library component, which one — by the name used in the Figma registries and **The inventory**'s inventory |
| `element.children` | Which elements this one contains, so a locally-built composition can be examined |
| `property.isTokenBound` | Is this styled property resolved through a design token, or written as a literal value? |
| `property.tokenName` | If bound, which token — by the name used on the token pages |
| `property.kind` | What is being styled: colour · type style · spacing · radius · border width · shadow |
| `output.declarations` | The declarations the generating agent produced under **When nothing fits** |

### Optional facts

A check that needs one a platform cannot supply reports `unavailable`, never
`0%`.

| Fact | Used by | If missing |
| --- | --- | --- |
| `element.viewportTier` | `C6 · Layout` | `C6 · Layout` stays inactive on that platform |
| `element.isComponentInternal` | `C3 · Token binding` | `C3 · Token binding` cannot exclude a component's own internals, so it reports `partial` |
| `element.locator` | The report | Findings are named but not addressable |

**`unavailable` is not a passing score and not a failing one.** It records that
the platform could not answer, which is a gap in the adapter, not in the output.

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

The two elements above, and what each check concludes.

**`12:3401` — a library Button**

| Check | Facts used | Verdict |
| --- | --- | --- |
| `C1 · Provenance` | library component, named `Button` | **pass** — `Button` is in the Components registry and not on the never-select list |
| `C2 · Tier ceiling` | not a local build | **not applicable** |
| `C3 · Token binding` | both properties token-bound | **pass** |
| `C4 · Authorisation` | `Surface/Brand/Primary/default` · `Spacing/16` | **pass** — neither is on a deny-list |
| `C5 · Declaration` | not an invention | **not applicable** |

**`12:3500` — a local build containing `Card`, `Image Slider` and `Tag`**

| Check | Facts used | Verdict |
| --- | --- | --- |
| `C1 · Provenance` | local build | **deduction** — it duplicates something the inventory contains |
| `C2 · Tier ceiling` | three of `Listing Card`'s parts | detected composition → verdict decided by `C5 · Declaration` |
| `C3 · Token binding` | one colour is a literal, `#1A1A1A` | **hard fail** — "never write a raw colour" |
| `C4 · Authorisation` | `Radius/8` | **pass** |
| `C5 · Declaration` | the declaration names an agency banner, not this | **hard fail** — no declaration covers this element, so `C2 · Tier ceiling` also hard-fails |

Note what the checker never had to decide: whether `12:3500` *is* a Listing
Card. It only had to count parts and look for a declaration.

### Naming, across platforms

Component and token names in the facts above are always **design-system names** —
`Listing Card`, `Spacing/16`, `body/16/regular` — never a platform's local
identifier. Translating a local identifier into a design-system name is the
adapter's job, and the reason `figma/*-registry.json` exists.

---

## How a run is scored

**One run = one output.** Whatever the generating agent produced from a single
wireframe and brief. If it produced three screens from one brief, that is one
run.

Six checks, `C1`–`C6`. Each is scored **independently**.

| | |
| --- | --- |
| **A hard fail fails its own check only** | It does not sink the run. Extend to run-level gating once the checker is proven — see [compliance-audit.md](compliance-audit.md) |
| **A deduction lowers a check's percentage** | The check can still pass |
| **A flag scores nothing** | It is recorded as a finding, for the ledger below |
| **`unavailable` scores nothing** | The adapter could not supply a required fact |

### Always write a check's name, never just its number

`C1 · Provenance`, not `C1`. Six two-character codes are not memorable, and a
report or a conversation that uses bare codes cannot be followed by anyone who
did not write it. This applies to every report, every audit entry, and every
sentence anyone writes about a run.

The report that carries these scores is a file, and its format is fixed. See
[The report](#the-report).

### Thresholds

**A threshold is derived from a rule, or it is "no regression". Never invented.**

| Check | Threshold | Where it comes from |
| --- | --- | --- |
| `C1 · Provenance` | **no regression** | No rule states a number |
| `C2 · Tier ceiling` | **0 undeclared compositions** | **Highest tier first** + **When nothing fits** |
| `C3 · Token binding` | **100%** | "Never write a pixel literal" · "Never write a raw colour" |
| `C4 · Authorisation` | **0 deny-listed** | The *Never use* / *Do not use* tables |
| `C5 · Declaration` | **100% of inventions declared** | **When nothing fits** |
| `C6 · Layout` | inactive | — |

**"No regression" compares runs of the same wireframe only.** Comparing a search
results page against a form measures the difficulty of the brief, not the
compliance of the output. Across different wireframes, report the score and do
not gate on it.

---

## The report

### A report is a file

**Every run produces a report, and the report is part of the output.** A run
whose screen exists but whose report does not is an unfinished run, not a
passing one.

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
| `report.md` | **yes** | the checking agent | The verdict. Template below |

**Why `facts.json` is kept rather than discarded after scoring.** When a rule or
a threshold changes, the checker can be re-run against a stored `facts.json` —
answering *would the new rule have caught the old mistake?* without regenerating
anything. Discard it and the next scorecard edit orphans every run before it.

### Report order is fixed

**Hard fails print first, by name, above any percentage.** A report that opens
with "C1 94%, C3 88%" reads as broadly fine even when it contains platform
chrome. Percentages never appear before the gates they could disguise.

**Every heading below appears in every report, including the empty ones.** A
*Hard fails (0)* heading is information. A missing one is ambiguous — the reader
cannot tell whether there were none or whether nobody looked.

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

The **wireframe** label is what makes `no regression` meaningful: two runs are
only comparable when this label matches.

## Hard fails (2)

| Check | Subject | Where | Why |
| --- | --- | --- | --- |
| `C1 · Provenance` | `Status Bar` | `12:3401` | On the never-select list — **Never select** |
| `C4 · Authorisation` | `Spacing/56` | `12:3500` | Deny-listed — spacing's *Do not use* |

## Scores

| Check | Score | Verdict |
| --- | --- | --- |
| `C1 · Provenance` | 94% | **FAIL** — 1 hard fail |
| `C2 · Tier ceiling` | 100% | PASS — 4 of 10 **Highest tier first** rows checked |
| `C3 · Token binding` | 88% | **FAIL** — threshold is 100% |
| `C4 · Authorisation` | — | **FAIL** — 1 deny-listed token |
| `C5 · Declaration` | 100% | PASS |
| `C6 · Layout` | — | INACTIVE |

A check whose facts the adapter could not supply reports `unavailable` — never
`0%`. `C2 · Tier ceiling` always states its coverage, because it reaches 4 of
**Highest tier first**'s 10 rows and must never imply it enforced all ten.

## Flags (1)

Findings, not failures. Also appended to
[the flag ledger](../../compliance-flag-ledger.md).

| Check | Subject | Why flagged |
| --- | --- | --- |
| `C4 · Authorisation` | `Spacing/40`, 3 elements | Unprecedented — no rule authorises or forbids it as a section gap |

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
| [compliance-run-ledger.md](compliance-run-ledger.md) | One row for the run — its scores and hard-fail count, so runs can be compared without opening any report |
| [compliance-flag-ledger.md](compliance-flag-ledger.md) | Every flag raised, so a finding seen three times can be spotted |

---

## C1 · Provenance

**Is each element a real library component, or was it built by hand?**

| | |
| --- | --- |
| **Enforces** | **The inventory** — a name absent from it does not exist · **Never select** |
| **Measure** | Every element reported as a library component must name a component that exists in the inventory. Every element **not** reported as a library component is a local build, and is examined by `C2 · Tier ceiling` |
| **Score** | library components ÷ (library components + local builds that duplicate an existing component) |
| **Facts used** | `isLibraryComponent` · `componentName` |

**Hard fail**

- A component on the **Never select** list: platform chrome, brand assets,
  another component's internals, or a withheld component.
- A component name that appears in no registry — it came from outside GSL.

**Deduction** — a locally-built element that duplicates a component the
inventory already contains.

**What this check cannot see** — whether the *right* component was chosen. `Chip`
where `Tag` was correct passes completely. That is the eval's job, not the
scorecard's.

---

## C2 · Tier ceiling

**Was a higher-tier component reinvented out of lower-tier parts?**

Where real compliance failures live. `components-rules-ai.md` calls it "the
single most common compliance failure".

| | |
| --- | --- |
| **Enforces** | **Highest tier first** — reach for the highest tier that fits |
| **Measure** | For each locally-built element, collect the library components it contains. Compare against the **parts list** of each **Highest tier first** row. Two or more parts of the same higher-tier component is a detected composition — the ruleset's own *count the parts* test |
| **Score** | 1 − (undeclared compositions ÷ local builds examined) |
| **Facts used** | `isLibraryComponent` · `componentName` · `children` · `declarations` |

**`C5 · Declaration` decides what a detection means.** This is what makes the
check decidable rather than a judgment call:

| Detected composition | Declaration | Verdict |
| --- | --- | --- |
| yes | **absent** | **Hard fail.** A higher-tier component was rebuilt, unannounced |
| yes | present, naming the higher-tier component and why it was ruled out | **Flag** → *awaiting human decision* |
| no | — | pass |

The checker never has to answer *"is this secretly a Listing Card?"*, which needs
a human. It only answers *"did the agent say what it was doing?"*, which does
not.

### Coverage — this check reaches 4 of **Highest tier first**'s 10 rows

**Highest tier first** now carries a machine-readable **Parts** column, so the check can run. It
does not cover every row, and reports which it skipped rather than passing them
silently.

| Kind | Rows | Covered? |
| --- | --- | --- |
| **Composed** — assembled from public components | `Listing Card` · `Filter bar` · `Wizard` · `Phone Number Field` | **yes** |
| **Container** — a shell with content slots | `Info State` · `Table` | no — no characteristic parts to count |
| **All-or-nothing** — used whole or not at all | `Map template` | no — no partial composition exists to detect |
| **Unresolved** | `Floor selection` · `Listing summary` · `Estimation card` | no — open questions in `components-audit.md` |

**Highest tier first still applies to all ten.** Six simply cannot be enforced by counting
parts. A report must state coverage as *4 of 10 rows checked*, never imply the
whole rule was enforced.

**Detecting a rebuilt container is unsolved.** Nothing currently catches an
agent that hand-builds an empty state instead of using `Info State`, because
there is no part set that characterises one. It needs a different mechanism, and
none is designed.

**What this check cannot see** — a composition of exactly one part. By the
ruleset's own threshold that is **Which component** territory, not a **Highest tier first** violation.

---

## C3 · Token binding

**Are values bound to design tokens, or written as literals?**

| | |
| --- | --- |
| **Enforces** | spacing's **No pixel literals** · colour's **No raw colour** · typography's **No hand-set fonts** |
| **Measure** | Every styled property — colour, type style, spacing, radius, border width, shadow — must be reported as token-bound |
| **Score** | token-bound properties ÷ all styled properties |
| **Threshold** | **100%.** The rules say never, not rarely |
| **Facts used** | `isTokenBound` · `tokenName` · `kind` · `isComponentInternal` *(optional)* |

**Hard fail**

- A colour written as a literal rather than resolved through a token.
- A spacing, radius or border-width literal.
- Type properties — family, size, weight, line height — set individually instead
  of through a text style.
- **Overriding a library component's own internal styling.**
  spacing's **Components first** says never do it.

**Deduction** — a property bound to a token from outside the GSL token set.

**Not counted** — a library component's internal properties. They belong to the
component and are correct by construction. If the adapter cannot distinguish
internals from local styling, this check reports `partial`.

**What this check cannot see** — whether a bound token is *allowed*. That is
`C4 · Authorisation`, and it is the difference between output that is
token-bound and output that is compliant.

---

## C4 · Authorisation

**Are the bound tokens allowed, or merely existing?**

The check the token audits paid for. 83 of 218 colour tokens have no consumer,
`Spacing/56` has no documented purpose, and no component binds a Display type
style. Without this check, output can score 100% on `C3 · Token binding` and
still rest entirely on values the audits rejected.

| | |
| --- | --- |
| **Enforces** | The *Never use*, *Restricted* and *Do not use* sections of the three token rulesets |
| **Measure** | Each bound token name is classified against three lists |
| **Threshold** | **0 deny-listed** |
| **Facts used** | `tokenName` · `kind` |

| Class | Source | Verdict |
| --- | --- | --- |
| **Forbidden** | `color-rules-ai.md` *Never use* — the symbol, native, scale and decorative-surface families, the focus border, the unreachable status leaves, the enumerated orphans · `spacing-rules-ai.md` *Do not use* · typography's **No Display** — the Display family | **Hard fail** |
| **Restricted** | `color-rules-ai.md` *Restricted* — allowed only as described | **Flag** → *awaiting human decision* |
| **Unprecedented** | Exists, is not forbidden, but sits outside the preferred set — e.g. outside typography's **The eleven used styles** | **Flag, never a failure** |

**Why unprecedented is a flag and not a deduction.** The rulesets say *prefer
these*, not *only these*. A scorecard stricter than the ruleset it enforces
blames the agent for reading the documentation correctly. And the flags are
findings in their own right — an agent reaching for an unprecedented token may
be revealing a gap in a ruleset rather than making a mistake. See the ledger.

**What this check cannot see** — whether an authorised token is the *right*
authorised token. A subdued surface where a default one was meant passes.

---

## C5 · Declaration

**When something new was invented, was it declared?**

| | |
| --- | --- |
| **Enforces** | **When nothing fits** — compliance means reuse before invention, not never inventing |
| **Measure** | Every local build flagged by `C1 · Provenance` or `C2 · Tier ceiling` must have a declaration |
| **Score** | declared inventions ÷ total inventions |
| **Threshold** | **100%** |
| **Facts used** | `declarations` |

A declaration must state all three:

1. **What was built.**
2. **Which problem from Which component it belongs under.**
3. **Which existing components were ruled out, and why.**

**Hard fail** — an invention with no declaration, or a declaration missing any
of the three parts. **When nothing fits**'s own words: *an undeclared new component is a
compliance failure even when it looks right.*

**A declared invention does not expire, and is never auto-promoted.** If the
same invention is declared repeatedly it is flagged as *awaiting human decision*
— it may be a missing component rather than a one-off, and only a person can
settle that. An open decision blocks nothing; it accumulates until it is ruled
on.

**This check is the pivot of the whole scorecard.** It converts
`C1 · Provenance` and `C2 · Tier ceiling` from judgment calls into decidable
ones.

---

## C6 · Layout · **INACTIVE**

**Does the page composition follow the documented rhythm?**

Defined so it is not forgotten. **Not scored, and not reported as a percentage,
until **Block 3 · Layout** completes.**

| | |
| --- | --- |
| **Would enforce** | spacing's **Container padding** · **Page rhythm** per tier · `grid-tokens.md` outer margin and gutter |
| **Would measure** | Outer margin, section gap, card-grid gap and form-field gap against spacing's **Page rhythm** table for the output's viewport tier; container padding against **Container padding** |
| **Facts used** | `viewportTier` *(optional)* — a platform that cannot report it leaves this check inactive |

**Why it is switched off.** Rules 6 and 7 carry an explicit warning in the
ruleset itself: *"Rules 6 and 7 are unverified. They describe product-page
composition, which lives outside the component library and could not be checked.
Follow them as the documented intent, but they do not carry the same evidence as
Rules 3–5."*

Scoring against unverified rules manufactures confidence the evidence does not
support. **Block 3 · Layout** verifies them against real product screens; this check
activates then, and this section says so rather than quietly scoring anyway.

---

## The flag ledger

**Flags accumulate across runs.** A flag in one run is noise; the same flag in
three runs is evidence a ruleset is missing a case.

Recorded in [compliance-flag-ledger.md](compliance-flag-ledger.md), appended
after every run, never rewritten.

| Column | Meaning |
| --- | --- |
| Run | Which run raised it |
| Check | Its number **and name** — `C4 · Authorisation` |
| Subject | Token name, component name, or element |
| Why flagged | Restricted · unprecedented · declared invention |
| Times seen | Cumulative across all runs |
| Verdict | `awaiting decision` · `ruleset gap` · `agent error` · `accepted` |

**A subject seen three times is raised for a human decision** — it is not
auto-promoted and not auto-dismissed. Gabriel rules on it, and the verdict says
which of the four it was. If the verdict is `ruleset gap`, it becomes an entry in
the relevant `-audit.md`, exactly as the component eval's misses did.

This is the mechanism by which running the checker improves the knowledge base
rather than only grading output.

---

## Runs

**The run log lives in [compliance-run-ledger.md](compliance-run-ledger.md)**,
one row per run, append-only.

It used to sit in this file, and moving it out is the point. **This file is the
ruler; a run log is a measurement.** A ruler is rewritten whenever a rule or a
threshold changes — and rewriting a file that also holds what happened on a date
reaches back and edits history. Keeping them apart is what lets the rules change
while the evidence stays fixed. It is the same split as
`-rules-ai` against `-ledger` everywhere else in this repo.

There is a second, duller reason: this file is read **before every run**. A log
that grows by a line each time a screen is generated does not belong inside it.

Record every run, including bad ones. A log that holds only good runs is a
highlight reel, not evidence.

---

## What this scorecard cannot see

Stated plainly so a passing score is not mistaken for a good screen.

| Blind spot | Whose job |
| --- | --- |
| Whether the **right** component was chosen | `components-eval.md` |
| Whether the **right** authorised token was chosen | Nothing yet |
| Whether the screen is **usable** | Human |
| Whether the screen is **good** | Human — the quality bar, undocumented by design |
| Page composition | `C6 · Layout`, inactive until **Block 3 · Layout** |
| Copy and tone | Nothing yet — `Content & UX Writing` is empty in 15 of 57 component docs |
| Accessibility beyond token choice | Nothing yet — `Accessibility (a11y)` is empty in 51 of 59 component docs |

A screen can score 100% on every active check and still be the wrong screen,
badly written and inaccessible. That is not a flaw in the scorecard; it is the
boundary of what compliance means.

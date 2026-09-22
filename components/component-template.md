_One sentence. What this component is, and its primary UX purpose._

![](images/<hash>.png)

_Optional hero image. Keep it where the source put it — directly under the
summary, above the readiness table._

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | To Do 🚧 | To Do 🚧 | Ready ✅ |

_**Figma answers a different question from the other three.** It says whether the
component exists in a Figma library — a Figma link below means yes. Web, iOS and
Android say whether it is built on that platform._

* [[Component Name] on Figma](<figma url>)
* [[Component Name] on Storybook](<storybook url>)

---

## Usage

_Narrative. The component's core purpose, what triggers it, where it sits in a
user flow._

### Platform
<!-- column: Platform -->

_Only when the source says something platform-specific — custom versus native,
or a real behavioural difference between Web, iOS and Android. **Omit the whole
section when there is nothing**, rather than writing "Not documented". The
readiness table above already says which platforms exist._

### When to use
<!-- column: When to use -->

* [A user intent or UI context where this component is right]
* [A condition where this component is required]

### When NOT to use
<!-- column: When NOT to use -->

* [A condition where another component is better] — _Use [Alternative] instead._

### Variant Selection Flow
<!-- column: Variant flow -->

```
VARIANT SELECTION FLOW
1. [Question that settles the primary need]?
   ├── YES ──> Use `[Variant A]` (Limit: 1 per section)
   └── NO ───> Go to Step 2

2. [Question that settles the secondary need]?
   ├── YES ──> Use `[Variant B]`
   └── NO ───> Go to Step 3
```

### Usage Guidance
<!-- column: Usage guidance -->

| DO | DON'T |
| --- | --- |
| ![DO](images/<hash>.png)<br>**DO:** [Global usage rule] | ![DON'T](images/<hash>.png)<br>**DON'T:** [The same rule, from the other side] |

_An unpaired DO goes in its own single-column table. Never in a shared row with
an empty cell:_

| DO |
| --- |
| ![DO](images/<hash>.png)<br>**DO:** [Rule with no opposite in the source] |

### Related Components
<!-- column: Related -->

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **[Component A]** | High / Med / Low | [One-line distinction] | [Specific scenario] |

## Variants & Modifiers
<!-- column: Variants -->

### [Variant Category Name]

#### [Variant Name]

| Variant A | Variant B | Variant C | Variant D |
| --- | --- | --- | --- |
| ![Variant A](images/<hash>.png) | ![Variant B](images/<hash>.png) | ![Variant C](images/<hash>.png) | ![Variant D](images/<hash>.png) |

_Description of this variant: visual weight, and when it is used._

| DO | DON'T | CAUTION |
| --- | --- | --- |
| ![DO](images/<hash>.png)<br>**DO:** [Rule for this variant only] | ![DON'T](images/<hash>.png)<br>**DON'T:** [Rule for this variant only] | ![CAUTION](images/<hash>.png)<br>**CAUTION:** [Rule for this variant only] |

### Modifiers
<!-- column: Modifiers -->

#### [Modifier Name]

_Functional behaviour, visual rules, scaling constraints._

## Behavior & Responsiveness

### Interactive States & Loading
<!-- column: States -->

* **Default / Hover / Pressed:** [Interaction feedback]
* **Disabled:** [Guidance]

### Touch Target & Layout
<!-- column: Touch target -->

* **Touch Target:** Minimum height `[e.g. 40px]` on touch devices.
* **Width Adaptability:** [Fixed width, content-hug, or full-width container]

### Breakpoints & Platform Adaptations
<!-- column: Breakpoints -->

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Mobile (<600px)** | [Behaviour] |
| **Desktop (>600px)** | [Behaviour] |

## Content & UX Writing
<!-- column: Writing -->
<!-- required: Capitalization, Label Formula, Length Limits -->

_These three are asked of **every** component. Answer them, or write
`Not documented` after the label. They are what makes one writing rule
comparable across the whole library — an audit can ask "does this component
state its capitalization rule?" and get an answer for all of them._

* **Capitalization:** [e.g. Sentence case]
* **Label Formula:** [e.g. {Action Verb} + {Noun}]
* **Length Limits:** [e.g. Maximum 3-4 words]

### [Writing topic]

_Free slot, and optional. What this component needs and no other does —
`rating` states number notation per language, `energy-tag` states per-country
wording. Add as many as the component actually has, or none._

_**Behaviour is not writing.** How a field scrolls when its content overflows
belongs in `Touch Target & Layout`, however much it is about content._

## Accessibility (a11y)
<!-- column: a11y -->

* **Keyboard Navigation:** [Focus order, trap behaviour, escape dismissal]
* **Screen Readers:** [ARIA roles, live regions]

## [A section the source has nothing for]

Not documented

---

# How to use this template

_Everything below this line is instructions. It is not part of a component doc —
delete it. The headings above are._

## What this file is

**The one definition of a component doc.** Three things at once:

| For | What it is |
| --- | --- |
| `components/coverage.py` | The contract. It reads the headings below, not a list of its own |
| A generator | The target shape to fill |
| A human contributor | The page you read before writing one by hand |

Because the checker reads this file, the template and the check cannot drift
apart. Change a heading here and the coverage ledger changes with it.

## A usage doc never names a tool

**Gabriel, 22 September 2026.** This page describes the component. Figma,
Zeroheight and Storybook are tools, and a page written in terms of one becomes a
reference for that tool instead of a description of the component.

**Confluence is stricter than the rest — it may not be mentioned at all.**
Gabriel, 22 September 2026. Not in the content, and not as a link either: a doc
that points at a Confluence page sends a reader somewhere this repo does not
control and most agents cannot open. The one place the word is allowed is an
`-audit` file recording where a fact originally came from.

| Where a tool name is fine | Where it is not |
| --- | --- |
| A link — `[X on Storybook](https://…)` | Anywhere in the content |
| The readiness table's `Figma` column | A tip about operating the tool |
| That component's own `<name>-figma.md` | A layer name, or where a fact was read from |

**A measurement is a property of the component, not of the tool.** Write
*"Height: 20"*, never *"Height: 20 in Figma"* — the component is 20 tall, and
where you measured it is not the reader's problem.

**What to do with the knowledge instead**, rather than delete it:

| Kind | Where it goes |
| --- | --- |
| A tip, a layer name, a quirk of how the tool renders it | `<name>-figma.md`, beside this doc. **Created only where there is something to say**, never empty |
| A key, a node ID, a variant count | The `figma/*-registry.json` files, which already hold them |
| Where a fact was read from, and when | `project/backlog.md`'s done list, and the registry's `auditedDate` |

There is no iOS or Android equivalent of `-figma.md` yet. Neither has a source
anyone has read.

`scripts/check-tool-neutral.py` enforces this.

## The rules that hold everywhere

These are layout rules. They apply to this markdown and to anything rendered
from it. They are not specific to one publishing surface.

| Rule | Why it exists |
| --- | --- |
| **A DO/DON'T row is always a matched pair** — a DO and the opposite DON'T of the same rule | A row with an empty or `—` cell renders as visibly broken |
| **An unpaired DO, DON'T or CAUTION gets its own single-column table** | Group several unpaired items of the *same* polarity into one table. Never one table per item |
| **A variant-comparison table caps at 5 columns** | Wider tables split silently when rendered, and the split-off half loses its header styling. Split it yourself — 5 + 5, never 6 + 4 |
| **Every image is a local file** — `images/<hash>.png`, relative to the doc | The hash is the Zeroheight asset identifier. It is how an image is matched back to its source |
| **Never rename an image file, and never open one to identify it** | Matching is by filename and hash only |

## A missing section

Write `Not documented` as the whole body. Leave the heading in place.

- `Not documented` tells a reader someone looked and the source had nothing.
- A missing heading tells them nobody ever looked.
- The coverage ledger marks those differently — ❌ against ⬜. Both are true things worth knowing.

The exception is `### Platform`, which is omitted entirely when it does not
apply. See that section above.

## The column markers

Each `<!-- column: X -->` marker names the column that heading becomes in
`components-coverage-ledger.md`. A heading with no marker is still a real
heading — it just isn't tracked as a column.

**Keep the markers in document order.** That order is the column order in the
ledger.

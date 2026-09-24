# Spec format for AI generation

_The format of a spec: the file a design agent writes and a build agent reads.
Created 24 September 2026. The worked example is [spec-001.md](spec-001.md)._

## What a spec is

A spec describes one interface in design-system names, and in nothing else.

```
source (a PRD, a brief, or a one-paragraph idea)
      │
      ▼
design agent ── writes ──► spec ── read by ──► build agent ──► running prototype
      ▲                                                             │
      └──────────── feedback edits the spec, then rebuild ──────────┘
```

| Who | Does what with the spec |
| --- | --- |
| **The design agent** | Writes it. Edits it on every round of feedback. It is the only writer |
| **A build agent** | Reads it and builds it on one platform. It never edits the spec |
| **A person** | Reads it to see what was decided and what was assumed |

**A spec is platform-neutral.** It never contains a Figma, web, iOS or Android
name, a code identifier, a file path inside an app, or a raw value such as a hex
colour or a pixel size. A build agent translates each neutral name with its own
platform's name map. On iOS that map is
[components-ios-map.md](../components/components-ios-map.md).

**A spec never says where to build.** The app, the branch, the Figma file or the
route is the build agent's input, passed beside the spec, never written into it.
The same spec must be buildable twice, in two places, without an edit.

**A spec never decides which component to use by itself.** The design agent
decides with [components-rules-ai.md](../components/components-rules-ai.md), the
token rulesets and [icons-rules-ai.md](../icons/icons-rules-ai.md). The spec
records the answer.

## Where specs live

| Path | What |
| --- | --- |
| `specs/spec-rules-ai.md` | This file. The format |
| `specs/spec-NNN.md` | One spec. `NNN` is three digits, the highest existing number plus one. Never reused |

**One idea, one spec file.** A round of feedback edits the same file and adds a
row to its change log. **A different idea starts a new spec file.** The test: if
the goals change, it is a different idea.

## Where every name in a spec comes from

**Every name in a spec must resolve in one of these files.** A name that resolves
in none of them is not allowed in a spec.

| Name of | Written as | Resolves in |
| --- | --- | --- |
| A component | The name in **The inventory** of `components-rules-ai.md`, in backticks. Example: `Text Button` | `components/components-rules-ai.md` |
| A variant | `Axis: Value`. The axis is the `###` or `####` heading under **Variants & Modifiers** in that component's own doc. The value is that section's column or option name. Example: `Emphasis: Secondary` | `components/<name>/<name>.md` |
| A modifier that is switched on or filled | `Modifier: on`, or `Modifier: "the text"`. Example: `Suffix: "€"` | `components/<name>/<name>.md` |
| A colour, text style, spacing, radius, shadow or border width | The token name in slash form, in backticks. Examples: `Content/Light/Default`, `body/14/bold`, `Spacing/16`, `Radius/4`. **Colour is always written in slash form**, as the colour family pages write it — never in the dotted form `content.light.default` that `color-rules-ai.md` also uses | The matching `tokens/<kind>/<kind>-rules-ai.md` decides whether it is allowed. The colour family pages linked from it confirm the slash name |
| An icon | The icon name, in backticks, with its variant axes. Example: `info` · `Circle: On` | `icons/icons-rules-ai.md` |

**A variant axis that the spec does not name is left at the component's
default.** Write only the axes that differ from the default, or that the rules
require you to state.

## The sections of a spec, in order

A spec has exactly these eight sections, in this order, under these headings.
**A section with nothing in it stays, and says `None.`** An absent section reads
as an oversight. A section that says `None.` reads as a decision.

| Section | Holds |
| --- | --- |
| `# Spec NNN — <what the screen is>` plus the header table | Identity and status |
| `## Source` | What the spec was made from, quoted or linked |
| `## Goals` | What the interface must let the user do |
| `## Acceptance criteria` | How anyone can tell, by looking at the built screen, that a goal is met |
| `## Assumptions` | Everything the source did not say that the spec had to decide |
| `## Screen` | The blocks and the elements, in reading order |
| `## Inventions` | Everything built outside the design system, declared |
| `## Change log` | One row per round of edits |

### The header table

| Field | Value |
| --- | --- |
| **Status** | `draft` or `agreed`. See **Status** below |
| **Width** | `mobile`, `tablet` or `desktop`. The width the screen is designed for |
| **Brand** | One of the six brands `color-tokens.md` names: `SeLoger`, `SeLoger Neuf`, `Logic Immo`, `Logic Immo Neuf`, `Belles Demeures`, `Meilleurs Agents`. `SeLoger` when the source names none, recorded as an assumption |
| **Last changed** | The date of the newest change log row, `YYYY-MM-DD` |

### Source

Either a link to the source file, or the source quoted in full in a blockquote.
**Never reword the source.** It is what every goal and every assumption is
measured against.

**A one-paragraph idea is a valid source.** A thin source produces a spec with
many assumptions. That is correct. It is never a reason to refuse or to stall.

### Goals

One table. Each goal is one thing the user must be able to do or understand.

| Column | Rule |
| --- | --- |
| **Goal** | A short kebab-case name. Example: `judge-running-cost`. It is a name, never a number |
| **What the user can do** | One sentence, from the user's side |
| **From** | `source` when the source states it. `assumed` when the design agent inferred it. An `assumed` goal also has a row in **Assumptions** |

**Every element in the screen serves at least one goal.** An element that serves
no goal is removed, or its goal is added as an assumption.

### Acceptance criteria

One table. Each criterion can be checked by a person looking at the built
screen, with no access to the spec's reasoning.

| Column | Rule |
| --- | --- |
| **Criterion** | One sentence that is true or false of the built screen. Example: _The monthly estimate is the most prominent figure in the Finance block_ |
| **Goal** | The goal it proves |
| **From** | `source` or `assumed`, as for goals |

**Every goal has at least one criterion.** A goal with no criterion cannot be
shown to be met.

### Assumptions

One table. **Anything the spec decided that the source did not say goes here.**
This is what lets a fast spec from a thin idea be safe: nothing invented is
hidden.

| Column | Rule |
| --- | --- |
| **Assumption** | What was decided, in one sentence |
| **Why** | What in the source, or in the rules, led to it |
| **Affects** | The element IDs, goals or criteria it changes |
| **Status** | `open`, `confirmed` or `rejected`, with who and the date for the last two. Example: `confirmed — Gabriel, 2026-09-24` |

**Copy the design agent wrote is an assumption.** Copy quoted from the source is
not.

**A rejected assumption is kept, not deleted.** The change log row that acted on
it names it.

### Screen

The screen is a list of **blocks**, top to bottom. Each block is a `###` heading
followed by one line and one table.

```
### <Block title> — `<block-id>`

Goal: `<goal>` · Stack: vertical · Gap: `Spacing/NN` · Padding: `Spacing/NN`

| ID | Element | Component | Variants | Copy | Data | Tokens | Behaviour | Inside |
```

**Stack, gap and padding** say how the block lays its elements out. Gap and
padding are spacing tokens. **Spacing guidance is not yet verified** — spacing's
**Container padding** and **Page rhythm** mark themselves unverified — so a
build agent treats these two values as the design agent's choice, not as a
checked rule.

**The table's rows are in reading order.** A build agent places them in that
order and never reorders them.

| Column | Rule |
| --- | --- |
| **ID** | `<block-id>.<element-name>`, kebab-case. Example: `finance.monthly-estimate`. **Unique in the spec. Never reused, never renumbered, never renamed** — feedback refers to an element by its ID |
| **Element** | What it is for, in plain words |
| **Component** | One of three: a component name from **The inventory**; `text` for plain text set in a text style; `composed` for anything built from parts, which must have a row in **Inventions** |
| **Variants** | Every variant and modifier that differs from the default, as `Axis: Value`, separated by ` · `. `—` when none |
| **Copy** | Every visible string, in double quotes, exactly as it must appear. A label that is spoken but never shown — the name of an icon-only control — is written in quotes followed by `, spoken only, never shown`. `—` when none |
| **Data** | Dynamic values, written one of three ways. **The source names the field:** `[fieldName]`, exactly as the source wrote it. **The source gives a value but no field name:** a short plain name, not in brackets, then the sample — `price, sample: 560.000 €`. Brackets always mean the source's own field name, so never put an invented name in them. **The value is computed from other elements:** `computed from` and their IDs — `computed from finance.price, finance.contribution`. A sample the source gave follows any of the three as `sample: …`. `—` when none |
| **Tokens** | **Only for `text` and `composed` rows.** For `text`: the text style and the colour. For `composed`: the words `See **Inventions**` — every token its parts use is listed there, under **What is built**. **For a library component this cell is always `—`**: a component carries its own tokens, and overriding them is not allowed |
| **Behaviour** | What happens on interaction, in plain words, from the user's side. A behaviour the prototype may fake says `mock`. `—` when static |
| **Inside** | The ID of the element whose slot this element fills. `—` when it sits directly in the block |

### Inventions

One `###` per `composed` element, headed with its ID. **Each has the three parts
that `components-rules-ai.md` requires under When nothing fits**, and a missing
part counts as the whole invention being undeclared:

| Part | What it says |
| --- | --- |
| **What is built** | The parts it is made of, named as components and element IDs, and **every token the parts use** |
| **Problem it belongs under** | The heading from **Which component** in `components-rules-ai.md` |
| **Ruled out** | Each existing component that looks like the answer, and why it is not |

**What needs declaring follows `components-rules-ai.md`, unchanged.** A frame
that only stacks things, and plain text in a published text style, are not
declared.

### Change log

One table, newest row at the top.

| Column | Rule |
| --- | --- |
| **Date** | `YYYY-MM-DD` |
| **What changed** | One sentence |
| **Why** | The feedback or the reason, quoted when it came from a person |
| **IDs** | Every element ID, goal, criterion or assumption touched |

**The first row is always the spec's creation.**

## Status

| Status | Means | Who sets it |
| --- | --- | --- |
| `draft` | At least one assumption is `open`. The spec can be built — prototypes are built from drafts all the time — but it is not decided | The design agent, on creation |
| `agreed` | Every assumption is `confirmed` or `rejected`, and the person who owns the idea has said so | The design agent, only when that person says so |

**A draft is built as readily as an agreed spec.** Status says what is decided,
never whether a prototype may be made.

## How feedback is applied

1. **Feedback edits the spec, never the built output.** A request such as "make
   the price bigger" is applied by the design agent to the spec. The build agent
   then rebuilds from the spec.
2. Find the element by its ID. Change that row. Leave every other row as it is.
3. A removed element: delete its row, and its **Inventions** entry if it has one.
   Its ID is never used again.
4. An added element: a new row with a new ID, in its reading-order position.
5. Add one change log row. Update **Last changed**.
6. If the feedback answers an assumption, set that assumption's status.

**Why the build agent never takes feedback directly:** a change made in the
built output and not in the spec is lost at the next rebuild, and the spec stops
describing what anyone saw.

## What a build agent does with a spec

- **Build every row, in order.** Skip nothing silently.
- **Translate each neutral name with the platform's name map.** Never guess a
  platform name that the map does not give.
- **When the platform has no equivalent** — the map says `not found` — build the
  closest thing from the platform's design system and **say so in its own
  report**, naming the element ID. Never edit the spec to match the platform.
- **Never change a variant, a token or a string** to make something fit.
  Report the conflict instead, naming the element ID.

## What a spec never contains

- A platform name, a platform component name, or a code identifier.
- A raw value: a hex colour, a pixel size, a font size, a font family. **A
  variant value copied from a component doc is not a raw value**, even when it
  reads like a size — `Radius: 8px` and `Size: 16` are names the doc gives, and
  they are allowed.
- A token on a library component's row.
- A destination: an app, a branch, a Figma file, a URL.
- Reworded source text.
- A decision that is not in the source and not in **Assumptions**.

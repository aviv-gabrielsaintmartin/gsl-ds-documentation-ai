# Run 002 — Listing detail, energy and finance blocks, mobile

| | |
| --- | --- |
| **Date scored** | 2026-09-14 |
| **Platform** | Figma |
| **Brief** | [brief-001.md](../brief-001.md) |
| **Destination** | Figma node `52-68179`, pasted with the brief on the day |
| **Output** | [block-1-energy-and-conditions.png](block-1-energy-and-conditions.png) · [block-2-finance.png](block-2-finance.png) |
| **Frame judged** | `132:5052` · page `Screen` |

_Metadata updated 15 September 2026: the `Wireframe` row was removed and a
`Destination` row added. The run now sits inside `brief-001/`, which is what
makes it comparable, so the label had nothing left to identify. **No answer and
no finding was changed.**_

_Reordered 14 September 2026 to the report format agreed that day. **No answer
and no finding was changed** — only the order and the wording. The original is in
git history._

## Verdict

The screen is built almost entirely from the design system. Twenty-six library
instances, and every token bound.

**Two things failed.** One block was built by hand and never declared, so nobody
can review whether building it was right. One component had its internal spacing
changed, which the rules forbid outright.

**Eight things need your ruling.** One of them looks like a Figma library bug
rather than a mistake by the agent.

Nothing on the screen used a forbidden token, a forbidden component, or a colour
written by hand.

## Decisions you need to make (8)

Rulings: `awaiting decision` · `agent error` · `ruleset gap` · `library defect` ·
`accepted`. **All eight were ruled by Gabriel on 14 September 2026**, in a cold
session that did not see the one that built or scored this run. None had been
seen in a previous run.

**The flag ledger carries three of these eight, not all eight.** Its rows were
written before failures were included there, and ledger rows are never
corrected. From run 003 on, every item in this table gets a row.

| What | Why it needs you | Ruling |
| --- | --- | --- |
| **The partner-offer block was built by hand and never declared** | The rules are clear that this fails. Whether the block should have been built at all is yours | **agent error** — building it was right, and nothing else in the libraries fits. The declaration was simply missing |
| **Four plain text nodes were built by hand and never declared** | Two section titles and two rating labels. The same rule catches them. They may be too small to be worth declaring, which would be a rules question | **ruleset gap** — the three-part declaration cannot be written for plain text. No problem heading covers writing a label, and no text component exists to rule out |
| **The donut chart's internal spacing was changed** | Its internal gap went from 56 to 2. The rules forbid touching a component's internals. Whether the chart needed it is yours | **ruleset gap** — no rule stated what the chart-to-legend gap should be. Now written: `Spacing/16` minimum, `Spacing/48` maximum |
| **The donut chart's legend sits beside the chart, not below** | The ruleset says below. The Figma component itself places it beside. One of the two is wrong, and this is not something the agent did | **library defect** — the component supports horizontal only and needs an alignment property. The ruleset's claim that the legend sits below was wrong and has been corrected |
| **`Energy tag` was used for the GES rating** | The rules say `Energy tag` is for energy ratings only. GES is emissions data. No scorecard question reaches this | **agent error** — not the colour. The tag and the scale beneath it state the same information twice in one container. The tag itself is defensible |
| **The energy scale colours were used** | A restricted family, used exactly as the rules describe. Restricted means a person looks | **accepted** — used exactly as the France table describes, including white letters on A and G only |
| **The CO₂ scale colours were used** | Used in the stated order. The rules record that ordering as never verified against code | **accepted** — used in the stated order, lowest to highest. The ordering stays marked unverified against code |
| **White letters on four CO₂ steps** | No rule allows or forbids it. It may be a gap in the rules rather than a mistake | **ruleset gap** — no rule existed. `Constant/White` on `Blue400`–`Blue700` was correct; `Default/Default` on `Blue100`–`Blue300` fails in dark mode at 1.49:1. Rule now written |

## Answers

| Step | Question | Answer | Reason |
| --- | --- | --- | --- |
| Define the content | _no question yet_ | — | — |
| Define the components to use | Was any element hand-built instead of taken from the library? | **yes** | **A finding, not a failure.** Five things were built by hand. Three are declared, two are not |
| Define the components to use | Was any never-select component used? | no | `Cell Content` is on the list but its own row permits this use, and **Which component** names it for exactly this case |
| Define the components to use | Was any component name used that appears in no registry? | no | Every library key resolves. The one local component is counted as hand-built, not as an outside name |
| Define what needs to be built | Was anything hand-built without a complete declaration? | **yes** | **Failure.** The partner-offer block has no declaration. Four plain text nodes have none either |
| Choose the tokens | Was any styled value written as a literal instead of bound to a token? | no | Every colour, text style, padding and gap resolves to a token. No hex anywhere |
| Choose the tokens | Was a library component's internal styling overridden? | **yes** | **Failure.** The donut chart's internal gap was changed from 56 to 2, bound to nothing |
| Choose the tokens | Was any deny-listed token used? | no | Checked against all six deny-lists. The two scale families are restricted, not denied |
| Choose the tokens | Was any token used that is not in the GSL token set? | no | Every name resolves on a token page routed from `tokens-index.md` |
| Put them on the screen | _no question yet_ | — | — |
| Place them according to the design guidance | _inactive_ | — | — |
| Check the content | _no question yet_ | — | — |

## Declarations (3)

Written by the generating agent, before scoring. Never edited afterwards.

### Seven-step rating scale (DPE and GES)

| | |
| --- | --- |
| **What was built** | Two horizontal seven-step scales, one under each rating, running best to worst. Each step is a rounded cell filled with its own scale token and carrying its class letter; the step matching this property's class is raised and set in the inverted content colour. The DPE scale is bound to `Scales/Energy/*` in the French A–G mapping (Green100, Green200, Green400, Yellow100, Orange100, Red100, Red200). The GES scale is bound to `Scales/CO2/Blue100`–`Blue700`, lowest to highest emission, because GES is greenhouse-gas emission data and the colour ruleset forbids energy colours for CO₂. Cell radius `Radius/4`, gaps and padding `Spacing/4` and `Spacing/8`, letters in `body/12/bold`. |
| **Problem it belongs under** | Showing progress and data |
| **Ruled out** | `Energy tag` — it is the grade call-out, not the scale: one letter in one coloured tag, 33×24 in Figma, with no seven-step ladder inside it, so it was placed beside each scale rather than instead of it · `Bar graph` — compares quantities across categories, and the seven classes carry no quantity to compare, only a position · `Progress bar` — linear task or goal completion, and this is neither a task nor a goal · `Progress circle` — same reason, in a circular format · `Donut chart` — shows how a total divides into parts of a whole, and a rating scale is not a total · `Slider` — an input control for selecting a value, whereas this scale is read-only and the buyer cannot move it · `Tag` — a single status label, not a scale |

### Finance simulator block

| | |
| --- | --- |
| **What was built** | The composed simulator the buyer adjusts: three inputs (property price and contribution as `Text Field` with a € suffix, loan duration as `Dropdown`), the recalculated answer shown with `KPI` plus a hand-set "per month" qualifier carrying footnote marker 1, the make-up of that figure shown with `Donut chart` with its legend switched on, and the three amounts as a list of `Cell Content` rows each carrying an info icon for its on-demand explanation. Footnote marker 2 is a hand-set superscript beside the partner-offer button. The container, the section stacking and the two footnote markers are the hand-built part; every control inside is a design-system component. |
| **Problem it belongs under** | Computing a figure from user input |
| **Ruled out** | `Estimation card` — it presents a completed estimate and carries no controls to adjust, whereas this block's whole purpose is that the buyer changes three numbers and the figure moves · `Wizard` — the buyer adjusts the three inputs freely and in any order, not through ordered, gated steps · `Filter bar` — its controls narrow a list of results, and these controls produce a figure · `KPI` on its own — it shows the figure but carries no controls, and it was used for exactly that half · `Slider` and `Counter field` — considered for the price and contribution inputs and rejected because the brief asks for exact euro amounts entered directly, not approximate values dragged or stepped |

### Hand-laid lists of Cell Content rows

| | |
| --- | --- |
| **What was built** | Two vertical lists laid out by hand, each a stack of `Cell Content` rows separated by `Divider` instances: the six property facts in Block 1 (label as title, value as body, non-clickable) and the three breakdown amounts in Block 2 (clickable, with a trailing info icon). The rows and the dividers are design-system components; the containers holding them are mine, because no `List` component exists in any GSL library. |
| **Problem it belongs under** | Grouping and structuring content |
| **Ruled out** | `Tables` — the rows are label-and-value pairs, not tabular data compared across shared columns · `Card` — these rows do not belong inside one grouped visual container, and the finance breakdown is already set apart by the chart above it · `Button card` — neither list is a single navigational action · `Toggle group` — no row carries an on/off setting · `Accordion` — the facts are always visible, and progressive disclosure is handled by the "See more" `Text Button` instead |

## Evidence

Written for a machine and for a dispute. Every locator lives here.

### How the screen was read

**Proved.** The frame was walked node by node through the Figma Plugin API. For
every node the walk recorded its type, its main component where it is an
instance, its overridden fields, its bound variables, its fills, strokes, corner
radius, padding, gap, effects and text style.

**Proved.** The live frame matches both screenshots in the run folder. A fresh
render of `132:5052` was compared against them.

**Proved.** The `## Declarations` section above was not read until the inventory
was complete, and was not edited.

### The inventory

**Proved.** The frame holds **26 library instances** and **50 nodes that are not
library instances**. One further element sits outside the frame: a local
component on the `Screen` page, swapped into a library `Card`.

| Library component | Instances | Where |
| --- | --- | --- |
| `Cell Content` | 9 | six property facts, three breakdown amounts |
| `Divider` | 7 | between facts, between breakdown rows |
| `Energy tag` | 2 | DPE grade, GES grade |
| `Text Field` | 2 | property price, your contribution |
| `Dropdown` | 1 | duration of our loan |
| `Text Button` | 1 | "See more" |
| `KPI` | 1 | the estimated monthly figure |
| `Donut chart` | 1 | the payment breakdown |
| `Card` | 1 | the partner offer |
| `Button` | 1 | "Customize simulation", nested in the local component |

**Proved.** Every one of those component keys resolves to a name in
`figma/figma-components-registry.json` or `figma/figma-patterns-registry.json`.
The two swapped-in icons, `chevron-right` and `info`, both resolve by name in
`figma/figma-icons-registry.json`.

### What was hand-built

**Proved.** The 50 non-instance nodes group into five things.

| Hand-built | Nodes | Locator | Declared? |
| --- | --- | --- | --- |
| Two seven-step rating scales — 14 cells, 14 letters, 2 containers | 30 | `133:5097` · `134:5090` | **yes** — declaration one |
| Layout containers and section stacking across both blocks | 11 | — | **partly** — declarations two and three each claim their own containers |
| Section titles and rating labels, as plain text | 4 | `133:5081` · `133:5085` · `134:5078` · `134:5968` | **no** |
| "per month" and the two footnote markers | 3 | — | **yes** — declaration two |
| The partner-offer content block | 5 + 1 local component | `138:5263` | **no** |

### The partner-offer block

**Proved.** `Partner offer content` is a **local Figma component**, node
`138:5263`, authored on the `Screen` page. Its key resolves in no registry. It is
swapped into the `Card`'s content slot through the `Content` property, which is
the documented way to fill a Card.

It contains two hand-set text nodes — "Find the right financing" and "Get a free,
personalised mortgage estimate with our partner Credit Agricole" — two hand-built
frames, a `Button` instance, and footnote marker 2.

**Proved.** No declaration block names a partner offer. Declaration two mentions
"the partner-offer button" in passing, states no problem heading for the block,
and rules out no component for it. All three required parts are absent, so the
declaration is absent. Footnote marker 2 is declared; the block holding it is not.

### Overriding a component's internals

**Proved.** The `Donut chart` instance at `136:5237` has its internal `Graph`
frame's gap changed from **56 to 2**. The main component's value is 56; the
instance's is 2, bound to nothing. That is a local spacing change on a library
component's internal frame.

**Not proved.** The chevron inside the `See more` `Text Button` at `134:5947`
carries `Color/Content/Interactive/Default`. The `chevron-right` icon
component's own vector carries `Color/Content/Default/Default`, so Figma lists
the fill as overridden. The `Text Button`'s own label is also
`Color/Content/Interactive/Default`, so the value may come from the component's
icon slot rather than from the agent. The slot's fill inside the main component
could not be read.

**Proved.** The `info` icons in the three breakdown rows carry
`Color/Content/Default/Default`, which is the `info` component's own fill. Those
override entries are an artefact of the instance swap, not a restyle.

### Tokens

**Proved.** Every colour in every hand-built element is bound to a variable. No
hex, no unbound paint. The full set used in hand-built elements:

- `Color/Background/Default`
- `Color/Content/Default/Default` · `Color/Content/Light/Default` · `Color/Content/Constant/White/Default`
- `Color/Scales/Energy/Green100` · `Green200` · `Green400` · `Yellow100` · `Orange100` · `Red100` · `Red200`
- `Color/Scales/CO2/Blue100` through `Blue700`
- `Spacing/48` · `Spacing/16` · `Spacing/8` · `Spacing/4` · `Spacing/2` · `Spacing/None`

**Proved.** Every name above resolves on a GSL token page reached from
`tokens/tokens-index.md`.

**Proved.** The DPE ladder matches the colour ruleset's France table exactly:
A→Green100, B→Green200, C→Green400, D→Yellow100, E→Orange100, F→Red100,
G→Red200. The letter colour follows the same rule — white on A and G only,
default content colour on B through F.

**Proved.** The GES ladder runs `Scales/CO2/Blue100` to `Blue700`, lowest to
highest, which is the ordering the Restricted section gives.

**Proved.** Every text node in every hand-built element carries a published GSL
text style. Seven distinct styles were used — `headline/22/bold`,
`body/16/bold`, `body/16/regular`, `body/14/bold`, `body/14/regular`,
`body/12/bold`, `body/12/regular`. All seven are inside typography's
**The eleven used styles**. No Display style, no headline regular, no hand-set
family.

**Proved.** Corner radius `4` is set as a plain number on all 14 scale cells,
bound to nothing. The radius ruleset's **Figma applies radius as a number**
states this is how the system is built and that a generating agent "must not
report this as an unbound-token violation". It is therefore not counted as a
literal. `4` is `Radius/4`, one of the five tiers.

**Proved.** No hand-built element carries a stroke or a shadow. No border-width
or shadow value was authored at all.

**Proved, and not counted.** 102 padding and gap properties across the
hand-built frames sit at `0` with no variable bound, while `Spacing/None` is
bound on two frames. This is an inconsistency in how zero was expressed. It is
not scored as a literal: an unset padding is the absence of a property, not a
value written by hand. Recorded here so the inconsistency is visible.

### Restricted and unprecedented token use

**Proved.** `Scales/Energy/Green100`–`Red200`, 7 cells at `133:5097`. Restricted
family, used exactly as colour's **Energy and CO2 scales** describes, including
white letters on A and G only.

**Proved.** `Scales/CO2/Blue100`–`Blue700`, 7 cells at `134:5090`. Restricted
family, used in the stated order, lowest to highest emission. The ruleset records
the CO₂ ordering as never verified against code.

**Proved.** `Color/Content/Constant/White/Default` on CO₂ steps D, E, F and G at
`134:5090`. Unprecedented — the colour ruleset prescribes letter colour on the
energy ladder and says nothing about the CO₂ ladder. The token exists and is not
denied.

### Two things no scorecard question covers

**Proved.** `Energy tag` was used for the GES rating as well as the DPE rating,
both at `Country=France, Class=A`. **Which component** says `Energy tag` is for
"property energy efficiency ratings **only**". GES is greenhouse-gas emission
data. Whether that is the right component is `components-eval.md`'s question,
not the scorecard's, so it is reported and not scored.

**Proved.** The `Donut chart`'s legend sits **beside** the chart, not below it.
`components-rules-ai.md` says "`Donut chart` has no side-placement option. Its
legend sits below". The Figma component's own `Graph` frame is a horizontal
auto-layout with a 56 gap, so the side placement is the library's default, not
the agent's composition. The ruleset and the library disagree.

## Quality verdict

_Human, free text, never scored. Not yet written._

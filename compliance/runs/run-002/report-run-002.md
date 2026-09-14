## Declarations (3)

### Seven-step rating scale (DPE and GES)

|                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What was built**           | Two horizontal seven-step scales, one under each rating, running best to worst. Each step is a rounded cell filled with its own scale token and carrying its class letter; the step matching this property's class is raised and set in the inverted content colour. The DPE scale is bound to `Scales/Energy/*` in the French A–G mapping (Green100, Green200, Green400, Yellow100, Orange100, Red100, Red200). The GES scale is bound to `Scales/CO2/Blue100`–`Blue700`, lowest to highest emission, because GES is greenhouse-gas emission data and the colour ruleset forbids energy colours for CO₂. Cell radius `Radius/4`, gaps and padding `Spacing/4` and `Spacing/8`, letters in `body/12/bold`.                                                |
| **Problem it belongs under** | Showing progress and data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Ruled out**                | `Energy tag` — it is the grade call-out, not the scale: one letter in one coloured tag, 33×24 in Figma, with no seven-step ladder inside it, so it was placed beside each scale rather than instead of it · `Bar graph` — compares quantities across categories, and the seven classes carry no quantity to compare, only a position · `Progress bar` — linear task or goal completion, and this is neither a task nor a goal · `Progress circle` — same reason, in a circular format · `Donut chart` — shows how a total divides into parts of a whole, and a rating scale is not a total · `Slider` — an input control for selecting a value, whereas this scale is read-only and the buyer cannot move it · `Tag` — a single status label, not a scale |

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

---

_Everything below this line was written by the checking agent, after the screen
existed and the declarations were fixed. The `## Declarations` section above was
not read until the inventory was complete, and was not edited._

| | |
| --- | --- |
| **Date scored** | 2026-09-14 |
| **Platform** | Figma |
| **Wireframe** | `listing-detail-energy-finance-mobile` |
| **Brief** | [prompt-run-002.md](prompt-run-002.md) |
| **Output** | [block-1-energy-and-conditions.png](block-1-energy-and-conditions.png) · [block-2-finance.png](block-2-finance.png) |
| **Frame judged** | `132:5052`, page `Screen`, file `kik7hPMCvylSCY5qSah656` |

## What the checking agent found

### How the screen was read

**Proved.** The frame was walked node by node through the Figma Plugin API.
For every node the walk recorded its type, its main component where it is an
instance, its overridden fields, its bound variables, its fills, strokes,
corner radius, padding, gap, effects and text style.

**Proved.** The live frame matches both screenshots in the run folder. A fresh
render of `132:5052` was compared against them.

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

| Hand-built                                                        | Nodes                 | Declared?                                                                                                                    |
| ----------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Two seven-step rating scales — 14 cells, 14 letters, 2 containers | 30                    | **Yes** — declaration one                                                                                                    |
| Layout containers and section stacking across both blocks         | 11                    | **Partly** — declaration two says the container and the stacking are its own; declaration three says the list containers are |
| Section titles and the two rating labels, as plain text           | 4                     | **No**                                                                                                                       |
| "per month" and the two footnote markers                          | 3                     | **Yes** — declaration two                                                                                                    |
| The partner-offer content block                                   | 5 + 1 local component | **No**                                                                                                                       |

### The partner-offer block

**Proved.** `Partner offer content` is a **local Figma component**, node
`138:5263`, authored on the `Screen` page. Its key resolves in no registry. It is
swapped into the `Card`'s content slot through the `Content` property, which is
the documented way to fill a Card.

It contains two hand-set text nodes — "Find the right financing" and "Get a
free, personalised mortgage estimate with our partner Credit Agricole" — two
hand-built frames, a `Button` instance, and footnote marker 2.

**Proved.** No declaration block names a partner offer. Declaration two mentions
"the partner-offer button" in passing, states no problem heading for the block,
and rules out no component for it. Footnote marker 2 is declared; the block
holding it is not.

### Overriding a component's internals

**Proved.** The `Donut chart` instance at `136:5237` has its internal `Graph`
frame's gap changed from **56 to 2**. The main component's value is 56; the
instance's is 2, bound to nothing. That is a local spacing change on a library
component's internal frame.

**Not proved.** The chevron inside the `See more` `Text Button` carries
`Color/Content/Interactive/Default`. The `chevron-right` icon component's own
vector carries `Color/Content/Default/Default`, so Figma lists the fill as
overridden. The `Text Button`'s own label is also
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
states this is how the system is built and that a generating agent
"must not report this as an unbound-token violation". It is therefore not
counted as a literal. `4` is `Radius/4`, one of the five tiers.

**Proved.** No hand-built element carries a stroke or a shadow. No border-width
or shadow value was authored at all.

**Proved, and not counted.** 102 padding and gap properties across the
hand-built frames sit at `0` with no variable bound, while `Spacing/None` is
bound on two frames. This is an inconsistency in how zero was expressed. It is
not scored as a literal: an unset padding is the absence of a property, not a
value written by hand. Recorded here so the inconsistency is visible.

### Two things no question covers

**Proved.** `Energy tag` was used for the GES rating as well as the DPE rating,
both at `Country=France, Class=A`. **Which component** says `Energy tag` is for
"property energy efficiency ratings **only**". GES is greenhouse-gas emission
data. Whether that is the right component is `components-eval.md`'s question,
not the scorecard's, so it is reported and not scored.

**Proved.** The `Donut chart`'s legend sits **beside** the chart, not below it.
`components-rules-ai.md` says "`Donut chart` has no side-placement option. Its
legend sits below". The Figma component's own `Graph` frame is a horizontal
auto-layout with a 56 gap, so the side placement is the library's default, not
the agent's composition. The ruleset and the library disagree. This is a finding
for a person; no scorecard question reaches it.

## Answers

| Step | Question | Answer | Reason |
| --- | --- | --- | --- |
| Define the content | _no question yet_ | — | — |
| Define the components to use | Was any element hand-built instead of taken from the library? | **yes** | **A finding, not a failure.** 50 nodes in `132:5052` are not library instances, plus the local component `Partner offer content` at `138:5263`. The substantial ones: two seven-step rating scales at `133:5097` and `134:5090`; the partner-offer content block at `138:5263`; layout containers across both blocks; four plain text nodes — two section titles at `133:5081` and `134:5968`, two rating labels at `133:5085` and `134:5078` |
| Define the components to use | Was any never-select component used? | no | `Cell Content` appears 9 times and is on **Never select**, but its own row permits it once the container is settled, and **Which component** names "a list you lay out yourself, of `Cell content` rows" for exactly this case. Both lists here are that. The `placeholder` swap value on the six fact rows is the component's untouched default for a slot switched off, not a placed component |
| Define the components to use | Was any component name used that appears in no registry? | no | All 26 instance keys resolve in `figma-components-registry.json` or `figma-patterns-registry.json`; both icons resolve in `figma-icons-registry.json`. `Partner offer content` resolves in none, and is counted as hand-built above rather than as a name from outside GSL |
| Define what needs to be built | Was anything hand-built without a complete declaration? | **yes** | **Failure.** The partner-offer content block at `138:5263` — a local component holding two hand-set text nodes, two frames and a `Button` — is in no declaration. Declaration two names "the partner-offer button" and footnote marker 2, states no problem heading for the block, and rules out no component for it. All three parts are absent, so the declaration is absent. Also undeclared: the four plain text nodes at `133:5081`, `133:5085`, `134:5078`, `134:5968` |
| Choose the tokens | Was any styled value written as a literal instead of bound to a token? | no | Every colour, every text style and every non-zero padding and gap in every hand-built element resolves to a token. Corner radius `4` on 14 cells is a plain number, which radius's **Figma applies radius as a number** requires and forbids reporting. No strokes and no shadows were authored |
| Choose the tokens | Was a library component's internal styling overridden? | **yes** | **Failure.** `136:5237` — the `Donut chart`'s internal `Graph` frame has its gap changed from the component's `56` to `2`, bound to nothing. Spacing's **Components first**: never override a component's internal padding. One more is suspected and unproved: the chevron fill inside the `See more` `Text Button` at `134:5947` |
| Choose the tokens | Was any deny-listed token used? | no | Checked against all six deny-lists. No `Spacing/56`, no Display style, no radius outside the five tiers, no shadow, no border width. `Scales/Energy/*` and `Scales/CO2/*` are **Restricted**, not denied, and both were used exactly as the Restricted section describes — flagged below |
| Choose the tokens | Was any token used that is not in the GSL token set? | no | Every token name used resolves on a token page routed from `tokens/tokens-index.md` |
| Put them on the screen | _no question yet_ | — | — |
| Place them according to the design guidance | _inactive_ | — | — |
| Check the content | _no question yet_ | — | — |

## Flags (3)

Findings, not failures.

| Step | Subject | Why flagged |
| --- | --- | --- |
| Choose the tokens | `Scales/Energy/Green100`, `Green200`, `Green400`, `Yellow100`, `Orange100`, `Red100`, `Red200` — 7 cells at `133:5097` | **Restricted.** Used exactly as colour's **Energy and CO2 scales** describes, including white letters on A and G only. Restricted tokens are flagged, never failed |
| Choose the tokens | `Scales/CO2/Blue100`–`Blue700` — 7 cells at `134:5090` | **Restricted.** Used in the stated order, lowest to highest emission. The ruleset records the CO₂ ordering as never verified against code, so a live use of it is worth a human's eye |
| Choose the tokens | `Color/Content/Constant/White/Default` on CO₂ steps D, E, F, G at `134:5090` | **Unprecedented.** The colour ruleset prescribes letter colour on the energy ladder and says nothing about the CO₂ ladder. The token exists and is not denied. The choice may be revealing a gap in the ruleset rather than an error |

## Awaiting human decision (3)

All three flags above are `awaiting decision`. None has been seen in a previous
run — `compliance-flag-ledger.md` holds no rows, and `run-001` was never scored.

## Quality verdict

_Human, free text, never scored. Not yet written._

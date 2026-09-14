# Run 003 — Listing detail, energy and finance blocks, mobile

| | |
| --- | --- |
| **Date scored** | 2026-09-14 |
| **Platform** | Figma |
| **Wireframe** | `listing-detail-energy-finance-mobile` |
| **Brief** | [prompt-run-003.md](prompt-run-003.md) |
| **Output** | [block-1-energy-and-conditions.png](block-1-energy-and-conditions.png) · [block-2-finance.png](block-2-finance.png) |
| **Frame judged** | `152:22144` · page `Screen` |

## Verdict

**Nothing failed.** This is the first run to answer every question compliantly.

Twenty-three library components were placed. Everything the agent built by hand
has a complete declaration. Every colour, every text style and every gap is
bound to a token — no value was written by hand anywhere on the screen.

The three things that failed in run 002 are all fixed. The chart's internal
spacing was left alone. The partner offer is declared. The energy tag is on the
energy rating only, not on the emissions one.

Both rating ladders match the colour rules exactly, letter colours included —
including the emissions rule that was written the same day, after run 002.

**Five things need your ruling.** Two are the restricted scale colours, which
you already accepted once. Two ask whether the agent was allowed to reach inside
the chart the way it did. One asks whether the page's own section frames need
declaring.

## Decisions you need to make (5)

Rulings: `awaiting decision` · `agent error` · `ruleset gap` · `library defect` ·
`accepted`.

| What | Why it needs you | Ruling |
| --- | --- | --- |
| **The energy scale colours were used** | A restricted family. Restricted always means a person looks. Used exactly as the France table describes, white letters on A and G only. You ruled the identical use `accepted` on run 002 | _unruled_ |
| **The emissions scale colours were used** | Same family rule. Used lowest to highest, with the letter colours the rule written after run 002 prescribes. That rule has now been followed once, so it works | _unruled_ |
| **The chart's legend was switched to stack vertically** | The component rules say the chart has no alignment property and tell an agent not to look for one. One exists on the legend's own internal part, and the agent used it. The rule may mean placement beside the chart, not how the legend's rows stack. It does not say | _unruled_ |
| **Parts inside the chart were hidden by hand** | The chart ships with five segments. The brief needs three. Two segments, two legend rows and the centre total were switched off and one segment reshaped. Some of that used the chart's own switches; some reached below them. No rule says where the line is | _unruled_ |
| **The page frame and the two section frames carry no declaration** | The rules say a layout container holding declared content is declared inside that content's declaration. These three hold content from several declarations at once, so they fit no single one. I judged them page structure rather than composed elements and passed the run. Your call | _unruled_ |

## Answers

| Step | Question | Answer | Reason |
| --- | --- | --- | --- |
| Define the content | _no question yet_ | — | — |
| Define the components to use | Was any element hand-built instead of taken from the library? | **yes** | **A finding, not a failure.** Five things were built by hand. All five are declared |
| Define the components to use | Was any never-select component used? | no | `Cell Content` is on the list, and its own row permits this use once the container is settled. **Which component** names the hand-laid list of `Cell content` rows for exactly this case |
| Define the components to use | Was any component name used that appears in no registry? | no | Every library key resolves in `figma/*-registry.json`. The one local component is counted as hand-built, not as a name from outside GSL |
| Define what needs to be built | Was anything hand-built without a complete declaration? | no | All five composed elements carry all three parts. The four plain text labels need none — the rules exempt text set in a published style. Three stacking frames carry none; see the last row of the decisions table |
| Choose the tokens | Was any styled value written as a literal instead of bound to a token? | no | Every colour, text style, padding and gap resolves to a published GSL variable. No hex, no hand-set font, no unbound gap |
| Choose the tokens | Was a library component's internal styling overridden? | no | Nothing local was set on any instance's colour, type, spacing, radius, border or shadow. The chart's internal gap was left at its library value |
| Choose the tokens | Was any deny-listed token used? | no | Checked against all six deny-lists. The two scale families are restricted, not denied |
| Choose the tokens | Was any token used that is not in the GSL token set? | no | Every name resolves on a token page routed from `tokens-index.md`, and every variable reads back as a published Foundations variable |
| Put them on the screen | _no question yet_ | — | — |
| Place them according to the design guidance | _inactive_ | — | — |
| Check the content | _no question yet_ | — | — |

## Declarations (5)

### DPE rating scale

| | |
| --- | --- |
| **What was built** | A seven-step horizontal ladder for the French DPE classes A–G, laid out as a frame of seven equal segments. Each segment is filled from `Scales/Energy/*` for its class (A `Green100`, B `Green200`, C `Green400`, D `Yellow100`, E `Orange100`, F `Red100`, G `Red200`), carries its letter in `body/12/bold`, and is corner-radiused at `Radius/4` as a chart bar. Letter colour follows the colour ruleset: `Content/Constant/White/Default` on A and G, `Content/Default/Default` on B–F. The property's own class is raised by giving that one segment `Spacing/16` vertical padding against `Spacing/8` on the others, with the row bottom-aligned. The header row above it pairs the label `[certificateType.DPE]` with an `Energy Tag` instance, Country=France Class=A, which is the grade callout. |
| **Problem it belongs under** | Showing progress and data |
| **Ruled out** | `Energy tag` — it is the component for the grade callout and was used there, but it renders one class letter and carries no seven-step scale · `Bar graph` — it compares quantities across categories, while a DPE ladder is a fixed regulatory classification, and its bar fills cannot be set per class to `Scales/Energy/*` · `Progress bar` — linear task or goal completion, not a position on a seven-step classification · `Segmented control` — switching between view modes, and this scale is not interactive |

### GES rating scale

| | |
| --- | --- |
| **What was built** | The same seven-step ladder built for the GES (greenhouse-gas) rating, filled from `Scales/CO2/Blue100`–`Blue700` in order, lowest emission to highest. Letter colour follows the CO₂ letter rule: `Content/Constant/Black/Default` on `Blue100`–`Blue300`, `Content/Constant/White/Default` on `Blue400`–`Blue700`. The property's class A segment is raised the same way. Its grade callout was also built by hand — a small `Radius/4` block filled `Scales/CO2/Blue100` carrying the letter A in `body/14/bold` on `Content/Constant/Black/Default`. |
| **Problem it belongs under** | Showing progress and data |
| **Ruled out** | `Energy tag` — energy-efficiency ratings only, and its France variants are coloured from the energy scale, which the colour ruleset forbids for CO₂ data · `Bar graph` — compares quantities across categories, not a fixed seven-step classification, and its bars cannot take `Scales/CO2/*` · `Donut chart` — shows how a total divides into parts of a whole; a GES class is a position on a scale, not a share of anything · `Progress bar` — linear completion, not a classification |

### Property facts list

| | |
| --- | --- |
| **What was built** | A plain list of the six known facts, laid out as a frame of six `Cell Content` instances (Alignment=Horizontal, Padding=16, Clickable=OFF) with the label in the Title slot and the value in the Body slot, separated by `Divider` instances. The list frame and the row order are mine; every row and every separator is a library component. `Text Button` sits below it as the "See more" control. |
| **Problem it belongs under** | Grouping and structuring content |
| **Ruled out** | `Tables` — the rows are label-and-value pairs, not comparable tabular data across shared columns · `Card` — the facts are a plain list, not one grouped visual block · `Accordion` — all six facts are always visible, with no progressive disclosure · `Toggle group` — no row carries an immediate on/off setting · a `List` component — none exists in any library, so laying the `Cell Content` rows out is the intended pattern |

### Mortgage simulator

| | |
| --- | --- |
| **What was built** | The whole Finance calculation block, composed because no Pattern or Experience is it. Controls: two `Text Field` instances (Content=Filled, Suffix "€") for Property price and Your contribution, the second carrying the Helper Text "(20% of total costs recommended)"; one `Dropdown` (Content=Selected) for Duration of our loan. Result: a `KPI` instance, Label "Estimated", value "2.256 €", with "per month" and the footnote marker 1 set beneath it in `body/14/regular` and `body/12/regular` on `Content/Light/Default`. Breakdown: a `Donut chart` instance with its legend switched on, plus three rows I laid out, each pairing the amount's name in `body/14/regular` with an icon-only `Text Button` carrying the `info` icon, Circle=On, as the explain-on-demand trigger, and the amount in `body/14/bold`. The `Donut chart`'s nested data booleans do not respond through the plugin API, so its two surplus arcs and two surplus legend rows were hidden and the third arc's sweep closed, to show three data points instead of five; the component's own legend gap was not touched. All frames use `Spacing/*` tokens for padding and gaps. |
| **Problem it belongs under** | Computing a figure from user input |
| **Ruled out** | `Estimation card` — it presents a completed price estimate and carries no controls to adjust, and this block recalculates from three inputs the buyer changes · `Wizard` — the buyer adjusts three values freely, with no ordered steps to advance through · `Filter bar` — its controls narrow a list of results rather than produce a figure · `Slider` — exact entry matters for a price and a contribution, so `Text Field` was used instead · `Counter field` — the loan duration is a small fixed set of values, which the ruleset routes to `Dropdown` · `Bar graph` — the breakdown is three parts of one whole, which is `Donut chart` |

### Partner offer content

| | |
| --- | --- |
| **What was built** | The content authored into the Content Placeholder slot of a `Card` instance (Radius=8, Color=Light): the heading "Find the right financing" in `body/16/bold` on `Content/Default/Default`, the line "Get a free, personalised mortgage estimate with our partner Credit Agricole" in `body/14/regular` on `Content/Light/Default`, and a secondary `Button` reading "Customize simulation" with the footnote marker 2 beside it in `body/12/regular`. The content frame pads at `Spacing/16` and gaps at `Spacing/8`, so the gap never exceeds the padding. The container itself is the `Card` component, not hand-built. |
| **Problem it belongs under** | Grouping and structuring content |
| **Ruled out** | `Button card` — the whole container is not one navigational action; it carries a heading, a description and one separate action · `Info state` — a full-area empty, error, success or loading state, not a partner offer inside a page · `Feedback message` — inline contextual guidance or status, not an offer with its own call to action · `Modal bottom sheet` — the offer persists on the page rather than overlaying it and blocking interaction · `Content Placeholder` — never selected on its own; the parent `Card` was placed and its slot filled |

## Evidence

Written for a machine and for a dispute. Every locator lives here.

### How the screen was read

**Proved.** Frame `152:22144`, page `Screen`, was walked node by node through
the Figma Plugin API over `figma-cli`. The walk covers 426 nodes. For every node
it recorded type, main component and component key where the node is an
instance, `componentProperties`, `overrides`, `boundVariables`, fills, strokes,
stroke weight, corner radius, padding, item spacing, effects and text style.

**Proved.** The local component swapped into the `Card` sits outside the frame,
on the `Screen` page. It was walked separately, by the same method, and its five
own nodes are counted with the hand-built total below.

**Proved.** The live frame matches both screenshots in the run folder. Every
element visible in `block-1-energy-and-conditions.png` and
`block-2-finance.png` was located in the walk, in the same order and with the
same content.

**Proved.** The `## Declarations` section above was read only after the
inventory was complete, and was not edited.

### The inventory

**Proved.** Inside the frame: **85 nodes** are not nested inside a library
instance. Of those, **22 are library instances** placed directly and **63 are
hand-built** — 36 frames and 27 text nodes. A twenty-third library instance,
`Button`, sits inside the local component outside the frame.

| Library component | Instances | Tier | Where |
| --- | --- | --- | --- |
| `Cell Content` | 6 | Components | the six property facts |
| `Divider` | 5 | Components | between the six facts |
| `Text Button` | 4 | Components | "See more", and the three explain triggers |
| `Text Field` | 2 | Components | property price, your contribution |
| `Energy Tag` | 1 | Components | the DPE grade callout |
| `Dropdown` | 1 | Components | duration of our loan |
| `Card` | 1 | Components | the partner offer container |
| `Button` | 1 | Components | "Customize simulation", inside the local component |
| `KPI` | 1 | Patterns | the estimated monthly figure |
| `Donut chart` | 1 | Patterns | the payment breakdown |

**Proved.** Every one of those keys resolves to a name in
`figma/figma-components-registry.json` or `figma/figma-patterns-registry.json`.

| Component | Key | Registry |
| --- | --- | --- |
| `Energy Tag` | `0e8d81cb86d1bcfd8958ceb7e4b8a307f72b63c6` | components |
| `Cell Content` | `71b1f5176db52eb12c7744a0df8c4096655ac6f4` | components |
| `Divider` | `4686de8c81968ab25756ab8579b639f27d2741ba` | components |
| `Text Button` | `4c5f262e38bee4fcb987e6ecba58ddc3c9ae4907` | components |
| `Text Field` | `f1c414ce0cf481118654da95ac073a068ad64a52` | components |
| `Dropdown` | `a5f4fb28f1a8011a07b7594d08fee6c8f06830d7` | components |
| `Card` | `cc742e4501a43a1d2a414295a816dbbd5ae7a55d` | components |
| `Button` | `97d227b9a0714f73ddf4679c1354f5430437b7e6` | components |
| `KPI` | `16e4d980776106384ed729c205b0d697ac3227ee` | patterns |
| `Donut chart` | `1e38854162ca35f39c5c905e74cbc861e98f978f` | patterns |

**Proved.** The one swapped-in icon, `info`, resolves by set key
`3daf5ac6038e34878dab7bc2ff73a5fea3abfb06` in
`figma/figma-icons-registry.json`. The variant placed is
`Name=info, Filled=Off, Circle=On, Square=Off`, which is the circled form.

**Proved.** `placeholder`, `badge`, `Tag` and `state_message` appear only as
internals of the components above. `placeholder` and `badge` are switched off in
every instance that carries them. None was selected by the agent, and
`placeholder` resolves in no registry because it is an unpublished internal.

### The never-select check

**Proved.** `Cell Content` is on **Never select**. Its own row states that once
the container is settled, `Cell content` is the correct row and using it there is
not a violation. The container here is a list the agent laid out, which
**Which component** names explicitly: *a list you lay out yourself, of
`Cell content` rows*. Not a violation.

**Proved.** `Content Placeholder` is on **Never select** and was not placed. The
`Card` was placed and its `Content` slot swapped, which is the row's own
instruction — *select the parent, put your content in the slot*.

**Proved.** No other never-select name appears anywhere in the frame. No
platform chrome, no brand asset, no `Map template` internal, no
`Programmatic Ads`, no `Tab Bar`, no `Footer`.

### What was hand-built

**Proved.** The 63 hand-built nodes in the frame, plus the 5 nodes of the local
component outside it, group into eight things. Five are composed elements and
carry a declaration; three are not.

| Hand-built | Nodes | Locator | Declared? |
| --- | --- | --- | --- |
| The DPE ladder — 7 cells, 7 letters, container, header row | 17 | `152:22598` · scale `152:22601` | **yes** — declaration one |
| The GES ladder — 7 cells, 7 letters, container, header row, and its own grade callout | 19 | `152:22654` · scale `152:22657` · callout `152:22646` | **yes** — declaration two |
| The facts list container | 1 | `152:22696` | **yes** — declaration three |
| The finance simulator — input stack, result stack, breakdown stack, three amount rows | 17 | `152:23033` · `152:23184` · `152:23303` · `152:23325` | **yes** — declaration four |
| The partner offer content, a local component swapped into the `Card` | 5 | `152:23403` | **yes** — declaration five |
| Two section titles and two rating labels, as plain text | 4 | `152:22591` · `152:23032` · `152:22600` · `152:22656` | **not required** |
| The page frame and the two section stacks | 3 | `152:22144` · `152:22145` · `152:22146` | **no** |
| "per month" and the two footnote markers | 3 | `152:23186` · `152:23188` · `152:23402` | **yes** — declarations four and five |

**Proved.** Each of the five declarations states all three required parts — what
was built, which problem heading from **Which component** it belongs under, and
which existing components were ruled out with reasons. None is missing a part.

**Proved.** The four plain text nodes need no declaration.
`components-rules-ai.md`'s *What needs declaring* table states that plain text
set in a published GSL text style is not declared, because the three-part
declaration cannot be written for it. All four carry a published style —
`headline/22/bold` on the two section titles, `body/14/bold` on the two rating
labels.

**Not settled by any rule.** The page frame and the two section stacks carry no
declaration of their own. The declaring rule says a layout container holding
declared content is declared *inside that content's own declaration*. Each of
these three holds content belonging to more than one declaration, so it fits
inside none of them. The same rule also says a declaration is not a receipt for
every node on the screen. They hold no content of their own and do no job beyond
stacking. Judged page structure, not composed elements, and raised for Gabriel's
ruling.

### The local component

**Proved.** `.run-003 partner offer content` is a **local Figma component**, node
`152:23403`, key `d302d37ca249eb2788e2e56dcf8518079de00dc5`, `remote: false`,
authored on the `Screen` page. Its key resolves in no registry, because the agent
made it. It is counted as hand-built, not as a component name from outside GSL.

It is swapped into the `Card`'s `Content#12142:0` property, which is the
documented way to fill a Card. It contains two text nodes, a layout frame, the
footnote marker, and one `Button` instance.

**Recorded, not scored.** Its name starts with a dot. In GSL grammar a leading
dot marks an unpublished internal part of a library component. Nothing in any
ruleset governs what an agent names a local component of its own, so this is not
a finding — noted because a future reader could mistake it for a library part.

### Overriding a component's internals

**Proved, and it is the run-002 failure not repeated.** The `Donut chart`
instance at `152:23189` has its internal `Graph` frame at gap **56**. The main
component's value is **56**. They match. Nothing was overridden, which is what
**Where a chart's legend sits** requires: *never change the gap between a chart
and its legend on an instance.*

**Recorded, not scored.** 56 is above the `Spacing/48` ceiling that
`components-rules-ai.md` states as intended. That ruleset already records the
discrepancy in its own words — *not what the Figma library does today; the
library uses a fixed 56, above the ceiling.* The agent followed the instruction
not to touch it, so the gap is the library's, not the agent's.

**Proved.** The `Donut chart`'s legend sits **beside** the chart. That is the
only placement the library offers and, since run-002's `library defect` ruling,
is correct output and not a finding.

**Proved.** No instance anywhere in the frame carries a local override of a
colour, a text style, a padding, an item spacing, a corner radius, a stroke
weight or an effect. The complete set of override fields across all 22 directly
placed instances is: `name`, `height`, `width`, `characters`,
`styledTextSegments`, `visible`, `arcData`, `componentProperties`,
`primaryAxisSizingMode`, and `fillStyleId`/`fills` on three icon vectors. None of
the first nine is a styled property.

**Proved, and it settles the run-002 "not proved" line.** The three icon vectors
at `I152:23329;11:12820;58963:4480`, `I152:23341;…` and `I152:23352;…` carry
`Color/Content/Interactive/Default`. Figma lists the fill as overridden because
the `info` icon component's own vector is `Color/Content/Default/Default`. The
`Text Button` **main component's** own icon slot was read directly: its
placeholder vector is bound to `Color/Content/Interactive/Default`, and the main
component itself lists that fill as an override of its placeholder. The value
therefore comes from the `Text Button` component, not from the agent. Run-002
could not read this and recorded it as *not proved*; it is now proved.

### How the chart was reconfigured

**Proved.** Recorded in full because two of the five decisions rest on it.

| Where | What changed | Through what |
| --- | --- | --- |
| `152:23189` — the `Donut chart` instance | `KPI` off, `Legend` on | the chart's own properties |
| `I152:23189;2782:13320` — `.Header` | `Filters` off, default on | a property of the internal, **not exposed on the chart** |
| `I152:23189;2782:13320;2414:399` — Subtitle | `visible: false` | a direct node edit inside the instance |
| `I152:23189;2782:13323` — `.Legend` | `Alignment` = `Vertical`, default `Horizontal` | a property of the internal, **not exposed on the chart** |
| `I152:23189;2782:13323;2423:4648` · `;2423:4652` | two legend rows `visible: false` | direct node edits inside the instance |
| `I152:23189;2782:13324` — `.Donut chart` | `Data 4` off, `Data 5` off, `Label` off, `Value` off | properties of the internal, **not exposed on the chart** |
| `I152:23189;2782:13324;2782:13333` · `;2782:13334` | two arc ellipses `visible: false` | direct node edits inside the instance |
| `I152:23189;2782:13324;2782:13335` | `arcData` endingAngle changed, closing the third arc's sweep | a direct node edit inside the instance |
| `I152:23189;2782:13324;2782:13338` — Total-container | `visible: false` | a direct node edit inside the instance |

**Proved.** All five arc ellipses keep their library-bound fills. No arc colour
was set by hand.

**Not settled by any rule.** `components-rules-ai.md` says a dot-prefixed
internal is reached *through the component that contains it — as a property to
switch on, or as a slot already exposed on it.* `Donut chart` exposes two
booleans, `KPI` and `Legend`. Everything in the table below those two rows went
past them. Nothing states whether that is permitted, so it is raised rather than
scored.

**Not settled by any rule.** The same file says of the legend: *there is no
alignment property — do not go looking for one.* An `Alignment` variant does
exist on `.Legend`, and the agent set it to `Vertical`. The sentence is about
where the legend sits relative to the chart; the property is about how the
legend's own rows stack. Both readings are available, so it is raised rather
than scored.

### Tokens

**Proved.** Every styled value in every hand-built element is bound to a
published variable. No hex, no unbound paint, no unbound padding or gap, no
hand-set font. The complete set used in hand-built elements:

- `Color/Background/Default`
- `Color/Content/Default/Default` · `Color/Content/Light/Default` ·
  `Color/Content/Constant/White/Default` · `Color/Content/Constant/Black/Default`
- `Color/Scales/Energy/Green100` · `Green200` · `Green400` · `Yellow100` ·
  `Orange100` · `Red100` · `Red200`
- `Color/Scales/CO2/Blue100` through `Blue700`
- `Spacing/48` · `Spacing/16` · `Spacing/8` · `Spacing/4` · `Spacing/2` ·
  `Spacing/None`

**Proved.** Every one of those names resolves on a GSL token page reached from
`tokens/tokens-index.md`. Every variable reads back with `remote: true` and
resolves to a Foundations collection — `3 - Brand` for colour, `1 - Primitive`
for spacing.

**Proved.** The DPE ladder matches colour's France table exactly.

| Class | Required | Used | Cell |
| --- | --- | --- | --- |
| A | `Scales/Energy/Green100` | `Scales/Energy/Green100` | `152:22602` |
| B | `Scales/Energy/Green200` | `Scales/Energy/Green200` | `152:22610` |
| C | `Scales/Energy/Green400` | `Scales/Energy/Green400` | `152:22616` |
| D | `Scales/Energy/Yellow100` | `Scales/Energy/Yellow100` | `152:22622` |
| E | `Scales/Energy/Orange100` | `Scales/Energy/Orange100` | `152:22628` |
| F | `Scales/Energy/Red100` | `Scales/Energy/Red100` | `152:22634` |
| G | `Scales/Energy/Red200` | `Scales/Energy/Red200` | `152:22640` |

**Proved.** Letter colour on the DPE ladder follows the same rule — white on A
and G only, `Content/Default/Default` on B through F.

**Proved.** The GES ladder runs `Scales/CO2/Blue100` to `Blue700` in order,
lowest to highest emission, across cells `152:22658` to `152:22690`.

**Proved.** Letter colour on the GES ladder matches the CO₂ rule written on
14 September 2026, in full.

| Steps | Required | Used |
| --- | --- | --- |
| `Blue100` · `Blue200` · `Blue300` | `Content/Constant/Black` | `Color/Content/Constant/Black/Default` |
| `Blue400` · `Blue500` · `Blue600` · `Blue700` | `Content/Constant/White` | `Color/Content/Constant/White/Default` |

**Proved.** The hand-built GES grade callout at `152:22646` is filled
`Scales/CO2/Blue100` with its letter in `Content/Constant/Black/Default`,
consistent with the same rule. `Energy Tag` was **not** used for the emissions
rating. That is run-002's `agent error` not repeated.

**Proved.** Every text node in every hand-built element carries a published GSL
text style, verified `remote: true`. Six distinct styles were used:
`headline/22/bold`, `body/16/bold`, `body/14/bold`, `body/14/regular`,
`body/12/bold`, `body/12/regular`. All six are inside typography's
**The eleven used styles**. No Display style, no regular headline, no hand-set
family. Nothing unprecedented.

**Proved.** Every text node inside a library instance whose characters were
retyped also carries a published GSL text style and a bound fill. Fifteen were
checked one by one — the six fact titles and bodies, the "See more" label, the
three field labels and values, the helper text, the two KPI texts and the three
legend labels. Each returns a single styled segment; none is mixed, none is
unstyled, none carries an unbound fill.

**Proved.** Corner radius `4` is set as a plain number on all 14 scale cells and
on the GES grade callout, bound to nothing. Radius's **Figma applies radius as a
number** states this is how the system is built and that a generating agent
*must not report this as an unbound-token violation*. It is therefore not
counted as a literal. `4` is `Radius/4`, which the five-tier table names for
*the fixed corner radius on chart bars*.

**Proved.** No hand-built element carries a stroke, a stroke weight or a shadow.
No border-width and no shadow value was authored at all, so neither deny-list can
be reached.

**Proved.** No deny-listed token appears anywhere. `Spacing/56` unused. No
Display style. No radius outside the five tiers and no `Corner radius/*` variable
set by the agent — the `Corner radius (🔒)/*` bindings present in the frame all
sit on library instances and are the components' own. No shadow of `24` or `32`,
no custom shadow. No border width other than the `1` the `Divider` component
carries itself. No `Symbol/*`, no `Native/*`, no `Surface/Decorative/*`, no
`Border/Focus`, no unreachable status leaf.

### Restricted token use

**Proved.** `Scales/Energy/Green100`–`Red200`, seven cells at `152:22601`.
Restricted family, used exactly as colour's **Energy and CO2 scales** describes,
including white letters on A and G only. Ruled `accepted` on run 002 for the
identical use.

**Proved.** `Scales/CO2/Blue100`–`Blue700`, seven cells at `152:22657` plus the
grade callout at `152:22646`. Restricted family, used in the stated order and
with the prescribed letter colours. The ruleset still records the CO₂ ordering as
never verified against code, and the letter-colour split as computed rather than
observed.

**Nothing unprecedented.** Run 002 raised white letters on the CO₂ ladder as an
unprecedented choice. A rule now covers it, and this run follows that rule, so
the same use is compliant rather than flagged.

## Quality verdict

_Human, free text, never scored. Not yet written._

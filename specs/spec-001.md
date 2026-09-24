# Spec 001 — Listing detail, energy and finance blocks

| Field | Value |
| --- | --- |
| **Status** | `draft` |
| **Width** | `mobile` |
| **Brand** | `SeLoger` |
| **Last changed** | 2026-09-24 |

_The worked example for [spec-rules-ai.md](spec-rules-ai.md). Component and
token choices follow run-003 of this source, which answered every scorecard
question compliantly:
[report-run-003.md](../compliance/briefs/brief-001/run-003/report-run-003.md)._

## Source

[brief-001.md](../compliance/briefs/brief-001/brief-001.md), unchanged.

## Goals

| Goal | What the user can do | From |
| --- | --- | --- |
| `judge-running-cost` | See at a glance how expensive the property will be to run | source |
| `judge-condition` | See at a glance what condition the property is in | source |
| `see-all-facts` | Ask for everything known about the property, beyond the six facts shown | source |
| `estimate-monthly-cost` | Work out the monthly cost of buying the property, by changing a few numbers | source |
| `understand-the-cost` | See what the monthly cost is made of, and have each part explained | source |
| `get-a-real-quote` | Hand over to a partner for a real mortgage estimate | source |

## Acceptance criteria

| Criterion | Goal | From |
| --- | --- | --- |
| The two ratings appear above the six facts | `judge-running-cost` | source |
| Each rating shows the seven-step scale and calls out this property's grade | `judge-running-cost` | source |
| All six facts are visible without any interaction | `judge-condition` | source |
| A "See more" control sits below the six facts | `see-all-facts` | source |
| Changing the price, the contribution or the duration changes the monthly estimate | `estimate-monthly-cost` | source |
| The monthly estimate is the most prominent figure in the Finance block | `estimate-monthly-cost` | source |
| The breakdown shows three amounts and a chart of their shares | `understand-the-cost` | source |
| Each of the three amounts can be explained on demand | `understand-the-cost` | source |
| The partner offer is visibly set apart from the simulation above it | `get-a-real-quote` | source |

## Assumptions

| Assumption | Why | Affects | Status |
| --- | --- | --- | --- |
| The brand is `SeLoger` | The source names no brand | Every colour | open |
| The loan durations offered are 10, 15, 20 and 25 years | The source says "a small set of durations" and names only 10 | `finance.duration` | open |
| The contribution guidance is the field's helper text | Helper text is part of a text field's header, and is for persistent guidance | `finance.contribution` | open |
| "See more" reveals the remaining facts in place, rather than opening another screen | The source says the buyer "can ask for the rest" and does not say where | `energy.see-more` | open |
| Each amount is explained by the `info` trigger beside it | The source says "explainable on demand" and names no control | `finance.borrowed-explain`, `finance.notary-explain`, `finance.interest-explain` | open |
| The explain triggers' spoken labels read "Explain the …" | An icon-only text button must still have a label, as its spoken name. The source gives none | `finance.borrowed-explain`, `finance.notary-explain`, `finance.interest-explain` | open |
| The explanation texts are placeholders | The source gives none | `finance.borrowed-explain`, `finance.notary-explain`, `finance.interest-explain` | open |
| The two footnote markers have no footnote text on this screen | The source gives the markers, and no text for them | `finance.footnote-one`, `finance.footnote-two` | open |
| The estimate recalculates with a simplified loan formula | The source says the buyer adjusts numbers, and gives no rate model beyond "4,9%" | `finance.monthly-estimate` | open |
| Section titles use `headline/22/bold` | The source names no style. Run-003 used it and passed | `energy.title`, `finance.title` | open |

## Screen

### Energy and conditions — `energy`

Goal: `judge-running-cost`, `judge-condition`, `see-all-facts` · Stack: vertical · Gap: `Spacing/16` · Padding: `Spacing/16`

| ID | Element | Component | Variants | Copy | Data | Tokens | Behaviour | Inside |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `energy.title` | Section title | `text` | — | "Energy and conditions" | — | `headline/22/bold` · `Content/Default/Default` | — | — |
| `energy.dpe-label` | Energy rating label | `text` | — | — | `[certificateType.DPE]` | `body/14/bold` · `Content/Default/Default` | — | — |
| `energy.dpe-grade` | This property's energy grade | `Energy Tag` | `Country: France` | — | energy grade, sample: A | — | — | — |
| `energy.dpe-scale` | The energy scale, A to G | `composed` | — | "A" "B" "C" "D" "E" "F" "G" | energy grade, sample: A | See **Inventions** | — | — |
| `energy.ges-label` | Emissions rating label | `text` | — | — | `[certificateType] GES` | `body/14/bold` · `Content/Default/Default` | — | — |
| `energy.ges-scale` | The emissions scale, A to G, with this property's grade called out | `composed` | — | "A" "B" "C" "D" "E" "F" "G" | emissions grade, sample: A | See **Inventions** | — | — |
| `energy.facts` | The six facts, as a list | `composed` | — | — | — | See **Inventions** | — | — |
| `energy.fact-year-built` | Year of construction | `Cell Content` | `Alignment: Horizontal` · `Title, body and description: Title and body` | "Year of construction" | `[yearOfConstruction]` | — | — | `energy.facts` |
| `energy.divider-year-built` | Separator | `Divider` | — | — | — | — | — | `energy.facts` |
| `energy.fact-last-modernisation` | Last modernisation | `Cell Content` | `Alignment: Horizontal` · `Title, body and description: Title and body` | "Last modernisation" | `[lastModernisation]` | — | — | `energy.facts` |
| `energy.divider-last-modernisation` | Separator | `Divider` | — | — | — | — | — | `energy.facts` |
| `energy.fact-state` | State of property | `Cell Content` | `Alignment: Horizontal` · `Title, body and description: Title and body` | "State of property" | `[ageState]`, `[constructionStyle]`, `[buildState]` | — | — | `energy.facts` |
| `energy.divider-state` | Separator | `Divider` | — | — | — | — | — | `energy.facts` |
| `energy.fact-energy-standard` | Energy standard | `Cell Content` | `Alignment: Horizontal` · `Title, body and description: Title and body` | "Energy standard" | `[houseEnergyStandardType]` | — | — | `energy.facts` |
| `energy.divider-energy-standard` | Separator | `Divider` | — | — | — | — | — | `energy.facts` |
| `energy.fact-heating` | Heating method | `Cell Content` | `Alignment: Horizontal` · `Title, body and description: Title and body` | "Heating method" · " heating: " | `[heatMethod]`, `[heatForm]` | — | — | `energy.facts` |
| `energy.divider-heating` | Separator | `Divider` | — | — | — | — | — | `energy.facts` |
| `energy.fact-energy-sources` | Energy sources | `Cell Content` | `Alignment: Horizontal` · `Title, body and description: Title and body` | "Energy sources" | `[energySource]`, `[energyGeneration]` | — | — | `energy.facts` |
| `energy.see-more` | Ask for the remaining facts | `Text Button` | — | "See more" | — | — | Reveals the remaining facts below the six. `mock` | — |

### Finance — `finance`

Goal: `estimate-monthly-cost`, `understand-the-cost`, `get-a-real-quote` · Stack: vertical · Gap: `Spacing/16` · Padding: `Spacing/16`

| ID | Element | Component | Variants | Copy | Data | Tokens | Behaviour | Inside |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `finance.title` | Section title | `text` | — | "Finance" | — | `headline/22/bold` · `Content/Default/Default` | — | — |
| `finance.simulator` | The mortgage simulator | `composed` | — | — | — | See **Inventions** | — | — |
| `finance.price` | Property price | `Text Field` | `Header: on` · `Suffix: "€"` | "Property price" | price, sample: 560.000 € | — | Editable. Changes `finance.monthly-estimate` | `finance.simulator` |
| `finance.contribution` | The buyer's contribution | `Text Field` | `Header: on` · `Suffix: "€"` | "Your contribution" · "(20% of total costs recommended)" | contribution, sample: 160.000 € | — | Editable. Changes `finance.monthly-estimate` | `finance.simulator` |
| `finance.duration` | Loan duration | `Dropdown` | `Header: on` | "Duration of our loan" · "10 years" · "15 years" · "20 years" · "25 years" | duration, sample: 10 years | — | Picks one duration. Changes `finance.monthly-estimate` | `finance.simulator` |
| `finance.monthly-estimate` | The monthly cost, the answer | `KPI` | `Layout: Vertical` · `Display Context: Independent` | "Estimated" · "2.256 €" | computed from `finance.price`, `finance.contribution`, `finance.duration` · sample: 2.256 € | — | Recalculates when a figure above changes. `mock` | `finance.simulator` |
| `finance.per-month` | Unit of the estimate | `text` | — | "per month" | — | `body/14/regular` · `Content/Light/Default` | — | `finance.simulator` |
| `finance.footnote-one` | Footnote marker | `text` | — | "1" | — | `body/12/regular` · `Content/Light/Default` | — | `finance.simulator` |
| `finance.breakdown-chart` | What the monthly cost is made of | `Donut chart` | — | "Amount borrowed" · "Notary fees (8%)" · "Interest cost (4,9%)" | computed from `finance.borrowed-amount`, `finance.notary-amount`, `finance.interest-amount` | — | — | `finance.simulator` |
| `finance.borrowed-label` | Amount borrowed, name | `text` | — | "Amount borrowed" | — | `body/14/regular` · `Content/Default/Default` | — | `finance.simulator` |
| `finance.borrowed-explain` | Explain the amount borrowed | `Text Button` | `Icon: icon only` · `info` · `Circle: On` · `Size: 16` | "Explain the amount borrowed", spoken only, never shown | — | — | Shows a short explanation. `mock` | `finance.simulator` |
| `finance.borrowed-amount` | Amount borrowed, value | `text` | — | — | amount borrowed, sample: 000.000 € | `body/14/bold` · `Content/Default/Default` | — | `finance.simulator` |
| `finance.notary-label` | Notary fees, name | `text` | — | "Notary fees (8%)" | — | `body/14/regular` · `Content/Default/Default` | — | `finance.simulator` |
| `finance.notary-explain` | Explain the notary fees | `Text Button` | `Icon: icon only` · `info` · `Circle: On` · `Size: 16` | "Explain the notary fees", spoken only, never shown | — | — | Shows a short explanation. `mock` | `finance.simulator` |
| `finance.notary-amount` | Notary fees, value | `text` | — | — | notary fees, sample: 55.000 € | `body/14/bold` · `Content/Default/Default` | — | `finance.simulator` |
| `finance.interest-label` | Interest cost, name | `text` | — | "Interest cost (4,9%)" | — | `body/14/regular` · `Content/Default/Default` | — | `finance.simulator` |
| `finance.interest-explain` | Explain the interest cost | `Text Button` | `Icon: icon only` · `info` · `Circle: On` · `Size: 16` | "Explain the interest cost", spoken only, never shown | — | — | Shows a short explanation. `mock` | `finance.simulator` |
| `finance.interest-amount` | Interest cost, value | `text` | — | — | interest cost, sample: 0.000 € | `body/14/bold` · `Content/Default/Default` | — | `finance.simulator` |
| `finance.partner-offer` | The partner offer, set apart | `Card` | `Color: Light` · `Radius: 8px` · `Padding: With padding` | — | — | — | — | — |
| `finance.partner-content` | What the offer says | `composed` | — | — | — | See **Inventions** | — | `finance.partner-offer` |
| `finance.partner-heading` | Offer heading | `text` | — | "Find the right financing" | — | `body/16/bold` · `Content/Default/Default` | — | `finance.partner-content` |
| `finance.partner-body` | Offer description | `text` | — | "Get a free, personalised mortgage estimate with our partner Credit Agricole" | — | `body/14/regular` · `Content/Light/Default` | — | `finance.partner-content` |
| `finance.partner-action` | Go to the partner | `Button` | `Emphasis: Secondary` | "Customize simulation" | — | — | Opens the partner's simulation. `mock` | `finance.partner-content` |
| `finance.footnote-two` | Footnote marker | `text` | — | "2" | — | `body/12/regular` · `Content/Light/Default` | — | `finance.partner-content` |

## Inventions

### `energy.dpe-scale`

| Part | |
| --- | --- |
| **What is built** | A row of seven equal segments, one per class A to G. Fills in order: `Scales/Energy/Green100`, `Scales/Energy/Green200`, `Scales/Energy/Green400`, `Scales/Energy/Yellow100`, `Scales/Energy/Orange100`, `Scales/Energy/Red100`, `Scales/Energy/Red200`. Each segment carries its letter in `body/12/bold`: `Content/Constant/White/Default` on A and G, `Content/Default/Default` on B to F. Corners `Radius/4`. This property's class is raised with `Spacing/16` vertical padding against `Spacing/8` on the others |
| **Problem it belongs under** | Showing progress and data |
| **Ruled out** | `Energy Tag` — it shows one class, not the seven-step scale, and is used beside the scale for the grade · `Bar graph` — compares quantities, and its fills cannot be set per class · `Progress bar` — completion of a task, not a position on a classification · `Segmented control` — switches views, and this scale is not interactive |

### `energy.ges-scale`

| Part | |
| --- | --- |
| **What is built** | The same seven-segment row for emissions, filled `Scales/CO2/Blue100` to `Scales/CO2/Blue700` in order, lowest emission to highest. Letters: `Content/Constant/Black/Default` on `Blue100` to `Blue300`, `Content/Constant/White/Default` on `Blue400` to `Blue700`. This property's class is raised the same way. Its grade callout is a `Radius/4` block filled with the class's own `Scales/CO2/*` colour, carrying the letter in `body/14/bold` with the same letter colour rule |
| **Problem it belongs under** | Showing progress and data |
| **Ruled out** | `Energy Tag` — energy-efficiency ratings only, and coloured from the energy scale · `Bar graph` — compares quantities, and its fills cannot take `Scales/CO2/*` · `Donut chart` — parts of a whole, not a position on a scale · `Progress bar` — completion, not a classification |

### `energy.facts`

| Part | |
| --- | --- |
| **What is built** | A list of six `Cell Content` rows separated by `Divider`, in the order of the table above. It uses no tokens of its own: the rows and separators carry theirs |
| **Problem it belongs under** | Grouping and structuring content |
| **Ruled out** | `Tables` — label and value pairs, not data compared across columns · `Card` — a plain list, not one grouped block · `Accordion` — every fact is always visible · no list component exists, so a list of `Cell Content` rows is the intended pattern |

### `finance.simulator`

| Part | |
| --- | --- |
| **What is built** | Three stacks, top to bottom. Inputs: `finance.price`, `finance.contribution`, `finance.duration`. Result: `finance.monthly-estimate`, then `finance.per-month` and `finance.footnote-one` below it. Breakdown: `finance.breakdown-chart`, then three rows, each a name, its explain trigger and its amount, left to right. Stack gaps and padding use `Spacing/8` and `Spacing/16`, never more gap than padding |
| **Problem it belongs under** | Computing a figure from user input |
| **Ruled out** | `Estimation card` — shows a finished estimate with no controls · `Wizard` — the figures are changed freely, not in ordered steps · `Filter bar` — narrows a list, produces no figure · `Slider` — a price and a contribution need exact entry · `Counter field` — a small fixed set of durations is a `Dropdown` · `Bar graph` — three parts of one whole is a `Donut chart` |

### `finance.partner-content`

| Part | |
| --- | --- |
| **What is built** | The content placed in the `Card`'s content slot: `finance.partner-heading`, `finance.partner-body`, then `finance.partner-action` with `finance.footnote-two` beside it. Padding `Spacing/16`, gap `Spacing/8` |
| **Problem it belongs under** | Grouping and structuring content |
| **Ruled out** | `Button card` — the whole container is not one action · `Info state` — a full-area state, not an offer · `Feedback message` — status or guidance, not an offer with its own action · `Modal bottom sheet` — the offer stays on the page · `Content Placeholder` — never selected; the parent `Card` is placed and its slot filled |

## Change log

| Date | What changed | Why | IDs |
| --- | --- | --- | --- |
| 2026-09-24 | Data cells rewritten to the three data forms, and the facts list's token line made explicit | `/task-check` found the example breaking its own format | `energy.dpe-grade`, `energy.dpe-scale`, `energy.ges-scale`, `energy.facts`, `finance.price`, `finance.contribution`, `finance.monthly-estimate`, `finance.breakdown-chart`, `finance.borrowed-amount`, `finance.notary-amount`, `finance.interest-amount` |
| 2026-09-24 | Spec created from `brief-001`, following run-003's component and token choices | The worked example for the spec format | All |

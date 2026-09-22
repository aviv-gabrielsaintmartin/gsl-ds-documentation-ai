An estimation card presents a finished property price estimate — a headline
figure, the range around it, and how much confidence to place in it.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not established 🚧 | Not established 🚧 | Not established 🚧 |

---

## Usage

An estimation card shows the user what a property is thought to be worth. It
carries the headline figure, the lowest and highest price of the range, and a
confidence reading that says how firm the estimate is.

**It presents a completed estimate and carries no controls to adjust it.** The
figure arrives already calculated. Nothing on the card changes the inputs or
recalculates the result.

**It does carry two controls, and neither one alters the estimate.** One expands
the card to show the detail behind the figure; the other asks the user whether
the estimate was useful. Both change what is shown, not what was computed.

**A price simulator is two halves, and this is one of them.** When the user
adjusts controls and a figure recalculates in front of them, the result half is
this component and the controls half has no component at all — compose it, and
declare it.

### Platform

**Designed. Not established anywhere else.**

* The component set exists in the GSL Experiences library, in 16 shapes.
* **No web build exists.** Searched the whole design-system web repository, not
  one package — nothing matches. _Proved by search, 22 September 2026._
* **iOS and Android are not established**: no source for either was read.
* The component names `Selling price` and `Renting price` as content types. It
  carries no platform axis of its own.

### When to use

* **Estimation card** — presenting a property price estimate that has already
  been calculated.
* A seller-facing screen that reports what a property is worth.
* The result half of a price simulator, with the controls composed separately.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The figure is not a property price estimate | **KPI** |
| The user adjusts controls and the figure recalculates | No component is the controls half — compose it and declare it |
| The user advances through ordered steps | **Wizard** |

### Variant Selection Flow

```
Is the estimate already calculated, and not adjustable here?
├─ No  → this is a simulator. The controls half has no component.
│         Compose it, declare it, and use this card for the result
└─ Yes → continue

What is being estimated?
├─ A selling price        → Type = `Selling price`
├─ A renting price        → Type = `Renting price`
└─ Both, on one card      → Type = `Sell and Rent price`

How much room does the card have?
├─ A full column of its own  → Size = `Large`
├─ A narrower column         → Size = `Medium`
├─ A summary, detail hidden  → Size = `Small`
└─ A wide, short strip       → Size = `Horizontal`

Is the detail behind the figure shown?
├─ No  → State = `Collapsed`
└─ Yes → State = `Expanded`

     `Small` and `Horizontal` have no expanded form. See
     Size below before choosing one.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Show the confidence reading with the figure. | **DON'T:** Present the headline figure alone. The range and the confidence are what make it honest. |
| **DO:** Use `Sell and Rent price` when both figures are offered together. | **DON'T:** Place two cards side by side to show a sell and a rent price. |
| **DO:** Compose and declare the controls half when the user can change the inputs. | **DON'T:** Treat this card as a simulator. Nothing on it recalculates. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Estimation card** | — | A completed property price estimate, with range and confidence. | "Your flat is worth about €1,224,300" |
| [**KPI**](../kpi/kpi.md) | High | A single figure the user cannot change, of any kind. | "318 views this week" |
| [**Listing summary**](../listing-summary/listing-summary.md) | Medium | A property's own details rather than its estimated value. | Thumbnail, price, features, location |
| [**Wizard**](../wizard/wizard.md) | Low | Collecting the inputs an estimate needs, step by step. | "Tell us about your property" |

## Variants & Modifiers

**Three axes, 16 variants.** `Size`, `State` and `Type`. Twenty-four
combinations are possible and eight do not exist — see the grid below.

### Size

#### Large, Medium, Small, Horizontal

**How much room the card has**, and how much of the estimate it can show.

| Size | Collapsed | Expanded | Shape |
| --- | --- | --- | --- |
| **Large** | 320 wide | **447 wide** | The only size that widens when expanded |
| **Medium** | 288 wide | 288 wide | Grows downward only |
| **Small** | 288 wide | **none** | Summary only |
| **Horizontal** | 438 × 156 | **none** | A wide, short strip |

_**`Large` is the only size that changes width between its two states.** Every
other size keeps its width and grows taller. Budget for the extra 127 before
choosing `Large` in a fixed column._

### State

#### Collapsed, Expanded

**Whether the detail behind the figure is shown.** Collapsed gives the headline
figure, the range and the confidence reading. Expanded adds the breakdown and
the feedback question.

**Two sizes have no expanded form.** `Small` and `Horizontal` exist as
`Collapsed` only. Choosing either is a decision that the detail will never be
reachable from this card.

### Type

#### Selling price, Renting price, Sell and Rent price

**Which estimate the card carries.**

| Type | What it shows |
| --- | --- |
| **Selling price** | One estimate, what the property would sell for |
| **Renting price** | One estimate, what it would rent for |
| **Sell and Rent price** | Both, switched between on the card itself |

_**`Sell and Rent price` is about 60 taller than the other two**, at every size
and state. It carries a second figure and the control that switches between
them._

### The grid, and the eight combinations that do not exist

| Size | Selling / Renting / Sell and Rent, Collapsed | …Expanded |
| --- | --- | --- |
| **Large** | all three | all three |
| **Medium** | all three | all three |
| **Small** | all three | **none** |
| **Horizontal** | **`Selling price` only** | **none** |

**`Horizontal` is a single variant.** Collapsed, selling price, and nothing
else. A horizontal card cannot show a renting price, cannot show both, and
cannot expand.

_**Whether these eight absences are deliberate is not tested.** Nobody has been
asked. Three other short grids in the system were confirmed deliberate on
21 September 2026; these were not among them._

### Modifiers

**The card's parts can each be set**, and they are reachable when you place it.

#### Price range

**How the lowest and highest price are presented.** Four options: as text, or
with icons at three sizes.

#### Confidence indicator

**How firm the estimate is.** Five levels, from most to least confident:
**High**, **Good**, **Medium**, **Mediocre**, **Low**.

_Five levels, not three. A card showing a figure without one is presenting an
estimate as though it were a fact._

#### Estimation details

**The breakdown behind the figure**, shown when the card is expanded. Two
presentations: with icons, or as text.

#### Feedback module

**The question asking whether the estimate was useful.** Three forms — a thumbs
score at two text sizes, or a form.

**The thumbs form places `Feedback thumb buttons`.** That component is built by
a team outside the design system and has never been adopted into it; this card
is a place it is genuinely used. See
[`feedback-thumb-buttons`](../feedback-thumb-buttons/feedback-thumb-buttons.md).

## Behavior & Responsiveness

### Interactive States & Loading

* **Expand and collapse:** a button with a chevron switches between the two
  states, on `Large` and `Medium` only.
* **Switching sell and rent:** `Sell and Rent price` carries its own control for
  moving between the two figures.
* **Hover, pressed, focus, disabled:** not documented. The card itself carries no
  such states; the controls inside it have their own.
* **Loading:** not documented. No loading or skeleton form is drawn, and an
  estimate that is still being calculated has no representation here.

### Touch Target & Layout

* **Touch Target:** the expand control is a button 40 high including its touch
  target. The card itself is not a control.
* **Widths:** 320 or 447 (`Large`), 288 (`Medium`, `Small`), 438
  (`Horizontal`).
* **Heights:** 178 to 720, set by size, state and type together.
* **Width Adaptability:** each variant is drawn at a fixed width. No variant
  fills or hugs.

### Breakpoints & Platform Adaptations

Not documented

_The card carries no breakpoint or device axis. `Size` is a layout choice, not a
screen-width rule, and nothing says which size belongs at which width._

## Content & UX Writing

* **Capitalization:** **Sentence case.** "Estimated selling value", "Lowest
  price", "Highest price", "Average price".
* **Label Formula:** the range labels are fixed — "Lowest price" and "Highest
  price". The headline label names what was estimated: {Estimated} + {what} +
  {value}.
* **Length Limits:** not documented. No maximum is stated for any label.

### The brand name is a placeholder

The feedback question reads **"Did you find the [Name of the brand] estimate
useful?"**. The bracketed part is a slot, not wording — replace it with the
brand the screen belongs to.

### Prices carry their currency and their thousands separators

Figures are written in full, with the currency symbol and grouped thousands —
`€1,224,300`, `€900,000`, `€1,500,000`. They are never abbreviated to `€1.2M`.

## Accessibility (a11y)

* **Screen Readers:** not documented. No roles, labels or live-region behaviour
  are specified. The figure changing when the user switches between a sell and a
  rent price is a change nothing announces.
* **The confidence reading must survive without colour.** Five levels are
  offered and each carries its own word — `High` through `Low` — so the meaning
  does not rest on colour alone.
* **Keyboard Navigation:** not documented. The expand control and the sell/rent
  control should be reachable in order and show a visible focus ring, and
  neither is specified here.
* **Contrast:** not verified.

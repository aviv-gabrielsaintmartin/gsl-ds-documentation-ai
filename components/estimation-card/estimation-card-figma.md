_What is true of `Estimation card` **in Figma** and nowhere else. Layer names,
quirks, and how to work with the component in the tool._

_**This is not the usage documentation.** [`estimation-card.md`](estimation-card.md)
describes the component; this page describes the tool. Identity — keys, node IDs,
variant counts, property definitions — lives in `figma/*-registry.json` and is
never restated here._

---

## The four parts are private helper sets

The card's parts are separate component sets on the same page, each named with a
leading dot:

| Set | What it drives | Its axis |
| --- | --- | --- |
| `.price_range` | The lowest and highest price | `Range type` — `Text`, `Icons L`, `Icons M`, `Icon S` |
| `.confidence_indicator` | How firm the estimate is | See below — the axis has no name |
| `.estimation_details` | The breakdown behind the figure | `Type` — `Icons`, `Text` |
| `.estimation_feedback_module` | The "was this useful?" question | `Type` — `Thumbs score 12px text`, `Thumbs score 14px text`, `Form` |

**They are not registered separately.** They are private to this page, reached
through the card's exposed sub-instances rather than placed on their own.

## The confidence indicator's axis is still called `Property 1`

The axis carrying the five confidence levels was never renamed from the default.
It reads **`Property 1`**, and its options are `High`, `Good`, `Medium`,
`Mediocre`, `Low`.

**Preserved here verbatim** so a lookup by name finds it. A sync matching the
literal string will break if it is renamed, so anyone renaming it should expect
to update whatever reads it.

## The thumbs form embeds the desktop feedback buttons

`.estimation_feedback_module`'s thumbs forms place a `Feedback Thumb Buttons`
instance at 120 × 48 — the `Device=Desktop` variant, on every size of card
including the narrow ones.

Whether a 288-wide card should carry the desktop form of that component is not
established.

## Annotation stickers sit on the page

The page carries loose annotation text — `Request it` and `Bad variable` —
placed beside several variants. They are review marks left in the file, not
content of the component, and they render in any full-page export.

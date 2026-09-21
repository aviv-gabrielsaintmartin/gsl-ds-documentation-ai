A score tag is a Tag fixed to one of four seller lead scoring tiers.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not built 🚧 | Not established 🚧 | Not established 🚧 |

---

## Usage

A score tag marks a seller lead with the tier it has been scored into. Four
tiers exist, and nothing else: **Diamond**, **Gold**, **Silver**, **Bronze**.

It is a specialised `Tag`, not a new shape. The component wraps a `Tag`
instance and fixes everything about it — icon, label, surface colour and content
colour all follow the tier.

**It is for seller lead scoring and nothing else.** Any other status or category
label is a plain `Tag`.

### Platform

**Figma only, so far as this repo can prove.**

* The component set exists in the GSL Components library.
* **No web implementation exists.** `@gsl-core-web/design-system-ui` has no such
  component.
* **The colour tokens exist and are unused.** `color.surface.score.*` and
  `color.content.score.*` are defined for all four tiers and have **zero**
  recorded uses in the web code — see
  [`color-usage-ledger`](../../tokens/color/color-usage-ledger.md).

_iOS and Android are **not established**: no source for either was read._

### When to use

* **Score tag** — displaying the scoring tier of a seller lead.
* An agent-facing screen that ranks or lists leads by tier.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The label is any other status or category — "New", "Sold", "Exclusive" | **Tag** |
| The rating is a property's energy efficiency | **Energy tag** |

### Variant Selection Flow

```
Is this a seller lead's scoring tier?
├─ No → not this component. Any other status label is `Tag`
└─ Yes → pick the tier the lead was scored into

     Diamond   (default)
     Gold
     Silver
     Bronze

The tier is given to you. It is not a design choice, and there is no
rule here for deciding which tier a lead belongs in.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Use the tier the scoring system returned. | **DON'T:** Pick a tier for visual effect. The colour carries a meaning that is not yours to set. |
| **DO:** Use **Tag** for every label that is not a seller lead score. | **DON'T:** Reuse a score tag as a decorative award or ranking marker elsewhere. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Score tag** | — | A seller lead's scoring tier, one of four. | "Diamond" beside a lead in an agent's list |
| [**Tag**](../tag/tag.md) | High | Any other non-interactive status or category label. | "New", "Sold", "Exclusive" |
| [**Energy tag**](../energy-tag/energy-tag.md) | Medium | A property's energy-efficiency rating. | A DPE class on a listing |
| [**Chip**](../chip/chip.md) | Low | The same kind of label, but interactive — selectable, filterable, removable. | A filter the user can switch off |

## Variants & Modifiers

### Type

#### Diamond, Gold, Silver, Bronze

Four variants, `Diamond` by default. **The tier sets the icon, the label text
and both colours together.** They cannot be set apart from one another.

| Type | Icon | Label | Surface token | Content token |
| --- | --- | --- | --- | --- |
| **Diamond** | `gem` | Diamond | `color.surface.score.diamond` | `color.content.score.diamond` |
| **Gold** | `trophy` | Gold | `color.surface.score.gold` | `color.content.score.gold` |
| **Silver** | `medal` | Silver | `color.surface.score.silver` | `color.content.score.silver` |
| **Bronze** | `award` | Bronze | `color.surface.score.bronze` | `color.content.score.bronze` |

_Read live from the Figma component set. Each variant binds its surface and
content colour to the token named above._

### Modifiers

Not documented

_The component has one property, `Type`. There is no size, no emphasis, no
icon slot and no way to hide the label._

#### What the inner Tag is fixed to

Every tier wraps the same `Tag` configuration: **Primary**, font size **14**,
hierarchy **Strong**, with the left icon shown and the label shown.

**The inner `Tag` is not exposed.** A designer placing a score tag cannot reach
those settings through the parent, which is what makes the four tiers fixed
rather than merely conventional.

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

_A score tag is not interactive. It has no hover, pressed, focus or disabled
state, and no loading state — the same as `Tag`, which it is built from._

### Touch Target & Layout

* **Touch Target:** none. The component is not a control.
* **Height:** 24, fixed.
* **Layout:** a horizontal row — icon, then label, with a gap of 4 between them
  and 8 of padding on each side.
* **Icon size:** 16.
* **Width Adaptability:** content-hug. The tag is as wide as its label.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. The four variants carry no device or
breakpoint axis._

## Content & UX Writing

* **Capitalization:** **Title case, and fixed.** The four labels are `Diamond`,
  `Gold`, `Silver`, `Bronze`, written into the component.
* **Label Formula:** none. The label is the tier name, and is not editable.
* **Length Limits:** not applicable, for the same reason.

### Translation

Not documented

_Whether the four tier names are translated, or stay in English across markets,
is not recorded anywhere in this repo._

## Accessibility (a11y)

* **Screen Readers:** Not documented. The component carries no role or label
  beyond its visible text, and the tier name is what would be read.
* **Colour alone:** **the tier is carried by colour, icon and word together.**
  Each tier has its own icon and its own written label, so the meaning survives
  without colour.
* **Keyboard Navigation:** not applicable. The component is not focusable.
* **Contrast:** not verified. The score colour tokens have no recorded contrast
  check, and no implementation exists to measure.

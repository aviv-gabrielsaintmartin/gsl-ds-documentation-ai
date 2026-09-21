A score tag is a Tag fixed to one of four seller lead scoring tiers.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

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

**Figma and web both carry it.**

* The component set exists in the GSL Components library.
* **The web component is built**, and lives in
  `@gsl-core-web/design-system-patterns-tag` — **not** in the main UI package.
  That is why a search of `libraries/ui` finds nothing.
* **The web build uses the score colour tokens**, one surface and one content
  token per tier, exactly as Figma does.

_iOS and Android are **not established**: no source for either was read._

_**A count of zero uses for the score colour tokens appears in
[`color-usage-ledger`](../../tokens/color/color-usage-ledger.md), and it measures
`libraries/ui` only.** The component sits in the patterns package, so the tokens
are used and the ledger's scope does not see it._

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

Four variants. **The tier sets the icon, the label text and both colours
together.** Icon and colour cannot be set apart from the tier on either
platform; only the label can be replaced, and only on web.

**The two platforms disagree on the default.** Figma opens on `Diamond`; the web
component defaults to `bronze`. Neither is wrong, and **a design agent should
set the tier explicitly rather than rely on either default.**

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

_The component has one property, `Type`. There is no size, no emphasis and no
icon slot. The label cannot be hidden; on web it can be replaced._

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

* **Capitalization:** **Title case.** Each tier's own name — `Diamond`, `Gold`,
  `Silver`, `Bronze` — supplied by the component, not typed by the user.
* **Label Formula:** none. The label is the tier name.
* **Length Limits:** not applicable. The longest word sets the width.

### The label can be overridden, and normally is not

**The default label is the tier name, and it is what you should use.** The web
component accepts a replacement string, so the text is not locked.

Figma is the stricter of the two: its four variants carry the tier names as
fixed text.

### Translation

**The four tier names are translated, in the web build, into four locales.**

| Tier | en-GB | fr-FR | de-DE | nl-NL |
| --- | --- | --- | --- | --- |
| **Diamond** | Diamond | Diamant | Diamant | Diamant |
| **Gold** | Gold | Or | Gold | Goud |
| **Silver** | Silver | Argent | Silber | Zilver |
| **Bronze** | Bronze | Bronze | Bronze | Brons |

_An overridden label is your own string and is not translated for you._

## Accessibility (a11y)

* **Screen Readers:** Not documented. The component carries no role or label
  beyond its visible text, and the tier name is what would be read.
* **Colour alone:** **the tier is carried by colour, icon and word together.**
  Each tier has its own icon and its own written label, so the meaning survives
  without colour.
* **Keyboard Navigation:** not applicable. The component is not focusable.
* **Contrast:** not verified. The score colour tokens carry no recorded contrast
  check in this repo.

A badge store is a replica of the official App Store or Google Play download
badge, offering the user a way to install the app.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | N/A | N/A | N/A |

---

## Usage

A badge store sends the user to the app's page on a public app store. It is the
button Apple and Google publish for exactly this purpose, redrawn here so the
design system can keep it consistent and up to date.

**It is mostly a footer or a landing page.** Gabriel, 21 September 2026. It is
not a general-purpose link and does not belong inside a flow.

**The artwork is not ours to change.** Apple and Google each publish rules for
how their badge may be drawn, sized and placed. The component carries an
approved drawing of each. Redrawing, recolouring or restretching one breaks
those rules.

### Platform

**Designed, and built nowhere — deliberately.**

* The component set exists in the GSL Components library, in eight shapes across
  four languages.
* **No web, iOS or Android build exists, and none is planned.** It is a replica
  of two badges Apple and Google publish, so there was nothing worth building on
  our side. Gabriel, 21 September 2026.
* **What that means when you place one:** place the component as it is. There is
  nothing to generate, and no code component to reach for.

### When to use

* **Badge store** — offering the user a download of the app from the App Store
  or Google Play.
* A footer that carries the app-download links.
* A landing page whose purpose is to get the app installed.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The destination is anything other than an app store | **Link** |
| A count or marker is pinned to another component | **Badge**, a different component one word away |

_**`Badge` and `Badge store` are unrelated.** One word apart, and nothing else in
common: `Badge` is an attention marker attached to a host component._

### Variant Selection Flow

```
Which store does this badge point at?
├─ Apple's  → Platform = `App Store`
└─ Google's → Platform = `Google Play`

Offering both stores? Place two badges, one per store.

Which surface is it sitting on?
├─ A light surface → Theme = `Light`
└─ A dark surface  → Theme = `Dark`

     `Dark` exists for `Outline` only. See Type below.

Which drawing?
├─ The filled badge, the one the stores publish as their
│  default → Type = `Filled`
└─ The outlined badge, for when the filled one is too
   heavy for the surface → Type = `Outline`

Which language is the page in?
└─ Language = `English`, `French`, `German` or `Dutch`

     The badge's own wording is drawn into the artwork. It does
     not follow the page's language on its own — pick it.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Match `Language` to the language of the page it sits on. | **DON'T:** Leave an English badge on a French, German or Dutch page. Nothing changes it for you. |
| **DO:** Place both store badges when the app is on both stores. | **DON'T:** Offer one store when the app is on both. |
| **DO:** Keep the badge at its drawn height of 40. | **DON'T:** Stretch, crop or recolour the artwork. It is a replica of a badge its owner sets rules for. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Badge store** | — | A download link to the App Store or Google Play. | The app-download row in a site footer |
| [**Badge**](../badge/badge.md) | High | An attention marker — a count or a dot — pinned to a host component. | "3" on a notifications icon |
| [**Link**](../link/link.md) | High | Any other navigation to another destination. | "Read our terms" |
| [**Button**](../button/button.md) | Low | An action taken on this screen rather than a departure from it. | "Save search" |

## Variants & Modifiers

**Four axes, 24 variants.** `Type`, `Platform`, `Theme` and `Language`.

### Store

#### App Store, Google Play

**Which store the badge points at.** Two options, and they are not
interchangeable — each is that company's own badge. The axis is named
`Platform`, and it means the app store, never the build platform.

| Store | Width | Height |
| --- | --- | --- |
| **App Store** | 120, and **126 in French** | 40 |
| **Google Play** | 135 | 40 |

_The French App Store badge is wider because its wording is longer. Nothing
else changes size._

### Type

#### Filled, Outline

**Two drawings of the same badge**, differing in weight.

| Type | What it is | Colour |
| --- | --- | --- |
| **Filled** | The solid badge, the one each store publishes as its default. | The store's own colours. Fixed, and not drawn from design-system tokens. |
| **Outline** | The lighter drawing — wordmark and logo on an outlined container, no solid fill. | Design-system tokens. See the table below. |

**`Filled` exists on a light theme only.** Sixteen `Outline` variants cover both
themes; eight `Filled` variants cover `Light`. That is 24 rather than 32, and
**it is deliberate** — Gabriel, 21 September 2026. The filled badge is drawn to
sit on any surface, so it needs no dark counterpart.

### Theme

#### Light, Dark

**Which surface the badge is sitting on**, for the `Outline` type.

| Theme | Outline colour | Wordmark colour |
| --- | --- | --- |
| **Light** | `Color/Border/Subdued/Default` | `Color/Content/Default/Default` |
| **Dark** | `Color/Border/Light/Default` | `Color/Content/Default/Default` |

_**The theme changes the outline, not the wordmark.** Both themes bind the same
content token; only the border token differs, so the wordmark stays legible
while the container adapts to the surface behind it._

### Language

#### English, French, German, Dutch

**Four languages, and the wording is drawn rather than typed.** "Download on the
App Store" and "Get it on Google Play" are supplied by the stores in each
language.

**Nothing translates this for you.** The wording is part of the artwork, so it
does not follow a page's locale, and it cannot be edited or replaced. Pick the
language when you place the badge.

### Modifiers

Not documented

_The component has no modifiers. Everything about it is set by the four axes
above — there is no size option, no icon slot, and no text to swap._

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

_No interactive states are drawn. The badge has no hover, pressed, focus or
disabled variant, and no loading state, though it is a link and behaves as one
when built._

### Touch Target & Layout

* **Touch Target:** **height 40**, which is the whole badge. This is below the
  44 minimum a touch target normally carries, and the artwork's height is fixed
  by the stores rather than by us.
* **Height:** 40, on every variant.
* **Width:** fixed per variant — 120 or 126 for App Store, 135 for Google Play.
* **Width Adaptability:** none. The badge is a fixed drawing and does not
  stretch, hug or fill.

### Breakpoints & Platform Adaptations

Not documented

_The component carries no device or breakpoint axis, and its size is the same at
every width. Two badges placed side by side on a narrow screen are the caller's
layout problem, not the component's._

## Content & UX Writing

* **Capitalization:** not ours to set. The wording is the store's own artwork —
  "Download on the App Store", "Get it on Google Play".
* **Label Formula:** none. There is no label to write.
* **Length Limits:** not applicable. The wording is fixed per language.

### There is nothing to write

**Every word on this component is drawn into it.** No text can be typed,
replaced or shortened. The only content decision is which of the four languages
to place.

## Accessibility (a11y)

* **Screen Readers:** **the badge carries no text a screen reader can read.**
  The wording is outlined artwork, not characters. Whatever surface this is
  built on must supply an accessible name — the store's own wording in the
  matching language is the right one.
* **Keyboard Navigation:** not documented. No focus treatment is drawn. As a
  link it should be reachable and show a visible focus ring, and neither is
  specified here.
* **Touch target:** **40 high, under the 44 minimum.** The artwork's height is
  set by Apple and Google. Give it clear space rather than resizing it.
* **Contrast:** not verified. The `Filled` artwork uses the stores' own colours,
  which carry no contrast check in this repo.

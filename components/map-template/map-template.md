A map template is a whole map screen — the map itself, its controls, its price
pins and a listing card — supplied as a starting point to build on.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not established 🚧 | Not established 🚧 | Not established 🚧 |

---

## Usage

A map template gives you a complete map screen rather than a piece of one. It
arrives carrying the map surface, the provider's attribution, the floating
actions over the map, the zoom and locate controls, price pins and a listing
card for the selected property.

**It is meant to be detached, and that is unusual.** The template is a
blueprint. You set the kind of map you need, switch off the elements you do not
want, then detach it and build on top. **This is the one place in the system
where detaching is the instruction rather than the failure.**

**It is all-or-nothing until you detach it.** A partial map template is not a
realistic build. Take the whole thing, then cut it down.

**Its pin sets are never selected directly.** The price pins and the polygon
layers belong to the template and are reached by placing it.

### Platform

**Designed. Not established anywhere else.**

* The component set exists in the GSL Experiences library, in 27 shapes.
* **No web build exists.** Searched the whole design-system web repository, not
  one package — nothing matches. _Proved by search, 22 September 2026._
* **iOS and Android are not established**: no source for either was read.
* **The component carries its own platform axis**, covering web, iOS and
  Android. That axis is about how the map *looks* on each — the provider's
  attribution and the control styling — not about whether anything is built.

### When to use

* **Map template** — building a map screen where the user browses properties
  geographically.
* A search results screen shown as a map rather than a list.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A single property is shown, with no map browsing | **Listing card** |
| Results are a list rather than a map | **Listing summary** |
| The screen filters results rather than maps them | **Filter bar** |

### Variant Selection Flow

```
Which platform is the screen for?
├─ Web     → Plateform = `Web`
├─ iOS     → Plateform = `iOS`
└─ Android → Plateform = `Android`

     The axis name is misspelled `Plateform` in the library.
     Type it as it is written. See the tool page.

How close is the map?
├─ Pulled back, a city or region   → Zoom level = `Away`
├─ Close in, a street              → Zoom level = `Close`
└─ Right down, buildings in 3D     → Zoom level = `Very zommed / 3D`

     Also misspelled, also typed as written.
     Android has no `Very zommed / 3D`. See the grid below.

How should the map look?
├─ The default map          → Style = `Standard`
├─ A dark map               → Style = `Dark Mode`
├─ Aerial imagery           → Style = `Satellite`
└─ Prices shown as a layer  → Style = `Price Map`

     `Dark Mode` does not exist for web.
     `Price Map` does not exist at the closest zoom.

Which elements does the screen need?
├─ The floating actions over the map → CTA = on
└─ The card for the selected property → Listing Card = on

     Both are on by default. Switch off what you do not need
     before detaching.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Detach the template once you have set it up. It is a blueprint. | **DON'T:** Keep it linked and then fight its structure to fit your screen. |
| **DO:** Switch off the elements you do not need before detaching. | **DON'T:** Delete parts out of a detached copy you could have switched off first. |
| **DO:** Place the whole template. | **DON'T:** Rebuild a map screen from the pins and controls yourself. |
| **DO:** Replace the price pins after detaching. | **DON'T:** Ship the pins that arrive with it — they are the superseded set. See below. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Map template** | — | A whole map screen, detached and built on. | Property search shown on a map |
| [**Listing card**](../listing-card/listing-card.md) | High | One property's summary card. Arrives inside the template. | The card for the pin the user tapped |
| [**Listing summary**](../listing-summary/listing-summary.md) | Medium | A property summary in a list rather than over a map. | A results list |
| [**Filter bar**](../filter-bar/filter-bar.md) | Medium | Narrowing what the map shows. | "2+ bedrooms, under €500k" |

## Variants & Modifiers

**Three axes and two switches, 27 variants.** Thirty-six combinations are
possible and nine do not exist.

### Map platform

#### Web, iOS, Android

**Which platform the map is drawn for.** It changes the provider's attribution
and the control styling, not the layout.

_The axis is misspelled in the library. It is typed as written, and the
misspelling is recorded on the tool page rather than corrected here._

### Zoom level

#### Away, Close, Very zommed / 3D

**How close the map sits.** `Away` shows a city or region, `Close` a street, and
the third option drops right down with buildings in three dimensions.

**Android has no closest zoom.** The third option exists for web and iOS only.

### Style

#### Standard, Dark Mode, Satellite, Price Map

**How the map surface looks.**

| Style | What it is | Where it exists |
| --- | --- | --- |
| **Standard** | The default map | Everywhere |
| **Satellite** | Aerial imagery | Everywhere |
| **Dark Mode** | A dark map surface | **iOS and Android only** |
| **Price Map** | Prices drawn as a layer over the map | **Not at the closest zoom** |

### The grid, and the nine combinations that do not exist

Three rules account for all nine.

| Rule | Combinations lost |
| --- | --- |
| **Web has no dark map** | 3 — one at each zoom |
| **Android has no closest zoom** | 4 — one per style |
| **The closest zoom has no price map** | 2 — web and iOS |

_**Whether these are deliberate is not tested.** Nobody has been asked. A web
map with no dark surface is the one worth querying, since web is the only
platform missing a style every other platform has._

### Modifiers

#### The two switches

| Switch | Default | What it controls |
| --- | --- | --- |
| **CTA** | on | The floating actions sitting over the map |
| **Listing Card** | on | The card for the selected property |

_Both are on when you place the template. Switch off what the screen does not
need before detaching, rather than deleting it afterwards._

#### The parts that arrive with it

| Part | What it is |
| --- | --- |
| **Map surface** | The map itself, following the three axes above |
| **Provider attribution** | The map provider's mark, required by the provider |
| **Floating actions** | The actions over the map, controlled by the `CTA` switch |
| **Map controls** | Zoom and locate, stacked at the edge |
| **Price pins** | The price markers on the map — **superseded, see below** |
| **Listing card** | The selected property's card, controlled by its switch |

#### The price pins that arrive are the superseded set

**Every one of the 27 variants carries the old price pins.** Three per variant,
81 in all, and the current pin sets are used nowhere in the template.

**What that means when you place it:** a detached copy inherits the old pins,
and they will not match a screen built from the current ones. Replace them after
detaching.

_**Proved by reading all 27 variants, 22 September 2026.** The exact names, and
the same problem in the floating actions, are on the tool page._

#### The polygon layers

Two layers draw an area on the map rather than a point: one outlines the shape,
the other dims everything outside it. **Both belong to the template and are
never selected on their own.**

The outline draws either a simple area or district boundaries. The dimming layer
follows a shape or a radius, and offers a light, a dark and a price-map form —
though **a radius has no price-map form**.

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

_No states are drawn. Panning, zooming, tapping a pin and selecting a property
are all real behaviours of a map screen, and none of them is specified here._

### Touch Target & Layout

* **Touch Target:** the map controls are buttons 40 × 40, stacked. The floating
  actions are 48 high.
* **Size:** every variant is drawn 1379 × 1379 — a square working area, not a
  screen size. The screen shape is yours to set after detaching.
* **Listing card:** 328 wide when shown.
* **Width Adaptability:** none as supplied. The template is detached and laid
  out to the real screen.

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web** | Provider attribution has a desktop form and two mobile forms, one of them open. No dark map. |
| **iOS** | Provider attribution in light and dark. All four styles. |
| **Android** | Provider attribution in light and dark. No closest zoom. |

_**No breakpoint number is given**, and the platform axis is not a breakpoint.
The template is a square working area; where one layout becomes another is
decided by the screen you build from it._

## Content & UX Writing

* **Capitalization:** not documented. The template carries no copy of its own —
  every word on it belongs to a component inside it or to the map data.
* **Label Formula:** none.
* **Length Limits:** not documented.

### Prices on pins are abbreviated

Pin labels carry a price and nothing else, shortened to fit the pin. Their exact
formatting is set by the pin set rather than by this template.

## Accessibility (a11y)

* **Screen Readers:** not documented. A map screen's accessible equivalent — a
  list of the properties shown — is not part of the template and is not
  specified anywhere.
* **Keyboard Navigation:** not documented. Panning and zooming a map by keyboard
  is not covered.
* **Touch target:** map controls are 40 × 40, **below the 44 minimum**. Floating
  actions are 48 and clear it.
* **The provider attribution is required.** It is not decoration and must not be
  removed when the template is cut down.
* **Contrast:** not verified. Pins and controls sit over map imagery that
  changes with the style, and no style was checked.

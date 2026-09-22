A mega menu is the panel a navigation bar entry opens on desktop.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not built here 🚧 | N/A | N/A |

---

## Usage

A mega menu is the wide panel that drops from the navigation bar when the user
picks a top-level entry. It holds that entry's links, laid out in columns.

**It is one part of the web navigation, not a component on its own.** The bar
holds the entries; the mega menu is what an entry opens on desktop; the burger
menu is what replaces it on mobile.

```
Web navigation
├─ Navigation bar     the bar itself, always visible
├─ Mega menus         ← this page, DESKTOP
└─ Burger menu        the mobile replacement
```

**It is a catalogue, not a configurable component.** Each variant is one brand's
one menu at one width. There is no generic empty mega menu to fill in.

### Platform

**Desktop web only.** Its breakpoints start at 1024, so it has no mobile form —
`Burger menu` is the mobile answer.

**Who owns it, precisely.** Gabriel, 21 September 2026:

* **The design was built by the design system team.**
* **It is not stored in the design system today.**
* **The transfer into the design system is ongoing.**

So it is a component moving in, not one sitting permanently outside. **No web
implementation exists in the design system's own code**, searched across every
package.

### When to use

* **Mega menus** — a navigation bar entry needs to open a panel of links, on desktop.
* Top-level navigation on the main B2C or B2B websites.
* Staying compliant with what the real product ships.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Global navigation inside a product screen rather than the main site | **Navigation bar** |
| The screen is mobile, where the panel is replaced | **Burger menu** |

### Variant Selection Flow

```
1. Which brand is the screen?
   Default · Immonet · Immoweb · Immowelt · Logic-Immo ·
   Meilleurs agents · SeLoger

2. Which width?
   1024 px · 1366 px · 1536 px

3. Which menu?
   The entry the user clicked in the navigation bar.
   The options are that brand's real menu names, prefixed by brand:
     SL •  SeLoger          IWT • Immowelt
     MA •  Meilleurs agents IWB • Immoweb
     IMT • Immonet          LI  • Logic-Immo

Pick the brand first. The Menu options are not shared between brands —
"SL • To rent" exists for SeLoger and nowhere else.
```

**There is no neutral mega menu.** `Brand=Default` is a starting point, not a
blank one.

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Pick the brand before anything else. The menu names depend on it. | **DON'T:** Take a menu from one brand and relabel it for another. The entries are that brand's real site structure. |
| **DO:** Match the breakpoint to the width you are drawing at. | **DON'T:** Draw a 1536 menu on a 1024 frame. The column count changes with the width. |
| **DO:** Draw the navigation bar with it. | **DON'T:** Show a mega menu floating with no bar above it. It has no meaning on its own. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Mega menus** | — | The desktop panel a navigation bar entry opens. | "To rent" opening a column of rental links |
| [**Navigation bar**](../navigation-bar/navigation-bar.md) | High | The bar that holds the entries and opens this. | The header of a SeLoger page |
| [**Burger menu**](../burger-menu/burger-menu.md) | High | What replaces this on mobile. | The same navigation at 320 px |
| [**Action menu**](../action-menu/action-menu.md) | Low | A dropdown of contextual **actions**, not navigation. | "Edit", "Duplicate", "Delete" |

## Variants & Modifiers

### Brand, breakpoint and menu

#### 96 variants, three axes

| Property | Options | Default |
| --- | --- | --- |
| **Brand** | `Default`, `Immonet`, `Immoweb`, `Immowelt`, `Logic-Immo`, `Meilleurs agents`, `SeLoger` | `Default` |
| **Breakpoint** | `1024 px`, `1366 px`, `1536 px` | `1024 px` |
| **Menu** | That brand's own menu names | `Default` |

**The Menu axis is content, not configuration.** Its options read as real site
navigation — *SL • To rent*, *SL • Offices & Shops*, *IWT • Property prices*,
*IMT • Real estate appraisal*, *IWB • Valuate*, *MA • Choose an agency*.

**The grid is sparse on purpose.** 96 variants, far fewer than every brand
crossed with every menu, because a brand only has the menus it has.

### Modifiers

Not documented

_The component carries no booleans, no instance swaps and no slots. Everything
is selected through the three variant axes._

#### One panel, columns inside

A mega menu is a full-width row of link columns. At 1536 the panel is 192 tall,
padded 24 top and bottom and 80 on each side, with 24 between columns; each
column is 326 wide.

**The column count is what the breakpoint changes**, not the type size or the
padding.

## Behavior & Responsiveness

### Interactive States & Loading

* **Opening:** the panel appears when a navigation bar entry is picked. **How it
  opens is not documented** — no motion, delay or dismissal rule exists in the
  component.
* **Hover / Pressed / Focus:** Not documented at the panel level. The links
  inside are their own components.
* **Loading:** Not documented.

### Touch Target & Layout

* **Touch Target:** none at the panel level. The links inside carry their own.
* **Panel width:** full viewport width, at the breakpoint chosen.
* **Side padding:** 80 at 1536.
* **Column gap:** 24. **Column width:** 326 at 1536.
* **Panel height:** 192 in the 1536 example, and it follows the content.

### Breakpoints & Platform Adaptations

| Breakpoint | Layout & Width Behaviour |
| --- | --- |
| **1024 px** | The narrowest mega menu. Fewest columns |
| **1366 px** | More columns |
| **1536 px** | Widest. 80 side padding, 326 columns |
| **Below 1024 px** | **No mega menu exists.** Use `Burger menu` |

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented. Each entry names a destination.
* **Length Limits:** Not documented.

### The content is the brand's, not ours

The menu names in this component are the real navigation of real sites —
*Historique des ventes*, *Annuaire des agences immobilières*, *Comprendre le
marché immobilier*.

**They are not examples to be replaced.** Choosing a variant is choosing a real
menu. Writing new entries is a change to a live site's information
architecture, which is not a design system decision.

**Some placeholder text survives in the library** — *Lorem ipsum* strings in the
documentation areas. Those are the exception and are not menu content.

## Accessibility (a11y)

* **Screen Readers:** Not documented. No implementation exists in the design
  system's code to read the behaviour from.
* **Keyboard Navigation:** Not documented. Whether the panel traps focus, and
  how it is dismissed, is unrecorded and would be the first thing to settle.
* **The panel has no accessible name** stated anywhere. It is opened by a
  navigation bar entry, and nothing says the two are associated.
* **Not established** whether the panel closes on `Escape`, on blur, or only on
  a second click of its entry.

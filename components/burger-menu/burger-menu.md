A burger menu is the panel that replaces the mega menu on mobile.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not built 🚧 | N/A | N/A |

---

## Usage

A burger menu is a full-height panel that slides over the page when the user
taps the burger icon in the navigation bar. It holds the site's navigation as a
list of rows.

**It is one part of the web navigation, not a component on its own.** Gabriel,
21 September 2026: **the burger menu replaces the mega menu on mobile.**

```
Web navigation
├─ Navigation bar     the bar itself, always visible
├─ Mega menus         what an entry opens on DESKTOP
└─ Burger menu        ← this page, MOBILE
```

### Platform

**Mobile web only.** Its two breakpoints are **320** and **768**, and there is
no desktop form — above those widths the mega menu is the answer.

**No web implementation exists**, searched across every package in the design
system's code.

### When to use

* **Burger menu** — the mobile navigation menu opened from the navigation bar's burger icon.
* The screen is at 320 or 768, where a mega menu does not exist.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Navigation stays visible across the top rather than behind an icon | **Navigation bar** |
| The list is contextual actions rather than navigation | **Action menu** on desktop, **Modal bottom sheet menu** on mobile |

### Variant Selection Flow

```
1. Which width?
   ├── 320 px ─> phone
   └── 768 px ─> tablet

2. Does the screen have a bottom bar behind the menu?
   ├── No  ─> Bottom bar = Off
   └── Yes ─> Bottom bar = On

That is all four variants. There is nothing else to set.
```

**There is no profile variant here.** `Burger menu (profil)` is a separate
component and is **never to be selected** — see the ruleset. Use this one.

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Match `Bottom bar` to what the screen behind actually has. | **DON'T:** Leave it `Off` on a screen that shows a bottom bar. The menu would overlap it. |
| **DO:** Draw the navigation bar with it. The menu is opened from the bar's burger icon. | **DON'T:** Show a burger menu with no bar. Nothing would have opened it. |
| **DO:** Use this on mobile and a mega menu on desktop. | **DON'T:** Treat them as alternatives you may pick between. The width decides. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Burger menu** | — | The mobile navigation panel, opened from the bar's burger icon. | The site's navigation at 320 px |
| [**Navigation bar**](../navigation-bar/navigation-bar.md) | High | The bar holding the burger icon that opens this. | The header of a mobile page |
| [**Mega menus**](../mega-menus/mega-menus.md) | High | What this replaces on desktop. | The same navigation at 1366 px |
| [**Action menu**](../action-menu/action-menu.md) | Low | Contextual **actions**, not navigation. | "Edit", "Share", "Delete" |

## Variants & Modifiers

### Breakpoint and bottom bar

#### Four variants

| Property | Options | Default |
| --- | --- | --- |
| **Breakpoint** | `320 px`, `768 px` | `320 px` |
| **Bottom bar** | `Off`, `On` | `Off` |

2 × 2 = 4. The full grid.

**`Burger menu (profil)` carries exactly the same two axes and the same four
variants.** The two differ in content only — which is why one is selectable and
the other is not.

### Modifiers

Not documented

_The component carries no booleans, no instance swaps and no slots. Both axes
are variants._

#### Anatomy

The variant is a device-sized canvas holding two things: a **backdrop** over the
page, and the **menu panel** itself.

| Part | What it is |
| --- | --- |
| **Backdrop** | The dimmed page behind the panel |
| **Close button** | 40 × 40, at the top of the panel |
| **Rows** | The navigation entries, 56 tall, padded 16 all round |
| **Dividers** | A 1-tall rule between rows |

At 768 the panel is 392 wide against a 768 canvas, with 56 of padding above the
first row. **The panel does not fill the width** — the backdrop stays visible
beside it.

## Behavior & Responsiveness

### Interactive States & Loading

* **Opening:** the panel appears when the navigation bar's burger icon is
  tapped. **How it opens is not documented** — no motion or timing is recorded.
* **Closing:** a close button sits at the top of the panel. **Whether tapping
  the backdrop also closes it is not established.**
* **Hover / Pressed / Focus:** Not documented at the panel level. The rows are
  their own components.
* **Loading:** Not documented.

### Touch Target & Layout

* **Touch Target:** each row is 56 tall, which carries the target. The close
  button is 40 × 40.
* **Panel width:** 392 at the 768 breakpoint.
* **Row padding:** 16 on all four sides. **Rows are separated by a 1-tall divider.**
* **Panel top padding:** 56, above the first row.
* **Width Adaptability:** the panel is a fixed width against the viewport, not a
  full-width sheet.

### Breakpoints & Platform Adaptations

| Breakpoint | Layout & Width Behaviour |
| --- | --- |
| **320 px** | Phone. The narrower of the two |
| **768 px** | Tablet. 392-wide panel, backdrop visible beside it |
| **Above 768 px** | **No burger menu.** Use `Mega menus` |

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented. Each row names a destination.
* **Length Limits:** Not documented. A row is 56 tall with 16 of padding, so a
  long label has one line to fit in.

### The content is the site's navigation

The rows carry a real site's entries, and the Figma page shows them in German
and French across brands.

**They are not examples to be replaced freely.** What appears here is the mobile
form of the same information architecture the mega menu carries on desktop, and
the two should not diverge.

## Accessibility (a11y)

* **Screen Readers:** Not documented. No implementation exists to read the
  behaviour from.
* **Keyboard Navigation:** Not documented. Whether the panel traps focus, and
  whether `Escape` closes it, is unrecorded.
* **The backdrop's role is not stated** — whether it is an inert dimmer or a
  dismiss target. **Not established**, and it changes how the panel is built.
* **The close button has no stated accessible name.** It is a 40 × 40 icon
  button, and an icon is not a name.

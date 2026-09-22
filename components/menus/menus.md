A menus component is the profile or language panel a navigation bar control opens.

> 🚫 **Never select this component.** It is withheld, **provisionally** — nothing
> requires it to build anything today, and `Navigation bar`'s own controls
> already carry the profile and language menus. Gabriel, 18 September 2026.
> **It is in use, though:** one brand, in one file, and what for is under
> investigation. This page describes what the component is; it is not permission
> to place it. Use `Navigation bar`.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not built 🚧 | N/A | N/A |

---

## Usage

A menus component is a narrow dropdown panel holding one of two lists: the
user's **profile** options, or the **language** choices.

It is a part of the web navigation family, opened from a control in the
navigation bar rather than from a top-level entry.

```
Web navigation
├─ Navigation bar     the bar itself — its own controls carry profile and language
├─ Mega menus         what an entry opens on desktop
├─ Burger menu        the mobile replacement
└─ Menus              ← this page, and normally not selected
```

**Why it is withheld.** `Navigation bar` already carries a profile button and a
language control. A separate `Menus` component duplicates them, and nothing
today needs it standing on its own.

### Platform

**Web only.** The panel is 320 wide and carries no breakpoint axis.

**No web implementation exists**, searched across every package in the design
system's code.

### When to use

* **Menus** — nothing, today. The component is on the never-select list.
* Use **Navigation bar**, whose own controls include the profile and language menus.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A user needs their profile or language options from the site header | **Navigation bar** |
| The list is contextual actions rather than account or language options | **Action menu** |

### Variant Selection Flow

```
This flow is here to describe the component, not to route you to it.
It is on the never-select list. Use `Navigation bar`.

1. Which list?
   ├── Profil   ─> the user's account options
   └── Language ─> the language choices

2. Which brand?
   Profil    → Default · SeLoger · Immonet · Immowelt · Meilleurs Agents · Immoweb
   Language  → Default only

3. Type follows from the list, it is not a free choice:
   Profil   is always Type=Default
   Language is always Type=Simple
```

**Seven variants, not twenty-four.** The three axes could cross to far more; only
seven exist, because `Language` has one brand and one type.

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Use **Navigation bar** for profile and language. Its own controls carry both. | **DON'T:** Place this component. It is withheld and duplicates the bar. |
| **DO:** Tell Gabriel if a real screen needs a profile or language menu standing on its own. | **DON'T:** Work around the restriction by rebuilding the panel from primitives. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Menus** | — | The profile or language panel. **Never select.** | — |
| [**Navigation bar**](../navigation-bar/navigation-bar.md) | High | Carries the profile and language controls itself. **Use this instead.** | The site header's account button |
| [**Action menu**](../action-menu/action-menu.md) | Medium | A dropdown of contextual actions rather than account options. | "Edit", "Duplicate" |
| [**Burger menu**](../burger-menu/burger-menu.md) | Low | The mobile navigation panel, which carries its own profile rows. | Navigation at 320 px |

## Variants & Modifiers

### Content, type and brand

#### Seven variants

| Property | Options | Default |
| --- | --- | --- |
| **Content** | `Profil`, `Language` | `Profil` |
| **Type** | `Default`, `Simple` | `Default` |
| **Brand** | `Default`, `SeLoger`, `Immonet`, `Immowelt`, `Meilleurs Agents`, `Immoweb` | `Default` |

**The grid is sparse and the pattern is readable:**

| Content | Type | Brands | Variants |
| --- | --- | --- | --- |
| **Profil** | `Default` | All six | 6 |
| **Language** | `Simple` | `Default` only | 1 |

**`Type` is not a free choice.** It tracks the content: a profile menu is
`Default`, a language menu is `Simple`. No variant pairs them otherwise.

**The profile menu is branded, the language menu is not.** Profile options differ
per brand; the language list does not.

### Modifiers

Not documented

_No booleans, no instance swaps, no slots. All three properties are variants._

#### Anatomy

The panel is **320 wide**, padded 8 above and below, and built from rows.

| Part | Size |
| --- | --- |
| **Header row** | 320 × 56, padded 16 all round |
| **Entry** | 280 × 48, padded 12 above and below, **48 on the left** |
| **Rule** | A full-width line between groups |

**The 48 of left padding on an entry is an indent**, which is what makes an
entry read as sitting under its header rather than beside it.

## Behavior & Responsiveness

### Interactive States & Loading

* **Opening:** the panel drops from a navigation bar control. **How it opens is
  not documented.**
* **Hover / Pressed / Focus:** Not documented at the panel level. The rows are
  their own components.
* **Loading:** Not documented.

### Touch Target & Layout

* **Touch Target:** a header row is 56 tall; an entry is 48. Both carry the
  target.
* **Panel width:** 320, fixed. No breakpoint axis exists.
* **Panel padding:** 8 above and below the row stack.
* **Entry indent:** 48 on the left, 16 on the right.
* **Width Adaptability:** none. The panel does not stretch.

### Breakpoints & Platform Adaptations

Not documented

_The component carries no breakpoint axis. It is a fixed 320-wide panel at every
width._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented.
* **Length Limits:** Not documented. An entry is 280 wide with 48 of left indent,
  so roughly 216 of room for a label.

### The profile list is per brand

Six brands carry their own profile entries. What differs between them is not
recorded here, and would need reading brand by brand.

**The language list is shared.** One variant covers every brand.

## Accessibility (a11y)

* **Screen Readers:** Not documented. No implementation exists to read the
  behaviour from.
* **Keyboard Navigation:** Not documented. Whether the panel traps focus and how
  it is dismissed is unrecorded.
* **The panel has no stated accessible name**, and nothing records its
  association with the control that opens it.
* **A language menu that does not name its languages in their own language** is
  a common failure. **Not established** whether this one does.

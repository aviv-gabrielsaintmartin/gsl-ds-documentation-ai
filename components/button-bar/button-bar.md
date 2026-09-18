Button bars hold the actions that close a form or a flow, anchored at its foot.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

A button bar carries up to two buttons at the foot of a form, a page or a modal.
It is the component that closes a task — submit and cancel, next and back, save
and discard. It can be sticky, so the actions stay reachable while the content
above scrolls.

### When to use

**Button bar** — up to two buttons anchored at the foot of a form or flow, sticky or not.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The buttons sit in normal page flow | **Button group** |
| Two or three actions float over content | **Floating button group** |
| A single action | **Button** |

### Variant Selection Flow

```
Number of buttons
├─ One action → One button, which sits at the end of the bar
└─ Two actions → Both, one at each end of the bar

Direction
├─ Room for both side by side → Horizontal
└─ Narrow width, or long labels → Vertical
   └─ Responsive: the direction may differ per breakpoint

Display mode — where the bar sits
├─ At the foot of a page or form → Page
└─ At the foot of a modal → Modal
   └─ The two differ in vertical padding above the phone breakpoint only

Full width
├─ The bar holds one button → It may span the full width
└─ The bar holds two → Neither is full width; they sit at opposite ends
```

### Usage Guidance

Not documented

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Button bar** | — | Holds the actions that close a form or flow, at its foot. | — |
| [**Button group**](../button-group/button-group.md) | High | Button groups present a set of related options as buttons. | The buttons sit in normal page flow, not anchored at the foot |
| [**Floating button group**](../floating-button-group/floating-button-group.md) | Medium | Two or three actions that float above scrolling content. | The actions overlay media or a map |
| [**Button**](../button/button.md) | Medium | Buttons trigger an immediate action. | Only one action closes the flow and it needs no bar |

## Variants & Modifiers

Not documented

### Modifiers

#### Display mode

Two modes, `page` and `modal`. They differ only in the vertical padding applied
from the `md` breakpoint up; below it both use the phone padding.

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

_The bar itself has no states. Each button inside it carries `Button`'s own
states — see [Button](../button/button.md)._

### Touch Target & Layout

* **Two buttons:** placed at opposite ends of the bar.
* **One button:** aligned to the start if it is the first slot, to the end if it is the second.
* **Width Adaptability:** a single button may span the full width. When two are
  present, neither does, even if both ask for it.

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web: below `md`** | Phone padding, both vertical and horizontal, whichever display mode is set |
| **Web: `md` and above** | Padding follows the display mode — page or modal |

_Direction is responsive and can be set per breakpoint._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** Not documented

_Each button's label follows [Button](../button/button.md)'s own rules._

## Accessibility (a11y)

Not documented

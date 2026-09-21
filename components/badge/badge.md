Badges mark an element with a short count or a dot.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

A badge is a small marker carrying a count or a short value. It normally sits on
another component's geometry — pinned to or overlapping a button, a tab label, a
menu entry or a cell row — and tells the user how much of something waits there.

**It may also stand alone**, for a case no other component covers — a count
beside a title, for example. The anchored use is the common one; the standalone
use is open, not exceptional.

### When to use

* A count or a dot pinned to a host component — a button, a tab label, a menu entry, a cell row.
* Standalone, where no other component covers the case — a count beside a title, for example.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The marker is a status or category word rather than a count or a dot | **Tag** |
| The marker is interactive — selectable, filterable, removable | **Chip** |

### Variant Selection Flow

```
Size
├─ Default → 24
└─ A tighter host, or a smaller type scale → 16
   └─ No rule for choosing between the two is documented

Colour variant
├─ Primary → two background behaviours: default, inverted
└─ Secondary → five background behaviours: default, inverted, constant,
   onPrimary, onSecondary
   └─ The variants are there to cover the surfaces a badge can sit on.
      They are visual, not semantic
   └─ No rule mapping a given surface to a given variant is documented
```

### Usage Guidance

Not documented

_The source states what a badge can be set to, and no advice on using it. The
one rule that does exist — a badge always carries an accessible label — is an
accessibility rule and is written once, under
[Accessibility](#accessibility-a11y), rather than in two places that could
drift._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Badge** | — | A short count or dot marking an element, usually its host. | — |
| [**Tag**](../tag/tag.md) | High | A non-interactive status or category label holding its own place in the layout. | "New", "Sold" — a word, not a count |
| [**Chip**](../chip/chip.md) | Medium | An interactive label — selectable, filterable, removable. | The user can press the marker to filter by it |

## Variants & Modifiers

### Size

#### 16 and 24

Two sizes, `16` and `24`, being the badge's height in pixels. Default `24`.
Minimum width equals the height, so a single-character badge renders as a
circle. No rule for choosing between them is documented.

### Colour variant

#### Primary and secondary

Two variant names, each with its own set of background behaviours:

| Variant | Background behaviours |
| --- | --- |
| **Primary** | `default`, `inverted` |
| **Secondary** | `default`, `inverted`, `constant`, `onPrimary`, `onSecondary` |

Each combination sets a background, a content colour and a border colour, and
carries its own disabled trio. Default is `primary` with the `default`
background behaviour.

### Modifiers

Not documented

_The size and colour axes above are the whole of what a badge can be set to,
beyond the disabled state described below._

## Behavior & Responsiveness

### Interactive States & Loading

* **Default:** the only rendered state. A badge is not interactive, so it has no hover and no pressed state.
* **Disabled:** takes the disabled background, content and border colours of whichever variant is set. The cursor shows the action is unavailable, and the badge is announced as disabled.
* **Loading:** Not documented — a badge has no loading state.

### Touch Target & Layout

* **Touch Target:** none. A badge is not interactive and is not focusable.
* **Height:** 16px or 24px, per the size set.
* **Width Adaptability:** content-hug, with a minimum width equal to the height.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. A badge renders identically at every
width._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** Not documented

_The displayed value is a number or a short string. No maximum length is
stated, and nothing truncates it._

## Accessibility (a11y)

* **Screen Readers:** a badge is announced as a status. **An accessible label is required, and is separate from the displayed value** — "3" alone does not say what is being counted, so the label supplies it.
* **Keyboard Navigation:** none. A badge is not focusable and cannot be reached or activated from the keyboard.
* **Disabled:** announced as disabled, alongside its label.

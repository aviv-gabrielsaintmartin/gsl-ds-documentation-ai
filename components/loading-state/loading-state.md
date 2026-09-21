Loading states tell the user that content is on its way.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

A loading state is a turning spinner that occupies its own place on the page,
with optional text beneath it. It is what stands in for content while that
content is being fetched.

**It takes the area, rather than sitting inside a control.** A dropdown fetching
its own options shows its own waiting behaviour; this component is for the case
where the wait itself needs an element.

### When to use

* Content is being fetched and the wait needs its own element on the page.
* A spinner alone is enough, or a spinner with a title, or with a description, or with both.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The area is empty, failed or succeeded rather than waiting | **Info state** |
| The wait belongs inside a control already on screen, such as a dropdown fetching its options | That component's own loading behaviour, not this |

### Variant Selection Flow

```
Spinner size
├─ Default → 32
└─ 24
   └─ No rule for choosing between the two is documented

Colour
├─ Default → dark
└─ Light
   └─ No rule for choosing is documented

Text
├─ Spinner only → set neither title nor description
├─ Spinner and a title → set the title
├─ Spinner and a description → set the description
└─ Spinner, title and description → set both
   └─ The two are independent; either may be set without the other
   └─ No rule for choosing how much text to show is documented
```

### Usage Guidance

Not documented

_The source states what a loading state can be set to, its defaults and its
layout. It states no advice on using it, and none has been written elsewhere._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Loading state** | — | A spinner, optionally titled, standing in for content being fetched. | — |
| [**Info state**](../info-state/info-state.md) | High | Full-area states — empty, error, success. | The fetch finished and returned nothing |

## Variants & Modifiers

### Spinner size

#### 24 and 32

Two sizes, `24` and `32`, being the spinner's size in pixels. Default `32`. No
rule for choosing between them is documented.

### Colour

#### Dark and light

Two colours, `dark` and `light`, default `dark`. **The colour applies to the
whole component** — the spinner, the title and the description all take it. No
rule for choosing is documented.

### Modifiers

#### Title

Optional. A single line of text below the spinner, centred, with a gap above it.

#### Description

Optional and independent of the title. Text below the title, centred, with its
own gap above it, in a smaller style than the title.

## Behavior & Responsiveness

### Interactive States & Loading

* **Default:** the spinner turns continuously for as long as the component is on screen. The turn is a full rotation, repeating without pause.
* **Interaction:** none. A loading state is not interactive, so it has no hover, pressed or disabled state.

### Touch Target & Layout

* **Touch Target:** none. A loading state is not interactive and is not focusable.
* **Layout:** a single vertical stack, centre-aligned — spinner, then title, then description.
* **Spinner:** 24px or 32px, per the size set.
* **Width Adaptability:** fills the width of its container; the text centres within it. The text is centre-aligned and wraps.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. The component renders identically at every
width._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** Not documented

_The visible title and description have no stated rule. The spinner's **spoken**
label is separate from both, and defaults to a translated "Loading…" — English,
French, German and Dutch._

## Accessibility (a11y)

* **Screen Readers:** the spinner is announced as a status, carrying a spoken label that defaults to the translated "Loading…" and can be replaced. **That label is separate from the visible title** — a loading state with no title still announces itself.
* **Announcement urgency:** assertive by default, meaning it interrupts. It can be set to polite, or switched off. No rule for choosing between the three is documented.
* **Keyboard Navigation:** none. A loading state is not focusable.

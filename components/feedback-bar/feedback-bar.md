A feedback bar asks the user to rate something on a scale of one to five.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not built 🚧 | Not established 🚧 | Not established 🚧 |

---

## Usage

A feedback bar is an illustration, a title and a row of buttons numbered one to
five. The user picks one number, and that is the whole interaction.

It asks for a **notation on a scale**. That is what separates it from
`Feedback thumb buttons`, which asks for a like or a dislike.

**It is a Pattern**, in the GSL Patterns library, with its own page.

### Platform

**Figma titles it "Feedback Bar (Web)".**

**No web implementation exists.** Searched across every package in the web
repo — `ui`, `patterns`, `core`, `internal` and the rest. Only
`FeedbackMessage` is there, which is a different component.

_iOS and Android are **not established**: no source for either was read._

#### Where it sits on the page

Figma states this, and it differs by platform:

| Platform | Where it goes |
| --- | --- |
| **Desktop** | A floating card over the content, **often at the end of a flow** |
| **Mobile** | Inside the content, or inside a `Modal bottom sheet` |

### When to use

* **Feedback bar** — asking the user to rate something on a scale.
* The end of a flow, once there is something to rate.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The question is a like or a dislike, not a score | **Feedback thumb buttons** |
| You are telling the user something rather than asking | **Feedback message** or **Snackbar** |

### Variant Selection Flow

```
1. Does the bar sit over the content, or in it?
   ├── Over it, as a floating card ─> Container = YES
   └── In the content flow ─────────> Container = NO

2. Which way round?
   ├── Desktop, or anywhere wide ──> Orientation = Horizontal
   └── Mobile, or a narrow column ─> Orientation = Vertical

That is all four variants. Then the parts:
   Pre-title     ─ on by default; a line above the title
   Illustration  ─ on by default, and swappable
```

**Figma's own page names the container pair** — `Container=NO` is *inline*,
`Container=YES` is *overlay*. The property is called Container; the page calls
the result an overlay. They are the same thing.

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Keep the title to two lines. The Figma component says "Title maximum 2 lines" in the component itself. | **DON'T:** Write a third line. Nothing truncates it for you; it will push the bar taller. |
| **DO:** Use the horizontal variant on desktop and the vertical one on mobile. | **DON'T:** Put the horizontal variant in a narrow column. It is 689 wide before it is anything else. |
| **DO:** Ask once, at the end of a flow. | **DON'T:** Put a feedback bar in the middle of a task the user is trying to finish. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Feedback bar** | — | Asking for a rating on a one-to-five scale. | "How was your search?" at the end of a flow |
| [**Feedback thumb buttons**](../components-rules-ai.md) | High | Asking for a binary opinion — thumbs up or down. **Built outside the design system**; see the ruleset. | "Was this useful?" |
| [**Feedback message**](../feedback-message/feedback-message.md) | Medium | Telling the user something inline, rather than asking. | "Your review was published" |
| [**Snackbar**](../snackbar/snackbar.md) | Medium | Transient confirmation after an action. | "Thanks for your feedback" |
| [**Rating**](../rating/rating.md) | Low | **Displaying** ratings that already exist, non-interactively. | An agency's average score |

## Variants & Modifiers

### Orientation and container

#### Four variants

| Property | Options | Default |
| --- | --- | --- |
| **Orientation** | `Horizontal`, `Vertical` | `Horizontal` |
| **Container** | `NO`, `YES` | `NO` |

2 × 2 = 4. The full grid.

| Variant | Size in Figma |
| --- | --- |
| Horizontal, no container | 689 × 82 |
| Horizontal, with container | 689 × 82 |
| Vertical, no container | 360 × 268 |
| Vertical, with container | 360 × 640 |

_The vertical pair differ in height because the container version is drawn at
full mobile height, not because the content changes._

### Modifiers

#### Pre-title

On by default. A line of text above the title, inside the same block.

#### Illustration

On by default, and **swappable** — the component exposes an illustration slot
rather than fixing one. The illustration is 50 × 50 in the horizontal variant.

#### The scale

The row of numbers is a **button group**, exposed so its buttons can be set
individually — each carries `Type`, `State` and `Selected`.

**The scale is one to five.** The group is configured with seven slots and
**two of them are hidden**, which is a Figma-side leftover rather than a rule.
**Do not read seven buttons into it**; five are visible and numbered 1 to 5.

Each button is 73 × 40, and they are laid out with a -1 gap so their borders sit
on top of one another rather than doubling.

## Behavior & Responsiveness

### Interactive States & Loading

* **Selected:** one button in the group carries `Selected=True`. The Figma
  example shows the fourth selected.
* **Default / Hover / Pressed / Disabled:** the buttons carry a `State`
  property. **What each state looks like is the button group's business**, not
  this component's, and is not documented here.
* **After the user answers:** Not documented. Nothing says whether the bar stays,
  collapses, or is replaced by a thank-you.
* **Loading:** Not documented.

### Touch Target & Layout

* **Touch Target:** each scale button is 73 × 40.
* **Outer padding:** 16 on all four sides.
* **Gap between the title block and the scale:** 56 in the horizontal variant.
* **Gap between the illustration and the title:** 16.
* **Width Adaptability:** the horizontal variant is 689 wide in Figma. Whether
  it stretches is **not established**.

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behaviour |
| --- | --- |
| **Desktop** | Horizontal, as a floating card over the content |
| **Mobile** | Vertical, in the content or inside a `Modal bottom sheet` |

_Read from the Figma page's own description. No breakpoint value is given for
where one becomes the other._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented. The title asks the question.
* **Length Limits:** **The title is capped at two lines**, stated in the Figma
  component itself. No limit is stated for the pre-title.

### The scale is unlabelled

The buttons carry the numbers 1 to 5 and nothing else. **Nothing in the
component says what 1 and 5 mean** — no anchor words at either end.

Whether that is deliberate, or a gap, is **not established**.

## Accessibility (a11y)

* **Screen Readers:** Not documented. No implementation exists on any platform
  to read the behaviour from.
* **Keyboard Navigation:** Not documented. The scale is a button group, so it
  would inherit that component's behaviour — **not verified**.
* **The scale has no anchor text**, so a screen reader announces five numbers
  with no stated meaning. Worth resolving before this ships anywhere.
* **Colour alone:** the selected value is carried by the button group's
  `Selected` state. **What that changes visually was not read**, so whether
  colour is the only signal is **not established**.

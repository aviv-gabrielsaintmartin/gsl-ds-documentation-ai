Feedback thumb buttons ask the user for a binary opinion — thumbs up or thumbs
down — about something on the screen.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not built 🚧 | N/A | N/A |

---

## Usage

Feedback thumb buttons collect a like or a dislike. They sit beside the thing
being judged — a result, a suggestion, a piece of content — and ask the user
whether it was any good.

**A like against a notation is the whole distinction.** Gabriel, 18 September
2026. When the answer is a score on a scale, the component is `Feedback bar`.
When the answer is up or down, it is this one.

**The two are separate components, and the thumbs are not inside the bar.**

**Choosing this component is itself a signal.** It was built by a team outside
the design system, kept because others might want it, and never brought in.
Gabriel, 21 September 2026. **You may still choose it** — and a run that does
should say so in its report, because more than one team needing it is the
condition for adopting it into the design system properly. **This is the only
component in the design system on these terms**, so far as Gabriel knows.

**No usage rules were ever written for it.** Gabriel, 18 September 2026. Use it
when the user's opinion is needed, until something better replaces it.

### Platform

**Web only, and built nowhere.**

* The component set exists in the GSL Components library, in two shapes.
* **Never iOS, never Android.** Gabriel, 21 September 2026. The set carries no
  platform axis at all, and its own page names it a web component.
* **`Desktop` and `Mobile` are web breakpoints, not native platforms.** See
  *Device* below. Reading them as iOS and Android is the mistake this line
  exists to stop.
* **No web build exists either.** The component is not in the web code repo, so
  a web team placing it has nothing to import.

### When to use

* **Feedback thumb buttons** — asking the user to like or dislike something, a
  binary opinion.
* A result or suggestion the user can judge good or bad in one tap.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The answer is a score on a scale rather than up or down | **Feedback bar** |
| The system is telling the user something rather than asking | **Feedback message** |
| The system is telling the user something briefly, over the screen | **Snackbar** |

_**`Rating` is not an alternative to this component.** It displays an opinion
that already exists and is not interactive. This one collects an opinion;
`Rating` shows one._

### Variant Selection Flow

```
Is the answer a like or dislike, rather than a score?
├─ No  → not this component. A score on a scale is `Feedback bar`
└─ Yes → continue

How wide is the screen?
├─ Narrow → Device = `Mobile`
│            The two buttons split the row and fill its width
└─ Wide   → Device = `Desktop`
             The two buttons stay square and sit at their own size

The width decides this, not the platform. Both options are web.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Place the pair next to the thing being judged. | **DON'T:** Use it to collect a score. A scale is **Feedback bar**. |
| **DO:** Report that you selected this component, so the adoption question reaches its owner. | **DON'T:** Treat `Mobile` and `Desktop` as iOS and Android. Both are web widths. |
| **DO:** Supply your own acknowledgement after the user answers. | **DON'T:** Expect the component to show which thumb was chosen. It carries no selected state. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Feedback thumb buttons** | — | Asking for a binary opinion, up or down. | "Was this suggestion useful?" |
| [**Feedback bar**](../feedback-bar/feedback-bar.md) | High | Asking for a notation on a scale, with room for an illustration and its own buttons. | "How would you rate this search, 1 to 5?" |
| [**Feedback message**](../feedback-message/feedback-message.md) | Medium | Telling the user something inline, rather than asking. | "Your search was saved" |
| [**Snackbar**](../snackbar/snackbar.md) | Medium | Telling the user something briefly, over the screen. | "Copied to clipboard" |
| [**Rating**](../rating/rating.md) | Low | Showing an opinion that already exists. Not interactive. | "4.2 out of 5, 318 reviews" |

## Variants & Modifiers

**One axis, two variants.** `Device`.

### Device

#### Desktop, Mobile

**The width the pair is laid out for.** Both are web breakpoints. Neither is a
native platform.

| Device | Each button | The pair | How the buttons size |
| --- | --- | --- | --- |
| **Desktop** | 48 × 48, square | 120 × 48 | Each hugs its icon |
| **Mobile** | 48 high, half the row | 48 high, full row | Each fills half the available width |

_**`Mobile` is not a fixed 328 wide.** Both buttons are set to fill, so the pair
takes whatever width it is given and splits it evenly between them. 328 is what
that comes to at the default placement, not a size the component holds._

**Both options use exactly the same button underneath.** The only thing `Device`
changes is whether the two buttons hug their icons or stretch to fill the row.

### Modifiers

Not documented

_The component has one property, `Device`. There is no size option, no state, no
label slot, and the two icons cannot be swapped._

#### What the two buttons are fixed to

Each thumb is a **Button**, configured identically in both variants: type
**Secondary**, style **Default**, **icon only**, size **48**, loading **No**.
One carries the `thumbs-up` icon, the other `thumbs-down`, each drawn at 24.

**Neither button is exposed.** Placing the pair gives you no way through to the
button underneath — you cannot change its type, set a state, or replace an
icon. The pair is all-or-nothing.

## Behavior & Responsiveness

### Interactive States & Loading

Not documented — **and this is a real gap, not an omission in the source.**

* **There is no selected state.** The component has one axis, `Device`, and
  nothing that records which thumb was chosen. After a user answers, the pair
  looks exactly as it did before.
* **There is no disabled state**, so nothing stops a second answer.
* **There is no loading state.**
* The buttons underneath carry hover, pressed and disabled states of their own,
  but those cannot be reached through the pair.

_**What to do about it:** whatever surface this is built on must show the
acknowledgement itself — a `Feedback message` or a `Snackbar` after the answer —
because the component will not._

### Touch Target & Layout

* **Touch Target:** **48 × 48** on desktop, 48 high on mobile. Both clear the 44
  minimum.
* **Height:** 48, on both variants.
* **Gap between the two buttons:** **24**, on both variants. It is a plain
  number and is not bound to a spacing token.
* **Padding inside each button:** 12 on all four sides.
* **Icon size:** 24.
* **Width Adaptability:** hugs on desktop; fills the available width on mobile,
  split evenly between the two buttons.

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Mobile** | Both buttons fill, splitting the row evenly. Height 48, gap 24. |
| **Desktop** | Both buttons hug their icons at 48 × 48. The pair is 120 wide, gap 24. |

_**No breakpoint number is given.** The component names two widths and does not
say where one becomes the other. Take the boundary from the screen's own layout._

## Content & UX Writing

* **Capitalization:** not applicable. The component carries no text.
* **Label Formula:** none. There is no label to write.
* **Length Limits:** not applicable.

### The question is not part of the component

**The pair is two icons and nothing else.** No question, no title, no
acknowledgement. Whatever asks the user — "Was this useful?" — is written and
placed by the screen, not supplied here.

That is one of the differences from `Feedback bar`, which carries its own
pre-title, illustration slot and buttons.

## Accessibility (a11y)

* **Screen Readers:** **not documented, and the component supplies nothing.**
  Both buttons are icon-only, so neither has visible text to announce. Whatever
  surface this is built on must give each an accessible name — "Yes, this was
  useful" and "No, this was not" rather than "thumbs up" and "thumbs down".
* **The answer is not announced.** With no selected state, nothing tells a
  screen-reader user that their answer registered. The acknowledgement has to
  come from the screen.
* **Keyboard Navigation:** not documented. No focus treatment is drawn. The two
  buttons should be reachable in order and show a visible focus ring, and
  neither is specified here.
* **Touch target:** 48 × 48, clearing the 44 minimum on both variants.
* **Contrast:** not verified. The buttons inherit the secondary button's
  colours, which carry no contrast check recorded against this component.

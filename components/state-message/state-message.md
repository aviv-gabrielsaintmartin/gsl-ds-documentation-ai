A state message is one line of feedback sitting under a single form field.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

A state message is an icon and a short line of text, set side by side. It
belongs to **one form field** and sits directly beneath it.

It answers a question about the field it is attached to: what to enter, what
went wrong, or that the entry was accepted. It never speaks for a section, a
page, or an action taken elsewhere.

**Five types:** `Helper`, `Information`, `Success`, `Warning`, `Error`. `Helper`
is the default, and is the only one with no icon.

### Platform

**Web, iOS and Android all carry the component. What they use it for differs.**

| Platform | What is used |
| --- | --- |
| **Web** | **Error only**, by convention. The component supports all five types; form fields use the error one |
| **iOS / Android** | All types — information, success, warning, error |

_Proved for web: the component in `@gsl-core-web/design-system-ui` accepts all
five variants. The error-only convention is stated in
[`text-field`](../text-field/text-field.md) and
[`text-area`](../text-area/text-area.md), which are the fields that carry it._

_**Not established** for iOS and Android: those two docs say all types are
available there, and no iOS or Android source has been read to confirm it._

### When to use

* **State message** — feedback attached to one form field, under that field.
* Guiding what to enter, before the user has typed anything.
* Correcting a single field after validation fails.
* Confirming one field was accepted.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The guidance covers a section or a group of fields, not one field | **Feedback message** |
| The feedback is a transient confirmation of an action, not a field's state | **Snackbar** |
| The whole area is empty, failed, loading or succeeded | **Info state** |

### Variant Selection Flow

```
Which type?

Is the field in an error state after validation?
└─ Yes → Error

Has the entry just been accepted, and does the user need to be told?
└─ Yes → Success

Is there a condition that may cause a problem, but has not yet?
└─ Yes → Warning

Is this guidance the user needs before typing — a format, a rule, a limit?
├─ The guidance is neutral and permanent → Helper
└─ The guidance carries a notice worth an icon → Information
    └─ No rule separates Helper from Information beyond the icon.
       Helper has none; Information has one. Not documented further

On web, only Error is used under a form field, by convention.
The other four exist in the component and are used on iOS and Android.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Attach the message to the one field it describes, directly beneath it. | **DON'T:** Use a state message to speak for a group of fields. That is **Feedback message**'s job. |
| **DO:** Keep it to a single line. | **DON'T:** Write a paragraph. The component is a single flex row and does not wrap by design. |
| **DO:** Use `Error` on web form fields. | **DON'T:** Reach for the other four types on web without checking the field actually uses them. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **State message** | — | One line of feedback under one form field. | "Enter at least 8 characters" under a password field |
| [**Feedback message**](../feedback-message/feedback-message.md) | High | Persistent inline guidance for a section, not a single field. | A notice above a group of address fields |
| [**Snackbar**](../snackbar/snackbar.md) | Medium | Brief, transient confirmation that an action completed. | "Your search was saved" |
| [**Info state**](../info-state/info-state.md) | Medium | A full-area state — empty, error, loading, success. | A results list with nothing in it |
| [**Alert**](../alert/alert.md) | Low | Critical, blocking information needing an immediate decision. | "Delete this listing?" |

## Variants & Modifiers

### Type

#### Helper, Information, Success, Warning, Error

Five types. `Helper` is the default. **The type sets three things at once** — the
icon, the content colour, and the gap between icon and text.

| Type | Icon | Colour token |
| --- | --- | --- |
| **Helper** | **None** | `stateMessage.color.helper.content` |
| **Information** | Filled circle, info | `stateMessage.color.info.content` |
| **Success** | Filled circle, check | `stateMessage.color.success.content` |
| **Warning** | Filled circle, exclamation | `stateMessage.color.warning.content` |
| **Error** | Filled circle, close | `stateMessage.color.error.content` |

_Proved from the web implementation and from the Figma component set, which
agree on all five. Figma's `Helper` variant holds a 16px spacer where the others
hold an icon; the web build renders nothing there._

**The gap is per type**, not a single value — the component reads
`stateMessage.spacing.<type>.gap`. In Figma the row's gap is 8.

### Modifiers

#### Icon

**The icon is not selectable.** It follows the type, and there is no way to
change it, remove it from a type that has one, or add one to `Helper`.

Icon size is 20 in Figma and `sizing.20` on web, for the four types that have
one.

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

_A state message is not interactive. It has no hover, pressed, focus or disabled
state, and no loading state. It is text and an icon._

### Touch Target & Layout

* **Touch Target:** none. The component is not a control.
* **Layout:** a single horizontal row — icon, then text. The row is an
  inline flex container and **does not wrap**.
* **Height:** 20 in Figma, with no padding of its own. Spacing from the field
  above belongs to the field, not to this component.
* **Width Adaptability:** content-hug. The message is as wide as its text.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. The component renders the same at every
width._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** No count is stated. **The row does not wrap**, so the
  practical limit is the width of the field above it. One line is the intent.

### What the message says

The message describes the field it is attached to, in the second person, about
that field alone. It does not name the form, the page, or another field.

_The repo holds no further writing rule for state messages. Both
[`text-field`](../text-field/text-field.md) and
[`text-area`](../text-area/text-area.md) point at an external content guideline
for them._

## Accessibility (a11y)

* **Screen Readers:** **Not documented, and the web build supplies nothing.** The
  component renders a plain container with text — no `role`, no `aria-live`
  region, and no programmatic link to the field it describes. An error message
  announced only visually is not announced at all.
* **Association with the field:** the component accepts an `id`. Pointing the
  field's `aria-describedby` at that `id` is what ties the two together, and
  **the component does not do it for you**.
* **Colour alone:** the type is carried by colour and an icon together, which is
  what keeps it from being colour-only. `Helper` has no icon, and carries no
  meaning that needs one.
* **Keyboard Navigation:** not applicable. The component is not focusable.

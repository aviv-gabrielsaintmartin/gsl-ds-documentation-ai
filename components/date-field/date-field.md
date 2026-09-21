A date field is a form field the user types a date into.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | **Not on its own** 🚧 | Not established 🚧 | Not established 🚧 |

---

## Usage

A date field is a labelled input that takes one date. The user types it, in the
order the placeholder shows.

It is the typing half of date entry. `Date picker` is the same field **plus** a
calendar the user can open and click a day in.

**It is a Pattern, not a Component** — it sits in the GSL Patterns library, on
the same page as `Date picker`, because the two are built from the same parts.

### Platform

**Figma offers two platform variants**, `Web/iOS` and `Android`. Web and iOS
share one; Android has its own.

**On web there is no standalone date field.** `DateField` exists in the web code
as an internal part of `DatePicker` — `libraries/ui/src/DatePicker/DateField` —
and **it is not exported**. A web build cannot place a date field on its own
today; it places a `DatePicker`.

_iOS and Android are **not established**: no source for either was read. Figma's
`Platform` axis says both are intended._

### When to use

* **Date field** — the user types a date, and no calendar needs to be offered.
* The date is one the user already knows — a birth date, a contract date.
* Typing is faster than finding the day in a month grid.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A calendar view is wanted, so the user can see and click a day | **Date picker** |
| The input is free-form text that is not a date | **Text field** |

### Variant Selection Flow

```
1. Which platform is the screen?
   ├── Web or iOS ─> Platform = Web/iOS
   └── Android ────> Platform = Android

2. State — the interaction state you are drawing
   Default · Hover · Active · Disabled

3. Content — is there a date in the field?
   ├── No  ─> Content = Empty    (the placeholder shows)
   └── Yes ─> Content = Filled

4. Error — has validation failed?
   ├── No  ─> Error = No
   └── Yes ─> Error = Yes, and the state message carries the reason

Then the parts, each its own switch:
   Required        ─ the asterisk beside the label
   Optional        ─ the word "(optional)" beside the label
   Tooltip         ─ an info icon beside the label
   Helper Text     ─ guidance under the field, before anything goes wrong
   State Message   ─ on by default; the error text lives here
   Clear icon      ─ on by default; clears what was typed
```

**`Required` and `Optional` are two separate switches, not one choice.** Nothing
in the component stops both being on at once, and nothing says what that would
mean. Turn on one, or neither.

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Show the expected order in the placeholder, as `DD/MM/YYYY` does. | **DON'T:** Leave the user guessing whether the day or the month comes first. |
| **DO:** Put the reason for a failure in the state message. | **DON'T:** Set `Error=Yes` and turn the state message off. The red border alone says nothing. |
| **DO:** Pick one of `Required` or `Optional`. | **DON'T:** Turn both on. The component allows it and no rule covers it. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Date field** | — | Typing one date, with no calendar to browse. | A date of birth |
| [**Date picker**](../date-picker/date-picker.md) | High | The same field plus a calendar the user can open. | Choosing a viewing appointment |
| [**Text field**](../text-field/text-field.md) | Medium | Short single-line input that is not a date. | A surname |
| [**State message**](../state-message/state-message.md) | Low | The line of feedback the field carries beneath it. | "Enter a date after today" |

## Variants & Modifiers

### Platform, state, content and error

#### The four axes

**32 variants — the full grid**, with nothing missing.

| Property | Options | Default |
| --- | --- | --- |
| **Platform** | `Web/iOS`, `Android` | `Web/iOS` |
| **State** | `Default`, `Hover`, `Active`, `Disabled` | `Default` |
| **Content** | `Empty`, `Filled` | `Empty` |
| **Error** | `No`, `Yes` | `No` |

2 × 4 × 2 × 2 = 32. **Every combination exists**, including `Disabled` with
`Error=Yes`.

### Modifiers

#### The switches

Six booleans, set independently of the variant.

| Switch | Default | What it adds |
| --- | --- | --- |
| **Required** | off | An asterisk beside the label |
| **Optional** | off | The word "(optional)" beside the label |
| **Tooltip** | off | An info icon beside the label, in its own 40 touch zone |
| **Helper Text** | off | A line of guidance under the field |
| **State Message** | **on** | The feedback line under the field — where an error's reason goes |
| **Clear icon** | **on** | Clears what has been typed |

_Both `Helper Text` and `State Message` render a `state_message` instance. They
are the same component in two roles: guidance before, feedback after._

#### The calendar button, and an open question

**The field carries a calendar button** — a 40-wide button holding a calendar
icon, at the right-hand end of the input.

**This appears to contradict the rule that sends you here.** The rule says to
choose a date field when *no calendar is offered*, and to choose `Date picker`
when one is. The component has a calendar affordance anyway.

**Not tested** — nobody has established whether that button opens a calendar, is
decorative, or is a leftover from the `Date picker` it shares a page with. Until
it is answered, **follow the rule, not the button**.

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Active:** three of the four `State` options. `Active` is
  the field while being typed into.
* **Disabled:** the fourth, and it exists in combination with `Error=Yes`.
* **Loading:** Not documented. The component has no loading state.

### Touch Target & Layout

* **Field height:** 48, with 4 of padding above and below, 16 on the left and 8
  on the right.
* **Touch Target:** the tooltip icon and the calendar button each sit in their
  own 40 × 40 zone, which is what carries the target rather than the 24 icon.
* **Internal spacing:** 16 between the typed value and the calendar button; 8
  between the leading icon and the text.
* **Label row:** 28 tall, 4 between the label and what follows it.
* **Width Adaptability:** the field fills its container. 280 in the Figma
  example, which is an example and not a rule.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. The only adaptation the component carries
is the `Platform` axis, and that is a platform split rather than a width one._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented. The label names the date being asked for.
* **Length Limits:** Not documented for the label. **The value's format is
  fixed** by the placeholder the field shows.

### The placeholder is the format

The placeholder is not a hint to be replaced with prose. It shows the order the
date must be typed in — `DD/MM/YYYY` in the Figma component.

**Whether that order changes by market is not recorded**, and it would be the
first thing to check before using this field outside France.

## Accessibility (a11y)

* **Screen Readers:** Not documented. No exported web implementation exists to
  read the behaviour from, and the Figma component carries no accessibility
  data.
* **Keyboard Navigation:** Not documented for the field itself. The web
  `DatePicker` it lives inside supports arrow keys to step a segment; whether
  that belongs to the field or to the picker was not established.
* **The error is not colour-only** when the state message is on, which is its
  default. Turning it off leaves the error carried by border colour alone.
* **The label is always present** in the component. There is no label-less
  variant.

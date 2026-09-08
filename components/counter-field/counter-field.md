<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830860391/Counter+field | Last modified: Aug 17, 2026 -->

# Counter field

Counter fields are used to enter or select numeric values.

![](images/theZ5Og8R2pC8tFQLmvTwA.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Counter field on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7278)
* [Counter field on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-counterfield--docs)

---

## Usage

Counter fields allow users to enter a numeric value or incrementally adjust a value with +/- buttons.

### Platform

Unlike other form components, we use the same counter field on all platforms.

### When to use

**Counter field** — numeric values adjusted with +/− controls.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Range selection where an approximate value is acceptable | **Slider** |
| Direct numeric text entry without controls | **Text field** |
| Only a small fixed set of values | **Dropdown** |

### Variant Selection Flow

```
Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO |
| --- |
| ![](images/8713257107d87169caf404.png) **DO:** Use the counter field to allow users to enter or select numeric values. |

| DON'T |
| --- |
| ![](images/b09c260c3e0f41c758b223.png) **DON'T:** Don't use the counter field to select the apartment floors. Instead, use the floor selection component. |
| ![](images/6dda486bc6f305bc73ff28.png) **DON'T:** Don't use the counter field for larger numbers. Use text fields instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Counter field** | — | Allows only numeric values — doesn't support letters or words. | — |
| **Floor selection** | High | Used to select floors; contains "GF" (ground floor) as a word. | User needs to pick an apartment floor, including ground floor |
| [**Text field**](../text-field/text-field.md) | High | Allows all kinds of free-form content; used for larger numbers such as prices, square meters, zip codes, or street numbers. | The number is large or formatted (price, zip code) rather than a small adjustable count |
| [**Slider**](../slider/slider.md) | High | A range slider can be used to select a single value or a range between minimum and maximum values. | Range selection where an approximate value is acceptable |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | Only a small fixed set of values |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, counter fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

## Behavior & Responsiveness

### Interaction

Numbers can be entered into the counter field using the keyboard — it is not possible to enter letters. Numbers can also be selected using the +/- buttons; consumers can decide how many steps the counter will increase/decrease per click (e.g. 0.5, 1, 5, 10 steps etc.). The counter field allows positive and negative integer and decimal numbers. The default, maximum and minimum values can be defined by the consumer.

### Interactive States & Loading

* **Default / Hover / Active / Disabled:** Counter fields have the states default, hover, active, and disabled. They don't have a pressed state — instead, they change to the active state when a user presses on the field. When in error state, they contain an error message.
* **Buttons:** The +/- buttons have the states default, hover, pressed and disabled.

### Touch Target & Layout

* **Width Adaptability:** The default size of the counter field is 144px. The width can also be set to 50% of the container if two counter fields are in the same row. Using the counter field at 100% (full-width) is not recommended. According to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start with a capital letter and use no punctuation (including colons).
* **Label Formula:** Noun form.
* **Length Limits:** 1-3 words for labels.

**Digit:** The counter field supports both positive and negative numbers. Decimal numbers are also supported.

**Labels:** Counter fields should always have a label, to help the user understand what information to enter.

**Helper text (optional):** Add a helper text if the user needs assistance completing a field. Use sentence-style capitalization and punctuation. Helper text is an optional feature and can be used instead of a tooltip. When used, helper text is always available when the input is focused and appears below the field — the exception is when an error or warning message replaces the helper text on Android.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

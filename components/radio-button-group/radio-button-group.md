<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831810661/Radio+button+group | Last modified: Aug 21, 2026 -->

# Radio button group

Radio button groups are used to select one option from a group of mutually exclusive choices.

![](images/p5-WvjoietVl-5Y7q03HeA.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Radio group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7281)
* [Radio group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-radiogroup--docs)

---

## Usage

Radio buttons are used for mutually exclusive choices, not multiple choices. Only one radio button can be selected at a time. When a user selects a new item, the previous selection is automatically deselected.

### Platform

On the web and iOS, we use custom radio buttons. On Android, we use native radio buttons.

| Web/iOS | Android |
| --- | --- |
| ![](images/a3ccf415f6e87c189a44d0.png) | ![](images/ff6fd2addbb124c13a853f.png) |

### When to use

**Radio button group** — mutually exclusive choices in a form, ≤5 options, enough vertical space.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| >5 options, long labels, or constrained space | **Dropdown** |
| Prominent visual treatment preferred | **Button group (single-select)** |
| Options benefit from icons or illustrations | **Select card group (single-select)** |
| Switching views rather than submitting a value | **Segmented control** |

### Variant Selection Flow

```
Alignment
├─ Default — best readability → Vertical
└─ The layout demands it → Horizontal

Border
├─ Complex options that must be clearly distinguished → With border
└─ Simple options, easily told apart → Without border

Columns, vertical groups only
├─ Few options, mobile, or limited vertical space → One column
└─ Six or more options → Two columns

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/15654f9eb4b52d35b3ab35.png) **DO:** Use radio buttons for mutually exclusive choices. | ![](images/91b9fd68d8f192a632c050.png) **DON'T:** Don't use radio buttons to allow users to select multiple options independently. Use checkboxes instead. |

| DON'T |
| --- |
| ![](images/7efa99f9c97aa2a31ca6e9.png) **DON'T:** Don't use radio button groups for binary choices that should take effect immediately. Use toggle groups instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Radio button group** | — | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. | — |
| [**Checkbox group**](../checkbox-group/checkbox-group.md) | Medium | Checkbox groups allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. | — |
| [**Toggle group**](../toggle-group/toggle-group.md) | Medium | Toggle groups are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving. | — |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | >5 options, long labels, or constrained space |
| [**Button group**](../button-group/button-group.md) | High | Button groups display multiple related choices in a horizontal row, allowing users to select one or more options. | Prominent visual treatment preferred |
| [**Select card group**](../select-card-group/select-card-group.md) | High | Select cards are used for single- or multi-selection inside forms. | Options benefit from icons or illustrations |
| [**Segmented control**](../segmented-control/segmented-control.md) | High | Segmented controls are used to select one option from a group of mutually exclusive choices. | Switching views rather than submitting a value |

---

## Variants & Modifiers

### Alignment

Radio button groups can be aligned vertically or horizontally, depending on the use case and layout structure. For better readability, arrange radio buttons vertically whenever possible.

| Vertical | Horizontal |
| --- | --- |
| ![](images/0776a58c72a3854c5fdefd.png) | ![](images/046eafd8c73ab0113b71b3.png) |

### Modifiers

#### Border

Radio button groups can also be used with or without a border. Add a border if you want to emphasize the options more clearly. Borders can also help to distinguish each radio button.

| Without border | With border |
| --- | --- |
| ![](images/07071ca38709cb46c479b8.png) | ![](images/9be10dcb23de8223b7833f.png) |

| DO |
| --- |
| ![](images/3d33673e9da0ee889595d4.png) **DO:** Use radio buttons without borders when the radio button group is simple and the options are easily distinguishable without added visual emphasis. |
| ![](images/208f8779df5d8e18622b2e.png) **DO:** Use borders around radio button groups when you want to clearly distinguish options, especially in complex forms. Borders help visually separate each option, making it easier for users to scan and understand their choices. |

#### Columns

Vertical radio button groups are available in one or two columns.

| One column | Two columns |
| --- | --- |
| ![](images/0776a58c72a3854c5fdefd.png) Single columns are used for concise layouts with fewer options, especially on mobile devices or when vertical space is limited. | ![](images/b3900d343444aa1ae79079.png) The two-column layout is used when presenting more options (6 or more) to efficiently use space, improve scannability, and facilitate comparison. It is especially useful for desktop interfaces. |

#### Header

Like all form components, radio button groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](images/145b3ee3a9a15704101c3b.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

Radio button groups have the states default, hover, pressed, and disabled. They can be selected or unselected, and they can be in an error state. When in error state, they contain an error message.

| Neutral | Error |
| --- | --- |
| ![](images/6cc7d75371477c2d673394.png) | ![](images/e83c3273106479b3c04d6d.png) |

![](images/df128d9f5a3b9a651b501c.png)
Radio button group with error message.

More information:
* [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
* [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

### Touch Target & Layout

Not only the radio button itself is clickable, but also the entire row. The row height is 48px.

![](images/f426a847be5fd3d2fcf0bf.png)

The width of the radio group component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

**Vertical wrapping:** Text that exceeds the available space is automatically wrapped to a new line. Radio button and content are aligned on top.

| One column | Two columns |
| --- | --- |
| ![](images/4e069e78e5905c139fcaee.png) Row height is determined by the content. | ![](images/7b30f9c8fd0148f8a4c255.png) The row height is determined by the radio button with the longest content. |

**Horizontal wrapping:** Radio buttons wrap to a new line if there is not enough space for all of them. Only if the text of a radio button is longer than the width of the available space, the text is wrapped. Radio button and content are aligned on top.

| Short content | Long content |
| --- | --- |
| ![](images/92089a78e3e565160908e4.png) Radio buttons wrapping onto a new line. | ![](images/a8da7800c6e2d083e5a785.png) Text breaking onto a new line. |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

### Main elements

* **Radio labels** appear on the right of radio button inputs. Always use clear and concise labels for radio buttons. Make sure to:
  - List options in a rational order that makes logical sense
  - Start with a capital letter
  - Not end in punctuation, if it's a single sentence or word
* **Group labels (optional):** Add a label to a group of radio buttons to provide additional clarity. In some cases, a group of radio buttons may be within a larger group of components that already have a group label. In this case, no additional group label is needed for the radio button component itself. A group label can either indicate the category of the grouping, or it can concisely instruct what action to take depending on the context.
* **Helper text (optional):** Add a helper text below the label to provide additional context and help the user make a decision.

### Overflow content

We recommend that radio button labels be less than 3 words. If you are running out of space, do not ellipsis the radio button label text; instead, put the text on 2 lines. Text should wrap under the radio button so that the control and label are top-aligned.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

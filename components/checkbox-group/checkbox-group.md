<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832367678/Checkbox+group | Last modified: Aug 17, 2026 -->

# Checkbox group

Checkbox groups are used to select multiple options from grouped checkboxes.

![](images/-yHOGviQOEqwMIUy1V3WXQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Partially available |

* [Checkbox group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7277)
* [Checkbox group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-checkboxgroup--docs)

---

## Usage

Checkbox groups are used for multiple choices, not for mutually exclusive options. Each checkbox operates independently, so selecting one does not affect the other selections in the group. They are commonly used in forms.

### Platform

As with standalone checkboxes, the group contains custom checkboxes on Web/iOS and native checkboxes on Android.

### When to use

**Checkbox group** — multi-select in a structured form.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Few options and prominent visual treatment preferred | **Button group (multi-select)** |
| Options benefit from card layout | **Select card group (multi-select)** |
| Long list or constrained space | **Dropdown** |
| Lightweight selections outside a form | **Chip group** |

### Variant Selection Flow

```
Alignment
├─ Default — best readability → Vertical
└─ The layout demands it → Horizontal

Border
├─ Complex options that must be clearly distinguished → With border
└─ Simple options, easily told apart → Without border

Columns, vertical groups only
├─ Short list → One column
└─ Long list and space allows → Two columns

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/49b65322e95052ccda608d.png) **DO:** Use checkboxes to allow users to select one or more options independently. | ![](images/d07989288d5f0e1192bba8.png) **DON'T:** Don't use checkboxes for mutually exclusive choices. Use radio buttons instead. |

| DON'T |
| --- |
| ![](images/8d8f82e09e86c96eb2dfbc.png) **DON'T:** Don't use checkboxes for binary choices that should take effect immediately. Use toggle groups instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Checkbox group** | — | Allows users to select one or more choices independently; used in forms that must be submitted before the change takes effect. | — |
| [**Radio button group**](../radio-button-group/radio-button-group.md) | High | Mutually exclusive choices, submitted before the change takes effect. | Only one option can ever be selected at a time |
| [**Toggle group**](../toggle-group/toggle-group.md) | High | Binary, mutually exclusive choices that take effect immediately, no submit/save needed. | Turning settings on/off with instant effect |
| [**Button group**](../button-group/button-group.md) | High | Button groups display multiple related choices in a horizontal row, allowing users to select one or more options. | Few options and prominent visual treatment preferred |
| [**Select card group**](../select-card-group/select-card-group.md) | High | Select cards are used for single- or multi-selection inside forms. | Options benefit from card layout |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | Long list or constrained space |
| [**Chip group**](../chip-group/chip-group.md) | High | Chip groups are collections of chips that allow users to filter, select, or manage multiple related options simultaneously. | Lightweight selections outside a form |

---

## Variants & Modifiers

### Alignment

Checkbox groups can be aligned vertically or horizontally, depending on the use case and layout structure. For better readability, arrange radio buttons vertically whenever possible.

### Modifiers

#### Border

Like standalone checkboxes, checkbox groups can also be used with or without a border. Add a border if you want to emphasize the options more clearly. Borders can also help to distinguish each checkbox.

| DO |
| --- |
| ![](images/7752f331e01717cfb623bd.png) **DO:** Use checkboxes without borders when the checkbox group is simple and the options are easily distinguishable without added visual emphasis. |
| ![](images/efe373b17363ee9e97f1a1.png) **DO:** Use borders around checkbox groups when you want to clearly distinguish options, especially in complex forms. Borders help visually separate each option, making it easier for users to scan and understand their choices. |

#### Columns

Vertical checkbox groups are available in one or two columns.

#### Header

Like all form components, checkbox groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

## Behavior & Responsiveness

### Interaction

Not only the checkbox itself is clickable, but also the entire row. The row height is 48px.

### Interactive States & Loading

* **Default / Hover / Pressed / Disabled:** Checkbox groups have the states default, hover, pressed, and disabled. They can be selected or unselected, and can be in an error state (containing an error message). Indeterminate checkboxes are also possible within the group, though this won't make sense for most use cases.

More information: [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79), [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages).

### Touch Target & Layout

* **Width Adaptability:** The width of the checkbox group component is determined by its content. According to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.
* **Wrapping & Alignment (Vertical):** Text that exceeds the available space is automatically wrapped to a new line. Checkbox and content are aligned on top.
* **Wrapping & Alignment (Horizontal):** Checkboxes wrap to a new line if there is not enough space for all of them. Only if the text of a checkbox is longer than the available space is the text itself wrapped. Checkbox and content are aligned on top.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start each list item with a capital letter; don't use commas or semicolons at the end of each line.
* **Label Formula:** Not documented.
* **Length Limits:** Less than 3 words; don't use an ellipsis to cut off label text — wrap to 2 lines if necessary.

**Checkbox labels:** Always use clear and concise labels. Labels appear to the right of checkbox inputs. A label is always required in the code, even if it's not shown in the interface.

**Group labels (optional):** In most cases, a group label precedes a set of checkboxes to provide further context or clarity, either indicating the category of the grouping or describing the actions to be taken below it. If the checkbox group is already within a larger group that has its own group label, no additional group label is required.

**Helper text (optional):** Add a helper text below the label to provide additional context and help the user make a decision.

**Overflow content:** Make sure that the text under the checkbox wraps to the next line, and that the checkbox and its label are aligned at the top.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

* **Keyboard Navigation:** Not documented.
* **Screen Readers:** A label is always required in the code for every checkbox, even when it's not visibly shown in the interface, so it can still be announced.

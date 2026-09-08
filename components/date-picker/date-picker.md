<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832367723/Date+picker | Last modified: Aug 21, 2026 -->

# Date picker

Date pickers are used to select a date using text input or a calendar view.

![](images/2df569a9fbe45f7d5d6cef.png)

| Web | iOS | Android |
| --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 |

* [Date picker on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7270)
* [Date picker on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-datepicker--docs)

---

## Usage

Date pickers allow users to select a date from a calendar or manually enter a date in the input field. They can enter dates from the recent past, present, or future, with each date including the day, month, and year (dd/mm/yyyy).

### Platform

We use platform-specific date pickers that differ between Web, iOS and Android. The main differences are the behavior of labels and placeholders in the date field and the appearance of the calendar view.

#### Web

On the web, the label is always at the top of the date field. The placeholder is visible until a date is selected. On the web, we use a custom calendar.

![](images/0b6371231f00c4a31b1523.png)

**Date field**

#### iOS

As on the web, the label is always at the top of the field on iOS. The placeholder is visible until a date is selected. On iOS we use the native calendar. On iOS, it's currently only possible to select the date using the calendar. It's not possible to type it directly into the field.

![](images/0b6371231f00c4a31b1523.png)

**Date field**

![](images/57265643348707e8a6597e.png)

**Date picker**

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. Instead of a placeholder, the date format is displayed with the helper text. On Android we use the native calendar.

![](images/ba4e2e38e0434c7faeb9c1.png)

**Date field**

![](images/d4c7ddc6ba4df9be285ea7.png)

**Date picker**

### When to use

**Date picker** — selecting a date using text input or a calendar view.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Free-form single-line text | **Text field** |
| Date entry without a calendar view | **Date field** |
| A range along a continuous scale | **Slider** |

### Variant Selection Flow

```
Entry mode
├─ The user picks from a calendar → Calendar view
└─ The user types the date → Text input
   └─ Date entry with no calendar at all → use Date field instead

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/104e9d17339dcba67cbcee.png) **DO:** Use the date picker to allow users to select a specific day in the past, present or future. | ![](images/57265643348707e8a6597e.png) **DON'T:** Don't use the date picker when users need to select a specific year. Instead, provide a text field where they can enter the year directly. |

| DON'T |
| --- |
| **DON'T:** The date picker doesn't currently support range selection. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Date picker** | — | Date pickers are used to select or enter specific dates in the past, present or future. | — |
| [**Text field**](../text-field/text-field.md) | Medium | Text fields allow short single-line and free-form content. They can be used to enter years. | Text field redirects here when: A date |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, date pickers contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](images/3ee42d07d88ceb05c14c67.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

#### Date field

Like text fields, date fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message. They don't have a pressed state. Instead, they change to the active state when a user presses on the date field. The icon button in the field has the states default, hover, pressed and disabled.

**Neutral — empty**

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| ![](images/2f8553b55fa2b9ff1e7e1e.png) | ![](images/1b100120c17b17daf7b584.png) | ![](images/e0b953017ba760895f35a7.png) | ![](images/c1946a57481ae00e7f9b56.png) |

**Neutral — filled**

| Default | Hover | Active | Disabled |
| --- | --- | --- | --- |
| ![](images/7d114f04de1d4e5b4e1edb.png) | ![](images/80d71c8f10dd7b5c5b6641.png) | ![](images/111a18c39c19316440dcbd.png) | ![](images/a2e36f45872d7354296d87.png) |

#### Date picker

The buttons in the date picker have the states default, hover, pressed and disabled. They can be selected or unselected.

**Day — unselected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](images/104e9d17339dcba67cbcee.png) | ![](images/1b100120c17b17daf7b584.png) | ![](images/6891ed71dfbb0a355ca82e.png) | ![](images/f700330535590a6ad9c8f0.png) |

**Day — selected**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](images/3c1c2012d6bb9868f7cad2.png) | ![](images/ba4e2e38e0434c7faeb9c1.png) | ![](images/cb51e5470d2ee6a4a51353.png) | ![](images/31e16c3227775c7690130d.png) |

---

## Content & UX Writing

For English, French, German, Spanish and Dutch content, we use slashes and write the date as: dd/mm/yyyy. For more information please refer to the [Number guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers).

---

## Accessibility (a11y)

Not documented

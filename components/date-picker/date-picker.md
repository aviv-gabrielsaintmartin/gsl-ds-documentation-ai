<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832367723/Date+picker | Last modified: Aug 21, 2026 -->

# Date picker

Date pickers are used to select a date using text input or a calendar view.

![](images/FKfcnOkggnHBX0X7-atNMA.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | To Do 🚧 |

* [Date picker on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7270)
* [Date picker on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-datepicker--docs)

---

## Usage

Date pickers allow users to select a date from a calendar or manually enter a date in the input field. They can enter dates from the recent past, present, or future, with each date including the day, month, and year (dd/mm/yyyy).

### Platform

We use platform-specific date pickers that differ between Web, iOS and Android. The main differences are the behavior of labels and placeholders in the date field and the appearance of the calendar view.

#### Web

On the web, the label is always at the top of the date field. The placeholder is visible until a date is selected. On the web, we use a custom calendar.

| Date field | Date picker |
| --- | --- |
| ![Date field](images/0b6371231f00c4a31b1523.png) | ![Date picker](images/41e99931d035072536c296.png) |

#### iOS

As on the web, the label is always at the top of the field on iOS. The placeholder is visible until a date is selected. On iOS we use the native calendar. On iOS, it's currently only possible to select the date using the calendar. It's not possible to type it directly into the field.

| Date field | Date picker |
| --- | --- |
| ![Date field](images/0b6371231f00c4a31b1523.png) | ![Date picker](images/997d23aab38ab10b66f1d9.png) |

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. Instead of a placeholder, the date format is displayed with the helper text. On Android we use the native calendar.

| Date field | Date picker |
| --- | --- |
| ![Date field](images/c370c0935f348501b14f0d.png) | ![Date picker](images/2ed53a399b7c6db55f9f05.png) |

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
| ![DO](images/2df569a9fbe45f7d5d6cef.png) **DO:** Use the date picker to allow users to select a specific day in the past, present or future. | ![DON'T](images/57265643348707e8a6597e.png) **DON'T:** Don't use the date picker when users need to select a specific year. Instead, provide a text field where they can enter the year directly. |

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

![](images/3916d6ebb9fe3a3c2622d9.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

**Date field**

Like text fields, date fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, they change to the active state when a user presses on the date field.

The icon button in the field has the states default, hover, pressed and disabled.

**Neutral**

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![Default empty](images/2f8553b55fa2b9ff1e7e1e.png) | ![Hover empty](images/fa0efc3330e0e7bc65325b.png) | ![Active empty](images/e0b953017ba760895f35a7.png) | ![Disabled empty](images/65c7e4677e9d361686e6c7.png) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![Default filled](images/7d114f04de1d4e5b4e1edb.png) | ![Hover filled](images/80d71c8f10dd7b5c5b6641.png) | ![Active filled](images/7e7d5d7b349759c23fc72c.png) | ![Disabled filled](images/17bd845737801a9343c028.png) |

**Error**

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![Default empty](images/65523a7512bc7390071d53.png) | ![Hover empty](images/754847e0256357e0074999.png) | ![Active empty](images/05c317e0086c7bacde6e72.png) | ![Disabled empty](images/707076edc3d03adfc8c58a.png) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![Default filled](images/a49a3c5ff0fbb65ad6760f.png) | ![Hover filled](images/7ec98bb20bf04ee666fd3e.png) | ![Active filled](images/7739c2f524b4c9ebc54ba0.png) | ![Disabled filled](images/f59c7ea81a21f8974157d1.png) |

**Date picker**

The buttons in the date picker have the states default, hover, pressed and disabled. They can be selected or unselected.

**Day**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/104e9d17339dcba67cbcee.png) | ![Hover](images/1b100120c17b17daf7b584.png) | ![Pressed](images/6891ed71dfbb0a355ca82e.png) | ![Disabled](images/f700330535590a6ad9c8f0.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![Default selected](images/f757ca2611e44665b4b661.png) | ![Hover selected](images/3011650a1037a828d2b27a.png) | ![Pressed selected](images/96c227666f990d071285a1.png) | ![Disabled selected](images/cb51e5470d2ee6a4a51353.png) |

**Month/Year**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/697b5a9d5738d1a1a94d99.png) | ![Hover](images/a2096d12f0f4821c6e4db6.png) | ![Pressed](images/2bc26fcaf12b1aa1639b6a.png) | ![Disabled](images/cf5674f586f62ae349c5d6.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![Default selected](images/680c40889990b2b7524cc0.png) | ![Hover selected](images/4edda695874eec1141794c.png) | ![Pressed selected](images/94a16eb986e42496d39772.png) | ![Disabled selected](images/2ec2cbc86ebe750a60a891.png) |

**Current day**

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/e0161856af54c89e741f2f.png) | ![Hover](images/e5ab617227c0611d3f7019.png) | ![Pressed](images/583da771712d0f480f3f41.png) | ![Disabled](images/b1f8463fe4828b6f430065.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![Default selected](images/326889608a9fde0edeb53e.png) | ![Hover selected](images/a294290e6a1dbc56085c24.png) | ![Pressed selected](images/ba4e2e38e0434c7faeb9c1.png) | ![Disabled selected](images/31e16c3227775c7690130d.png) |

#### Date field interaction

#### Typing

The user can select a date by typing it into the date field. On the Web, we use a placeholder with progressive disclosure to help them understand the required format.

| Day | Month | Year |
| --- | --- | --- |
| ![Day](images/c1946a57481ae00e7f9b56.png) | ![Month](images/522c6d2697032ae52e9c4a.png) | ![Year](images/fb97b488cfb254b420af3e.png) |

#### Clearing

Web only. Clearing on other platforms is done in the Date Picker.

The user can clear the date when the field is filled by clicking on the "clear" icon on the right. This button is optional.

![](images/4e8dd7051eecf627b72a90.png)

#### Calendar interaction

#### Opening and closing

**Modal view**

The calendar opens when the user clicks the Calendar button. It closes when the user clicks the button again, clicks the Okay or Cancel button, clicks outside the calendar, or presses the Esc key.

To select a date, the user must click a day and then press the Okay button.

| Opening and closing | Selecting and closing | Closing |
| --- | --- | --- |
| ![Opening and closing](images/4b430718c1ddd43927b018.png) | ![Selecting and closing](images/3f04b522020e19557b6d6d.png) | ![Closing](images/3cb52a3f3f8d54cbcfabaf.png) |

**Dropdown view**

The calendar opens when the user clicks on the calendar button. It closes when the user clicks on the button again, selects a day, clicks outside the calendar or presses the esc key.

To select a date, the user simply has to click on a day. The buttons are not needed in the dropdown view.

| Opening and closing | Selecting and closing | Closing |
| --- | --- | --- |
| ![Opening and closing](images/326130bb616034ac3dbd7a.png) | ![Selecting and closing](images/0a051c5bb4f6d1b1d0eee1.png) | ![Closing](images/930f79ec089673dd7b73aa.png) |

#### Changing months and year

Users can change the month and year by pressing the corresponding button and selecting an option from the dropdown list. In addition, they can change the month using the chevron buttons.

In the dropdown view, the user must change the month and year before selecting a day because the calendar closes when the day is selected. In the modal view, this is not relevant because the calendar only closes when the user presses a button.

| Calendar | Month selection | Year selection |
| --- | --- | --- |
| ![Calendar](images/24a120504f0fdb2a12883c.png) | ![Month selection](images/f83ceaa8888c58e6a6f0ac.png) | ![Year selection](images/00cc17d886b8654fd53a03.png) |

The month and year selection looks slightly different in the native iOS and Android picker. The native variants for this are currently not available in Figma.

On the web, we currently still use the native browser dropdowns for the month and year selection. This will be fixed and aligned with Figma in the future.

#### Clearing

The user can clear the date when the field is filled by clicking on the "clear" button in the datepicker. This button is optional.

| Android | iOS |
| --- | --- |
| ![Android](images/fe441943cd0f27090d2180.png) | ![iOS](images/68c92743667a90941bc2fb.png) |

#### Position and scrolling

**Modal view**

The modal calendar is centered vertically in the middle of the screen.

| Centered |
| --- |
| ![Centered](images/3ee42d07d88ceb05c14c67.png) |

**Dropdown view**

By default, the calendar is positioned below the field. If there is not enough space below it, it is positioned on top of the field. If there are more options than space available, the calendar becomes scrollable. Whether the scrollbar is visible or not depends on the user's system settings.

| Below the field | On top of the field | Scrolling |
| --- | --- | --- |
| ![Below the field](images/f1a69c2096aaa0873348b0.png) | ![On top of the field](images/b3baedef4b896e78f84a26.png) | ![Scrolling](images/ba2ab9cff8c4c5a11f2ce3.png) |

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

#### Breakpoints and width

##### Date field width

The width of the date fields can be set to 100% (full-width) or 50% of the container. It's also possible to set it to a fixed size.

According to our form guidelines, the form container should have a max-width of 448px.

![](images/f9bb53f523b1d783c6ef3d.png)

##### Calendar width and breakpoints

The appearance of the date picker changes depending on the platform and breakpoint. To learn more about our breakpoints, see our grids and breakpoint guidelines.

In the modal view, which is used on mobile web and apps, the calendar is full-width (minus 16px margin).

In the dropdown view, which is used on desktop, the calendar has a fixed width that can't be changed. The width depends on the brand and language. For example, in the aviv brand, in English, it has a width of 330px.

| Modal | Dropdown |
| --- | --- |
| ![Modal](images/3ee42d07d88ceb05c14c67.png) | ![Dropdown](images/807ee32a14005536773746.png) |

## Content & UX Writing

For English, French, German, Spanish and Dutch content, we use slashes and write the date as: dd/mm/yyyy. For more information please refer to the [Number guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers).

---

## Accessibility (a11y)

Not documented

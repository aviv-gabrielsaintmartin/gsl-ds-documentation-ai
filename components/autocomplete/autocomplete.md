<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831941697/Autocomplete | Last modified: Aug 13, 2026 -->

# Autocomplete

Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more efficiently by providing relevant results.

![](images/qVZPr35vzW8m3tMKJ-mqyg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | Ready ✅ |

[Autocomplete on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7275) · [Autocomplete on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-autocomplete--docs)

---

## Usage

The autocomplete component is an advanced text input that simplifies the selection of one or more values from a long list of options.

### Platform

We use platform-specific autocomplete components that differ between Web, iOS and Android. The main differences are the platform-specific text field and the modal bottom sheet.

#### Web

On the web, the autocomplete appears in a full-screen modal bottom sheet on phones and as a standalone dropdown on desktop.

| Phone | Desktop |
| --- | --- |
| ![](images/486554d10fef4951da216b.png) | ![](images/d2ee331462c3eab7487938.png) |

#### iOS

On iOS, the autocomplete appears in a full-screen modal bottom sheet on phones and in a full-height modal on tablets. The iOS-specific text field and modal are used.

| Phone | Tablet |
| --- | --- |
| ![](images/e1c43ae8d77c56479b99cb.png) | ![](images/6c9f15486c1c819c46bbc8.png) |

#### Android

On Android, the autocomplete appears in a full-screen modal bottom sheet on phones and in a full-height modal on tablets. The Android-specific text field and modal are used.

| Phone | Tablet |
| --- | --- |
| ![](images/22c10d372af196b406f99e.png) | ![](images/22f89a2c97334e617f13f5.png) |

### When to use

* To help users find what they're looking for quickly when there's a large amount of data or options

### When NOT to use

* When there is a small, predefined list of choices — *Use Dropdown instead.*

### Variant Selection Flow

```
Dropdown row size
├─ Dense list, short labels → Small rows
└─ Labels wrap, or a caption is shown → Large rows

Helper button at the end of the list
├─ Offering geolocation ("use my location") → Include the text button
├─ The user may not find the result they expect → Include the text button
└─ Otherwise → Omit it

Surface, by platform
├─ Phone → Presented with a top bar
├─ iOS / Android tablet → Presented in a modal
└─ Web → Inline dropdown list
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/62ed5641632c2aa60f312c.png) **DO:** Use autocomplete to help users find what they're looking for quickly when there's a large amount of data or options. | ![](images/85b2ced17869df1b966737.png) **DON'T:** Use the autocomplete when there is a small, predefined list of choices. Use a dropdown instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Autocomplete** | — | Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more efficiently by… | — |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns display a predefined list of options for users to choose from. | When there's a small, predefined list of choices |
| [**Text field**](../text-field/text-field.md) | High | Text fields are used to enter and edit single-line text content. | No suggestions needed |

---

## Variants & Modifiers

### Modifiers

#### Dropdown list

The dropdown list consists of a mandatory label and an optional caption on the right. The number of displayed rows is defined by the consumer, with no fixed limit. The list rows are available in small and large heights.

| Small rows | Large rows |
| --- | --- |
| ![](images/60880df7075e58567f4065.png) | ![](images/aa3d130c0d29c9cda062a0.png) |

The dropdown list includes an optional text button. The button is positioned at the end of the list.

![](images/6c58b8546b280230f617d7.png)

| DO |
| --- |
| ![](images/15b224e8e74e7a2ac8b7bb.png) **DO:** Use the button for geolocation tracking. |
| ![](images/b4f5a9c2fe2ffc5f2be0f6.png) **DO:** Use the button to help users when they can't find the result they expect. |

The dropdown list also includes optional icons on the left and right.

![](images/5d2db2b6e1ae0349b83e74.png)

#### Text field

The autocomplete contains a text field. See the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-97e03c-84052978-35) to learn more about the modifiers of this component.

#### Modal

On iOS/Android tablets, the autocomplete appears in a modal. See the [modal bottom sheet documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet) to learn more about this component's modifiers.

#### Top bar

The autocomplete on phones contains a top bar. See the [top bar documentation](https://zeroheight.com/626199550/p/27f21d-top-bar) to learn more about the modifiers of this component.

---

## Behavior & Responsiveness

### Interactive States & Loading

The autocomplete component has the following main states:

* **Default empty:** The input field is inactive, meaning the user hasn't yet interacted with the field.
* **Active empty:** The input field is active (focused) but still empty, ready for user input.
* **Filled:** The user has entered text, and a dropdown list of matching suggestions appears below the input field.
* **No results:** No matching options were found. A message informs the user, with additional text offering suggestions or alternative actions.

| State | Phone | Desktop |
| --- | --- | --- |
| Default empty | ![](images/10d6e0d851cdd6cb7e0961.png) | ![](images/75d102677c9a78079afac3.png) |
| Active empty | ![](images/833db8d9ea603f33875e9e.png) | ![](images/63e23d902630b7913f1c62.png) |
| Filled | ![](images/486554d10fef4951da216b.png) | ![](images/d2ee331462c3eab7487938.png) |
| No results | ![](images/fc15b121b4d9294cf05a99.png) | ![](images/fff9aea0eae6817b6a64ed.png) |

**Interaction — Desktop:** the dropdown list opens when the user begins typing in the input field. It closes when the user selects an option from the list, clicks outside the dropdown, or presses the Esc key twice.

| Opening | Selecting and closing | Closing |
| --- | --- | --- |
| ![](images/f9da2061d57e4f2c1a9d72.png) Typing in the field | ![](images/0c3db4ea6c0363d8898dd2.png) Clicking an option | ![](images/c608abb3a876e94c3f2c6a.png) Clicking outside the dropdown or pressing the Esc key twice |

**Interaction — Phone and tablets:** autocomplete opens in a modal bottom sheet (full-screen on phones and modal on tablets) when the user presses the input field. In the modal, the user can filter results by typing in the text field. When the user selects an option, the modal closes. The user can also close the modal by tapping the x-button.

| Opening | Selecting and closing | Closing |
| --- | --- | --- |
| ![](images/666f627b001a2c8c610fa4.png) Tapping the field | ![](images/0c53ba394cb68d3bff83d2.png) Tapping an option | ![](images/31b26715f0c0c74edc41c3.png) Tapping the x-button |

The rows in the dropdown list have the states default, hover and pressed. They can be selected or unselected.

| Unselected | Selected |
| --- | --- |
| ![](images/f6c0c35dd55ebe8fef2c8d.png) | ![](images/95fe1ae882fdd6fae827d5.png) |

The loading state appears when suggestions are being fetched after the user enters a query.

| Phone | Desktop |
| --- | --- |
| ![](images/06f494bdffd409131b5cf3.png) | ![](images/c87fe818210eabf9c823a6.png) |

### Touch Target & Layout

By default, the dropdown list is positioned below the field. On desktop, it is placed above the field if there is not enough space below it. If the options exceed the available space, the dropdown list becomes scrollable — whether the scrollbar is visible depends on the user's system settings. To avoid complexity, not all positions are available in Figma; feel free to detach the component.

| Phone | Desktop |
| --- | --- |
| ![](images/1e049b2917d22b3b2b3120.png) | ![](images/5d96886ea6a78866969c03.png) ![](images/43c4d88350bf7ac160d22b.png) |

### Breakpoints & Platform Adaptations

The style of the autocomplete depends on the breakpoint on web and Android, and on the device on iOS. See our [grids and breakpoints guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| Web: XXS – XS (0–599px) Android: Medium – Expanded (>599dp) iOS: iPhone | ![](images/486554d10fef4951da216b.png) Full page — full-screen modal bottom sheet |
| Web: SM – XXXL (>599px) Android: Compact (0–599dp) iOS: iPad | ![](images/d2ee331462c3eab7487938.png) Standalone dropdown |

---

## Content & UX Writing

* **Text field:** Refer to the [text field documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/980e7b-text-field/t/page-980e7b-84054521-39) to learn about labels, helper and placeholder texts in the input field.
* **Dropdown list:** The label should clearly identify the option — use a value of your choice depending on the requirement (e.g. name of town, department, district, street...). The caption should provide supporting details (e.g. department, town, district...). Try to keep it under 2 lines.
* **No results:** Refer to the [info state documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/84818f-info-state/t/page-7142d3-87401819-40) to learn more.

---

## Accessibility (a11y)

Not documented

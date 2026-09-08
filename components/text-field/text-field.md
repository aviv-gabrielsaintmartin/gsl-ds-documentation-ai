<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831057031/Text+field | Last modified: Aug 21, 2026 -->

# Text field

Text fields are used to enter and edit single-line text content.

![](images/O-ifxQ8--9J3s4P5GVBDpQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

[Text field on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7284) · [Text field on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textfield--docs)

---

## Usage

Text fields allow users to input and edit short free-form content. They are commonly used in forms for purposes such as contact and property information, login, registration and search queries.

### Platform

We use platform-specific text fields that differ between Web/iOS and Android. The main difference is the behavior of labels and placeholders.

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](images/0a965e77a8aef88bb3d9e5.png) | ![](images/7aa352821725425a35ffc4.png) | ![](images/48468276ca16cfe3d6c497.png) | ![](images/b6098fb25947b6668621df.png) |

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](images/8a08ee21c14bbdcc823503.png) | ![](images/5578b0c969891362472467.png) | ![](images/9a02898367c4e6491ae28c.png) | ![](images/584aaf5dc9c4355014efbe.png) |

### When to use

**Text field** — short, single-line free-form input.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Multi-line or longer than a sentence | **Text area** |
| Suggestions appear as the user types | **Autocomplete** |
| Numeric with increment/decrement controls | **Counter field** |
| A date | **Date picker** |

### Variant Selection Flow

```
Label
├─ Almost always → Visible label
└─ Context is unmistakable → Hidden label, with an invisible aria-label for accessibility

State message
├─ Web → Error only
└─ iOS and Android → Error · Information · Success

Icons
├─ A visual cue only → Left icon, never clickable
├─ An action on the field, such as clearing it → Right icon, as a clickable icon button
└─ Both → Left and right

Suffix
└─ Measurements, currency, or another contextual constraint → Add a suffix

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO |
| --- |
| ![](images/5e6555cc253b965b20274f.png) **DO:** Use text fields for short single-line content such as name and address. |

| DON'T |
| --- |
| ![](images/532d40c146b56f14b4f452.png) **DON'T:** Use text fields for large amounts of content that exceed one line. Use the text areas instead. |
| ![](images/a46349c76e41f79c3709b6.png) **DON'T:** Use text fields for phone numbers. Use the phone number field instead. |
| ![](images/b4ed32640a65f8edf46ae7.png) **DON'T:** Use text fields for date selection. Use the date field instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Text field** | — | Text fields are used to enter and edit single-line text content. | — |
| [**Text area**](../text-area/text-area.md) | High | Text areas allow multi-line text content. | Multi-line or longer than a sentence |
| [**Phone number field**](../phone-number-field/phone-number-field.md) | Medium | Phone number fields are only used to input phone numbers. | — |
| **Date field** | Medium | Date fields are only used to input dates. | — |
| [**Autocomplete**](../autocomplete/autocomplete.md) | High | Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more efficiently by… | Suggestions appear as the user types |
| [**Counter field**](../counter-field/counter-field.md) | High | Counter fields are used to enter or select numeric values. | Numeric with increment/decrement controls |
| [**Date picker**](../date-picker/date-picker.md) | High | Date pickers are used to select a date using text input or a calendar view. | A date |
| [**Media upload**](../media-upload/media-upload.md) | Medium | Media upload components allow users to upload, view, and manage media files such as images, videos and documents. | Media upload redirects here when: The user provides a URL or file path instead |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, text fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](images/d77a493e42c980caf750ba.png)

Text fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

#### State message

State messages can be used to provide additional information or feedback on the usage of the text field. On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

| Error (Web, iOS, Android) | Information (iOS/Android) | Success (iOS/Android) | Warning (iOS/Android) |
| --- | --- | --- | --- |
| ![](images/138f10ddaacd880a8444b7.png) | ![](images/c14bcaa093daf8fac310b9.png) | ![](images/6c76ce29f122c1379aaa47.png) | ![](images/7851910ed639ac6c2d789d.png) |

More information: [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79) · [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

#### Icons

Icons can be added as visual cues to provide clarity to the user. Icons on the left are non-clickable. Icons on the right can be clickable (icon button) or non-clickable.

| Left | Right | Left and right |
| --- | --- | --- |
| ![](images/d9770ea189e8433a54c515.png) | ![](images/ac4a6da6a87f7091d5f924.png) | ![](images/c09ccb650adc7881e59835.png) |

| DO |
| --- |
| ![](images/9ccbb65f3b8055de7c7b07.png) **DO:** Use non-clickable icons to provide visual cues to the user. |
| ![](images/9c21161133b43f8fcd551b.png) **DO:** Use clickable icon buttons for actions related to the text field, such as deleting the contents of the box. |

#### Suffix

The suffix can be added to provide additional context or constraints for the user input.

![](images/a335366c9093da955f9f28.png)

| DO |
| --- |
| ![](images/3599980db7caed657874f2.png) **DO:** Use the suffix for measurements, currency, or contextual information. |

---

## Behavior & Responsiveness

### Interactive States & Loading

Text fields have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message. They don't have a pressed state. Instead, they change to the active state when a user presses on the text field.

#### Neutral

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](images/0a965e77a8aef88bb3d9e5.png) | ![](images/78c15dff022700b808c7d9.png) | ![](images/48468276ca16cfe3d6c497.png) | ![](images/7ff6ba339845321b5b9f1e.png) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](images/7aa352821725425a35ffc4.png) | ![](images/ab3a5ac9820ab938da43d7.png) | ![](images/b6098fb25947b6668621df.png) | ![](images/4a28d6128a85c6df604e2c.png) |

#### Error

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![0dfceb07a896e570f3ee01c.png](https://avivgroup.atlassian.net/wiki/pages/viewpageattachments.action?pageId=2831057031&preview=%2F2831057031%2F3456073745%2F0dfceb07a896e570f3ee01c.png)  <!-- MISSING LOCAL IMAGE: 0dfceb07a896e570f3ee01c.png --> | ![](images/eb069fe9059a04d1d175d4.png) | ![](images/7fe648d0f4729ace591a3e.png) | ![](images/7ff6ba339845321b5b9f1e.png) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](images/e02a7fcf3b461512fb9f7d.png) | ![](images/a854598021b70d6e1f73cd.png) | ![](images/6b72832fe45d75f295d878.png) | ![](images/4a28d6128a85c6df604e2c.png) |

* **Overflow content:** If a user's content is too long for the single line of text input, the value content can scroll horizontally within the field container as the cursor moves from one end of the value to the other.

### Touch Target & Layout

Width Adaptability: The width can be set to 100% (full-width) or 50% of the container. For special use cases it is also possible to define a fixed size. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![](images/d806b1ae08125adc31d93c.png)

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Labels:** Text fields should always have a label, to help the user understand what information to enter. Keep the label short and concise (1-3 words) and in noun form. Start with a capital letter and use no punctuation (including colons).
* **Helper text (optional):** Add a helper text if the user needs assistance completing a field, such as explaining the correct data format. Use sentence-style capitalization and punctuation. Helper text is an optional feature and can be used instead of a tooltip. When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text in apps.
* **Placeholder text:** Placeholder text disappears after the user begins entering data. Placeholder text within a form field makes it difficult for people to remember what information belongs in a field, and to check for and fix errors. If you use a placeholder text, make sure it's just an example.
* **Placeholder text - numbers:** When designing a text field that will contain numbers (price, size, etc.) please make sure you use numbers or leave the text field empty. For example a text field for minimum price to maximum price should say 0 €, allowing the user to type in a number if they wish. See the [Number Guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers) to learn more about the rules for designing with number-related text.

---

## Accessibility (a11y)

Not documented

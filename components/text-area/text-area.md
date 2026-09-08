<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831024256/Text+area | Last modified: Aug 21, 2026 -->

# Text area

Text areas are used to enter and edit multi-line text content.

![](images/Wui_hPh43PH8foRvC0PW4w.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Text area on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7285)
* [Text area on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-textarea--docs)

---

## Usage

Text areas are used for entering and editing larger amounts of text compared to single-line [text fields](https://zeroheight.com/626199550/p/980e7b-text-field). They are commonly used in forms for purposes such as entering descriptions, comments, and messages.

### Platform

We use platform-specific text areas that differ between Web, iOS and Android. The main difference is the behavior of labels, placeholders and the resize handle.

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled. On Web, the field contains a resize handle; on iOS, it doesn't.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](images/0a965e77a8aef88bb3d9e5.png) | ![](images/7aa352821725425a35ffc4.png) | ![](images/48468276ca16cfe3d6c497.png) | ![](images/b6098fb25947b6668621df.png) |

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

| Default empty | Default filled | Active empty | Active filled |
| --- | --- | --- | --- |
| ![](images/3a68903f4e686c60ecee46.png) | ![](images/0fd6695160c85c20bd973b.png) | ![](images/d018d0db0fece167ac65af.png) | ![](images/584aaf5dc9c4355014efbe.png) |

### When to use

**Text area** — multi-line free-form text — descriptions, comments, messages.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Single-line | **Text field** |
| Attaching a file | **Media upload** |

### Variant Selection Flow

```
Label
├─ Almost always → Visible label
└─ Context is unmistakable → Hidden label, with an invisible aria-label for accessibility

State message
├─ Web → Error only
└─ iOS and Android → Information · Success · Warning · Error

Icons and suffix
└─ None — unlike the text field, the text area has neither

Character counter
├─ There is a limit worth surfacing → Show the counter
└─ Behaviour when the limit is exceeded differs by platform:
   ├─ Web → The counter enters an error state
   ├─ Android → The whole field enters an error state and shows a message
   └─ iOS → Typing beyond the limit is blocked

Resizing
├─ Web → Resize handle; height only, never width
├─ Android → The field grows automatically as the content lengthens
└─ iOS → Fixed height; the user cannot resize it

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/5e6555cc253b965b20274f.png) **DO:** Use text areas for multi-line text content. | ![](images/ef5c447c139d4f6782a88c.png) **DON'T:** Don't use text areas for single-line content. Use text fields instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Text area** | — | Text areas allow multi-line text content. | — |
| [**Text field**](../text-field/text-field.md) | High | Text fields allow short single-line and free-form content. | Single-line |
| [**Phone number field**](../phone-number-field/phone-number-field.md) | Medium | Phone number fields are only used to input phone numbers. | — |
| **Date field** | Medium | Date fields are only used to input dates. | — |
| [**Media upload**](../media-upload/media-upload.md) | High | Media upload components allow users to upload, view, and manage media files such as images, videos and documents. | Attaching a file |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, text areas contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](images/d77a493e42c980caf750ba.png)

Text areas should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

#### State message

State messages can be used to provide additional information or feedback on the usage of the text area.

On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

More information:
* [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
* [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

#### Icons and suffix

Unlike the text field, the text area does not contain any icons or suffixes.

#### Character counter

A character counter can be added to display the number of characters entered and the total number of characters allowed.

![](images/a054629da917411b9068dc.png)

Depending on the platform, there is different behavior when the character count is exceeded.

| Web | Android | iOS |
| --- | --- | --- |
| ![](images/4ccfcd4aee702ae8a68e30.png) The counter goes into an error state. | ![](images/4d90d005499114fe0fdaa9.png) The entire field goes into an error state and an error message is displayed. | ![](images/7d4c0c89adc99aa919d11d.png) It is not possible to type in more characters than are allowed by the character limit. |

#### Resize handle

Only on Web the text area contains a resize handle. It allows the user to change the height of the field. It is not possible to change the width of the field with the handle. It's also not possible to make the field smaller than the min-height (96px).

On Android, the field automatically grows if the content is longer than the field.

On iOS, the field has a fixed height. The user cannot resize the field.

| Web | iOS | Android |
| --- | --- | --- |
| ![](images/232bdbc835f0812a296a26.png) | ![](images/110683ffe2c33e96eb5457.png) | ![](images/4f5e83c9862cba5861ad73.png) |

---

## Behavior & Responsiveness

### Interactive States & Loading

Text areas have the states default, hover, active, and disabled. They can be empty or filled, and they can be in an error state. When in error state, they contain an error message.

They don't have a pressed state. Instead, it changes to the active state when a user presses on the text area.

#### Neutral

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](images/0a965e77a8aef88bb3d9e5.png) | ![](images/78c15dff022700b808c7d9.png) | ![](images/48468276ca16cfe3d6c497.png) | ![](images/b569b6334589c6a6dfe686.png) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](images/7aa352821725425a35ffc4.png) | ![](images/ab3a5ac9820ab938da43d7.png) | ![](images/b6098fb25947b6668621df.png) | ![](images/6c1090682b7917ff893a38.png) |

#### Error

| Default empty | Hover empty | Active empty | Disabled empty |
| --- | --- | --- | --- |
| ![](images/cf176ee34dacba35071dbd.png) | ![](images/4deda66b55dd8e1ab3ecd9.png) | ![](images/604e9334ee8787fb6e89b7.png) | ![](images/4f5e83c9862cba5861ad73.png) |

| Default filled | Hover filled | Active filled | Disabled filled |
| --- | --- | --- | --- |
| ![](images/6486197d246ce8420e742c.png) | ![](images/a854598021b70d6e1f73cd.png) | ![](images/6b72832fe45d75f295d878.png) | ![](images/2fe47d7aa8e569c4fd9400.png) |

### Touch Target & Layout

The text area can have a fixed width or can be set to 100% (full-width) of the container. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

The min-height of the text-area is 96px. On Web the user can make the field longer by pulling on the resize handle. On Android, the field automatically grows if the content is longer than the field. And on iOS, the field has a fixed height, which the user cannot resize. When the field is smaller than the content inside, vertical scrolling is available.

| Default height | Height increased by user | Height smaller than content |
| --- | --- | --- |
| ![](images/0868f5900d9e01e9a76091.png) | ![](images/d1310b7960969765d0459e.png) | ![](images/b744133ff7f53b70006d2f.png) |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

### Main elements

#### Labels

Text areas should always have a label, to help the user understand what information to enter.
* Keep the label short and concise (1-3 words) and in noun form.
* Start with a capital letter and use no punctuation (including colons).

#### Helper text (optional)

Add a helper text if the user needs assistance completing a field. Use sentence-style capitalization and punctuation. Helper text is an optional feature and can be used instead of a tooltip. When used, helper text is always available when the input is focused and appears below the field. The exceptions are when an error or warning message replaces the helper text.

#### Placeholder text

Placeholder text disappears after the user begins entering data. Placeholder text within a form field makes it difficult for people to remember what information belongs in a field, and to check for and fix errors. If you use a placeholder text, make sure it's just an example.

### Overflow content

If a user's content exceeds the vertical space of the variable text area, the user can either expand the field container using the resize handle or scroll the content vertically within the set field container.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

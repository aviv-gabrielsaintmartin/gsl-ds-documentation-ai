<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831450231/Media+upload | Last modified: Aug 26, 2026 -->

# Media upload

Media upload components allow users to upload, view, and manage media files such as images, videos and documents.

![](images/1b4a98eae8fe1f596d9242.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | To Do 🚧 |

* [Media upload on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7271)
* [Media upload on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-mediaupload--docs)

---

## Usage

Media upload components allow users to upload files by either dragging and dropping them or by clicking the drop zone.

### When to use

**Media upload** — the user uploads files by drag-and-drop or file picker.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The user provides a URL or file path instead | **Text field** |

### Variant Selection Flow

```
Empty drop zone
└─ Add an illustration placeholder — a pictogram is recommended

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO |
| --- |
| ![](images/776559d2e41699d96ab984.png) **DO:** Use the media upload to allow users to upload images, videos, or documents. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Media upload** | — | Media upload components allow users to upload, view, and manage media files such as images, videos and documents. | — |
| [**Text field**](../text-field/text-field.md) | High | Text fields are used to enter and edit single-line text content. | The user provides a URL or file path instead |
| [**Text area**](../text-area/text-area.md) | Medium | Text areas are used to enter and edit multi-line text content. | Text area redirects here when: Attaching a file |

---

## Variants & Modifiers

### Modifiers

#### Header

Like all form components, media uploads contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![](images/2cb54be6c5aecae5a6d92c.png)

#### Illustration

The empty drop zone contain a illustration placeholder. We recommend adding a pictogram.

**Figma tip:** To choose the correct illustration go the common page in the illustration library. For example: [Common Picto Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-249). There you find illustrations for most use cases such as informative purposes, error messages, and more. If you can't find the illustration you're looking for please request it on #gemini_symbols.

---

## Behavior & Responsiveness

### Interactive States & Loading

An error is displayed if an unsupported file is uploaded.

![](images/01ffc12ece62b3d86ef020.png)

### Touch Target & Layout

* **Action menu:** The user can access the following options from the action menu: **Choose as cover** (set the file as a cover; any file type can be set as a cover), **Move forward** (moves the file one step forward; files can also be dragged and dropped to any position), **Move backwards** (moves the file one step backward), **Edit caption** (opens a modal to change the file name/caption), **Edit image** (opens an external image editor), **Remove** (deletes the file).
* **Width Adaptability:** The media upload cards adjust to the width of their container, filling the available space based on the size of the container. The width can be set to 100% (full-width) or 50% of the container. The cards have a fixed aspect ratio of 3:2.

![](images/0bd5e11d9fdeb7a8ab3081.png)

### Breakpoints & Platform Adaptations

The text and style of the empty drop zone depends on the breakpoint. On the desktop, the dashed border and text indicates that drag and drop is possible. On phones and tablets, this is much less common, so the design is adjusted to reflect the different behavior. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web: XXS to MD (0 - 1023 px)** | ![](images/6d603121a27d36810f8107.png) Tap. Android and iOS: used on all breakpoints. |
| **Web: LG to XXXL (> 1024 px)** | ![](images/2b857ba963f26c30513960.png) Drag and drop. Android and iOS: not used. |

---

## Content & UX Writing

* **Labels:** Media uploads should always have a label, to help the user understand what files they are supposed to upload. Keep the label short and concise (1-3 words) and in noun form. Start with a capital letter and use no punctuation (including colons).
* **Helper text (optional):** Add helper text if the user needs assistance with uploading files, such as explaining the allowed file type, size, or number of files. It can also be used to explain the drag and drop feature of the file preview cards. Use sentence-style capitalization and punctuation.
* **Error messages:** See the UX Writing guidelines to learn about [error messages](https://zeroheight.com/626199550/p/4051b4-error-messages).

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

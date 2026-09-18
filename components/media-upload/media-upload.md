Media upload components allow users to upload, view, and manage media files such as images, videos and documents.

![](images/o_n_WvAV6f-6H3j2GuTtiw.png)

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
| ![DO](images/1b4a98eae8fe1f596d9242.png) **DO:** Use the media upload to allow users to upload images, videos, or documents. |

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

![](images/187f823e2e62eecdda93ef.png)

#### Illustration

The empty drop zone contain a illustration placeholder. We recommend adding a pictogram.

**Figma tip:** To choose the correct illustration go the common page in the illustration library. For example: [Common Picto Illustrations](https://www.figma.com/design/BwvS9ir2UuM4gBHVMhjy0O/1.-Gemini-Symbols-Library?node-id=5688-249). There you find illustrations for most use cases such as informative purposes, error messages, and more. If you can't find the illustration you're looking for please request it on #gemini_symbols.

---

#### File counter

The media upload includes an optional counter. In most cases, we recommend using the counter to give the user a clear idea of how many files they can upload.

| With counter | Without counter |
| --- | --- |
| ![With counter](images/880c4038d25b8d9ba08a15.png) | ![Without counter](images/2cb54be6c5aecae5a6d92c.png) |

#### Filename

The image/file preview includes an optional filename. In most cases, we recommend displaying the filename to give the user more clarity about what files they can upload. Since the file preview (non-image) only displays a generic illustration, the filename will still be displayed below the icon even if the filename is hidden.

The default filename includes the file extension, e.g. bathroom.jpg. The filename (caption) can be changed using the action menu.

| With filename | Without filename | With filename | Without filename |
| --- | --- | --- | --- |
| ![With filename](images/5b2d48c09686999ae48c10.png) | ![Without filename](images/7111f10fc22b8c8d846288.png) | ![With filename](images/c5493817b8ebc63fba50e2.png) | ![Without filename](images/363b6d408549c144cdba6e.png) |

#### Cover photo tag

The image/file preview includes an optional cover tag. This tag can be used to mark the cover image. The cover image can be changed in the action menu or by dragging and dropping an image to the first position. The tag can be applied to any type of file.

| With cover image tag | Without cover image tag |
| --- | --- |
| ![With cover image tag](images/8fef7bee11a1dab59bc687.png) | ![Without cover image tag](images/0c2438e649ae2febe96063.png) |

## Behavior & Responsiveness

### Interactive States & Loading

An error is displayed if an unsupported file is uploaded.

![](images/a994c59668710803348146.png)

#### Types and states

#### File upload

Users can upload files by dragging and dropping or by clicking on the drop zone. The allowed file type, file size, and number of files must be defined by the consumer. If an unsupported file is uploaded, an error is displayed.

| Uploading | Loading | File preview | Uploading |
| --- | --- | --- | --- |
| ![Uploading](images/c72799846c597ec3fa1857.png) | ![Loading](images/af9d91d1bb783322180c76.png) | ![File preview](images/03b0934511da3790d8a2e4.png) | ![Uploading](images/0900e0cc46ef1d5db2e036.png) |

| Loading | File preview | Error |
| --- | --- | --- |
| ![Loading](images/cbe776a8abec1380157270.png) | ![File preview](images/17f8f866d170a656b8cfee.png) | ![Error](images/bfc849e7ab25f3684158ea.png) |

#### Action menu

* Choose as coverSet the file as a cover. Any file type can be set as a cover.

* Move forwardMoves the file one step forward. Alternatively, files can be dragged and dropped to any position.

* Move backwardsMoves the file one step backward. Alternatively, files can be dragged and dropped to any position.

* Edit captionOpens a modal where the user can change the file name (caption).

* Edit imageOpens an external image editor.

* RemoveDeletes the file.

![](images/17f8f866d170a656b8cfee.png)

##### Empty drop zone

Empty drop zones have the states default, hover, active and disabled. And they can be in an error state. When in error state, they contain an error message.

Depending on whether it's the first upload or additional files are being uploaded, the icon and text inside the drop zone will change.

**Neutral**

| Default empty | Hover empty | Active empty (Web only) | Disabled empty |
| --- | --- | --- | --- |
| ![Default empty](images/a4b09ec62d0f10521bb698.png) | ![Hover empty](images/776559d2e41699d96ab984.png) | ![Active empty (Web only)](images/2af623c793e3170d8e7496.png) | ![Disabled empty](images/400257164c5cac0bfba86a.png) |

| Default empty | Hover empty | Active empty (Web only) | Disabled empty |
| --- | --- | --- | --- |
| ![Default empty](images/ce4c56b2108785da2ce40b.png) | ![Hover empty](images/2d6a092f1c29cbf7ccefad.png) | ![Active empty (Web only)](images/ddaa2e6691127c4d3b803f.png) | ![Disabled empty](images/a4af2e21329813700d77c3.png) |

**Error**

| Default empty | Hover empty | Active empty (Web only) | Disabled empty |
| --- | --- | --- | --- |
| ![Default empty](images/094ba96cd4e550bee56d82.png) | ![Hover empty](images/171e138ab8c7c6bec30e31.png) | ![Active empty (Web only)](images/029eca1d9c3c535e1e671b.png) | ![Disabled empty](images/28a80ef1d0ce10e3ed37f5.png) |

| Default empty | Hover empty | Active empty (Web only) | Disabled empty |
| --- | --- | --- | --- |
| ![Default empty](images/01ffc12ece62b3d86ef020.png) | ![Hover empty](images/2aabcfbb942cc6e75b7290.png) | ![Active empty (Web only)](images/13d7ad6a36af06f54d1adf.png) | ![Disabled empty](images/945298e13c73bd6a0b0c18.png) |

##### Filled with image

When the user uploads an image, a preview of that image is displayed. The image preview can be either clickable or non-clickable. The clickable image preview has four states: default, hover, pressed and disabled.

The drag & drop indicator text (Drag images to rearrange order) is only displayed on web desktop.

| Default filled | Hover filled | Pressed filled | Disabled filled | Error filled |
| --- | --- | --- | --- | --- |
| ![Default filled](images/128dd5be931f516c86532c.png) | ![Hover filled](images/319d4aa29266ab320a781f.png) | ![Pressed filled](images/7ba6dc0434c2f4c21b372b.png) | ![Disabled filled](images/045626cf8769e8b21a4df4.png) | ![Error filled](images/960bf8f50c98c4a926ee3c.png) |

**Object fit**

Consumers can choose the preview behavior of uploaded images.

| Cover (default) | Contain |
| --- | --- |
| ![Cover (default)](images/09be8f087c388905cc51aa.png) | ![Contain](images/a2010b622796b5d6bc54df.png) |

##### Filled with file

When the user uploads any other file (non-image), a generic file icon is displayed. The file preview can be either clickable or non-clickable. The clickable image preview has four states: default, hover and pressed.

| Default filled | Hover filled | Pressed filled | Error filled |
| --- | --- | --- | --- |
| ![Default filled](images/af71a7fc363743bc2a6dfc.png) | ![Hover filled](images/49941ef241cca8f4ca1c5e.png) | ![Pressed filled](images/478d4e164609813a769422.png) | ![Error filled](images/960bf8f50c98c4a926ee3c.png) |

The disabled state is not currently available. If needed, please request it in [#gemini_support](https://kugawana.slack.com/archives/C048JM75SAC).

### Touch Target & Layout

* **Action menu:** The user can access the following options from the action menu: **Choose as cover** (set the file as a cover; any file type can be set as a cover), **Move forward** (moves the file one step forward; files can also be dragged and dropped to any position), **Move backwards** (moves the file one step backward), **Edit caption** (opens a modal to change the file name/caption), **Edit image** (opens an external image editor), **Remove** (deletes the file).
* **Width Adaptability:** The media upload cards adjust to the width of their container, filling the available space based on the size of the container. The width can be set to 100% (full-width) or 50% of the container. The cards have a fixed aspect ratio of 3:2.


### Breakpoints & Platform Adaptations

The text and style of the empty drop zone depends on the breakpoint. On the desktop, the dashed border and text indicates that drag and drop is possible. On phones and tablets, this is much less common, so the design is adjusted to reflect the different behavior. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web: XXS to MD (0 - 1023 px)** |  Tap. Android and iOS: used on all breakpoints. |
| **Web: LG to XXXL (> 1024 px)** |  Drag and drop. Android and iOS: not used. |

---

| Tap | Drag and drop |
| --- | --- |
| ![Tap](images/7eac4c848283063478caf2.png) | ![Drag and drop](images/a4b09ec62d0f10521bb698.png) |

## Content & UX Writing

* **Labels:** Media uploads should always have a label, to help the user understand what files they are supposed to upload. Keep the label short and concise (1-3 words) and in noun form. Start with a capital letter and use no punctuation (including colons).
* **Helper text (optional):** Add helper text if the user needs assistance with uploading files, such as explaining the allowed file type, size, or number of files. It can also be used to explain the drag and drop feature of the file preview cards. Use sentence-style capitalization and punctuation.
* **Error messages:** See the UX Writing guidelines to learn about [error messages](https://zeroheight.com/626199550/p/4051b4-error-messages).

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

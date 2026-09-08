<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831581316/Modal+bottom+sheet | Last modified: Aug 21, 2026 -->

# Modal bottom sheet

Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen.

![](images/EqU4JRZ6DUy6dKER-TKYFg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| [Modal bottom sheet on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7293) | Ready ✅ | Ready ✅ | Ready ✅ |

[Modal bottom sheet on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-overlay-modal--docs)

---

## Usage

Modal bottom sheets are used to display contextual information that is related to the current screen or to offer actions that are relevant to the user's current context.

### Platform

We use platform-specific modal bottom sheets that differ between Web, iOS and Android.

#### Web

On the Web, the component appears as a bottom sheet on phones and as a modal on desktop. The modal bottom sheet is not draggable on the Web.

![](images/30df24c67f6ae5792c6630.png)
Phone

![](images/EqU4JRZ6DUy6dKER-TKYFg.png)
Desktop

#### iOS

On iOS, we use native, draggable modal bottom sheets. As on the web, the component looks like a bottom sheet on phones and a modal on tablets. The tablet modals have a fixed height on iOS. If you have a small amount of content, please use the pop-up component instead.

![](images/30df24c67f6ae5792c6630.png)
Phone

![](images/351db6f4ee500ec694134b.png)
Tablet Portrait

![](images/bf7e0487e7c53c2031ff2b.png)
Tablet Landscape

#### Android

On Android we use native, draggable modal bottom sheets. The component appears as a bottom sheet on phones. On tablet you can choose between a bottom sheet (`ModalBottomSheet`) or a modal (`SheetSuite`).

### When to use

**Modal bottom sheet** — contextual content must overlay the screen and block interaction.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Content is a simple action list | **Modal bottom sheet menu** |
| Content should persist on the page | **Card** |
| An immediate, blocking decision is required | **Alert** |

### Variant Selection Flow

```
Surface, by platform and device — this is not a free choice
├─ Web
│  ├─ Phone → Bottom sheet
│  ├─ Desktop → Modal
│  └─ Never draggable on the web
├─ iOS → Native, draggable
│  ├─ Phone → Bottom sheet
│  └─ Tablet → Modal, portrait and landscape
└─ Android → Native, draggable
   ├─ Phone → Bottom sheet
   └─ Tablet → Bottom sheet or modal

Content volume
├─ Content exceeds the available space → Scrollable
└─ Small amount of content → Use Pop-up instead; see **Which component**
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/fd2ebc408db494d4962d86.png) **DO:** Use modals when it's important to get the user's full attention. | ![](images/2a4638419d0ead2105e341.png) **DON'T:** Don't use modal bottom sheets when the information or action isn't urgent or can be completed inline without interrupting the user's flow. They can be disruptive if overused. Use other components such as feedback messages, snackbars or info states. |

| DO |
| --- |
| ![](images/cda6de5897d42698ba1996.png) **DO:** In most use cases, the close button is located in the upper left corner. The "X" is quick to locate and is best for quick exits. |
| ![](images/f74d63cd9f47826dfa710f.png) **DO:** When using modals as alerts that require users to take action or make a decision, include a "Cancel" button next to the primary action. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Modal bottom sheet** | — | Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen. | — |
| [**Modal bottom sheet menu**](../modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) | High | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. | Content is a simple action list |
| [**Card**](../card/card.md) | High | Cards are flexible containers used to visually group content. | Content should persist on the page |
| [**Alert**](../alert/alert.md) | High | Alerts are modals that provide users with critical information they need immediately. | An immediate, blocking decision is required |

### Scrolling

When the content exceeds the available space, the modal becomes scrollable, allowing users to access all the information without having to resize or close the modal. Whether the scrollbar is visible or not depends on the user's system settings. To better separate the content from the header, a divider line appears when the user scrolls the modal.

| Default | Scrolling |
| --- | --- |
| ![](images/3f89087a83ce7793045037.png) | ![](images/e38e8f49fa34e5631a367c.png) |

### Interactive States & Loading

Not documented

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

The style of the modal bottom sheet depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). Breakpoints are different on iOS and Android. Check the [platform documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet/t/a053439e7a) to see the differences.

| Bottom sheet | Modal |
| --- | --- |
| ![](images/30df24c67f6ae5792c6630.png) Web: XXS - SM (0 - 767 px) Android: Compact (0 - 599 dp) iOS: iPhone | ![](images/EqU4JRZ6DUy6dKER-TKYFg.png) Web: MD - XXXL (> 767 px) Android Medium - Expanded (> 599 dp) iOS: iPad |

---

## Content & UX Writing

* **Title:** The title should be short and concise. Titles are optional, but recommended to improve clarity and explain the purpose of the modal.
* **Content:** Give users enough context within the modal itself to understand what they're being asked to do without having to refer to the main screen. Format the modal content with headings, bulleted lists, or short paragraphs to make it easy to read quickly. Include only essential information; remove anything irrelevant to the decision or action the user needs to take.
* **Buttons:** Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button.
  - **Capitalization:** Sentence case without punctuation.
  - **Label Formula:** {Action Verb} + {Noun}, in the infinitive tense, leading with an action verb — except for common actions like "Done," "Close," "Cancel," or "OK."
  - **Length Limits:** Keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

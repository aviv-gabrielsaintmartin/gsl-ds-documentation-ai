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

Desktop

| Phone | Dektop |
| --- | --- |
| ![Phone](images/d062ffe312cd74bc9b893f.png) | ![Dektop](images/41df3408fbf6071b6c7c59.png) |

#### iOS

On iOS, we use native, draggable modal bottom sheets. As on the web, the component looks like a bottom sheet on phones and a modal on tablets. The tablet modals have a fixed height on iOS. If you have a small amount of content, please use the pop-up component instead.

| Phone | Tablet Portrait | Tablet Landscape |
| --- | --- | --- |
| ![Phone](images/e3d0f3ac3069d6327fcb36.png) | ![Tablet Portrait](images/ed1fde2d97f6a3b4bf99a9.png) | ![Tablet Landscape](images/bf091153c3902a7f794d89.png) |

#### Android

On Android we use native, draggable modal bottom sheets. The component appears as a bottom sheet on phones. On tablet you can choose between a bottom sheet (`ModalBottomSheet`) or a modal (`SheetSuite`).

| Phone | Tablet Portrait | Tablet Landscape |
| --- | --- | --- |
| ![Phone](images/fc9f83fb7489f3094e780c.png) | ![Tablet Portrait](images/0bf342eca7cd882ac037e3.png) | ![Tablet Landscape](images/074371d52d47076b2bbd18.png) |

| Phone | Modal Bottom Sheet | Modal Bottom Sheet |
| --- | --- | --- |
| ![Phone](images/fc9f83fb7489f3094e780c.png) | ![Modal Bottom Sheet](images/aef50d8e4f281b86c6a74c.png) | ![Modal Bottom Sheet](images/0c19b2da0c434d0565c40a.png) |

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
|  **DO:** In most use cases, the close button is located in the upper left corner. The "X" is quick to locate and is best for quick exits. |
|  **DO:** When using modals as alerts that require users to take action or make a decision, include a "Cancel" button next to the primary action. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Modal bottom sheet** | — | Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen. | — |
| [**Modal bottom sheet menu**](../modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) | High | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. | Content is a simple action list |
| [**Card**](../card/card.md) | High | Cards are flexible containers used to visually group content. | Content should persist on the page |
| [**Alert**](../alert/alert.md) | High | Alerts are modals that provide users with critical information they need immediately. | An immediate, blocking decision is required |

## Variants & Modifiers

Not documented

### Modifiers

Not documented

---

#### Padding

The modal bottom sheet can be used with or without padding.

| With padding | Without padding |
| --- | --- |
| ![With padding](images/13e3027049de64b3eed723.png) | ![Without padding](images/53778fedefec46d8f989a4.png) |

| DO |
| --- |
| ![DO](images/f4c40a59272d3d2b916e5c.png)<br>**DO:** Use the modal bottom sheet with padding for most use cases. The padding helps separate text, illustrations and components from the border. |
| ![DO](images/3508db5cb528925a2f8d88.png)<br>**DO:** Use the modal bottom sheet without padding when you want to display maps or images in full width. |

#### Header and footer

The modal bottom sheet contains an optional header and footer.

| Header and footer | Only footer | Only header |
| --- | --- | --- |
| ![Header and footer](images/da5e7f4d04e6cfa017a69c.png) | ![Only footer](images/3a9588326f4a08eb319f0a.png) | ![Only header](images/55422e1247df5840a3a9a5.png) |

**Header**

The header has a close button on the left, a title in the middle and either a secondary button or up to 2 icons on the left. All elements of the header are optional.

| Header with button | Header with 1 - 2 icons |
| --- | --- |
| ![Header with button](images/784ae0b521fef55a13db5f.png) | ![Header with 1 - 2 icons](images/ff37120ef9bff095370337.png) |

ℹ️ If a close button is needed, it should be on the left. Please don't change the position in the top bar.

**Footer**

The footer (bottom bar) has 1 - 2 buttons. They can be aligned horizontally or vertically. We recommend vertical alignment only if there is not enough space to align them side by side.

| Footer with 1 button | Footer with 2 horizontal buttons | Footer with 2 vertical buttons |
| --- | --- | --- |
| ![Footer with 1 button](images/6ef2c23100ccf98bbf1b3e.png) | ![Footer with 2 horizontal buttons](images/00596a51c708c0fa221638.png) | ![Footer with 2 vertical buttons](images/8b43da026a2055df5f532e.png) |

### Sizes

The modal bottom sheet is available in different heights.

| Default (hug content) | Full-Height | Full-Screen |
| --- | --- | --- |
| ![Default (hug content)](images/d062ffe312cd74bc9b893f.png) | ![Full-Height](images/ec430392ecf777096d581d.png) | ![Full-Screen](images/b7614ea8769c174ea57664.png) |

| DO |
| --- |
| ![DO](images/7ca99b6cb52352ef7ecf74.png)<br>**DO:** Use the default size when the modal contains a small amount of content. Since the height adjusts to fit the content, it's ideal for compact information or simple actions that don't require scrolling. |
| ![DO](images/995c40378354c2d10cc72e.png)<br>**DO:** Use the full-height size when the modal contains a large amount of content and may require scrolling. The fixed height ensures consistency within flows. |
| ![DO](images/2269c122cf728b29f5e6b0.png)<br>**DO:** Use full-screen size for extensive content or detailed data entry. Full-screen modals are ideal when users need to focus solely on the modal content without distractions. It's useful for displaying maps or full-width images. |

## Behavior & Responsiveness

Not documented

### Interactive States & Loading

Modal bottom sheets appear in response to a user action, such as clicking a button, submitting a form, or completing a task. They can also appear automatically based on user behavior, such as reaching a certain scroll depth, spending time on a page, or attempting to exit.

They can be closed by clicking the close button, performing an action, or clicking outside the modal. On iOS and Android, they can also be closed by dragging them down.

| Clicking the x-button | Clicking an action | Clicking outside | Dragging modal |
| --- | --- | --- | --- |
| ![Clicking the x-button](images/ef67289bf551fb4167f01e.png) | ![Clicking an action](images/96b68eaad5eebcb5e80c2e.png) | ![Clicking outside](images/3f7ac9bb770523e808c63e.png) | ![Dragging modal](images/1615b0b63fc14c33a7841c.png) |

X-button vs. cancel button

| DO |
| --- |
| ![DO](images/c55b8535e8870a31ba2109.png)<br>**DO:** In most use cases, the close button is located in the upper left corner. The "X" is quick to locate and is best for quick exits. |
| ![DO](images/2a4638419d0ead2105e341.png)<br>**DO:** When using modals as alerts that require users to take action or make a decision, include a "Cancel" button next to the primary action. |

### Touch Target & Layout

When the content exceeds the available space, the modal becomes scrollable, allowing users to access all the information without having to resize or close the modal. Whether the scrollbar is visible or not depends on the user's system settings. To better separate the content from the header, a divider line appears when the user scrolls the modal.

| Default | Scrolling |
| --- | --- |
|  | ![](images/e38e8f49fa34e5631a367c.png) |

### Breakpoints & Platform Adaptations

The style of the modal bottom sheet depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). Breakpoints are different on iOS and Android. Check the [platform documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/5942fd-modal-bottom-sheet/t/a053439e7a) to see the differences.

| Bottom sheet | Modal |
| --- | --- |
|  Web: XXS - SM (0 - 767 px) Android: Compact (0 - 599 dp) iOS: iPhone | ![](images/EqU4JRZ6DUy6dKER-TKYFg.png) Web: MD - XXXL (> 767 px) Android Medium - Expanded (> 599 dp) iOS: iPad |

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

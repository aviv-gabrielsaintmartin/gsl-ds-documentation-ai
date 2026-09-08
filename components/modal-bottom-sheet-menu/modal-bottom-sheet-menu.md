<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831155273/Modal+bottom+sheet+menu | Last modified: Aug 21, 2026 -->

# Modal bottom sheet menu

Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps.

![](images/tuOhRVIC_5-SjJutQovUAQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

* [Modal bottom sheet menu on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=16366-21887&t=CDJo3x00MVOumTTf-4)
* [Modal bottom sheet menu on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/story/ui-navigation-actionmenu--default)

---

## Usage

Modal bottom sheet menus display a list of context-specific actions in a bottom sheet. As with the action menu, they are used when additional options are available to the user, but space is limited. They are only used on mobile screens or on apps.

### Platform

On web the modal bottom sheet menu is part of the Action menu. The bottom sheet is only displayed on breakpoints smaller than SM. On larger breakpoints the action menu displays a dropdown list.

On iOS/Android the modal bottom sheet menu and action menu are two separate components that can be used regardless of the screen size.

The style of the modal bottom sheet slightly differs between each platform. For more information please refer to the modal bottom sheet documentation.

| Web mobile & iOS/Android | Web desktop & iOS/Android |
| --- | --- |
| ![](images/ce2db68f84b1749f3e7955.png) Modal bottom sheet menu | ![](images/1f6b21644d93cc8f79fb71.png) Action menu |

### When to use

**Modal bottom sheet menu** — a list of contextual actions on mobile or in apps.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Desktop, SM and above | **Action menu** |
| Content richer than a simple action list | **Modal bottom sheet** |

### Variant Selection Flow

```
Header
├─ Title → Mandatory, but may be hidden when the context is unmistakable
└─ Web only → Optional subtitle

Badges
└─ Highlighting a new feature or an update → Badge to the right of the menu entry
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/acdeda841d82cbb4371bff.png) **DO:** In most use cases, display icons on the left of the labels. | ![](images/fe1e2362b5fa492a5acbf5.png) **DON'T:** Avoid mixing options with and without icons within the same modal bottom sheet menu. Icons can be omitted if none of the options require them. |
| ![](images/b0aeed31569c898452b524.png) **DO:** Use dividers to group related options in a menu. Grouping options helps users quickly scan the menu and find what they need. | ![](images/89a1ca7702989d92214a00.png) **DON'T:** Avoid overusing dividers. Too many dividers create visual noise, which can make the menu harder to read. |
| ![](images/d659fdf55982edc939ad3f.png) **DO:** Group destructive actions (e.g. Delete, Remove) at the end of the menu, separated by a divider, and style them in red to prevent accidental clicks. | ![](images/780f7c8a9bb6fd1621b3ab.png) **DON'T:** Don't place destructive actions at the top or in the middle of a menu, as this increases the risk of users accidentally triggering them. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Modal bottom sheet menu** | — | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. | — |
| [**Action menu**](../action-menu/action-menu.md) | High | Action menus display context-specific actions in a dropdown list. | Desktop, SM and above |
| [**Modal bottom sheet**](../modal-bottom-sheet/modal-bottom-sheet.md) | High | Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen. | Content richer than a simple action list |

---

## Variants & Modifiers

### Modifiers

#### Badges

Badges can be added to the right of the menu entries to highlight new features or updates.

![](images/c8db584e1e206065c34f20.png)

#### Header

The modal bottom sheet menu contains a title. On Web, an optional subtitle can be added. The title is mandatory, but can be hidden if the context is clear.

![](images/027d18a3896875c1fffe38.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

The menu entries have default, hover, pressed, and disabled states.

![](images/bce9b3cdc3d2333463069b.png)

The modal bottom sheet menu can be opened and closed in different ways.

| Open | Open | Close | Close |
| --- | --- | --- | --- |
| ![](images/51436237726e2e30afe7f4.png) Clicking an option | ![](images/38964f9215466280ae0ccb.png) Web and app | ![](images/7e7c684e654d3900e2c9e4.png) Clicking outside the action menu or pressing esc | ![](images/b798ebab30542d30601c00.png) App only |

### Breakpoints & Platform Adaptations

On the Web, for XXS and XS breakpoints (from 0 to 600px) the modal bottom sheet menu is used. For the breakpoints above SM, the action menu is used.

On Android and iOS both components can be used regardless of the screen size.

To learn more about our breakpoints, see our grids and breakpoint guidelines.

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Modal bottom sheet menu** | Web: XXS to XS (0 - 599 px) Android and iOS: used on all breakpoints |
| **Action menu** | Web: SM to XXXL (> 599 px) Android and iOS: used on all breakpoints |

### Scrolling

When the content exceeds the available space, the modal bottom sheet menu becomes scrollable. For more information please refer to the modal bottom sheet documentation.

![](images/489919cbdd949b1b7bd193.png)

---

## Content & UX Writing

* **Capitalization:** Sentence case without punctuation.
* **Label Formula:** Lead with an action verb that encourages action, in the infinitive tense.
* **Length Limits:** Try to keep it under 2 lines.

For more information on content guidelines, please refer to the UX Writing principles.

---

## Accessibility (a11y)

Not documented

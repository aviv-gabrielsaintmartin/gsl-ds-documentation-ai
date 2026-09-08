<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830991466/Wizard | Last modified: Aug 21, 2026 -->

# Wizard

Wizards guide users through step-by-step processes to achieve their goal.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

[Wizard on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7269) · [Wizard on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-wizard--docs)

---

## Usage

Wizards guide users through a multi-step processes by breaking it down into smaller, more manageable tasks. Each step is presented sequentially, with visual indicators showing which steps are completed, active, or pending. This helps users navigate complex processes with ease and provides a clear sense of progress.

![](images/5d7a28f10e12822e484449.png)

### When to use

**Wizard** — guiding users through a sequential multi-step process.

**Pattern**-tier component. Rule 0: do not compose a step-by-step flow from Tabs + Progress bar — this component already is it.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Sections are independent and non-sequential | **Tabs** |
| Showing task completion without step-by-step input | **Progress bar** |

### Variant Selection Flow

```
List type
├─ Steps must be completed in order, each depending on the one before → Numbered list
└─ The user may move between steps freely → Unordered list

Description
└─ Optional — add it when a step needs explaining
```

### Usage Guidance

| DO |
| --- |
| ![](images/5d7a28f10e12822e484449.png) **DO:** Use the wizard to guide users through a linear, step-by-step process. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Wizard** | — | Wizards guide users through step-by-step processes to achieve their goal. | — |
| [**Tabs**](../tabs/tabs.md) | High | Tabs are used to organize related content into different views and allow users to seamlessly switch between them. | Sections are independent and non-sequential |
| [**Progress bar**](../progress-bar/progress-bar.md) | High | A progress bar shows a task's progress. | Showing task completion without step-by-step input |

---

## Variants & Modifiers

### List type

The wizard list is available as an unordered or numbered list.

| Unordered list | Numbered list |
| --- | --- |
| ![](images/33eb53f293c0c4812482a6.png) | ![](images/88193d19405aa05b1e1244.png) |

**Unordered list:** Used when the user needs the flexibility to jump between steps without following a strict sequence. This variant is suitable for tasks where the order of completion is not critical.

**Numbered list:** Used when processes must be completed in a specific order, where each step depends on the completion of the previous one. This variant is suitable for tasks where linear progress is crucial.

### Modifiers

#### Description

The description is optional.

| With description | Without description |
| --- | --- |
| ![](images/c7e45c5d20f8ab2c21e0f4.png) | ![](images/4c37a067583570848ec29f.png) |

---

## Behavior & Responsiveness

### Interactive States & Loading

The wizard has the step types to do, done, error and disabled. Each type of step has the states default, hover and pressed.

#### To do

Uncompleted steps are marked with a black circle.

| Default | Hover | Pressed |
| --- | --- | --- |
| ![](images/96b51a8407263b31adb323.png) | ![](images/fb913ca19d61a467f1854b.png) | ![](images/72865b5ba0b7d4ee5a1ea3.png) |

| Default active | Hover active | Pressed active |
| --- | --- | --- |
| ![](images/5c3120ebc77969cda768bb.png) | ![](images/c935fa364abeb4ad13c57f.png) | ![](images/3aa8a9253b03e54d4c081c.png) |

#### Done

Validated steps are marked with a check mark in a green circle. This includes mandatory steps that have been completed or non-mandatory steps that don't need to be completed.

| Default | Hover | Pressed |
| --- | --- | --- |
| ![](images/0fc147c7b9f12391447911.png) | ![](images/e1aeacc85f434d35c00e05.png) | ![](images/fd22df9b94b65c93d1949d.png) |

| Default active | Hover active | Pressed active |
| --- | --- | --- |
| ![](images/f9c7d48490531ab61b64af.png) | ![](images/d5562d3d8e1ea343020708.png) | ![](images/cede43438a93c2ea669a42.png) |

#### Error

Input errors are marked with an exclamation mark in a red circle.

| Default | Hover | Default active | Hover active | Pressed active |
| --- | --- | --- | --- | --- |
| ![](images/b078343960b0cfb58392f8.png) | ![](images/a0743e8e5ac7cc263086e5.png) | ![](images/b5184e6250472e4d9e74a5.png) | ![](images/390bbf5f62ab5021b28662.png) | ![](images/92a772ccfe176d341cf181.png) |

#### Disabled

Steps that are not yet clickable because other steps must be completed first are grayed out.

![](images/b2942f3f4f64a2d85ad4dd.png)

> **Figma tip:** If the vertical lines between steps have the wrong color, select the layer Top line or Bottom line and change the variant to Done, To do or Disabled. If it's the first or last step select Start or End.

### Touch Target & Layout

* **Interaction:** Each row is clickable, but the icon is not.
* **Width:** The width of the wizard is determined by its content. If the container is smaller than the title and description, the text flows to the next line. Texts have a maximum length of two lines. If the text is longer, it is truncated.

![](images/d9147e883b24d0779ffdd9.png)

### Breakpoints & Platform Adaptations

**Desktop:** On desktop the wizard can be used on its own or can be placed on any background. For example, it can be used in a sidebar.

![](images/292b013ad39fab737f8caf.png)

**Mobile:** On mobile devices, the wizard must be placed inside a modal bottom sheet.

| Phone | Tablet |
| --- | --- |
| ![](images/222041afa273438334d55f.png) | ![](images/3448739f9074108ccc8aaf.png) |

**Entry point:** The top bar can be used as an entry point to open the modal bottom sheet.

| Web | iOS | Android |
| --- | --- | --- |
| ![](images/458fdb74c0e53fecc0fdfb.png) | ![](images/719fc8fa13b2b9ed50653c.png) | ![](images/b17849b14d5726c0eb94fd.png) |

**Scrolling:** If the wizard is longer than the container, it becomes scrollable.

![](images/6195099fe37c02abf16d1d.png)

---

## Content & UX Writing

* **Step titles:** Should be descriptive and help users understand what is expected of them. Keep titles short and concise, using 1-3 words. Start with a capital letter. Use consistent terminology between the wizard and your page titles to avoid confusion.
* **Step descriptions:** Use short, clear language to describe the user's progress. If needed, provide a simple summary of completed steps.
* **Progress indication:** Where appropriate, use numbers to clearly indicate progress through the steps.
* **Overflow content:** Title and description are limited to two lines. If the text is longer, it will be truncated.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

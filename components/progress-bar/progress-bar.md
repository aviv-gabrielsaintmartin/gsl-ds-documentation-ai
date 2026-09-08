<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832203875/Progress+bar | Last modified: Aug 21, 2026 -->

# Progress bar

A progress bar shows a task's progress.

![](images/l648xU_EnNU42mKld-eSBw.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

* [Progress bar on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=8346-132327)
* [Progress bar on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-progressbar--docs)

---

## Usage

We only provide the progress bar itself. Other elements, such as labels, can be added, removed or customized to suit your needs, depending on the context. Please share your use cases with us to help improve the guidelines.

| Stepper | Bar |
| --- | --- |
| ![](images/cd6b69bc7d726e4f1d99d3.png) It serve as a simple stepper, augmented with additional labels to enhance clarity and understanding. | ![](images/d010f410ccec94d0002e45.png) The progress bar can be a simple graph and a valuable visual representation of task completion. |

### When to use

**Progress bar** — linear task or goal completion.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A compact circular format fits better | **Progress circle** |
| Progress involves sequential user-input steps | **Wizard** |

### Variant Selection Flow

```
Style
├─ Normal surface → Default
├─ Dark background → Inverted
└─ Should recede visually → Neutral

Size
├─ Default → 8px
├─ Minor element in the hierarchy → 4px
└─ Prominent → 12px

Width
├─ Constrained by its container → Fixed
└─ Spans the container → Full width

Label — required for accessibility; the bar alone is not sufficient
├─ Always → A numerical label, such as 75% or 1/5
└─ Position → Left or right
```

### Usage Guidance

Not documented

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Progress bar** | — | A progress bar shows a task's progress. | — |
| [**Progress circle**](../progress-circle/progress-circle.md) | High | A progress circle shows a task's progress. | A compact circular format fits better |
| [**Wizard**](../wizard/wizard.md) | High | Wizards guide users through step-by-step processes to achieve their goal. | Progress involves sequential user-input steps |
| [**Charts**](../charts/charts.md) | Medium | Charts are data visualisation components used to represent numerical data and trends clearly and accessibly. | Charts redirects here when: Completion of a single goal |

---

## Variants & Modifiers

### Styles

| Default | Inverted (on dark background) | Neutral | Success |
| --- | --- | --- | --- |
| ![317f2597405101a14c67aa.png](https://avivgroup.atlassian.net/wiki/pages/viewpageattachments.action?pageId=2832203875&preview=%2F2832203875%2F3454861537%2F317f2597405101a14c67aa.png)  <!-- MISSING LOCAL IMAGE: 317f2597405101a14c67aa.png --> | ![](images/40f2a10ff2e74743a8926d.png) | ![](images/a60659031d091e087e1364.png) | ![](images/69f85024f52a373e9ae68a.png) |

### Size

| 4px | 8px (default) | 12px |
| --- | --- | --- |
| ![95a7f115-4d70-4a3d-a70f-bfd24f54e73e.png](https://avivgroup.atlassian.net/wiki/pages/viewpageattachments.action?pageId=2832203875&preview=%2F2832203875%2F3454861543%2F95a7f115-4d70-4a3d-a70f-bfd24f54e73e.png)  <!-- MISSING LOCAL IMAGE: 95a7f115-4d70-4a3d-a70f-bfd24f54e73e.png --> | ![](images/b4c7f48808532a039ccd08.png) | ![](images/fb7d2d7424c7576a9f7bc3.png) |

**4px:** Only recommended when the progress bar has a small hierarchy in the interface.

### Width

The width can be adapted to the context.

| Fixed | Full width |
| --- | --- |
| ![](images/c0bbb0ec9744b8872e8f15.png) | ![](images/c5702c6b28eaa6b1753e66.png) |

### Labels

The progress bar alone does not provide sufficient information to be accessible. It should be accompanied by a numerical progress label (e.g. 75% or 1/5). Both the positioning and size can be customized to suit your needs, depending on the context.

| Left | Right |
| --- | --- |
| ![](images/904f17a9726917642d3c1c.png) | ![](images/83b9d3bbad1586381c7ba9.png) |

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

| Default | In progress | Done | Success |
| --- | --- | --- | --- |
| ![](images/58b9bd5cca93714b4b8f7d.png) | ![](images/958666050afe4c4aa56110.png) | ![](images/ee68423c59f84a86d48a99.png) | ![](images/2c2becdf12e426bf3be441.png) |

**Success:** This state is not mandatory. It's recommend to use it when the bar is used as a chart and not a stepper.

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented

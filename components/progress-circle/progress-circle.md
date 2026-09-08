<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832695351/Progress+circle | Last modified: Aug 21, 2026 -->

# Progress circle

A progress circle shows a task's progress.

![](images/pDWPVEQ-P3kMaAjdQZ2-2w.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To Do 🚧 | To Do 🚧 |

* [Progress circle on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=8346-132488)
* [Progress circle on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-progresscircle--docs)

---

## Usage

The progress circle can be a simple graph and a valuable visual representation of task completion.

### When to use

**Progress circle** — a single completion percentage in a compact circular format.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A linear format fits the layout better | **Progress bar** |

### Variant Selection Flow

```
Style
├─ Normal surface → Default
└─ Dark background → On-dark

Size
└─ 64px, 96px or 128px

Label — required for accessibility; the circle alone is not sufficient
└─ A numerical label, such as 75% or 1/5 — its position is fixed and cannot be changed
```

### Usage Guidance

Not documented

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Progress circle** | — | A progress circle shows a task's progress. | — |
| [**Progress bar**](../progress-bar/progress-bar.md) | High | A progress bar shows a task's progress. | A linear format fits the layout better |

---

## Variants & Modifiers

### Styles

| Default | On-dark |
| --- | --- |
| ![](images/ece47a159e4c43b998c023.png) | ![](images/fcb884c2f25f8b05ea22a7.png) |

### Size

| 64px | 96px | 128px |
| --- | --- | --- |
| ![](images/2a55fff191c7acdcccf815.png) | ![](images/c89d91604d1a808b1a14a2.png) | ![](images/a1f522a1fb3503dff97138.png) |

### Labels

The progress bar alone does not provide sufficient information to be accessible. It should be accompanied by a numerical progress label (e.g. 75% or 1/5). Label position can't be changed.

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

| Default | In progress | Complete | Success |
| --- | --- | --- | --- |
| ![](images/70d345cc49b5d3f25469b4.png) | ![](images/c8397526ab523b137e1760.png) | ![](images/69f85024f52a373e9ae68a.png) | ![](images/19aa924a262256eef5c189.png) |

Success is an optional variant. Use it to add gamification.

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

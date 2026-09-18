The floating button group is used to display icon-only actions on top of images and maps.

![](images/WqQGeGstUtnnr_3NT0v-kg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | N/A | N/A |

⚠️ Web only

* [Floating button group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7292)
* [Floating button group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-overlay-floatingbuttongroup--docs)

---

## Usage

The floating button group is used for quick access to important actions without taking up much screen space. They are mainly used for zooming on maps.

### Platform

The component is only used on the web. On iOS and Android, native components are used instead. The native components are not available in the gemini figma libraries.

| Web | iOS | Android |
| --- | --- | --- |
| ![Web](images/a3028d3db3eef52230ce98.png) | ![iOS](images/32ee2e83cd6579ce41ca91.png) | ![Android](images/b1ac1c48932cddc54fb059.png) |

### When to use

**Floating button group** — actions that float above scrolling content, typically overlaying media.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Actions sit in normal page flow | **Button group** |
| A dropdown list of contextual actions | **Action menu** |
| A single action | **Button** |

### Variant Selection Flow

```
Number of buttons
└─ Two or three

Alignment
├─ Wide space available → Horizontal
└─ Narrow space, or anchored to a screen edge → Vertical
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![DO](images/7243514103f50bfb0c442f.png) **DO:** Use the floating button group for related actions, such as zooming on maps. | ![DON'T](images/bf5a4cc03dec2d8251a7fd.png) **DON'T:** Don't use the floating button group for unrelated actions. Instead, use individual floating buttons. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Floating button group** | — | Floating button groups are used to group related actions together and position them on top of images and maps. | — |
| **Button (floating)** | Medium | Floating buttons are used for unrelated actions on top of images and maps. | — |

---

## Variants & Modifiers

### Buttons

The floating button group is available with 2 - 3 buttons.

| 2 buttons | 3 buttons |
| --- | --- |
| ![2 buttons](images/5ea1fa999707d4695be553.png) | ![3 buttons](images/64a43ddb52947d74851a76.png) |

### Alignment

The floating button group is available with a vertical and horizontal alignment.

| Vertical | Horizontal |
| --- | --- |
| ![Vertical](images/dc161aeb21a1e213a94f77.png) | ![Horizontal](images/55c3553648968711b47c85.png) |

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

The buttons in the floating button group have the states default, hover, pressed and disabled.

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/f2c9e2e09a33da60b368d3.png) | ![Hover](images/2b91af1c33aaa37933cb07.png) | ![Pressed](images/5b0ef9cf95f0ba6b9db6b5.png) | ![Disabled](images/422d5915eb1b9c06a7f4ec.png) |

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

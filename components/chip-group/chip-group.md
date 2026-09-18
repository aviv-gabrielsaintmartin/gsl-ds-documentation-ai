Chip groups are collections of chips that allow users to filter, select, or manage multiple related options simultaneously.

![](images/7dz3_WZlIb8gPjEvmTpK2w.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | To do 🚧 | To do 🚧 |

* [Chip group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7273)
* [Chip group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-action-chipgroup--docs)

---

## Usage

Chip groups are dynamic, interactive collections of chips that allow users to filter content, toggle options, or make multiple selections within a related set, providing an efficient way to organize and manage complex choices or actions.

### When to use

**Chip group** — lightweight multi-select filtering or input outside a structured form.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Inside a structured form with labels and helper text | **Checkbox group** |
| Constrained space or numerous options | **Dropdown** |
| Filtering a SERP or data table with structured panels | **Filter bar** |
| The element is non-interactive | **Tag** |

### Variant Selection Flow

```
Type
├─ Toggling filters on and off across a set of options → Filter chip, selectable
├─ Representing user input or a selection inside a form, removable → Input chip, selectable
└─ Triggering a quick, secondary contextual action → Action chip, which cannot be selected
   └─ Never use action chips for primary navigation or for critical actions
   └─ Whether one group may mix types is not documented

Wrapping — the group's own layout, not the chip's
└─ The chips do not fit the container width → They wrap to a new line
   └─ How many chips a group may hold is not documented

Icons
└─ Optional — add one only when it makes the chip's purpose clearer
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![DO](images/0af2c5aa73ebef16e887a2.png) **DO:** Use chip groups to allow users to filter content, make selections, or perform actions. | ![DON'T](images/c255a7657ec74151ec1ac2.png) **DON'T:** Don't use chip groups to display static, non-interactive labels. Use tags instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Chip group** | — | Collections of chips that allow users to filter, select, or manage multiple related options simultaneously. | — |
| [**Chip**](../chip/chip.md) | High | Dynamic, clickable standalone component for selecting, filtering, or removing items. | Only a single, standalone chip is needed |
| [**Button**](../button/button.md) | Medium | Triggers actions. | A primary or critical action, not filtering/selection |
| [**Tag**](../tag/tag.md) | High | Non-interactive component for fixed information such as labels, categories, or statuses. | Displaying a static label or status with no interaction |
| [**Checkbox group**](../checkbox-group/checkbox-group.md) | High | Checkbox groups are used to select multiple options from grouped checkboxes. | Inside a structured form with labels and helper text |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | Constrained space or numerous options |
| [**Filter bar**](../filter-bar/filter-bar.md) | High | Filter bars are used to narrow down search results or displayed content based on selected criteria. | Filtering a SERP or data table with structured panels |

---

## Variants & Modifiers

### Type

#### Filter chips

Filter chips are used to represent filters in a set of options. They allow users to toggle selections on and off, providing a way to dynamically apply or remove filters.

| DO |
| --- |
| ![](images/544697cc2860084ff95b3f.png) **DO:** Use filter chips to filter content. |

| Default | Hover | Pressed |
| --- | --- | --- |
| ![Default](images/b5a8cb3fe735a039bb209b.png) | ![Hover](images/9d8b11be2f634b31e51085.png) | ![Pressed](images/20936c663268f602f0475b.png) |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
| ![Default selected](images/f6f41ab608e173d21c3df4.png) | ![Hover selected](images/6ada907c9a41507a8dfa94.png) | ![Pressed selected](images/e87611de0a497af72fce04.png) |

#### Input chips

Input chips represent user input, selections, or entries within a form. They can be removed with the close icon.

| DO |
| --- |
| ![DO](images/574d018b46ea06536e7623.png) **DO:** Use input chips to select items or enter information into a field. |

| Default | Hover | Pressed |
| --- | --- | --- |
| ![Default](images/253b3733f21b40ad573bbf.png) | ![Hover](images/58a6e3270568199c7b2a9e.png) | ![Pressed](images/2dc7687549d78437b21ae9.png) |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
| ![Default selected](images/0602ea86c95d398346c503.png) | ![Hover selected](images/c78d6e34f846b6e89da421.png) | ![Pressed selected](images/47b639128b0cd8551e589d.png) |

#### Action chips

Action chips trigger actions when clicked, often performing contextual tasks that enhance the primary functionality of a page. They are lightweight, intuitive, and designed for quick, secondary actions.

| DO | DON'T |
| --- | --- |
| ![](images/c74d01ef7a2e85b14c66f6.png) **DO:** Use action chips when users need a lightweight, dynamic way to perform quick actions relevant to their current task. | ![](images/542b44f72e5418bf61522c.png) **DON'T:** Don't use action chips as primary navigation or for critical actions. Don't use them to move to the next/previous step or to complete/progress in a user journey. Use buttons instead. |

| Default | Hover | Pressed |
| --- | --- | --- |
| ![Default](images/4ff5fffd1ff0fa20bf6508.png) | ![Hover](images/ed07b7f177727db911439f.png) | ![Pressed](images/d6eaed9a39988e64255fdc.png) |

### Modifiers

#### Icons

Icons are optional and can be included to provide additional context or visual cues that make the purpose of the chips more intuitive and easier to understand.

---

| With icon | Without icon |
| --- | --- |
| ![With icon](images/edf914b6000d9e2b3af20a.png) | ![Without icon](images/7fcd910cf0c1d7d707c565.png) |

### Filter chips

| Unselected | Selected |
| --- | --- |
| ![Unselected](images/68441a0dddbd1c296048bf.png) | ![Selected](images/f6fec4e56a3908386de839.png) |

### Input chips

| Unselected | Selected |
| --- | --- |
| ![Unselected](images/fab4640d1161aae1c810d3.png) | ![Selected](images/3dd187bc26c16e39f5f37c.png) |

### Action chips

| Default |
| --- |
| ![Default](images/57e908805a25bc06905581.png) |

## Behavior & Responsiveness

### Interactive States & Loading

The states of the individual chips in the chip groups are the same as for [standalone chips](https://zeroheight.com/626199550/p/32f686-chip).

* **Filter chips:** Default, hover and pressed states; can be selected or unselected.
* **Input chips:** Default, hover and pressed states; can be selected or unselected.
* **Action chips:** Default, hover, and pressed states, but cannot be selected.

#### Touch target

![](images/4c9dc090ecdeb93c1c6a15.png)

#### Wrapping

| One line | Wrapped on second line |
| --- | --- |
| ![One line](images/817e8d55a60f70520f1e2a.png) | ![Wrapped on second line](images/9ccef6f14b1b3e43183ac5.png) |

### Touch Target & Layout

* **Touch Target:** To ensure accessibility, the touch target of each chip has a height of 40px.
* **Width Adaptability:** Chips wrap to a new line if there is not enough space for all of them.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Sentence case, without punctuation.
* **Label Formula:** For action chips, {Verb} + {Noun}, leading with an action verb in the infinitive tense.
* **Length Limits:** 2-3 words, about 20-30 characters in English.

**Filter chips:** Use concise, descriptive labels that clearly communicate the purpose of the filter. Keep labels consistent across similar filters.

**Input chips:** Write labels that are specific and relevant to the input or selection being represented. Maintain brevity while ensuring that users can easily identify the context or purpose of the input.

**Action chips:** Use action-oriented labels that clearly indicate the task being performed. Keep labels short and concise. To provide enough context to users, use the {verb} + {noun} content formula.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

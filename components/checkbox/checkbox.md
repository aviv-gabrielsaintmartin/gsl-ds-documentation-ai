<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830958639/Checkbox | Last modified: Aug 17, 2026 -->

# Checkbox

Checkboxes are used to select one or more options from a list.

![](images/IJ0shhF-zzNGnmO1vqaB7Q.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Partially available |

* [Checkbox on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7276)
* [Checkbox on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-checkbox--docs)

---

## Usage

Checkboxes are selection components that are used for multiple choices. They allow the user to select none, one or more items. They can also be used to display a single option that requires acceptance or confirmation before submission.

### Platform

On the web and iOS, we use custom checkboxes. On Android, we use native checkboxes.

| Web/iOS | Web/iOS | Android | Android |
| --- | --- | --- | --- |
| ![Web/iOS](images/68a69190dd1de99d48f027.png) | ![Web/iOS](images/6da80ca1022ba4d95a1153.png) | ![Android](images/c225f268ecbf3ac76476be.png) | ![Android](images/8c1d3962d115062488fa25.png) |

### When to use

**Checkbox** — a single binary choice that is submitted as part of a form.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The setting takes effect immediately | **Toggle** |
| Several related options are presented together | **Checkbox group** |
| The choices are mutually exclusive | **Radio button group** |

### Variant Selection Flow

```
Border
├─ Options need emphasis, or must be clearly separated from one another → With border
└─ Simple, easily distinguished options → Without border

Label
├─ Almost always → With label
└─ Context makes the meaning unambiguous, such as a table row selector → Without label

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![DO](images/542914cd9229c90ce4c019.png) **DO:** Use a standalone checkbox in forms where the selection takes effect only after the form is submitted. | ![DON'T](images/af554c5064cca28d1075c4.png) **DON'T:** Avoid using a checkbox to toggle a state on and off immediately. Use a switch instead. |
| ![DO](images/b572f720a0cba44b6cfb97.png) **DO:** Use checkboxes to allow users to select one or more options in a list of related choices. | ![DON'T](images/7a02b3d997f475a4311a00.png) **DON'T:** Don't use checkboxes for mutually exclusive choices or when only one item can be selected. Use radio buttons instead. |

| CAUTION |
| --- |
| ![](images/49b65322e95052ccda608d.png) **CAUTION:** When you want to use checkboxes in a list, consider using the checkbox group component. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Checkbox** | — | Allows users to select one or more choices independently; used in forms that must be submitted before the change takes effect. | — |
| [**Radio button**](../radio-button-group/radio-button-group.md) | High | Mutually exclusive choices, submitted before the change takes effect. | Only one option can ever be selected at a time |
| [**Toggle**](../toggle/toggle.md) | High | Binary, mutually exclusive choices that take effect immediately, no submit/save needed. | Turning a setting on/off with instant effect |

---

## Variants & Modifiers

### Border

Checkboxes can be used with or without a border. Add a border when you want to emphasize the options more clearly. Borders can also help to distinguish each checkbox.

| Without border | With border |
| --- | --- |
| ![Without border](images/68a69190dd1de99d48f027.png) | ![With border](images/bd3775696caf5b56e10e03.png) |

### Label

Checkboxes should be used with a label in most cases. Only in a few exceptions, when the context is clear, can checkboxes be used without labels. For example, in tables.

| With label | Without label |
| --- | --- |
| ![With label](images/c121ffd3c8735a6de45a90.png) | ![Without label](images/18b3e9a5b3d92d492c0f20.png) |

### Modifiers

Checkboxes have the same elements as all form components:

* Required asterisk to the right of the label (visible by default)
* Optional mention to the right of the label
* Tooltip to the right of the checkbox

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

| Required | Required | Optional |
| --- | --- | --- |
| ![Required](images/07e29a906fa67f5ad05051.png) | ![Required](images/ad450c2c51d3aaa414858d.png) | ![Optional](images/99e0de38c377deeefcc0aa.png) |

| Optional | Tooltip | Tooltip |
| --- | --- | --- |
| ![Optional](images/ee8a5565d49338f2b0ef29.png) | ![Tooltip](images/cf5d6fd466edad4f0c7d36.png) | ![Tooltip](images/89f41d67435577f0a190ab.png) |

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed / Disabled:** Checkboxes have the states default, hover, pressed, and disabled. They can be selected, unselected or indeterminate, and they can be in an error state.

#### Neutral

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/68a69190dd1de99d48f027.png) | ![Hover](images/47c32b95502516bf164a5e.png) | ![Pressed](images/821a3d77cc3ff1c3d1e6de.png) | ![Disabled](images/93ffa50bca7ec189690c41.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![Default selected](images/6da80ca1022ba4d95a1153.png) | ![Hover selected](images/dd2f05463d169a8568e608.png) | ![Pressed selected](images/b0db0c2429842f19d5fb24.png) | ![Disabled selected](images/bc81c0b0d23870c0ccfde3.png) |

| Default indeterminate | Hover indeterminate | Pressed indeterminate | Disabled indeterminate |
| --- | --- | --- | --- |
| ![Default indeterminate](images/02998288f0a1d6d1bed870.png) | ![Hover indeterminate](images/33a2072eb12ac72da23528.png) | ![Pressed indeterminate](images/0129aba845af2974089b77.png) | ![Disabled indeterminate](images/125ac482b9e708363c27f9.png) |

#### Error

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/39465ff71a5e9eeefe537e.png) | ![Hover](images/ba859e8c8858b7d80de9de.png) | ![Pressed](images/4c1fa6ee405a3f24a2216b.png) | ![Disabled](images/78a67d22fed4357dd6e2a0.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![Default selected](images/cd80945498a021b431310c.png) | ![Hover selected](images/4d60fa89791b8d3a96f354.png) | ![Pressed selected](images/2a14605fde4bc0134e7104.png) | ![Disabled selected](images/69ae44202728dfd556eec1.png) |

| Default indeterminate | Hover indeterminate | Pressed indeterminate | Disabled indeterminate |
| --- | --- | --- | --- |
| ![Default indeterminate](images/b4c331391127dfd574a24c.png) | ![Hover indeterminate](images/fed61addd7a5e4517c2961.png) | ![Pressed indeterminate](images/7b3cc20ce4e4d149019b65.png) | ![Disabled indeterminate](images/90c420629577fd315e4f39.png) |

![](images/a92a956ce1de8a03388c20.png)

### Touch Target & Layout

* **Width Adaptability:** The width of the checkbox component is determined by its content. According to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

Not only the checkbox itself is clickable, but also the entire row. The row height is 48px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start each list item with a capital letter; don't use commas or semicolons at the end of each line.
* **Label Formula:** Not documented.
* **Length Limits:** Less than 3 words; don't use an ellipsis to cut off label text — wrap to 2 lines if necessary.

**Checkbox labels:** Always use clear and concise labels for checkboxes. Labels appear to the right of checkbox inputs. A label is always required in the code for a checkbox, even if it's not shown in the interface.

**Overflow content:** Make sure that the text under the checkbox wraps to the next line, and that the checkbox and its label are aligned at the top.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

### Checkbox lists

Lists that use checkboxes should:

* **Start with a capital letter**

* Not use commas or semicolons at the end of each line

## Accessibility (a11y)

* **Keyboard Navigation:** Not documented.
* **Screen Readers:** A label is always required in the code for every checkbox, even when it's not visibly shown in the interface, so it can still be announced.

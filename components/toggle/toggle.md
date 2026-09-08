<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832400439/Toggle | Last modified: Aug 21, 2026 -->

# Toggle

Toggles are used to switch between on and off states.

![](images/gvq4xxgMMGqLso7a0Yy7WA.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

[Toggle on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7286&t=cY0FVB8lofjw9Zwd-11) · [Toggle on Storybook](https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-toggle--docs)

---

## Usage

The toggle component is a component that allows users to switch between two states: on and off. It is commonly used when a user needs to enable or disable a feature or option.

### Platform

On the web, we use custom toggles. On Android and iOS, we use native toggles.

| Web | Android | iOS |
| --- | --- | --- |
| ![](images/21985e0f14a9f406db5b51.png) | ![](images/c2ba71293d61e03e8fc281.png) | ![](images/3604d514ef08c6bfd38188.png) |

### When to use

**Toggle** — a binary on/off setting that takes effect immediately — settings, preferences.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The setting is submitted as part of a form | **Checkbox** |

### Variant Selection Flow

```
Toggle position
├─ The control leads the label → Left
└─ The control trails the label → Right

Header elements, as with every form component
├─ Mandatory field → Required asterisk to the right of the label, visible by default
├─ Optional field → Optional mention to the right of the label
└─ Needs an explanation → Tooltip to the right of the toggle label
```

### Usage Guidance

| DO |
| --- |
| ![](images/92e1082ee2270b02819095.png) **DO:** Use toggles for binary on/off choices, where the selection is applied immediately. |

| CAUTION |
| --- |
| ![](images/c06701d4502d99c2f300b3.png) **CAUTION:** Avoid using toggle inside forms. Toggles should take effect immediately, without having to submit a form. Use checkboxes instead. |
| ![](images/58e71b838bbd28d5ac26b4.png) **CAUTION:** When you want to use toggles in a list, consider using the toggle group component. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Toggle** | — | Toggles are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving. | — |
| [**Checkbox**](../checkbox/checkbox.md) | High | Checkboxes allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. | The setting is submitted as part of a form |
| [**Radio button**](../radio-button-group/radio-button-group.md) | Medium | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. | — |

---

## Variants & Modifiers

### Toggle position

Toggle can be positioned on the left or on the right depending on the use case.

| Left | Right |
| --- | --- |
| ![](images/21985e0f14a9f406db5b51.png) | ![](images/d06824aafcb4722cb0f010.png) |

### Modifiers

Toggles have the same elements as all form components:
* Required asterisk to the right of the label (visible by default)
* Optional mention to the right of the label
* Tooltip to the right of the toggle label

See the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

| Optional | Required | Tooltip |
| --- | --- | --- |
| ![](images/556f41e3ff1803cfca8c35.png) | *Image not available in source export* | ![](images/556f41e3ff1803cfca8c35.png) |

---

## Behavior & Responsiveness

### Interactive States & Loading

#### Neutral

Toggles have the states default, hover, pressed, and disabled. They can be selected or unselected. Unlike [checkboxes](https://zeroheight.com/626199550/p/3044f1-checkbox) or [radio buttons](https://zeroheight.com/626199550/p/55bfd7-radio-button-group), they don't have a red border indicating an error state, but they have an error message.

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![](images/d06824aafcb4722cb0f010.png) | ![](images/f03b8342f2341bed4b41b4.png) | ![](images/402ebb3d34d7d07dc3b5e3.png) | ![](images/5d0130447dd755db4dbcae.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![](images/e5ebd41350c841d30abb19.png) | ![](images/2bc82b01a4dfb77d36019d.png) | ![](images/732726df1041347a28959f.png) | ![](images/7a00d13324345468d61fbd.png) |

#### Error

![](images/039b68f0c122a0f9ca367d.png)

#### Loading

This state is typically triggered when the action initiated upon click involves an API call or server query. This provides the user with a visual indication that their action is being processed.

During this waiting period, a loader will be shown in place of the toggle. If the loading process fails, a snackbar can be utilized to display the error message.

To avoid a flashing effect, the loader will be displayed for a minimum of 600 milliseconds.

| iOS | Web & Android |
| --- | --- |
| ![](images/525974ab367abd197b87d2.png) | ![](images/79d7be54a5810a38c20b52.png) |

### Touch Target & Layout

**Interaction:** Not only the toggle itself is clickable, but also the entire row. The row height is 48px.

![](images/5cd74b4fd31c14661bf3f2.png)

**Width:** The width of the toggle component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Toggle lists** — Lists that use toggles should start with an uppercase letter.
* **Toggle labels** — Always use clear and concise labels for toggles. Labels appear to the right or left of the toggle.
* **Overflow content** — We recommend that toggle labels be less than 3 words. Don't use an ellipsis to cut off the text of a toggle label. If necessary, use 2 lines.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

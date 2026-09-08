<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831351902/Toggle+group | Last modified: Aug 21, 2026 -->

# Toggle group

Toggle groups are used to organize related options, allowing users to switch between multiple settings, with each toggle independently controlling an on or off state.

![](images/jSIv4dliExAz9xxnc9HL0Q.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | To Do 🚧 |

* [Toggle group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=11-60709&t=G4GRFXe9ksnNqcW5-11)
* [Toggle group on Storybook](https://gemini-storybook.prompt-scorpion-dev.aws.aviv.eu/16ebe6f/?path=/docs/ui-forms-togglegroup--docs)

---

## Usage

Toggle groups allow users to enable one or more options from a predefined set of choices. The preference should take effect immediately, without the need to submit or save the action. They are most often used for preferences and settings.

### Platform

As with standalone toggles, the group contains custom toggles on Web and native toggles on iOS and Android.

### When to use

**Toggle group** — multiple independent on/off settings, grouped.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Settings are part of a form submitted later | **Checkbox group** |
| Switching between views rather than toggling settings | **Segmented control** |

### Variant Selection Flow

```
Toggle position
├─ The control leads the label → Left
└─ The control trails the label → Right
   └─ Every toggle in a group takes the same position — never mix them

Header, as with every form component
├─ Mandatory field → Required asterisk to the right of the label
├─ Optional field → Optional mention to the right of the label
├─ Needs an explanation → Tooltip icon
└─ Needs persistent guidance → Helper text
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/d2c96f848ec3af778748c1.png) **DO:** Use toggle groups in settings for binary choices, where the choice is applied immediately. | ![](images/ea2c658f02bc80106054a0.png) **DON'T:** Don't use toggle groups when only one item can be selected. Use radio buttons instead. |

| CAUTION |
| --- |
| ![](images/ee57fdcd9d9f3ef70d0fc5.png) **CAUTION:** Avoid using toggle groups within forms. Toggles should take effect immediately, without submitting a form. Use checkboxes instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Toggle group** | — | Toggle groups are used for binary, mutually exclusive choices that take effect immediately and don't require submitting or saving. | — |
| [**Checkbox group**](../checkbox-group/checkbox-group.md) | High | Checkbox groups allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. | Settings are part of a form submitted later |
| [**Radio button group**](../radio-button-group/radio-button-group.md) | Medium | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. | — |
| [**Segmented control**](../segmented-control/segmented-control.md) | High | Segmented controls are used to select one option from a group of mutually exclusive choices. | Switching between views rather than toggling settings |

---

## Variants & Modifiers

### Modifiers

#### Toggle position

Like standalone toggles, toggle groups can also switch from a toggle left position to a toggle right position, depending on use case and layout.

| DO | DON'T |
| --- | --- |
| ![](images/3d931fe720f0a3e4d0ba1d.png) **DO:** All toggles in a toggle group should have the same position. | ![](images/309ba374f9c8c42f5ff723.png) **DON'T:** Don't mix positions in the same toggle group. |

#### Header

Like all form components, toggle groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

---

## Behavior & Responsiveness

### Interactive States & Loading

Like the standalone toggle, groups have the states default, hover, pressed, and disabled. They can be selected or unselected, and they can be in an error state. When in error state, they contain an error message.

They also contain a loading state which is typically triggered when the action initiated upon click involves an API call or server query. To learn more about toggle loading go to the [toggle documentation](https://gemini.zeroheight.com/styleguide/s/92948/p/4685c0-toggle/t/e5617ecdeb).

* [Guidelines on form validation and displaying errors](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-79)
* [Content guidelines for state messages](https://zeroheight.com/626199550/p/526801-state-messages)

### Touch Target & Layout

* **Interaction:** Not only the toggle itself is clickable, but also the entire row. The row height is 48px.
* **Width:** The width of the toggle group component is determined by its content. According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the max-width should be kept at 448px.
* **Wrapping and alignment:** Text that exceeds the available space is automatically wrapped to a new line. Toggle and content are centered.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Toggle group:** Toggle group labels should start with a capital letter, and not use commas or semicolons at the end of each line.
* **Toggle label:** Always use clear and concise labels for toggles. Labels appear to the right or left of toggles.
* **Group labels (optional):** In most cases, a group label precedes a set of toggles to provide further context or clarity. A group label can either indicate the category of the grouping or describe the actions to be taken below it. In some cases, a group of toggles may be within a larger group of components that already have a group label — in this case, no additional group label is required for the toggle component itself.
* **Helper text (optional):** Add an helper text below the label to provide additional context and help the user make a decision.
* **Overflow content:** We recommend that toggle labels are less than a few words. Don't use an ellipsis to cut off the text of a toggle label — if necessary, use 2 lines. Make sure that the text under the toggle wraps to the next line, and that the toggle and its label are aligned at the centre. For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831450204/Slider | Last modified: Aug 21, 2026 -->

# Slider

A range slider can be used to select a single value or a range between minimum and maximum values.

![](images/Hb0YZ9yT3xcGE1HqbHjylg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | WIP 🚧 | To-do 🚧 | To-do 🚧 |

* [Slider on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=10755-46456)

---

## Usage

The slider component allows users to select a value from a specified range by sliding a handle along a track. This is particularly useful for adjusting settings such as volume, brightness, or any other numerical value.

The range slider allows to select a range by sliding 2 handles along the track. This is useful to choose a price range, a distance or any range.

![](images/917e1494d13816f6face82.png)
![](images/96eadfaf3ede3bdcad4150.png)

### When to use

**Slider** — selecting a value or range along a continuous scale.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Precision and exact entry matter | **Counter field** |
| Only discrete values available | **Dropdown** |

### Variant Selection Flow

```
Selected value
├─ Default → Shown at the top right
└─ The value already appears elsewhere, or updates live such as when cropping an image → Hidden

Minimum and maximum values
├─ Selecting a numeric value → Mandatory, shown left and right
└─ Other uses, such as a sound level → Optional

Step marks and step values
└─ The slider allows only predefined values → Show the step marks, and optionally the step values

Text fields
├─ A precise value matters, such as monthly revenue → Show the text fields
└─ An approximate value is enough → Omit them

Header
└─ Used as a form element → Show the form header: tooltip trigger, required or optional mention, helper text
```

### Usage Guidance

Not documented

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Slider** | — | A range slider can be used to select a single value or a range between minimum and maximum values. | — |
| [**Counter field**](../counter-field/counter-field.md) | High | Counter fields are used to enter or select numeric values. | Precision and exact entry matter |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | Only discrete values available |

---

## Variants & Modifiers

### Modifiers

#### Display the selected value

The slider value should always be visible to the user. By default, it can be displayed on the top right of the component.

The value can be hidden if displayed in another place on the screen or if the selection value is visible in live such as when cropping an image.

![](images/917e1494d13816f6face82.png)
![](images/96eadfaf3ede3bdcad4150.png)

#### Display the min and max value

The minimum and maximum selectable value can be displayed on the left and right of the slider.

Those values are mandatory when selecting a numeric value but not for other use cases such as sound level selection slider.

![](images/e750dad74e336bbdd968bc.png)
![](images/33fa2cdabc6dea81cc3028.png)

#### Display the steps marks

If your slider only allow predefined value, they should be displayed. Additionally, you can display the steps value.

![](images/20eff6edf555cf2c6ffce7.png)
![](images/b37185839a28010ddf7ad1.png)

#### Display the steps values

If your slider only allow predefined value, they should be displayed. Additionally, you can display the steps value.

![](images/e3902c81d67255f23c95d1.png)
![](images/c049160ed802b307db0611.png)

#### Display the text fields

When a numeric value is selectable, you can display the text field, allowing user to write directly the requested value. This is strongly recommend when a precise value such as the monthly revenue. When the text field is displayed, the selected value is hidden.

![](images/82feb14f4b505814e3ae59.png)
![](images/51f5e1c053ebdd902ed2f2.png)

#### Display the header

When used as a form element, you can display the form header, including the tooltip trigger, required and/or optional mentions and the helper text.

![](images/59b5592ac0bbe6c4c80f8f.png)
![](images/0a978dd997a20cdc814212.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** The slider itself has the states default and disabled. The handles have all the states: default, hover, pressed and disabled.
* **Disabled State Guidance:** The slider can be fully disabled, preventing interaction with both the track and the handles.

![](images/2584faa6da55918c7cab8b.png)
![](images/009bb277a1ba4017580050.png)
![](images/4105b724c3fc9fa5d98973.png)
![](images/1d78a5b4c3496812143d4a.png)

**Error:** the error can only occur when the text fields are displayed. The error occurs when the user writes a value that is outside the allowed range. On click on the slider track, the value is selected and the error disappears. The user should correct the error themselves.

![](images/7ebb523cd00e66c2590d2e.png)
![](images/60ae037da3c3da3b16df5f.png)

**Interaction:** value selection by touch/click — on click on the track, the closest handle will move where the click happens. Value selection by filling the text fields — when the text field is displayed, any change in the handle position will automatically update the value of the text field; conversely, updating the text field value will also adjust the handle position accordingly.

### Touch Target & Layout

* **Width Adaptability:** The slider adjusts to the width of its container, filling the available space based on the size of the container. The minimum recommended width is 288px (minimum mobile size minus the left and right margin).

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Labels:** Slider should always have a label, to help the user understand what information to enter.
* **Capitalization:** Start with a capital letter and use no punctuation (including colons) for labels; helper text uses sentence-style capitalization and punctuation.
* **Label Formula:** Keep the label in noun form.
* **Length Limits:** Keep the label short and concise (1-3 words).
* **Helper text (optional):** Add a helper text if the user needs assistance completing a field. Helper text is optional and can be used instead of a tooltip. When used, it is always available when the input is focused and appears below the field — exceptions are when an error or warning message replaces the helper text in apps.

For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

Select cards are used for single- or multi-selection inside forms.

![](images/G2bDxxkNTYzq1_kXW1-F9A.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Not documented | Ready ✅ | Ready ✅ | Partially developed |

* [Select card group on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7282)
* [Select card group on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-forms-selectcardgroup--docs)

---

## Usage

Select card groups are collections of cards organized together to allow users to choose between related options. They provide a visually engaging alternative to traditional radio buttons or checkboxes. They support single- and multi-select and include icons, illustrations and descriptions.

### Platform

Select cards contain custom checkboxes on Web/iOS and native checkboxes on Android.

| Web/iOS | Android |
| --- | --- |
| ![Web/iOS](images/6a325afb510e3ea785e0e7.png) | ![Android](images/62e2493e7840e775680a6f.png) |

### When to use

**Select card group** — form selection benefits from a visual, card-based layout with icons or illustrations.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Simpler single-select | **Radio button group** |
| Simpler multi-select | **Checkbox group** |
| The intent is navigation, not selection | **Button card** |

### Variant Selection Flow

```
Grouping
├─ Several related cards → Group
└─ One standalone choice → Individual select card

Selection type
├─ One option only → Single-select, no indicator
└─ Several options → Multi-select, with a checkbox

Alignment
├─ Wide space, longer content → Horizontal
└─ Narrow space → Vertical

Leading visual
├─ Illustration → 40px or 64px; pictograms recommended
└─ Icon → When an illustration would be too heavy

Text
├─ Title → Mandatory
└─ Description → Optional, for extra explanation
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/842d0178eda49810307333.png) **DO:** Use select cards to display more visual engaging choices, that are enhanced with icons, illustrations and descriptions. | ![](images/4669b8f4755e09945dbafa.png) **DON'T:** Don't use select cards when you need to display more than 6 options, or when there is limited space available. Use radio and checkbox groups instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Select card group** | — | Select cards are used for single- or multi-selection inside forms. | — |
| [**Radio button group**](../radio-button-group/radio-button-group.md) | High | Radio buttons allow users to make mutually exclusive choices. They are used in forms that must be submitted before the change takes effect. | Simpler single-select |
| [**Checkbox group**](../checkbox-group/checkbox-group.md) | High | Checkbox groups allow users to select one or more choices independently. They are used in forms that must be submitted before the change takes effect. | Simpler multi-select |
| [**Button card**](../button-card/button-card.md) | High | Button cards are prominent calls to action that can be used alone or in a group, with icons or pictograms. | The intent is navigation, not selection |
| [**Button card**](../button-card/button-card.md) | High | Button cards are prominent calls to action that can be used alone or in a group, with icons or pictograms. | The intent is navigation, not selection |

---

## Variants & Modifiers

### Group

Select cards are available as a group or individual select cards.

| In a group | Individual card |
| --- | --- |
| ![In a group](images/320237bf5c6c0ee5282736.png) | ![Individual card](images/7b033a3ec4274431b65b4d.png) |

### Type

Select cards are available as single or multi-selection component. The multi-selection variant contains a checkbox, the single-selection one doesn't contain an indicator.

| Single-select (radio) | Multi-select (checkbox) |
| --- | --- |
| ![Single-select (radio)](images/7b033a3ec4274431b65b4d.png) | ![Multi-select (checkbox)](images/edb378e1684dc72bae908a.png) |

### Alignment

The content inside select cards can be in a vertical or horizontal alignment, depending on the use case and layout structure.

| Vertical | Horizontal |
| --- | --- |
| ![Vertical](images/edb378e1684dc72bae908a.png) | ![Horizontal](images/eb2dbcc491f5267a5763cd.png) |

### Modifiers

#### Icons and illustration

Select cards contain optional icons and illustrations. The illustrations are available in the size 40 and 64px. If you use an illustration we recommend the usage of pictograms.

| Icon | 40px illustration | 64px illustration |
| --- | --- | --- |
| ![Icon](images/edb378e1684dc72bae908a.png) | ![40px illustration](images/500effc1ad3cb6f03299e7.png) | ![64px illustration](images/6b11efdabba4899d7a9f31.png) |

| Icon | 40px illustration | 64px illustration |
| --- | --- | --- |
| ![Icon](images/eb2dbcc491f5267a5763cd.png) | ![40px illustration](images/0a65930c1b4a3b80917da3.png) | ![64px illustration](images/c736e66423251efd701d7d.png) |

#### Title and description

The select cards contain a mandatory title and an optional description, that can be added to provide additional explanations.

---

| With description | Without description |
| --- | --- |
| ![With description](images/0f5bc62c25585fac11eddb.png) | ![Without description](images/0e410919cd0e97b7bf645e.png) |

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** Select cards support default, hover, and pressed states, and can be selected or unselected.
* **Disabled State Guidance:** Select cards support a disabled state and an error state; not documented further.

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/2ab570cdae4073b6baa74d.png) | ![Hover](images/a3747e13e1454030ab27db.png) | ![Pressed](images/484a6b1a6d095edd0d69d2.png) | ![Disabled](images/5e3b4e59318da5ed972a3f.png) |

| Default selected | Hover selected | Pressed selected | Disabled selected |
| --- | --- | --- | --- |
| ![Default selected](images/f70327cb19c4096f3fdf85.png) | ![Hover selected](images/2467c08180913667b51235.png) | ![Pressed selected](images/5cde9e887629a5a7043aa3.png) | ![Disabled selected](images/595ffef34872a5730e1084.png) |

#### Error

| Default | Hover | Pressed |
| --- | --- | --- |
| ![Default](images/46d79e1b90d38a8f100484.png) | ![Hover](images/0e1a65b5b0cd3b88c0b927.png) | ![Pressed](images/ab92d2f326f43a027119ac.png) |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
| ![Default selected](images/9cd5e0c1d72cbb7028db5b.png) | ![Hover selected](images/a9d14c26a6d0507281c9b1.png) | ![Pressed selected](images/4b947d9682d650e491d45b.png) |

#### Error message

| Select card group with error message |
| --- |
| ![Select card group with error message](images/5f8dc5954864a0fdb06b70.png) |

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* The title is mandatory, the description is optional. Both title and description can be multi-line.
* The **title** helps to structure the content. It's concise and has no punctuation.
* If you need to give additional guidance to the user, use the **description**.
* For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

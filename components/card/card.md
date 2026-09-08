<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831712331/Card | Last modified: Aug 17, 2026 -->

# Card

Cards are flexible containers used to visually group content.

![](images/8py3RJZZnPsqp4NWg8cD5Q.png)
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Card on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7306)
* [Card on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-card--docs)

---

## Usage

Cards are used to group related content and actions into a visually distinct, cohesive container. They help structure information and provide an organized layout.

### When to use

**Card** — visually grouping related content in a cohesive container.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Content should be collapsible | **Accordion** |
| Content overlays the screen | **Modal bottom sheet** |
| The whole container is a single navigational action | **Button card** |

### Variant Selection Flow

```
Background colour
└─ Four are available — choose by how much attention the card should draw

Radius
├─ Small card → 4px
├─ Medium card → 8px
└─ Large card → 16px

Padding
├─ Content must be separated from the card edge → 8px padding
└─ Wrapping clickable cell contents, which carry their own padding → No padding

Slots
└─ 1 to 5 content slots, used to structure what sits inside
```

### Usage Guidance

| DO |
| --- |
| ![](images/31c903cc435aed09c0276f.png) **DO:** Use cards to encapsulate related content or actions that belong together. You can add text, actions, icons, illustrations and images within cards. Place elements in a way that creates a clear hierarchy and is easy to scan. |
| ![](images/51d5299c88c8b000e83f3f.png) **DO:** Separate larger cards with a divider. |
| ![](images/0cde26c1018209be5a6da0.png) **DO:** Create clickable cards by placing the cell content component inside the card. |

| DON'T |
| --- |
| **DON'T:** Don't use cards for selection. Use select cards instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Card** | — | Cards are flexible containers used to visually group content. | — |
| [**Select card**](../select-card-group/select-card-group.md) | High | Use instead of Card when the container itself represents a selectable option | User needs to pick one or more options presented as cards |
| [**Cell content**](../cell-content/cell-content.md) | High | Place inside a Card to make the whole card clickable | Card acts as a clickable row or tile linking to another page |
| [**Accordion**](../accordion/accordion.md) | High | Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of information in a… | Content should be collapsible |
| [**Modal bottom sheet**](../modal-bottom-sheet/modal-bottom-sheet.md) | High | Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen. | Content overlays the screen |
| [**Button card**](../button-card/button-card.md) | High | Button cards are prominent calls to action that can be used alone or in a group, with icons or pictograms. | The whole container is a single navigational action |

---

## Variants & Modifiers

### Color

The card is available with 4 different background colors. Choose the color according to how much attention you want to draw to the card.

| DO |
| --- |
| ![](images/57aa0c258410f1dcb861ec.png) **DO:** Use different background colors to create visual hierarchy. |

### Radius

Cards are available with a radius of 4, 8 or 16px. Choose the radius according to the size of the card. The bigger the card, the bigger the radius should be.

### Padding

The card can be used with 8px padding or without padding. Choose the padding according to the content you want to put inside.

| DO |
| --- |
| ![](images/8d2a2a8042cd11a6898fd5.png) **DO:** Use the card with padding to separate content from the edge. |
| ![](images/c86bb98d81329fec8cfeab.png) **DO:** When you wrap clickable cell contents inside cards, no padding is needed because the cell contents already contain padding. This makes the entire card clickable. |

### Slots

The content placeholder in the card is available with 1 to 5 slots. You can use the slots as a helper to structure the content inside.

---

## Behavior & Responsiveness

### Interaction

Cards themselves are not clickable. If you want to create clickable cards, place a [cell content](https://zeroheight.com/626199550/p/27116a-cell-content) inside the card.

### Interactive States & Loading

Not documented

### Touch Target & Layout

* **Width Adaptability:** The width and height of the card are determined by its contents, with the card adapting to the elements inside.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

For general content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/v/latest/p/324518-intro). If you are using cell content within a card, please see the [cell content guidelines](https://zeroheight.com/626199550/p/27116a-cell-content/t/page-27116a-84054092-25).

---

## Accessibility (a11y)

Not documented

<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831450186/Segmented+control | Last modified: Aug 21, 2026 -->

# Segmented control

Segmented controls are used to select one option from a group of mutually exclusive choices. They are displayed as a horizontal row of buttons.

![](images/LUb7n7xTzybQHn85eZqO-A.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | To Do 🚧 | To Do 🚧 | To Do 🚧 |

[Segmented control on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=15480-471)

---

## Usage

Segmented controls are used to choose between mutually exclusive options. They can be used to make selections within a form, to switch views or filter content. They are similar to [tabs](https://zeroheight.com/626199550/p/45521d-tabs).

### When to use

**Segmented control** — switching between mutually exclusive view modes or display options — not a form value.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The choice is a form value | **Button group** |
| Switching full content sections | **Tabs** |
| Standard form styling needed | **Radio button group** |

### Variant Selection Flow

```
Icons
├─ Icon with label → Preferred, icon on the left
├─ Icon alone → Only when its meaning is unmistakable
└─ No icon → Label only
   └─ Never mix these combinations within one control

Badge
└─ Drawing attention to one segment → Badge next to the label
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/33af8808ceccd7985fb3d9.png) **DO:** Use segmented controls to allow users to choose between 2-5 options that are closely related and mutually exclusive. | ![](images/935b1814fa79a01e0f09ec.png) **DON'T:** Don't use segmented controls when there are more than 5-7 options. Use other selection components like dropdown or radio buttons instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Segmented control** | — | Segmented controls are horizontally arranged buttons that allow users to select one option from a group of mutually exclusive choices. They are often used to switch views or filter content within the same screen. There is always one option selected. | — |
| [**Tabs**](../tabs/tabs.md) | High | Tabs are navigational components used to switch between distinct content areas or views, typically at the page or section level. There is always one option selected. | Switching full content sections |
| [**Button group**](../button-group/button-group.md) | High | Button groups display multiple related choices in a horizontal row, allowing users to select one or more options. It's possible to have nothing selected. | The choice is a form value |
| [**Radio button group**](../radio-button-group/radio-button-group.md) | High | Radio button groups are used to select one option from a group of mutually exclusive choices. | Standard form styling needed |
| [**Toggle group**](../toggle-group/toggle-group.md) | Medium | Toggle groups are used to organize related options, allowing users to switch between multiple settings, with each toggle independently controlling… | Toggle group redirects here when: Switching between views rather than toggling settings |

---

## Variants & Modifiers

### Modifiers

#### Icons

Icons can be added as visual cues to provide clarity to the user. The icon is always to the left of the label.

| Icon only | Icon left | No icon |
| --- | --- | --- |
| ![](images/5e1eaefb301dae2b8feda6.png) | ![](images/15d4f13e2348822d547878.png) | ![](images/d1038a893a1c7511a9501e.png) |

| DO | DON'T |
| --- | --- |
| ![](images/33af8808ceccd7985fb3d9.png) **DO:** Combine icons with text for clarity. | ![](images/32eb0e2363d405b94eaaa4.png) **DON'T:** Avoid mixing different combinations. |

#### Badges

A badge can be placed next to the label.

![](images/9b517b810df1071efe9479.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

* The unselected buttons have the states default, hover, pressed and disabled. The selected buttons only have a default state.
* Segmented control components only support single-select. There is always one button selected per default.

![](images/3b5d2997c201321d4beb8d.png)

![](images/3b5d2997c201321d4beb8d.png)

### Touch Target & Layout

* **Width Adaptability:** The segmented control can either hug the content inside or fill a container.

| Hug content | Fill container |
| --- | --- |
| ![](images/15f19986cc53f35dd75023.png) | ![](images/5c8b74dd9b717b1e0fb49f.png) |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Start with a capital letter and do not use punctuation (nor colons).
* **Label Formula:** Noun form, of similar length across buttons.
* **Length Limits:** Keep button labels short and concise (1-3 words). Labels should be clear and descriptive.

For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831286379/Line+chart | Last modified: Aug 25, 2026 -->

# Line chart

Line charts are effective tools for showcasing trends in numerical data, especially continuous data over time, enabling quick analysis.

![](images/s3pZKPGI0xVBDZlbdExx_w.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | In progress 🚧 | To Do 🚧 | To Do 🚧 |

[Figma component](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=2782-14231&node-type=canvas&t=7DllDaSor798cNsl-11)

---

## Usage

They are particularly useful for tracking trends and making comparisons.

![](images/44acb82a7f708c0902c957.png)

### When to use

**Line chart** — showing how a value moves across a continuous axis, most often time.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Comparing discrete categories rather than following a trend | **Bar chart** |
| The point is each part's share of a whole | **Donut chart** |
| A single metric is more informative than a trend | **KPI** |

### Variant Selection Flow

```
Highlight
└─ A specific time frame needs emphasis, such as the impact of a campaign → Highlight that range

Dots
├─ Few data points, or accessibility for visual and cognitive needs → With dots
└─ A dense series where dots would clutter the line → Without dots
   └─ Dots are not required, but they carry a real accessibility benefit

Legend
├─ Two or more series → Mandatory
└─ A single series → Omit it; rely on the chart title and axis labels

Tooltip
└─ Hovering a line shows that point's value, alongside the other dataset's value
```

### Usage Guidance

| DO |
| --- |
| ![](images/e13345a24dc2f7166feb52.png) **DO:** Use a baseline different than 0 accordingly to your data. It is not required for a line chart to use a 0 baseline. The primary purpose of a line chart is to highlight value changes, not the actual values. |

| CAUTION |
| --- |
| ![](images/f9108e125c6b333b74c94e.png) **CAUTION:** Limit the number of lines to 4 or 5 to maintain clarity. Exceeding this limit may result in a confusing "spaghetti chart" with excessive line overlaps. |
| ![](images/a7b450b8545273bfb819b8.png) **CAUTION:** Be careful about the width/height ratio as it can affect how trends are perceived in line charts. A broader chart can create the impression of smoother trends, while a more compact chart emphasizes data fluctuations. It's important to consider how design choices impact the interpretation of the chart. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Line chart** | — | Show a trend over a continuous axis. | — |
| [**Bar chart**](bar-chart.md) | High | Compare quantities across categories. | A different question about the same data |
| [**Donut chart**](donut-chart.md) | High | Show a distribution across parts of a whole. | A different question about the same data |
| [**KPI**](../kpi/kpi.md) | High | A single measurable value shown prominently. | One metric is more informative than a trend |
| [**Legend**](legend.md) | Medium | Identifies which series each colour represents. | Two or more series are shown — then it is mandatory |

---

## Variants & Modifiers

### Variants

#### Highlight

![](images/ecb004bdf6e6f500216854.png)

You can emphasize a specific time frame on your graph (e.g., to illustrate the impact of booster packs consumed by an agent).

#### Dots

![](images/f039aca43c43515e05a6a8.png)

Dots are not required but this provide extra accessibility benefits for people with visual or cognitive accessibility needs.

### Modifiers

Not documented
---

## Behavior & Responsiveness

### Interactive States & Loading

**Tooltip on hover:** When hovering a line, you can display the value of this point and the other dataset value.

![](images/5d8126ac0729234df170ae.png)

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
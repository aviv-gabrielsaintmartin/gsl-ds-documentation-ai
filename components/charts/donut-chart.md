<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2830762135/Donut+chart | Last modified: Aug 25, 2026 -->

# Donut chart

A donut chart compares each group's contribution to a whole by dividing a circle into radial slices representing proportions.

![](images/eovAIWoZB8ToM9RwvuVsoQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| To Do 🚧 | To Do 🚧 | To Do 🚧 | To Do 🚧 |

---

## Usage

A donut chart represents the distribution of a total amount across categories of a variable by dividing a circle into radial slices.

### When to use

**Donut chart** — showing how a total divides into parts of a whole.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Comparing values across categories | **Bar chart** |
| Following a value over a continuous axis | **Line chart** |
| There is only one value to show | **KPI** |

### Variant Selection Flow

```
Segments
└─ Each segment is one part of the total; together they make the whole

Legend
├─ Two or more segments → Mandatory
└─ Only one value → A donut chart is the wrong choice; use KPI

No further variant axes are documented for this chart type.
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/68f4761dfc85d8ec856766.png) **DO:** Order your slices — start with the largest and move to the smallest, or follow a natural category order if one exists. | ![](images/33152149a8b6eb4eed8233.png) **DON'T:** Leave slices unordered — a logical order helps readers grasp the chart easily. |
| ![](images/68f4761dfc85d8ec856766.png) **DO:** Start slices from the top — it aligns with natural reading direction and the mental model of time progression on a clock face. | ![](images/16041511b6f6e61538fe20.png) **DON'T:** Start slices from an arbitrary position. |

| DO |
| --- |
| ![](images/9a2dc554fa2c8059bce79b.png) **DO:** If comparing groups is the focus, consider using a different chart type. |
| ![](images/28754847071a29bab88fc9.png) **DO:** Include percentage annotations in the graph or the legend — it's hard to determine precise proportions from a donut chart outside simple fractions like 1/2, 1/3, or 1/4. |
| ![](images/9c3d94d22a395014d4f893.png) **DO:** Include percentage annotations in the graph or the legend. |

| CAUTION |
| --- |
| ![](images/c27fd27a2391c675386d21.png) **CAUTION:** Use a donut chart to analyze each group's contribution to the whole rather than to compare groups directly — differentiating between slices can be challenging, even when sorted by size. |
| ![](images/6e83c6488571de49b2bc8b.png) **CAUTION:** Display only 5 categories or group small slices in neutral gray — charts with many slices are difficult to read, and using enough distinct colors can be challenging. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Donut chart** | — | Show a distribution across parts of a whole. | — |
| [**Bar chart**](bar-chart.md) | High | Compare quantities across categories. | A different question about the same data |
| [**Line chart**](line-chart.md) | High | Show a trend over a continuous axis. | A different question about the same data |
| [**KPI**](../kpi/kpi.md) | High | A single measurable value shown prominently. | There is only one value to show |
| [**Legend**](legend.md) | Medium | Identifies which segment each colour represents. | Two or more segments are shown — then it is mandatory |

---

## Variants & Modifiers

Not documented
---

## Behavior & Responsiveness

Not documented
---

## Content & UX Writing

Not documented
---

## Accessibility (a11y)

Not documented
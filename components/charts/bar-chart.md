<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832203896/Bar+chart | Last modified: Aug 25, 2026 -->

# Bar chart

A bar chart, or bar graph, shows numeric values as bars, with one axis for categories and the other for values. Each bar represents a category, with length indicating the value.

![](images/YnFGbHFdQBWSeuY7aX4G0g.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Not documented | To Do 🚧 | To Do 🚧 | To Do 🚧 |

---

## Usage

This chart aids in comparing values easily. It's great for data distribution and metric comparisons, making it easy to spot trends. Bar charts are widely used for various tasks.

### When to use

| Comparison | Ranking | Grouped |
| --- | --- | --- |
| ![](images/9b61438f4abe2f801a35a0.png) | ![](images/689009bc8ec67e8b715c33.png) | ![](images/80cc3f8f13b697ddc9259f.png) |

* **Comparison:** Bar charts are used to compare different categories, to show changes over time, usually against one metric.
* **Ranking:** Don't hesitate to arrange the bar order to rank items.
* **Grouped:** Grouped bar charts are handy for comparing multiple categories across different groups.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A trend over a continuous axis matters more than comparing categories | **Line chart** |
| The point is each part's share of a whole | **Donut chart** |
| A single metric is more informative than a comparison | **KPI** |
| Showing completion of one goal | **Progress bar** |

### Variant Selection Flow

```
Purpose
├─ Comparing values across categories → Comparison
├─ Ordering categories from highest to lowest → Ranking
└─ Comparing several series within each category → Grouped

Legend
├─ Two or more data categories → Mandatory
└─ A single data set → Omit it; rely on the chart title and axis labels

Tooltip
└─ Hover on desktop, tap on mobile, showing the selected bar's value
   └─ The user controls dismissal — moving the pointer away, or tapping outside
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/98be152baef82b53937760.png) **DO:** Use a 0 value baseline. The zero baseline simplifies comparison of bar lengths and ensures the accuracy of the data visualization. | ![](images/e3bdbc4ddab303cd19d5a3.png) **DON'T:** Use a non-zero baseline. It has the potential to mislead when comparing different groups, as bar lengths may not accurately reflect true values. |
| ![](images/732592e2c9663bb89403a5.png) **DO:** Use a horizontal layout when dealing with lengthy category labels, easing readability. | ![](images/f63aa880b63bc0131d76ca.png) **DON'T:** Use a vertical layout with lengthy category labels — it may cause label overlap, requiring rotation or shifting for readability. |
| ![](images/0757e30d2d40e5ef52a106.png) **DO:** Maintain the rectangular, slightly rounded bar shape at a 4px corner radius. This helps users understand the value of each bar easily and simplifies direct comparisons. | ![](images/97c9f2937b042f934a374a.png) **DON'T:** Change the radius of the rounded bar corner. |
| ![](images/-1Okf2N_kkXToCNFYRYMvQ.jpg) **DO:** If colors don't aid in understanding the graph or compete with the same value, stick with the default color for each bar. | ![](images/Wj1hkUAEbCI7Pg-iyE0UoQ.jpg) **DON'T:** Use different bar colors when competing against the same measure (e.g. K/€). Exceptions are only allowed when colors have a specific meaning (e.g. red for Se Loger, blue for Immonet, yellow for Immowelt). |

| CAUTION | DO |
| --- | --- |
| ![](images/bd966f107431fd4f01950f.png) **CAUTION:** When the number of categories is greater than seven, consider the amount of data displayed, especially on mobile devices — too much data can hinder users from easily scanning and understanding the information. | ![](images/9385e7dd144a4b193ad288.png) **DO:** Opt for the horizontal variant when categories exceed seven — it allows better visual organization and easier readability. |

| DO |
| --- |
| **DO:** Arrange the bar order to serve your message. If your objective is to rank different values, order them from the greatest value on the left to the lowest value on the right. |
| ![](images/MvGI9Dgli7g_4vfhnFIymQ.jpg) **DO:** Highlight data with color. Use the disabled color to reduce emphasis on less important parts, while sticking to the default color to emphasize critical information. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Bar chart** | — | Compare quantities across categories. | — |
| [**Line chart**](line-chart.md) | High | Show a trend over a continuous axis. | A different question about the same data |
| [**Donut chart**](donut-chart.md) | High | Show a distribution across parts of a whole. | A different question about the same data |
| [**KPI**](../kpi/kpi.md) | High | A single measurable value shown prominently. | One metric is more informative than a comparison |
| [**Legend**](legend.md) | Medium | Identifies which series each colour represents. | Two or more data categories are shown — then it is mandatory |

---

## Variants & Modifiers

Not documented
---

## Behavior & Responsiveness

### Interactive States & Loading

* **Tooltip:** When hovering over a bar with the pointer on desktop, or touching it on mobile, a tooltip appears showing the value of the selected item.
* **Dismissal:** Users should be able to control when tooltips disappear, by moving the mouse away or clicking outside the tooltip.
* **Position:** The position is automated.

![](images/7b5d817c5ff2dacc03de95.png)

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
<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831122547/Filters+and+actions | Last modified: Aug 25, 2026 -->

# Filters and actions

You can change the data displayed using filters or/and an interactive legend.

Not documented

---

## Usage

Not documented

### When to use

**Filters and actions** — letting the user narrow, or act on, the data a chart displays.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Filtering a SERP or a data table rather than a chart | **Filter bar** |
| Setting a single value inside a form | **Dropdown** |
| Triggering a list of contextual actions | **Action menu** |

### Variant Selection Flow

```
Filter control
├─ Five options or fewer → Chip
└─ More than five options → Dropdown
   └─ Any other component used as a filter must be validated by user testing first, and the findings shared

Position
├─ Default → Above the graph
├─ Space allows → Beside the graph title
└─ Space is tight → Below the graph title
   └─ Placing filters below the graph itself needs user-testing evidence first
```

### Usage Guidance

Not documented

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Filters and actions** | — | Narrow or act on the data a chart displays. | — |
| [**Filter bar**](../filter-bar/filter-bar.md) | High | Filter bars narrow search results or table content using structured criteria. | Filtering a SERP or data table, not a chart |
| [**Chip group**](../chip-group/chip-group.md) | High | Collections of chips for filtering or selecting multiple related options. | Five filter options or fewer |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | More than five filter options |
| [**Action menu**](../action-menu/action-menu.md) | Medium | Action menus display context-specific actions in a dropdown list. | Triggering actions rather than setting filter criteria |

---

## Variants & Modifiers

### Type

If you use other components as filters and confirm it works with user testing, we kindly ask you to share your findings with us.

| Chip | Dropdown |
| --- | --- |
| ![](images/5b800373949d91fa1fb6d5.png) Works better with 5 options or less | ![](images/e9d984921e565e109fac48.png) Use it if you have more than 5 options available |

### Position

Filters should be displayed above the graph. Depending on the space available, they can be next or below the graph title.

If you encounter a use case where the filters position make more sense below and is proving working by user test, please share it with us.

| Right | Below |
| --- | --- |
| ![](images/e1866ab134b4b2e0db8f5b.png) | ![](images/8da7320a136489287bd484.png) |

| DO |
| --- |
| ![](images/6beedc1c11ebc4a322bd5e.png) **DO:** For mobile devices or in situations with limited screen space, we recommend displaying the filters in a modal bottom sheet. These filters can be accessed by clicking on a designated filter button. Use the close icon on the top left to cancel and the primary button to validate the changes. |

| DON'T |
| --- |
| ![](images/e4b766635f53137d38858e.png) **DON'T:** When space is limited, it's important not to conceal the filters, as this could diminish their visibility and ease of access. |

| CAUTION |
| --- |
| ![](images/c79ae21f48a79c344f9979.png) **CAUTION:** Displaying filters stacked on top of each other on small screens can diminish usability and overwhelm users. |

### Modifiers

#### Legend

You can filter the data using the legend when interactive.

To show/hide data sets, some design systems (e.g. [Carbon](https://carbondesignsystem.com/data-visualization/legends/#:~:text=about%20geospatial%20legends.-,Interactions,-Hover%20to%20highlight)) and frameworks (e.g. [HighChart.js](https://www.highcharts.com/demo/highcharts/bar-chart) or [Chart.js](https://www.chartjs.org/docs/latest/samples/bar/horizontal.html)) use the legend as a clickable element, acting like a checkbox.

Usually, there is no clear indication the legend is clickable leading in our opinion to discoverability issues.

We can expect our users to learn how to show/hide data with a product they'll need to reuse recurrently like a dashboard on a B2B product.

On a B2C product, the need to show/hide data sets should occur less often but we can't expect our user to understand the features without any indications, that's why we added a checkbox.

#### Other actions

You can include all the complementary actions you need depending on your use case.

This action menu is mandatory and should at least include the color-blind mode (on the web) and the table format. [Know more about accessibility](https://zeroheight.com/626199550/p/025089-accessibility)

![](images/cf7233283abd42aea22eb0.png)

---

## Behavior & Responsiveness

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3492184533/Tables | Last modified: Aug 25, 2026 -->

# Tables

Tables are used to organize and display all information from a data set. Display, organize, and sort data for users to analyze and take action on.

![](images/0rDon-JZve3x_5TApwfbyA.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | In progress 🚧 | To do 🚧 | To do 🚧 |

* [Tables in Figma](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?m=auto&node-id=7816-62373&t=NvnSmro4NrlL31fg-1)

---

## Usage

Table component is essential for displaying large volumes of structured information in an organized, grid-like format, making it ideal for use cases where users need to compare, sort, and analyze data efficiently. It is best suited for scenarios involving datasets with multiple attributes, where clarity and accessibility are paramount. Utilize this component when you need to present data in a way that empowers users to derive insights quickly and make informed decisions based on comprehensive, easy-to-navigate information.

### Anatomy

There are a few types of Tables, but the primary elements that constitute the Table component are as follows:

![](images/x_TXX02RB_7Va9U24CIHcg.svg)

| Sub-component | Enable/Disable capability | Padding |
| --- | --- | --- |
| Header row | Yes | Left, Right: 12px, 16px, 20px |
| Header cell | Yes | Left, Right: 12px, 16px, 20px |
| Sorting button | Yes | N/A |
| Additional info button | Yes | N/A |
| Table row | N/A | Top, Down, Left, Right: 12px, 16px, 20px |
| Table cell | Yes | Left, Right: 12px, 16px, 20px |
| Footer | Yes | Left, Right: 0px, 16px |
| Footer Legend | Yes | N/A |
| Pagination | Yes | N/A |

### Padding options

The set of spacing available for this component is limited as we've documented in the Anatomy of the component. You can combine a set of 12, 16 and 20px spacing units. Just make sure the spacing is balanced and consistent throughout the table.

#### Example

![](images/eAbmr7WRmMrO-ogUco5GA.png)
12px gap between cells in the Header

![](images/MjDQBLJbpu0aOhJxEgSGHQ.png)
12px gap between fixed cells and the rest

![](images/w22S4PTrN3brsXl7LLTxcg.png)
12px gap between cells and 16px padding top and bottom of the row

![](images/thHqALE35ga2w6LlJV1oTQ.png)
Other padding can be used within the cell content. E.g.: 8px

### When to use

**Tables** — organising and displaying a data set in rows and columns for users to scan, sort and act on.

**Experience**-tier component. **Highest tier first**: do not compose a data grid from Cell content rows — this component already is it.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Grouping content visually rather than tabulating a data set | **Card** |
| Summarising one property rather than comparing many rows | **Listing card** |
| Narrowing which rows are shown | **Filter bar** |

### Variant Selection Flow

```
Device
├─ Desktop → Desktop version
└─ Phone or tablet → Mobile version
   ├─ Row data reads across → Horizontally distributed
   ├─ Row data reads down → Stacked
   └─ Maximising screen space → Full-width, "unboxed"
      └─ If there is a footer, align it to the full-width table too

Selectable rows
└─ Users must act on rows individually or in bulk → Selectable rows
   ├─ Applied to every row by default
   └─ The header must carry a checkbox to select and unselect all

Expandable rows
├─ Rows reveal a larger panel of contextual data → Expandable rows
│  └─ Desktop only — the interaction is not available on mobile
└─ Apply to all rows; mixing expandable and fixed rows needs an explicit cue

Horizontal scroll
└─ Very wide data sets with many columns → Horizontal scroll, with edge shadows showing the overflow
   └─ Never combine horizontal scroll with the stacked row view
```

### Usage Guidance

* **Left-align text columns:** Everything that's made up of letters should be left-aligned.
* **Match heading alignment to column:** Column headers should always align according to their column content. Not following this rule creates off putting whitespaces and brings in unnecessary visual noise.
* **Avoid using center alignment:** Using the right alignment for the right type of content is key for enhancing the user's readability, mental calculations and comparisons between rows. Center alignment prevents quick scanning and noticing irregularities and ultimately makes the eye jump around unnecessarily.
* **Avoid duplication:** When possible, avoid repeating the title in every cell of a given column. For example, you can omit repeating the word "lead" in every cell like "Qualified Lead" or "Nurturing Lead". Placing the word "Lead" in the heading and just using qualifiers in the rows will help reduce visual noise.
* **Right-align numeric columns when standalone:** When numbers are the only value within a column, unlike text, numerical values are much easier to compare and contrast when they're right-aligned. The goal is to align numbers according to the position of the decimal.
* **Vertical alignment:** Use vertical center-align for when the row height varies only slightly (up to 3 lines). If row height varies more than 3 or 4 lines, using top-alignment makes most sense in terms of legibility and ensuring everything is visible.

Follow our Gemini content guidelines for [numbers](https://zeroheight.com/626199550/p/60fe5b), [dates](https://zeroheight.com/626199550/p/06ce3b-date-and-time) and [capitalization](https://zeroheight.com/626199550/p/437aef-capitalization).

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Tables** | — | Tables are used to organize and display all information from a data set. | — |
| [**Cell content**](../cell-content/cell-content.md) | Medium | Cell contents are building blocks used to create elements such as lists or button cards. | Composed inside Tables — never selected on its own, see **Never select** |
| [**Card**](../card/card.md) | Medium | Cards are flexible containers used to visually group content. | Grouping content visually rather than tabulating a data set |
| [**Listing card**](../listing-card/listing-card.md) | Low | Listing cards are actionable cards that summarize the details of a property listing. | Summarising one property rather than comparing many rows |

---

## Variants & Modifiers

Table variants are either Device or Feature driven so it adapts to different use cases:
* **Device:** Desktop, Phone/Tablet
* **Selectable rows:** Functionality to enable rows that can be selected individually or in bulk from the Header
* **Expandable rows:** Functionality to enable rows that can be expanded thanks to a button so it displays a bigger panel with more contextual data
* **Horizontal scroll:** Functionality to enable data sets within columns to overflow the Table container and scroll horizontally
* **Full width (Phone/Tablet only):** Reserved for Phone and Tablet devices — to maximize screen real estate the Table component gets "unboxed" so it can be expanded to the full width of the screen

### Device

![](images/LCyx8QoOEJo84AhKjvceFw.svg)
There is a Desktop and a Phone/Tablet version of the Table

Tables for mobile devices have two ways of presenting the data within the rows:

| Horizontally distributed | Stacked |
| --- | --- |
| ![](images/YsTHgKXfLGgIAn8KlxOBA.svg) | ![](images/YAX7hq_q0zPg8HA11Blw_g.svg) |

But also can be aligned to the full-width of the device, making the most out of the available space:

| Horizontally distributed full-width | Stacked full-width |
| --- | --- |
| ![](images/Ko7MrVP0vUzFplLvk0dYWw.svg) | ![](images/iL9WsgLnWGLglDKXGB4akw.svg) |

#### Phone / Tablet Guidelines

| DO |
| --- |
| ![](images/z6WxrwdMcw81a5uXENrLiA.svg) **DO:** Tables can have the same appearance as on Desktop devices, having a boxed Table as one of our Phone/Tablet views. |
| ![](images/sNoWD8iXsHahxbzAx6pd-A.svg) **DO:** To make the most out of the space on the screen, mobile device Tables can be aligned to the full-width of the screen. |
| ![](images/DL4tHZM-ssxZjIoJ1zv1sA.svg) **DO:** As normally the content of the tables won't fit in smaller devices, besides scrolling horizontally to display more data, optionally you can stack the content of a whole row vertically. |
| ![](images/t1P5ejGTOdXxzhhNR5f4Qg.svg) **DO:** Also expand the Table to the full-width for better readability. |
| ![](images/su0Rj0qwmtdABVm2k6SQ3w.svg) **DO:** When using the full-width Table for mobile devices, make sure that in case you have the footer, you must have the padded version. |

| DON'T |
| --- |
| ![](images/uE7cn0yV1LhypVQoQtd8KA.svg) **DON'T:** You can't combine the stacked row view with the horizontal scroll. |

### Selectable rows

To facilitate the selection of rows you can implement the selectable rows variant.

![](images/4HKNkmiTi3gb44DcynCmVw.svg)

| DO | DON'T |
| --- | --- |
| ![](images/JUZB0o0rpovcH3tRVx-QVQ.svg) **DO:** When adding the functionality of selecting rows in a table, it is implemented to all rows by default. | ![](images/PQl3n-tPGrD6cSr1NxESfQ.svg) **DON'T:** The Header of the table should have a Checkbox to facilitate selecting/unselecting all rows — don't randomize the functionality of selecting rows in a table, without context users won't be able to understand why some rows can be selected and others don't. |

### Expandable row

You might need rows that can expand in order to show and hide contextual data. For this purpose you can use the Expandable row variant, which is NOT available for mobile Tables as the interaction of this type of row might be difficult to interact with on smaller devices.

![](images/8WFVpkT8Y_IQQpCJ-0Nxcg.svg)

| DO |
| --- |
| ![](images/jeFGkJ8iH5Eu_ep8kG1GJQ.svg) **DO:** When adding expandable rows, try to have the same functionality for all rows. |

| CAUTION |
| --- |
| ![](images/QNqurQigj-HxhivAPpFVoQ.svg) **CAUTION:** Without context, users might not know why some rows can't be expanded. Only mix the functionality when you know why. |

### Horizontal scroll

For very complex data sets that need a large number of columns to display, this variant allows the content of the rows to overflow the container — a shadow on the edges appears to depict the overflowing content.

![](images/nGDgvL10dPWjIHJO1KY8vg.svg)

| DO |
| --- |
| ![](images/-QbNkckaNr8U8Qq8W0L8Cw.svg) **DO:** When the content of the Table can't be fitted inside the Table container, enable "horizontal scroll" — a shadow will appear to help the user notice there's more content underneath. |

### Modifiers

#### Sorting

Sorting helps users order the data on the Table based on that column's values, from highest to lowest or from lowest to highest. Clicking the sorting button first sorts highest to lowest, clicking again sorts lowest to highest, and clicking a third time returns to the default sorting. This functionality and the icon that enables it can be disabled and hidden.

![](images/QgXzBbW0TZkeMMzC42P78w.svg)
Sorting and info features enabled

![](images/RH1YSbCH6xggYF_fzhAV8Q.svg)
Sorting icon changes depending on the sorting direction

#### Info

The info icon gives contextual information about the data visible in that column. Just like any other info icon across the product, on hover or tap (mobile) it displays a tooltip with additional information. This functionality and the icon that enables it can be disabled and hidden.

![](images/-PWgOzQj0I6MjaLVoiM8Ww.svg)
Activating the info icon displays a tooltip

![](images/Um3pirW3epFwOHWrOyUEog.svg)
Both features can be disabled

#### Header placement

| DO | DON'T |
| --- | --- |
| ![](images/bFGoywFVfrZHBZwHwcf3-Q.svg) **DO:** Keep the Header at the top of the Table. | ![](images/nkLvZ_mljPASg1oisdPVeg.svg) **DON'T:** Don't place the Header in between rows. |

| CAUTION |
| --- |
| ![](images/46DJ-PfFn9jeJ1W2BJkfJA.svg) **CAUTION:** Alternatively you can have a Table without a Header. Use it carefully — Tables without a header are reserved for simple tables where each column's data point can be understood by the user without context. |

---

## Behavior & Responsiveness

### Interactive States & Loading

#### Loading

When a Table component takes some time to load its content, you can display a skeleton depicting the type of content the user will encounter, keeping the column amount and row amount. If the Headers can be displayed in advance, there's no need for a skeleton on the header of the Table.

![](images/zBCgT8-TwjjRublJ_4cqlA.svg)
When the Table data is loading it will display a skeleton

#### Hover and Selected

Table rows can be selected independently and in bulk, so Table rows have different states to depict that interactivity. On Default state, Table rows use the `color-surface-default-default` color token.

![](images/qIdgm-bbuFsMswGvTO1wg.svg)
Hover state rows use the `color-surface-default-hover` color token

![](images/ZEHr3nSLFHRS61EKGGCW6g.svg)
Selected state rows use the `color-surface-default-pressed` color token

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

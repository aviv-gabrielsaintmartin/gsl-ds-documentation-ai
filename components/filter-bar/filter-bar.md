Filter bars are used to narrow down search results or displayed content based on selected criteria.

![](images/xZ1WvNc74cFYoOJVLSaUGg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | N/A | N/A | N/A |

Figma only (owned by SERP team).
* [Filter bar on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?m=auto&node-id=2240-119052&t=44YLeVrnPbcXxr0R-1)

---

## Usage

The filter bar allows users to set criteria to narrow down displayed content on a search results page or in a table. It consists of filter buttons that refine the results based on the user's selected criteria.

### When to use

**Filter bar** — narrowing search results or table content using structured criteria — SERP or data page.

**Pattern**-tier component. **Highest tier first**: do not compose a filter row from Chips or Buttons — this component already is it.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Lightweight inline filters without dropdown panels | **Chip group** |
| A single filter criterion inside a form | **Dropdown** |
| Triggering filter-related actions rather than setting criteria | **Action menu** |

### Variant Selection Flow

```
Size
├─ Default, or a dense layout → 40px
└─ Roomier layout, or matching 48px controls beside it → 48px
```

### Usage Guidance

Not documented

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Filter bar** | — | Filter bars are used to narrow down search results or displayed content based on selected criteria. | — |
| [**Chip group**](../chip-group/chip-group.md) | High | Chip groups are collections of chips that allow users to filter, select, or manage multiple related options simultaneously. | Lightweight inline filters without dropdown panels |
| [**Dropdown**](../dropdown/dropdown.md) | High | Dropdowns are used to select one option from a list. | A single filter criterion inside a form |
| [**Action menu**](../action-menu/action-menu.md) | High | Action menus display context-specific actions in a dropdown list. | Triggering filter-related actions rather than setting criteria |

---

## Variants & Modifiers

### Size

The filter bar is available with a height of 40 and 48px.

| 40px | 48px |
| --- | --- |
| ![40px](images/ef64cd158a9107bc1ae30e.png) | ![48px](images/4fb33b409efbe92b150592.png) |

### Modifiers

Not documented

---

#### Show/hide filters button (desktop only)

All the filters button can be shown or hidden.

| All filters visible | Hidden filters |
| --- | --- |
| ![All filters visible](images/47f4b46654d668fe4a24d1.png) | ![Hidden filters](images/e72a01c262bf3ecefe9e14.png) |

#### Show/hide primary button

Since the primary button is not a validation button, it is optional and can be hidden.

| With primary button | Without primary button |
| --- | --- |
| ![With primary button](images/47f4b46654d668fe4a24d1.png) | ![Without primary button](images/b16bcb11512bcc371eb3c0.png) |

## Behavior & Responsiveness

### Interactive States & Loading

When the user click on a filter button either a dropdown or a modal opens. The dropdown/modal closes when the user click outside or on a submit button.

| Dropdown panel | Modal Bottom Sheet |
| --- | --- |
| ![Dropdown panel](images/3ddb5ba4b1cf0a905efd00.png) | ![Modal Bottom Sheet](images/41df3408fbf6071b6c7c59.png) |

| DO |
| --- |
| ![DO](images/5d156ef0bfba10639e4ad6.png)<br>**DO:** When using the dropdown panel, align it to the right or left edge of the filter button. |

| CAUTION |
| --- |
| ![CAUTION](images/8ef5ba5749529b52f69cb2.png)<br>**CAUTION:** It's possible to combine the filter bar with a modal, but it should be checked how it affects the usability. For a seamless flow, the dropdown panel is often the better choice. |

#### Breakpoints and width

To learn more about our breakpoints, see our grids and breakpoint guidelines.

| Desktop | Tablet | Mobile 1 | Mobile 2 |
| --- | --- | --- | --- |
| ![Desktop](images/4fb33b409efbe92b150592.png) | ![Tablet](images/0d74b8cd557fcf81392526.png) | ![Mobile 1](images/ebf3eac4d97ed0fab99c33.png) | ![Mobile 2](images/a2d1fb807e992597dfe27c.png) |

### Touch Target & Layout

| 40px | 48px |
| --- | --- |
| ![40px](images/ef64cd158a9107bc1ae30e.png) | ![48px](images/4fb33b409efbe92b150592.png) |

#### Filter button types

There are three types of filter buttons, each offering a different user interaction:

| Opens Modal | Opens dropdown | Boolean |
| --- | --- | --- |
| ![Opens Modal](images/341e30e19ac6c559ca401a.png) | ![Opens dropdown](images/bf0784e7ed7770bf69cebe.png) | ![Boolean](images/5f30f2634356d44230cebf.png) |

| DO |
| --- |
| ![DO](images/A2fbNou0uwRx0RM4j4uVGQ.png)<br>**DO:** Place all of the dropdown filter buttons together. |
| ![DO](images/hwpmAtR1o0BmBo2CS-_eqg.png)<br>**DO:** Place all boolean filter buttons together, even if they exist next to another type of filter button. |

| CAUTION |
| --- |
| ![CAUTION](images/y0NM8-VnVlVHsHt9FJEbpA.png)<br>**CAUTION:** Try not to mix alternating boolean filter buttons with dropdown filter buttons, as this can cause confusion. |
| ![CAUTION](images/ASjo4dk27AQfwka6x2xImg.png)<br>**CAUTION:** Try not to mix alternating boolean filter buttons with open modal filter buttons, as this may cause confusion. |

#### Filter number counter

Optionally an open modal filter button can display a counter with the number of filter applied.

* In the filter bar, in the filter button clicked on step 1, the badge is shown with the amount of filters selected.

* In the filter bar, in the "More" button, the badge is shown with the total amount of filters selected in all the filters.

![](images/9b4306ff1b9e4b7cf8a730.png)

### Breakpoints & Platform Adaptations

The appearance of the filter bar changes depending on the breakpoint. To learn more about our breakpoints, see our grids and breakpoints guidelines.

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Desktop** | ![](images/4fb33b409efbe92b150592.png) Web: XL - XXXL (> 1279 px) |
| **Tablet** |  Web: SM - LG (600 - 1279 px) |
| **Mobile 1** |  Web: XXS - XS (0 - 599 px) |
| **Mobile 2** | ![](images/47f4b46654d668fe4a24d1.png) Web: XXS - XS (0 - 599 px) |

We don't recommend stretching the filter bar over the entire width on desktop as this can cause usability issues.

---

## Content & UX Writing

Filter buttons should be clear and concise. Our users should be able to anticipate what will happen when they click the button. Use consistent terminology and structure across all filters. If one label reads "Price Range," another should not read "Select Area," but rather "Location."

* Use sentence case without punctuation.
* Try to keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented

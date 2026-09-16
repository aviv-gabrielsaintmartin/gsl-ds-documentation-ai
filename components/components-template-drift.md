<!-- GENERATED FILE — do not edit by hand. Re-run: python3 components/template-drift.py -->

# Template drift

_How far each component doc sits from
[component-template.md](component-template.md), and what would close the
gap. **Written by a script** — re-run it and the numbers move. Never edit
this page._

---

## Why this page exists and the coverage ledger does not cover it

[components-coverage-ledger.md](components-coverage-ledger.md) measures what
is **filled in**. It looks for the template's own headings and reports which
carry content.

It cannot see a heading the template never defined. A doc can put half its
content under sections that do not exist and still score well there. This
page is the other half of the question.

---

## Where things stand

| | Count |
| --- | --- |
| Component docs measured | **57** |
| — already match the template | **8** |
| — need something changed | **49** |
| Chart support pages, listed apart | 5 |
| Headings the template does not define | **115**, under 74 distinct names |
| Template sections absent from a page | **66** |
| Sections at the wrong heading level | **0** |
| Sections out of template order | **0** |
| Pages with no readiness table | **3** |

---

## The three fixes, and how much of the drift each one clears

Every off-template heading found so far falls into one of these. None has
ever needed a fourth.

| The fix | Headings | What it is |
| --- | --- | --- |
| **One level down** | 75 | The heading names an axis of the component — `Size`, `Type`, `Alignment`, `Dots`. An axis is not a section. Its content is right; only its level is wrong. **Mechanical** |
| **Rename and merge** | 38 | The heading is a template section under another word — `Interaction` for states, `Scrolling` for layout. **Not mechanical:** both headings can hold content, and merging them is a judgement |
| **Move out of the sections** | 2 | The heading is a list of links to other pages. Links belong under the title, above the first `##` |

**`Anatomy` is not a section, and will not become one.** Decided 16 Sep 2026:
a component's elements can be shown or hidden, and often cannot all appear
at once, so a picture of every part at once misleads. What those sections
really hold — which sub-components exist, and what each can be set to — is
**Modifiers**.

---

## What each doc needs

Ordered by how much. `—` means nothing to do in that column.

| Doc | Extra headings | Missing sections | What to do |
| --- | --- | --- | --- |
| [coach-mark/coach-mark.md](coach-mark/coach-mark.md) | `Boolean`, `Tag position`, `Position`, `Interaction`, `Scroll`, `Animation` | Modifiers | `Boolean`, `Tag position`, `Position` → one level down, under the section above it; `Interaction`, `Animation` → rename to **Interactive States & Loading** and merge; `Scroll` → rename to **Touch Target & Layout** and merge |
| [tables/tables.md](tables/tables.md) | `Anatomy`, `Padding options`, `Device`, `Selectable rows`, `Expandable row`, `Horizontal scroll` | — | `Anatomy` → rename to **Modifiers** and merge; `Padding options`, `Selectable rows`, `Expandable row` → one level down, under the section above it; `Device` → rename to **Breakpoints & Platform Adaptations** and merge; `Horizontal scroll` → rename to **Touch Target & Layout** and merge |
| [avatar/avatar.md](avatar/avatar.md) | `Shapes and sizes`, `No padding`, `No border`, `Icons and initials`, `Rectangular, adaptive avatar` | Modifiers | `Shapes and sizes`, `No padding`, `No border`, `Icons and initials`, `Rectangular, adaptive avatar` → one level down, under the section above it |
| [card/card.md](card/card.md) | `Color`, `Radius`, `Padding`, `Slots`, `Interaction` | Modifiers | `Color`, `Radius`, `Padding`, `Slots` → one level down, under the section above it; `Interaction` → rename to **Interactive States & Loading** and merge |
| [carousel/carousel.md](carousel/carousel.md) | `Arrow position`, `Dots`, `Clipped content`, `Interaction`, `Carousel Items` | — | `Arrow position`, `Dots`, `Carousel Items` → one level down, under the section above it; `Clipped content` → rename to **Touch Target & Layout** and merge; `Interaction` → rename to **Interactive States & Loading** and merge |
| [navigation-bar/navigation-bar.md](navigation-bar/navigation-bar.md) | `Opening menu`, `Icon tooltip`, `Language menu`, `Arrows` | Interactive States & Loading, Touch Target & Layout | `Opening menu`, `Icon tooltip`, `Language menu`, `Arrows` → one level down, under the section above it |
| [rating/rating.md](rating/rating.md) | `Size`, `Condensed display`, `Scale`, `Rating results`, `Reviews` | — | `Size`, `Condensed display`, `Rating results`, `Reviews` → one level down, under the section above it; `Scale` → rename to **Touch Target & Layout** and merge |
| [phone-number-field/phone-number-field.md](phone-number-field/phone-number-field.md) | `Overflow Content` | Variants & Modifiers, Modifiers, Behavior & Responsiveness, Interactive States & Loading, Touch Target & Layout | `Overflow Content` → rename to **Touch Target & Layout** and merge; **no readiness table** |
| [progress-bar/progress-bar.md](progress-bar/progress-bar.md) | `Styles`, `Size`, `Width`, `Labels` | — | `Styles`, `Size` → one level down, under the section above it; `Width` → rename to **Touch Target & Layout** and merge; `Labels` → rename to **Content & UX Writing** and merge |
| [button/button.md](button/button.md) | `Emphasis`, `Size`, `Context` | — | `Emphasis`, `Size`, `Context` → one level down, under the section above it |
| [cell-content/cell-content.md](cell-content/cell-content.md) | `Alignment`, `Padding`, `Interaction` | — | `Alignment`, `Padding` → one level down, under the section above it; `Interaction` → rename to **Interactive States & Loading** and merge |
| [checkbox/checkbox.md](checkbox/checkbox.md) | `Border`, `Label`, `Interaction` | — | `Border` → one level down, under the section above it; `Label` → rename to **Content & UX Writing** and merge; `Interaction` → rename to **Interactive States & Loading** and merge |
| [floor-selection/floor-selection.md](floor-selection/floor-selection.md) | `Digit`, `Labels`, `Helper text` | — | `Digit`, `Labels`, `Helper text` → rename to **Content & UX Writing** and merge |
| [kpi/kpi.md](kpi/kpi.md) | `Anatomy`, `Layout`, `Display Context` | — | `Anatomy` → rename to **Modifiers** and merge; `Layout`, `Display Context` → one level down, under the section above it |
| [link/link.md](link/link.md) | `Type`, `Size`, `Context` | — | `Type`, `Size`, `Context` → one level down, under the section above it |
| [progress-circle/progress-circle.md](progress-circle/progress-circle.md) | `Styles`, `Size`, `Labels` | — | `Styles`, `Size` → one level down, under the section above it; `Labels` → rename to **Content & UX Writing** and merge |
| [radio-button-group/radio-button-group.md](radio-button-group/radio-button-group.md) | `Alignment`, `Main elements`, `Overflow content` | — | `Alignment` → one level down, under the section above it; `Main elements` → rename to **Content & UX Writing** and merge; `Overflow content` → rename to **Touch Target & Layout** and merge |
| [select-card-group/select-card-group.md](select-card-group/select-card-group.md) | `Group`, `Type`, `Alignment` | — | `Group`, `Type`, `Alignment` → one level down, under the section above it |
| [top-bar/top-bar.md](top-bar/top-bar.md) | `Size`, `Style`, `Scrolling` | — | `Size`, `Style` → one level down, under the section above it; `Scrolling` → rename to **Touch Target & Layout** and merge |
| [modal-bottom-sheet/modal-bottom-sheet.md](modal-bottom-sheet/modal-bottom-sheet.md) | `Scrolling` | Variants & Modifiers, Modifiers, Behavior & Responsiveness | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [button-group/button-group.md](button-group/button-group.md) | `Number of items`, `Interaction` | — | `Number of items` → one level down, under the section above it; `Interaction` → rename to **Interactive States & Loading** and merge |
| [charts/donut-chart.md](charts/donut-chart.md) | — | Modifiers, Interactive States & Loading, Touch Target & Layout, Breakpoints & Platform Adaptations | — |
| [checkbox-group/checkbox-group.md](checkbox-group/checkbox-group.md) | `Alignment`, `Interaction` | — | `Alignment` → one level down, under the section above it; `Interaction` → rename to **Interactive States & Loading** and merge |
| [date-picker/date-picker.md](date-picker/date-picker.md) | — | Touch Target & Layout, Breakpoints & Platform Adaptations | **no readiness table** |
| [dropdown/dropdown.md](dropdown/dropdown.md) | `Interaction`, `Position & Scrolling` | — | `Interaction` → rename to **Interactive States & Loading** and merge; `Position & Scrolling` → rename to **Touch Target & Layout** and merge |
| [feedback-message/feedback-message.md](feedback-message/feedback-message.md) | `Type`, `Floating and corner radius` | — | `Type`, `Floating and corner radius` → one level down, under the section above it |
| [floating-button-group/floating-button-group.md](floating-button-group/floating-button-group.md) | `Buttons`, `Alignment` | — | `Buttons`, `Alignment` → one level down, under the section above it |
| [listing-card/listing-card.md](listing-card/listing-card.md) | `Layout`, `S Carousel` | — | `Layout`, `S Carousel` → one level down, under the section above it |
| [snackbar/snackbar.md](snackbar/snackbar.md) | `Type`, `Actions` | — | `Type`, `Actions` → one level down, under the section above it |
| [tabs/tabs.md](tabs/tabs.md) | `Number of items` | — | `Number of items` → one level down, under the section above it; **no readiness table** |
| [text-area/text-area.md](text-area/text-area.md) | `Main elements`, `Overflow content` | — | `Main elements` → rename to **Content & UX Writing** and merge; `Overflow content` → rename to **Touch Target & Layout** and merge |
| [divider/divider.md](divider/divider.md) | `Orientation` | Modifiers | `Orientation` → one level down, under the section above it |
| [modal-bottom-sheet-menu/modal-bottom-sheet-menu.md](modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) | `Scrolling` | Touch Target & Layout | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [accordion/accordion.md](accordion/accordion.md) | `Border` | — | `Border` → one level down, under the section above it |
| [action-menu/action-menu.md](action-menu/action-menu.md) | `Scrolling` | — | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [button-card/button-card.md](button-card/button-card.md) | `Alignment` | — | `Alignment` → one level down, under the section above it |
| [charts/line-chart.md](charts/line-chart.md) | `Variants` | — | `Variants` → rename to **Variants & Modifiers** and merge |
| [chip-group/chip-group.md](chip-group/chip-group.md) | `Type` | — | `Type` → one level down, under the section above it |
| [chip/chip.md](chip/chip.md) | `Type` | — | `Type` → one level down, under the section above it |
| [counter-field/counter-field.md](counter-field/counter-field.md) | `Interaction` | — | `Interaction` → rename to **Interactive States & Loading** and merge |
| [energy-tag/energy-tag.md](energy-tag/energy-tag.md) | `Country` | — | `Country` → rename to **Content & UX Writing** and merge |
| [filter-bar/filter-bar.md](filter-bar/filter-bar.md) | `Size` | — | `Size` → one level down, under the section above it |
| [listing-summary/listing-summary.md](listing-summary/listing-summary.md) | `Anatomy` | — | `Anatomy` → rename to **Modifiers** and merge |
| [tag/tag.md](tag/tag.md) | `Context / Style` | — | `Context / Style` → one level down, under the section above it |
| [toggle/toggle.md](toggle/toggle.md) | `Toggle position` | — | `Toggle position` → one level down, under the section above it |
| [wizard/wizard.md](wizard/wizard.md) | `List type` | — | `List type` → one level down, under the section above it |
| [charts/bar-chart.md](charts/bar-chart.md) | — | Modifiers | — |
| [info-state/info-state.md](info-state/info-state.md) | — | Modifiers | — |
| [pagination/pagination.md](pagination/pagination.md) | — | Modifiers | — |

**8 docs need nothing**: `alert`, `autocomplete`, `breadcrumb`, `media-upload`, `segmented-control`, `slider`, `text-field`, `toggle-group`.

---

## The chart support pages

These document a part of a chart — the legend, the palettes, the
accessibility fallback — not a component. Most template sections cannot
apply to them, so their missing sections are not counted above. What is
listed here is only the off-template headings.

| Doc | Extra headings | What to do |
| --- | --- | --- |
| [charts/chart-accessibility.md](charts/chart-accessibility.md) | `Color-blind friendly mode`, `Table format` | `Color-blind friendly mode` → rename to **Accessibility (a11y)** and merge; `Table format` → one level down, under the section above it |
| [charts/chart-colors.md](charts/chart-colors.md) | `Categorical`, `Sequential`, `Diverging`, `Semantic`, `Resources` | `Categorical`, `Sequential`, `Diverging`, `Semantic` → one level down, under the section above it; `Resources` → link list — belongs under the title, not in a section |
| [charts/charts.md](charts/charts.md) | `Chart types`, `Supporting documentation` | `Chart types` → one level down, under the section above it; `Supporting documentation` → link list — belongs under the title, not in a section |
| [charts/filters-and-actions.md](charts/filters-and-actions.md) | `Type`, `Position` | `Type`, `Position` → one level down, under the section above it |
| [charts/legend.md](charts/legend.md) | — | — |

**Whether the template should apply to them at all is undecided.** Nobody
has asked the question; they are split out here so they do not drown the
component list above.

---

## Which sections go missing

| Section | Absent from |
| --- | --- |
| Usage | 3 docs |
| Platform | 35 docs |
| When to use | 3 docs |
| When NOT to use | 3 docs |
| Variant Selection Flow | 3 docs |
| Usage Guidance | 3 docs |
| Related Components | 2 docs |
| Variants & Modifiers | 4 docs |
| Modifiers | 14 docs |
| Behavior & Responsiveness | 5 docs |
| Interactive States & Loading | 7 docs |
| Touch Target & Layout | 9 docs |
| Breakpoints & Platform Adaptations | 6 docs |
| Content & UX Writing | 3 docs |
| Accessibility (a11y) | 1 docs |

**Read `Platform` differently from the rest.** The template says to omit it
when a component has no platform restriction, so its absence is expected on
most pages and is not counted as drift above. Which of those absences are
deliberate is unknown — nobody has checked.

---

## What this page is built from

| Input | Used for |
| --- | --- |
| [component-template.md](component-template.md) | The sections every doc is measured against |
| `components/<name>/<name>.md` | Every heading counted here |
| `SYNONYM_OF` in `components/template-drift.py` | Which template section an off-template heading duplicates. **The one judgement on this page** |

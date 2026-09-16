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
| — already match the template | **23** |
| — need something changed | **34** |
| Chart support pages, listed apart | 5 |
| Headings the template does not define | **51**, under 34 distinct names |
| Template sections absent from a page | **66** |
| Sections at the wrong heading level | **0** |
| Sections out of template order | **0** |
| Pages with no readiness table | **3** |

---

## The three fixes, and how much of the drift each one clears

Every off-template heading found so far falls into one of these. None has
ever needed a fourth. All three need a person, for the reason under each.

**None of the three is a script.** Each was tried: a scripted pass was
built for the first and thrown away, because in all 11 cases the heading
has to move to a different parent rather than down a level where it is.

| The fix | Headings | What it is |
| --- | --- | --- |
| **Move to the right section** | 11 | The heading names an axis of the component — `Opening menu`, `Rating results`, `Padding options` — sitting under a section it does not belong to. **Not mechanical:** demoting it in place would leave it under whatever happens to sit above, or under nothing at all. Somebody has to choose the destination |
| **Rename and merge** | 38 | The heading is a template section under another word — `Interaction` for states, `Scrolling` for layout. **Not mechanical:** both headings can hold content, and merging them is a judgement |
| **Move out of the sections** | 2 | The heading is a list of links to other pages. Links belong under the title, above the first `##` |

**A free-name slot is not drift.** The template writes one H3 as
`### [Variant Category Name]` — a slot that takes any name. A doc filling
it with `### Shapes and sizes` is using the template correctly. Those are
not counted here. Before this was handled the page reported 64 of them as
drift, which was wrong and made the real work look three times bigger.

**A free slot still does not take a section's name.** `### Labels` under
*Variants & Modifiers* is writing guidance sitting in a variants slot, and
the slot being free does not make that right. Those stay in the table.

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
| [navigation-bar/navigation-bar.md](navigation-bar/navigation-bar.md) | `Opening menu`, `Icon tooltip`, `Language menu`, `Arrows` | Interactive States & Loading, Touch Target & Layout | `Opening menu`, `Icon tooltip`, `Language menu`, `Arrows` → one level down, under the section above it |
| [coach-mark/coach-mark.md](coach-mark/coach-mark.md) | `Position`, `Interaction`, `Scroll`, `Animation` | Modifiers | `Position` → one level down, under the section above it; `Interaction`, `Animation` → rename to **Interactive States & Loading** and merge; `Scroll` → rename to **Touch Target & Layout** and merge |
| [phone-number-field/phone-number-field.md](phone-number-field/phone-number-field.md) | `Overflow Content` | Variants & Modifiers, Modifiers, Behavior & Responsiveness, Interactive States & Loading, Touch Target & Layout | `Overflow Content` → rename to **Touch Target & Layout** and merge; **no readiness table** |
| [tables/tables.md](tables/tables.md) | `Anatomy`, `Padding options`, `Device`, `Horizontal scroll` | — | `Anatomy` → rename to **Modifiers** and merge; `Padding options` → one level down, under the section above it; `Device` → rename to **Breakpoints & Platform Adaptations** and merge; `Horizontal scroll` → rename to **Touch Target & Layout** and merge |
| [carousel/carousel.md](carousel/carousel.md) | `Clipped content`, `Interaction`, `Carousel Items` | — | `Clipped content` → rename to **Touch Target & Layout** and merge; `Interaction` → rename to **Interactive States & Loading** and merge; `Carousel Items` → one level down, under the section above it |
| [floor-selection/floor-selection.md](floor-selection/floor-selection.md) | `Digit`, `Labels`, `Helper text` | — | `Digit`, `Labels`, `Helper text` → rename to **Content & UX Writing** and merge |
| [rating/rating.md](rating/rating.md) | `Scale`, `Rating results`, `Reviews` | — | `Scale` → rename to **Touch Target & Layout** and merge; `Rating results`, `Reviews` → one level down, under the section above it |
| [modal-bottom-sheet/modal-bottom-sheet.md](modal-bottom-sheet/modal-bottom-sheet.md) | `Scrolling` | Variants & Modifiers, Modifiers, Behavior & Responsiveness | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [charts/donut-chart.md](charts/donut-chart.md) | — | Modifiers, Interactive States & Loading, Touch Target & Layout, Breakpoints & Platform Adaptations | — |
| [checkbox/checkbox.md](checkbox/checkbox.md) | `Label`, `Interaction` | — | `Label` → rename to **Content & UX Writing** and merge; `Interaction` → rename to **Interactive States & Loading** and merge |
| [date-picker/date-picker.md](date-picker/date-picker.md) | — | Touch Target & Layout, Breakpoints & Platform Adaptations | **no readiness table** |
| [dropdown/dropdown.md](dropdown/dropdown.md) | `Interaction`, `Position & Scrolling` | — | `Interaction` → rename to **Interactive States & Loading** and merge; `Position & Scrolling` → rename to **Touch Target & Layout** and merge |
| [progress-bar/progress-bar.md](progress-bar/progress-bar.md) | `Width`, `Labels` | — | `Width` → rename to **Touch Target & Layout** and merge; `Labels` → rename to **Content & UX Writing** and merge |
| [radio-button-group/radio-button-group.md](radio-button-group/radio-button-group.md) | `Main elements`, `Overflow content` | — | `Main elements` → rename to **Content & UX Writing** and merge; `Overflow content` → rename to **Touch Target & Layout** and merge |
| [text-area/text-area.md](text-area/text-area.md) | `Main elements`, `Overflow content` | — | `Main elements` → rename to **Content & UX Writing** and merge; `Overflow content` → rename to **Touch Target & Layout** and merge |
| [card/card.md](card/card.md) | `Interaction` | Modifiers | `Interaction` → rename to **Interactive States & Loading** and merge |
| [modal-bottom-sheet-menu/modal-bottom-sheet-menu.md](modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) | `Scrolling` | Touch Target & Layout | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [action-menu/action-menu.md](action-menu/action-menu.md) | `Scrolling` | — | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [button-group/button-group.md](button-group/button-group.md) | `Interaction` | — | `Interaction` → rename to **Interactive States & Loading** and merge |
| [cell-content/cell-content.md](cell-content/cell-content.md) | `Interaction` | — | `Interaction` → rename to **Interactive States & Loading** and merge |
| [charts/line-chart.md](charts/line-chart.md) | `Variants` | — | `Variants` → rename to **Variants & Modifiers** and merge |
| [checkbox-group/checkbox-group.md](checkbox-group/checkbox-group.md) | `Interaction` | — | `Interaction` → rename to **Interactive States & Loading** and merge |
| [counter-field/counter-field.md](counter-field/counter-field.md) | `Interaction` | — | `Interaction` → rename to **Interactive States & Loading** and merge |
| [energy-tag/energy-tag.md](energy-tag/energy-tag.md) | `Country` | — | `Country` → rename to **Content & UX Writing** and merge |
| [kpi/kpi.md](kpi/kpi.md) | `Anatomy` | — | `Anatomy` → rename to **Modifiers** and merge |
| [listing-summary/listing-summary.md](listing-summary/listing-summary.md) | `Anatomy` | — | `Anatomy` → rename to **Modifiers** and merge |
| [progress-circle/progress-circle.md](progress-circle/progress-circle.md) | `Labels` | — | `Labels` → rename to **Content & UX Writing** and merge |
| [tabs/tabs.md](tabs/tabs.md) | — | — | **no readiness table** |
| [top-bar/top-bar.md](top-bar/top-bar.md) | `Scrolling` | — | `Scrolling` → rename to **Touch Target & Layout** and merge |
| [avatar/avatar.md](avatar/avatar.md) | — | Modifiers | — |
| [charts/bar-chart.md](charts/bar-chart.md) | — | Modifiers | — |
| [divider/divider.md](divider/divider.md) | — | Modifiers | — |
| [info-state/info-state.md](info-state/info-state.md) | — | Modifiers | — |
| [pagination/pagination.md](pagination/pagination.md) | — | Modifiers | — |

**23 docs need nothing**: `accordion`, `alert`, `autocomplete`, `breadcrumb`, `button`, `button-card`, `chip`, `chip-group`, `feedback-message`, `filter-bar`, `floating-button-group`, `link`, `listing-card`, `media-upload`, `segmented-control`, `select-card-group`, `slider`, `snackbar`, `tag`, `text-field`, `toggle`, `toggle-group`, `wizard`.

---

## The chart support pages

These document a part of a chart — the legend, the palettes, the
accessibility fallback — not a component. Most template sections cannot
apply to them, so their missing sections are not counted above. What is
listed here is only the off-template headings.

| Doc | Extra headings | What to do |
| --- | --- | --- |
| [charts/chart-accessibility.md](charts/chart-accessibility.md) | `Color-blind friendly mode`, `Table format` | `Color-blind friendly mode` → rename to **Accessibility (a11y)** and merge; `Table format` → one level down, under the section above it |
| [charts/chart-colors.md](charts/chart-colors.md) | `Resources` | `Resources` → link list — belongs under the title, not in a section |
| [charts/charts.md](charts/charts.md) | `Chart types`, `Supporting documentation` | `Chart types` → one level down, under the section above it; `Supporting documentation` → link list — belongs under the title, not in a section |
| [charts/filters-and-actions.md](charts/filters-and-actions.md) | — | — |
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

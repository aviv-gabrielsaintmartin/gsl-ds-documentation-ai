<!-- GENERATED FILE — do not edit by hand. Re-run: python3 components/coverage.py -->

# Component documentation coverage

_Which components have a doc, and which template sections that doc actually
fills. **Written by a script** — every mark below is read out of a file, not
judged. Never edit this page; re-run `components/coverage.py`._

---

## How to read it

| Mark | Meaning |
| --- | --- |
| ✅ | The section has content |
| ❌ | The section is there and says `Not documented` |
| ⬜ | The section heading is missing from the page entirely |

✅ means somebody wrote something, not that it is complete or correct.
A few pages say *"Not applicable"* and explain why — that counts as written.

❌ and ⬜ differ in what they tell you. ❌ means someone
looked at the section and had nothing. ⬜ means the section was never
put on the page. Where an `##` parent says `Not documented` and its `###`
children are missing, the children are marked ❌ — the parent already
declared them.

There is no *not relevant* mark. Deciding a section does not apply to a
component is a judgement, and no rule for it exists yet. Nothing here is
inferred.

---

## Where things stand

| | Count |
| --- | --- |
| Registry entries across the four Figma libraries | **98** |
| — have a doc | **63** |
| — no doc, and an agent may select them | **12** entries, 12 names |
| — no doc, and an agent should never select them | **23** entries, 21 names |

Entries outnumber names because `Brand Logo` and `Image Ratio` each exist in **two** Figma
libraries under the same name, with different keys. They are two distinct
components, so both entries are listed.

Across the 63 documented entries there are 1008 template
sections to fill. **648 are filled** — 64%.

---

## Which sections are worst

Ordered by how many documented components leave the section empty.

| Section | ✅ | ❌ | ⬜ | Filled |
| --- | --- | --- | --- | --- |
| a11y | 11 | 52 | 0 | 17% |
| Label Formula | 12 | 51 | 0 | 19% |
| Capitalization | 18 | 45 | 0 | 29% |
| Breakpoints | 19 | 44 | 0 | 30% |
| Length Limits | 21 | 42 | 0 | 33% |
| Platform | 27 | 0 | 36 | 43% |
| Variants | 40 | 23 | 0 | 63% |
| Modifiers | 44 | 19 | 0 | 70% |
| Touch target | 45 | 18 | 0 | 71% |
| Writing | 49 | 14 | 0 | 78% |
| Usage guidance | 55 | 8 | 0 | 87% |
| States | 55 | 8 | 0 | 87% |
| When to use | 63 | 0 | 0 | 100% |
| When NOT to use | 63 | 0 | 0 | 100% |
| Variant flow | 63 | 0 | 0 | 100% |
| Related | 63 | 0 | 0 | 100% |

**Read `Platform` differently from the rest.** It is prose saying a component
is restricted to some platforms — *"pagination is only used on the web"*. A
component with no restriction needs no such section, so its ⬜ is
probably correct rather than a gap. Every other row here is a real gap.
**Which of the 36 are deliberate is unknown** — nobody has
checked, and until somebody does this row cannot be read as a score.

**`a11y` and `Breakpoints` are the two worth acting on.** Between them they
account for 96 pages that
looked at the section and wrote nothing.

---

## Which components are worst

The ten documented components filling fewest of the 16 sections.

| Component | Tier | Filled |
| --- | --- | --- |
| [Avatar](avatar/avatar.md) | Components | 5 / 16 |
| [Donut chart](charts/donut-chart.md) | Patterns | 5 / 16 |
| [Bar graph](charts/bar-chart.md) | Patterns | 6 / 16 |
| [Divider](divider/divider.md) | Components | 6 / 16 |
| [KPI](kpi/kpi.md) | Patterns | 6 / 16 |
| [Progress Bar](progress-bar/progress-bar.md) | Components | 6 / 16 |
| [Progress Circle](progress-circle/progress-circle.md) | Components | 6 / 16 |
| [Line chart](charts/line-chart.md) | Patterns | 7 / 16 |
| [Listing Card](listing-card/listing-card.md) | Experiences | 7 / 16 |
| [Listing summary](listing-summary/listing-summary.md) | Experiences | 7 / 16 |

---

## The matrix — 63 documented entries

| Component | Tier | Readiness | Platform | When to use | When NOT to use | Variant flow | Usage guidance | Related | Variants | Modifiers | States | Touch target | Breakpoints | Writing | a11y | Capitalization | Label Formula | Length Limits | Filled |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Accordion](accordion/accordion.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | 11 |
| [Action Menu](action-menu/action-menu.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 14 |
| [Alert](alert/alert.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Autocomplete](autocomplete/autocomplete.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Avatar](avatar/avatar.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 |
| [Badge](badge/badge.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | 9 |
| [Bar graph](charts/bar-chart.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 6 |
| [Breadcrumb](breadcrumb/breadcrumb.md) | Patterns | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Button](button/button.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 14 |
| [Button Bar](button-bar/button-bar.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 8 |
| [Button Card](button-card/button-card.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | 11 |
| [Button Group](button-group/button-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 14 |
| [Card](card/card.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 9 |
| [Carousel](carousel/carousel.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | 14 |
| [Cell Content](cell-content/cell-content.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 12 |
| [Checkbox](checkbox/checkbox.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | 14 |
| [Checkbox Group](checkbox-group/checkbox-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | 14 |
| [Chip](chip/chip.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 13 |
| [Chip Group](chip-group/chip-group.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 13 |
| [Coachmark](coach-mark/coach-mark.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | 11 |
| [Counter Field](counter-field/counter-field.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 13 |
| [Date Picker](date-picker/date-picker.md) | Patterns | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 9 |
| [Divider](divider/divider.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 6 |
| [Donut chart](charts/donut-chart.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 |
| [Dropdown](dropdown/dropdown.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 12 |
| [Energy Tag](energy-tag/energy-tag.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 9 |
| [Feedback Messages](feedback-message/feedback-message.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Filter bar](filter-bar/filter-bar.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 9 |
| [Floating Button Group](floating-button-group/floating-button-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 8 |
| [Floor selection](floor-selection/floor-selection.md) | Experiences | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Image Slider](image-slider/image-slider.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | 11 |
| [Info State](info-state/info-state.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 8 |
| [KPI](kpi/kpi.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 6 |
| [Line chart](charts/line-chart.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 7 |
| [Link](link/link.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Listing Card](listing-card/listing-card.md) | Experiences | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 7 |
| [Listing summary](listing-summary/listing-summary.md) | Experiences | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 7 |
| [Loading State](loading-state/loading-state.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | 10 |
| [Media Upload](media-upload/media-upload.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Modal Bottom Sheet](modal-bottom-sheet/modal-bottom-sheet.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 13 |
| [Modal Bottom Sheet Menu](modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 14 |
| [Navigation bar](navigation-bar/navigation-bar.md) | Patterns | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Pagination](pagination/pagination.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 8 |
| [Phone Number Field](phone-number-field/phone-number-field.md) | Experiences | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | 11 |
| [Progress Bar](progress-bar/progress-bar.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 6 |
| [Progress Circle](progress-circle/progress-circle.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 6 |
| [Radio Button Group](radio-button-group/radio-button-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Rating](rating/rating.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Segmented Control](segmented-control/segmented-control.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 12 |
| [Select Card Group](select-card-group/select-card-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Slider](slider/slider.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 11 |
| [Snackbar](snackbar/snackbar.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | 13 |
| [Table](tables/tables.md) | Experiences | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 8 |
| [Tabs](tabs/tabs.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Tag](tag/tag.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | 13 |
| [Text Area](text-area/text-area.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Text Button](text-button/text-button.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | 12 |
| [Text Field](text-field/text-field.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Toggle](toggle/toggle.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Toggle Group](toggle-group/toggle-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Tooltip](tooltip/tooltip.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | 12 |
| [Top Bar](top-bar/top-bar.md) | Patterns | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 13 |
| [Wizard](wizard/wizard.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |

**Readiness** is the `Figma | Web | iOS | Android` table at the top of a page,
not a template section — so it is not counted in *Filled*. 63 of 63 pages
carry it. The 0 without it: .

### Chart pages that are not registry components

`Bar graph`, `Donut chart` and `Line chart` are registry entries and appear
in the matrix above. These five pages support them and have no registry entry
of their own, so they are listed rather than scored.

| Page | What it covers |
| --- | --- |
| [charts/charts.md](charts/charts.md) | Routing page — points at the chart types below |
| [charts/legend.md](charts/legend.md) | The chart legend, shared by every chart type |
| [charts/filters-and-actions.md](charts/filters-and-actions.md) | Filters and actions attached to a chart |
| [charts/chart-colors.md](charts/chart-colors.md) | Categorical, sequential, diverging and semantic palettes |
| [charts/chart-accessibility.md](charts/chart-accessibility.md) | Colour-blind mode and the table fallback |

---

## The gap — 12 components an agent may select, with no doc at all

These have no page anywhere in this repo. The *What it is* column is the one
sentence the ruleset's inventory gives — enough for an agent to pick the right
component, never enough to build one correctly.

| Component | Tier | What it is |
| --- | --- | --- |
| Badge Store | Components | Our replicas of the official App Store and Google Play badges, kept here so they can be maintained. |
| Burger menu | Patterns | Mobile menu opened from the navigation bar burger icon. |
| Date Field | Patterns | Date input — distinct from the Date Picker calendar view. |
| Estimation card | Experiences | Presents a completed price estimate — range, confidence, selling or renting. Carries no controls to adjust it. |
| Feedback Bar | Patterns | Asks the user to rate something — a notation on a scale. |
| Feedback Thumb Buttons | Components | Asks the user for a binary opinion — thumbs up or thumbs down. |
| Map template | Experiences | The map experience container. |
| Mega menus | Patterns | Top-level navigation on the main B2C and B2B websites. Shared across teams, not built or maintained by the design system. |
| Navigation Bar (App) | Components | Persistent in-app navigation between top-level destinations. |
| Pop-up | Components | Small-content alternative to a Modal bottom sheet. |
| Score Tag | Components | A Tag specialised for seller lead scoring. |
| State Message | Components | Inline feedback inside a form field. |

**All 12 carry a sentence in the ruleset.** None is a doc, so an
agent can choose these components and cannot build them without inventing
the detail.

---
## No doc, and none needed — 21 names

An agent should never select these, so the missing doc is not a gap. The
reasons are the ruleset's own, read from the rows it marks 🚫.

| Component | Tier | Why no doc is needed |
| --- | --- | --- |
| Brand App Icons | Foundations | asset — brand config |
| Brand Logo | Components | asset — brand config |
| Brand Logo | Foundations | asset — brand config |
| Burger menu (profil) | Patterns | withheld — adapted to consumer content, use Burger menu |
| Button Card Group | Components | withheld — never developed, should leave Figma |
| Content Placeholder | Components | composed-only — a slot, swapped for local content |
| Favicon | Foundations | asset — brand config |
| Filter button | Patterns | composed-only — inside Filter bar |
| Filter dropdown container | Patterns | composed-only — inside Filter bar |
| Flag | Foundations | asset — brand config |
| Footer | Patterns | withheld — Figma only, not built |
| Home Indicator | Components | chrome — the OS draws it |
| Image Ratio | Components | withheld — a Figma-internal ratio helper for designers |
| Image Ratio | Foundations | withheld — a Figma-internal ratio helper for designers |
| Map Polygon | Experiences | composed-only — inside Map template |
| Map Polygon backdrop | Experiences | composed-only — inside Map template |
| mapPinsV2_IWT | Experiences | composed-only — inside Map template, Immowelt |
| mapPinsV2_SL | Experiences | composed-only — inside Map template, SeLoger |
| Menus | Patterns | withheld, provisional — nothing requires it today, use Navigation bar |
| Programmatic Ads | Components | withheld — commercial ad slot |
| Status Bar | Components | chrome — the OS draws it |
| Tab Bar | Components | withheld — mid-refactor, use Tabs |
| Webview | Components | chrome — an embedded browser container |

**Careful with `Cell Content`.** It is in the matrix above
with a doc, and still not selectable. A well-filled row in this page is not
permission to use the component. The ruleset decides that, not this page.

---

## What this page is built from

| Input | Used for |
| --- | --- |
| `figma/figma-components-registry.json` | The Components tier — what exists |
| `figma/figma-patterns-registry.json` | The Patterns tier |
| `figma/figma-experiences-registry.json` | The Experiences tier |
| `figma/figma-foundations-components-registry.json` | The Foundations tier |
| `components/<name>/<name>.md` | Every mark in the matrix |
| [component-template.md](component-template.md) | Which sections are columns, and in what order |
| [components-rules-ai.md](components-rules-ai.md) | What each component is for, and which may never be selected |
| [components-audit.md](components-audit.md) | The five name aliases |

### Does the ruleset's inventory still match the files?

**Yes.** All 96 inventory rows agree with the files on disk about
whether a doc exists. Checked every time this page is generated, because the
inventory went stale unnoticed once already.


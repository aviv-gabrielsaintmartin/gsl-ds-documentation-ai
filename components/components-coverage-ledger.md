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
| — have a doc | **58** |
| — no doc, and an agent may select them | **23** entries, 22 names |
| — no doc, and an agent should never select them | **17** entries, 16 names |

Entries outnumber names because `Brand Logo` and `Image Ratio` each exist in **two** Figma
libraries under the same name, with different keys. They are two distinct
components, so both entries are listed.

Across the 58 documented entries there are 928 template
sections to fill. **594 are filled** — 64%.

---

## Which sections are worst

Ordered by how many documented components leave the section empty.

| Section | ✅ | ❌ | ⬜ | Filled |
| --- | --- | --- | --- | --- |
| a11y | 6 | 52 | 0 | 10% |
| Label Formula | 12 | 46 | 0 | 21% |
| Capitalization | 18 | 40 | 0 | 31% |
| Breakpoints | 19 | 39 | 0 | 33% |
| Length Limits | 19 | 39 | 0 | 33% |
| Platform | 27 | 0 | 31 | 47% |
| Variants | 35 | 23 | 0 | 60% |
| Modifiers | 40 | 18 | 0 | 69% |
| Touch target | 40 | 18 | 0 | 69% |
| Writing | 44 | 14 | 0 | 76% |
| States | 50 | 8 | 0 | 86% |
| Usage guidance | 52 | 6 | 0 | 90% |
| When to use | 58 | 0 | 0 | 100% |
| When NOT to use | 58 | 0 | 0 | 100% |
| Variant flow | 58 | 0 | 0 | 100% |
| Related | 58 | 0 | 0 | 100% |

**Read `Platform` differently from the rest.** It is prose saying a component
is restricted to some platforms — *"pagination is only used on the web"*. A
component with no restriction needs no such section, so its ⬜ is
probably correct rather than a gap. Every other row here is a real gap. Which
of the 29 are deliberate is unknown — nobody has checked.

**`a11y` and `Breakpoints` are the two worth acting on.** Between them they
account for 91 pages that
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

## The matrix — 58 documented entries

| Component | Tier | Readiness | Platform | When to use | When NOT to use | Variant flow | Usage guidance | Related | Variants | Modifiers | States | Touch target | Breakpoints | Writing | a11y | Capitalization | Label Formula | Length Limits | Filled |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Accordion](accordion/accordion.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | 11 |
| [Action Menu](action-menu/action-menu.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 14 |
| [Alert](alert/alert.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Autocomplete](autocomplete/autocomplete.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Avatar](avatar/avatar.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 |
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
| [Info State](info-state/info-state.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 8 |
| [KPI](kpi/kpi.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 6 |
| [Line chart](charts/line-chart.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 7 |
| [Link](link/link.md) | Components | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Listing Card](listing-card/listing-card.md) | Experiences | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 7 |
| [Listing summary](listing-summary/listing-summary.md) | Experiences | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 7 |
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
| [Text Field](text-field/text-field.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Toggle](toggle/toggle.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |
| [Toggle Group](toggle-group/toggle-group.md) | Components | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 10 |
| [Top Bar](top-bar/top-bar.md) | Patterns | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 13 |
| [Wizard](wizard/wizard.md) | Patterns | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 11 |

**Readiness** is the `Figma | Web | iOS | Android` table at the top of a page,
not a template section — so it is not counted in *Filled*. 58 of 58 pages
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

## The gap — 22 components an agent may select, with no doc at all

These have no page anywhere in this repo. An agent asked to use one has
nothing to read. Where the *Known from* column is filled, the repo describes
the component inside **another component's** page — a sentence, not a doc.

| Component | Tier | What it is | Known from |
| --- | --- | --- | --- |
| Badge | Components | Attention marker attached to a host element | button, tabs, cell-content |
| Burger menu | Patterns | Mobile menu opened from the navigation bar | navigation-bar |
| Burger menu (profil) | Patterns | A distinct component from Burger menu | registry |
| Date Field | Patterns | Date input, distinct from the Date Picker calendar | date-picker, text-area |
| Filter button | Patterns | The individual filter control inside Filter bar | filter-bar, charts |
| Image Ratio | Components | Enforces an image aspect ratio | registry |
| Image Ratio | Foundations | Enforces an image aspect ratio | registry |
| Image Slider | Components | Horizontally sliding image sequence | listing-card, carousel |
| Loading State | Components | Signals data or content is being fetched | autocomplete, dropdown, info-state |
| Map template | Experiences | The map experience container | registry |
| Menus | Patterns | Profile and language menus | registry |
| Navigation Bar (App) | Components | In-app navigation between destinations. Mobile only | tabs, registry |
| Pop-up | Components | The small-content alternative to Modal bottom sheet | modal-bottom-sheet |
| Score Tag | Components | A Tag specialised for seller lead scoring | tag |
| State Messages | Components | Inline form feedback — guide, correct, inform | alert, text-area, text-field |
| Text Button | Components | A distinct component from Button | button, action-menu, autocomplete |
| Tooltip | Components | Brief overlay clarifying one UI element | coach-mark |
| Badge Store | Components | **Unknown** | — |
| Button Card Group | Components | **Unknown** | — |
| Estimation card | Experiences | **Unknown** | — |
| Feedback Bar | Patterns | **Unknown** | — |
| Feedback Thumb Buttons | Components | **Unknown** | — |
| Mega menus | Patterns | **Unknown** | — |

**6 of those 22 have no evidence anywhere in the repo** —
no doc, and no other page mentions what they do: `Badge Store`, `Button Card Group`, `Estimation card`, `Feedback Bar`, `Feedback Thumb Buttons`, `Mega menus`.

---
## No doc, and none needed — 16 names

An agent should never select these, so the missing doc is not a gap.
The reasons are copied from
[components-audit.md](components-audit.md#not-selectable-and-why) — that
classification is the one human judgement this page carries.

| Component | Tier | Why no doc is needed |
| --- | --- | --- |
| Brand App Icons | Foundations | Asset — per-platform, per-brand exports |
| Brand Logo | Components | Asset — configured by brand, not chosen by design intent |
| Brand Logo | Foundations | Asset — configured by brand, not chosen by design intent |
| Content Placeholder | Components | Composed-only — a slot, swapped for local content |
| Favicon | Foundations | Asset — fixed, no properties of its own |
| Filter dropdown container | Patterns | Composed-only — sibling pattern to Filter bar |
| Flag | Foundations | Asset — country flag family |
| Footer | Patterns | Withheld — Figma only, not developed. Owned by Header/Footer team |
| Home Indicator | Components | Chrome — iOS system affordance |
| Map Polygon | Experiences | Composed-only — part of the Map experience |
| Map Polygon backdrop | Experiences | Composed-only — part of the Map experience |
| mapPinsV2_IWT | Experiences | Composed-only — brand-specific pin set (Immowelt) |
| mapPinsV2_SL | Experiences | Composed-only — brand-specific pin set (SeLoger) |
| Programmatic Ads | Components | Withheld — commercial ad slot, not a design choice |
| Status Bar | Components | Chrome — OS-rendered |
| Tab Bar | Components | Withheld — in-progress refactor. Use Tabs until it settles |
| Webview | Components | Chrome — embedded browser container, iOS/Android only |

**Careful with `Cell Content`.** It is in the matrix above
with a full doc, and it is still not selectable — composed-only — a slot inside cards and lists. A well-filled
row in this page is not permission to use the component. The ruleset decides
that, not this page.

---

## What this page is built from

| Input | Used for |
| --- | --- |
| `figma/figma-components-registry.json` | The Components tier — what exists |
| `figma/figma-patterns-registry.json` | The Patterns tier |
| `figma/figma-experiences-registry.json` | The Experiences tier |
| `figma/figma-foundations-components-registry.json` | The Foundations tier |
| `components/<name>/<name>.md` | Every mark in the matrix |
| [components-audit.md](components-audit.md) | The five name aliases, and which components are not selectable |


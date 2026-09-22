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
| Component docs measured | **77** |
| — already match the template | **77** |
| — need something changed | **0** |
| Chart support pages, listed apart | 3 |
| Headings the template does not define | **5**, under 5 distinct names |
| Template sections absent from a page | **38** |
| Sections at the wrong heading level | **0** |
| Sections out of template order | **0** |
| Pages with no readiness table | **0** |

---

## The three fixes, and how much of the drift each one clears

Every off-template heading found so far falls into one of these. None has
ever needed a fourth. All three need a person, for the reason under each.

**None of the three is a script.** Each was tried: a scripted pass was
built for the first and thrown away, because in all 11 cases the heading
has to move to a different parent rather than down a level where it is.

| The fix | Headings | What it is |
| --- | --- | --- |
| **Move to the right section** | 2 | The heading names an axis of the component — `Opening menu`, `Rating results`, `Padding options` — sitting under a section it does not belong to. **Not mechanical:** demoting it in place would leave it under whatever happens to sit above, or under nothing at all. Somebody has to choose the destination |
| **Rename and merge** | 1 | The heading is a template section under another word — `Interaction` for states, `Scrolling` for layout. **Not mechanical:** both headings can hold content, and merging them is a judgement |
| **Move out of the sections** | 2 | The heading is a list of links to other pages. Links belong under the title, above the first `##` |

**A free-name slot is not drift.** The template writes one H3 as
`### [Variant Category Name]` — a slot that takes any name. A doc filling
it with `### Shapes and sizes` is using the template correctly. Those are
not counted here. Before this was handled the page reported 64 of them as
drift, which was wrong and made the real work look three times bigger.

**A free slot takes any name, including a section's.** `### Width` under
*Variants & Modifiers* looks like a misfiled layout section and is not:
it holds a Fixed / Full width comparison. All nine such collisions were
read on 16 Sep and every one was a real variant category.

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

**77 docs need nothing**: `accordion`, `action-menu`, `alert`, `autocomplete`, `avatar`, `badge`, `badge-store`, `breadcrumb`, `burger-menu`, `button`, `button-bar`, `button-card`, `button-group`, `card`, `carousel`, `cell-content`, `charts`, `charts`, `charts`, `charts`, `charts`, `checkbox`, `checkbox-group`, `chip`, `chip-group`, `coach-mark`, `counter-field`, `date-field`, `date-picker`, `divider`, `dropdown`, `energy-tag`, `estimation-card`, `feedback-bar`, `feedback-message`, `feedback-thumb-buttons`, `filter-bar`, `floating-button-group`, `floor-selection`, `image-slider`, `info-state`, `kpi`, `link`, `listing-card`, `listing-summary`, `loading-state`, `map-template`, `media-upload`, `mega-menus`, `menus`, `modal-bottom-sheet`, `modal-bottom-sheet-menu`, `navigation-bar`, `navigation-bar-app`, `pagination`, `phone-number-field`, `progress-bar`, `progress-circle`, `radio-button-group`, `rating`, `score-tag`, `segmented-control`, `select-card-group`, `slider`, `snackbar`, `state-message`, `tables`, `tabs`, `tag`, `text-area`, `text-button`, `text-field`, `toggle`, `toggle-group`, `tooltip`, `top-bar`, `wizard`.

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

**Whether the template should apply to them at all is undecided.** Nobody
has asked the question; they are split out here so they do not drown the
component list above.

---

## Which sections go missing

| Section | Absent from |
| --- | --- |
| Usage | 3 docs |
| Platform | 41 docs |
| When to use | 3 docs |
| When NOT to use | 3 docs |
| Variant Selection Flow | 3 docs |
| Usage Guidance | 3 docs |
| Related Components | 2 docs |
| Variants & Modifiers | 2 docs |
| Modifiers | 3 docs |
| Behavior & Responsiveness | 3 docs |
| Interactive States & Loading | 3 docs |
| Touch Target & Layout | 3 docs |
| Breakpoints & Platform Adaptations | 3 docs |
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

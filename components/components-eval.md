# Component selection eval

_The check on [components-rules-ai.md](components-rules-ai.md). This repo has no
test suite, so this is how the ruleset is verified against `CLAUDE.md`'s one
test: **could an agent build a compliant interface from this alone?**_

## How to run it

1. Start an agent with **only** `components-rules-ai.md` in context. Not the
   component pages, not the audit, not this file's Expected column.
2. Give it each Intent verbatim. Ask for one component name and the rule that
   led there.
3. Score. **Every miss is a defect in the ruleset, not in the agent** — fix the
   rule, then re-run the whole set, not just the failed row.

A pass needs the right component *and* the right reason. Landing on `Snackbar`
by luck when the rule should have routed via Rule 2 still fails.

## The set

Twenty-seven intents. Rows 8, 18–22 and 24 matter most: they test tier order,
rule precedence and the never-select list — the places where a plausible-looking
wrong answer is the default failure.

| # | Intent | Expected | Tests |
| --- | --- | --- | --- |
| 1 | "A control that takes the user to the pricing page" | `Link` | Rule 1 — action vs navigation |
| 2 | "A 'Read more' control under a truncated description" | `Text button` | Rule 1 — button weight |
| 3 | "Let the user pick one of 12 property types in a form" | `Dropdown` | Rule 1 — the ≤5 threshold |
| 4 | "Let the user pick one of 3 property types in a form" | `Radio button group` | Rule 1 — same threshold, other side |
| 5 | "Switch the results between map view and list view" | `Segmented control` | Rule 1 — view mode vs form value |
| 6 | "Switch between the Description, Photos and Location sections of a listing" | `Tabs` | Rule 1 — full content sections |
| 7 | "Let the user tick several amenities inside the listing-creation form" | `Checkbox group` | Rule 1 — structured form |
| 8 | "Quick inline filters above search results, no dropdown panels" | `Chip group` — **not** `Filter bar` | **Rule 0 vs Rule 1 precedence.** Rule 0 names filter rows, but Rule 1 routes the lighter case here |
| 9 | "Show 'New' on a listing — not clickable" | `Tag` | Rule 1 — holds its own place in the flow, vs `Badge` anchored to a host |
| 10 | "Narrow a SERP by price, surface and rooms with structured panels" | `Filter bar` | Rule 1 — structured criteria |
| 11 | "Let the user write a 3-paragraph description of their property" | `Text area` | Rule 1 — multi-line |
| 12 | "Let the user type a city and pick from matching suggestions" | `Autocomplete` | Rule 1 — type to filter |
| 13 | "Pick a number of bedrooms with + and − controls" | `Counter field` | Rule 1 — numeric with controls |
| 14 | "A budget range across a continuous scale" | `Slider` | Rule 1 — range, approximate |
| 15 | "Turn email notifications on, effective immediately" | `Toggle` | Rule 1 — immediate vs submitted |
| 16 | "Contextual actions on a listing card, on a phone" | `Modal bottom sheet menu` | Rule 1 + Rule 2 — mobile |
| 17 | "Confirm before deleting a listing, blocking, **on web**" | `Pop-up` for a short confirmation, `Modal bottom sheet` for richer content — **never** `Alert` | **Rule 2 overrides Rule 1.** Alert is not yet available on web. Either answer passes; `Alert` fails |
| 18 | "A card summarising a property: photo carousel, price, surface, tags" | `Listing Card` (Experience) | **Rule 0.** Fails if it composes Card + Image slider + Tag |
| 19 | "An input for a phone number with a country prefix" | `Phone Number Field` (Experience) | **Rule 0.** Fails if it composes Text field + Dropdown |
| 20 | "A row inside a list, with a title, subtitle and trailing icon" | A list you lay out yourself, of `Cell content` rows — never `Cell Content` as the answer to "which component" | **Rule 3 + Rule 1.** There is no `List` component; laying it out yourself is the intended pattern |
| 21 | "Show all search results at once in a grid rather than a carousel" | A grid layout of `Card`s — **no** `Card grid` component exists | **Rule 2.** Fails if it searches for a Card grid component |
| 22 | "The bar at the very top of the phone showing battery and signal" | Nothing — the OS draws it | **Rule 3.** Fails if it selects `Status Bar` |
| 23 | "An unread-message count sitting on a navigation icon" | `Badge` | Rule 1 — anchored to a host, vs `Tag` |
| 24 | "A settings list where each row has a label and an on/off control taking effect immediately" | `Toggle group` | Rule 1 — the composite, not hand-built rows of toggles |
| 25 | "A step-by-step property-valuation flow where step 3 depends on step 2" | `Wizard` | Rule 0 / Rule 1 — sequential dependency |
| 26 | "A brief hint explaining what the DPE field means, on hover of the info icon" | `Tooltip` | Rule 1 — single clarification, vs `Coach mark` |
| 27 | "Tell the user their saved-search limit is reached, inline, and keep it visible" | `Feedback message` | Rule 1 — persistent and inline, vs `Snackbar` |

## Scoring

| Band | Meaning |
| --- | --- |
| 27/27 | The ruleset is doing its job |
| 23–26 | Usable. Fix the missed rows before extending Rule 1 |
| ≤22 | The ruleset is not yet the single entry point. Do not point agents at it |

Record each run below.

## Runs

| Date | Score | Misses | Fix applied |
| --- | --- | --- | --- |
| 2026-09-08 · run 1 | **22/22** | None. Two answers reached at low confidence (#2, #20), one at medium (#9) | Four ruleset defects the score did not catch — all fixed, see below |
| 2026-09-08 · run 2 | **27/27** (5 new intents added) | None. Run 1's fixes moved #2 and #9 to high confidence | Five more defects, including a Rule 0 / Rule 1 contradiction introduced by run 1 — all fixed |
| 2026-09-08 · run 3 | **10/10** focused | None. Both run-2 fixes confirmed working, quoted back by the agent | Three more defects — `Pop-up` missing from Rule 1, `Charts` unbranched, Rule 0 threshold qualitative — all fixed |

### Run 1 — 2026-09-08

A cold agent given only `components-rules-ai.md` answered all 22 correctly, with
the correct rule each time, including the three traps (17 Alert-on-web, 20 Cell
Content, 21 Card grid) and both Rule 0 tier cases (18, 19).

**The score hid four real defects.** A perfect score reached by forcing an answer
is not a working ruleset — these came from the agent's own friction report:

| Defect | Fix |
| --- | --- |
| **`Badge` was absent from Rule 1 entirely.** It sat in the Rule 4 inventory with no routing to it, so "New" on a listing had two plausible answers (`Tag`, `Badge`) and zero criteria between them | Added a `Badge` row under *Providing feedback and status*, split from `Tag` on whether the marker is attached to a host or stands alone in the layout |
| **No case for revealing content in place.** "Read more" under truncated text — an extremely common listing pattern — had no anchor; the agent forced it into the button-weight branch | Added a `Text button` row under *Grouping and structuring content* |
| **Rule 3 told the agent to "select the Card or list", but no `List` component exists** in any of the four libraries | Rewrote the `Cell Content` row: names `Card` and `Table` as the real containers, states plainly that there is no `List` component, and reframes Cell content as what you build rows *from* rather than something banned |
| **No precedence when an intent matched several rows.** "Long list" appears as the *Otherwise* of three different rows | Added a five-step precedence order at the top of Rule 1 |

Re-run after these changes before trusting the score.

### Run 2 — 2026-09-08

Re-run cold after the Run 1 fixes, with **five extra intents** (23–27) probing
the gaps Run 1 exposed: a count on a navigation icon, a settings list, a
sequential valuation flow, a hover explanation, a persistent inline limit warning.

**27/27**, every one with the correct rule. Both Run 1 fixes held: "Read more"
and the "New" label moved from low and medium confidence to **high**.

Again the score hid defects — one of them introduced by the Run 1 fixes:

| Defect | Fix |
| --- | --- |
| **Rule 0 contradicted Rule 1.** Rule 0's table said "a filter row from Chips or Buttons → Filter bar", while Rule 1's Filter bar row says "lightweight inline filters without dropdown panels → Chip group". Since Rule 0 "wins whenever both apply", an agent following precedence literally reached the *wrong* component | Narrowed the Rule 0 row to a **structured, multi-criteria** filter panel, and added a "What Rule 0 does not cover" table: when Rule 1 routes to a **lighter** component for a smaller version of the same job, that is not a Rule 0 violation |
| **No container existed for a plain list.** Rule 3 offered only `Card` or `Tables`, neither of which is a settings screen or an index list, while stating no `List` component exists | Added a Rule 1 row for **a list you lay out yourself, of `Cell content` rows**, stating explicitly that this is the intended pattern rather than a workaround, and softened Rule 3 to match |
| **`Toggle group` vs. hand-built rows of toggles was unresolved** — two paths producing identical UI from different components | `Toggle group`'s row now names the settings-screen case and forbids hand-building the rows |
| **`Tag` vs `Badge` was example-driven, not rule-driven.** It resolved only because the word "New" appeared in Tag's row; "Verified" would have been ambiguous | Replaced the examples with a structural test — does the marker **hold its own place in the layout flow** (Tag) or is it **anchored to a host component's geometry** and meaningless without it (Badge) |
| **`Tooltip` had no first-class row**, reachable only via Coach mark's *Otherwise* | Given its own row under *Providing feedback and status* |

Still open, and tracked in the audit rather than the ruleset: seven components
are marked *Undescribed* in Rule 4, so for those the ruleset knowingly points
outside itself. See [components-audit.md](components-audit.md)
open question 2.

### Run 3 — 2026-09-08 · focused

Ten intents targeting only what Run 2's fixes changed, plus two direct questions
asking the agent to quote the rule that decides a contested case.

**10/10.** Both fixes confirmed working, in the agent's own words:

- On the Rule 0 / Rule 1 precedence — the inline-filter case is *"pre-adjudicated,
  not left to inference"*.
- On `Tag` vs `Badge` — *"the test is general, not word-matching"*. It noted that
  an agent pattern-matching on the example words would still pass, but would
  misclassify a "Verified" marker overlapping a card corner, which the geometry
  test correctly sends to `Badge`.

Three further defects found and fixed:

| Defect | Fix |
| --- | --- |
| **`Pop-up` had no Rule 1 row.** It existed only in the Rule 0 exception table and the inventory, so an agent reading Rule 1 as the flat decision table — which is how the ruleset describes itself — would never find it. Nothing separated a short web confirmation between `Pop-up` and `Modal bottom sheet` | Gave `Pop-up` its own row under *Overlaying content*, and rewrote `Alert`'s web fallback to split on content size rather than sending everything to `Modal bottom sheet` |
| **`Charts` was one row for three chart types**, with no branching. The Bar / Line / Donut distinction existed only in Rule 4's inventory strings, which Rule 1 never pointed to | Split into four rows — `Bar graph`, `Line chart`, `Donut chart`, `Legend` — each with its own trigger and redirects |
| **The Rule 0 threshold was qualitative** — "the full job" vs "a lighter version" gave no operational test, so two agents could disagree and both cite the text | Added **count the parts**: two or more of the higher-tier component's own moving parts means Rule 0; one part means Rule 1. With a worked table for `Filter bar` and `Wizard` |

Accepted, not fixed: the five-step precedence ladder is stated once at the top of
Rule 1 rather than repeated per row. Repeating it 51 times would bloat the table
for a reader that always has the whole file in context.

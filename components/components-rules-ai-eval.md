# Component selection eval

_The check on [components-rules-ai.md](components-rules-ai.md). This repo has no
test suite, so this is how the ruleset is verified against `CLAUDE.md`'s one
test: **could an agent build a compliant interface from this alone?**_

## How to run it

1. Start an agent with **only** `components-rules-ai.md` in context. Not the
   component pages, not the audit, not this file's Expected column.
2. Give it each Intent verbatim. Ask for the answer and the rule that led there.
   **Do not ask for a component name.** Some rows have no component as their
   answer: the right answer may be that nothing is placed, that a layout is laid
   out by hand, or that a declaration is written. Asking for a component name
   tells the agent one exists.
3. Score. **Every miss is a defect in the ruleset, not in the agent** — fix the
   rule, then re-run the whole set, not just the failed row.

A pass needs the right answer *and* the right reason. Landing on `Snackbar`
by luck when the rule should have routed via **Platform limits** still fails.

## The set

**Sixty-four intents.** Rows 1–27 were run three times on 2026-09-08. **All 64
were run once, on 2026-09-23 — run 4, 60/64.** Rows 29 and 54 are defective as
written and are marked so under *Run 4*, below.

The rows where a plausible-looking wrong answer is the default failure:

| Rows          | What they probe                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------- |
| 8, 18–22, 24  | Tier order, rule precedence, the never-select list, and the two non-composed kinds of higher-tier component           |
| 28–31         | The container and all-or-nothing kinds, and the `Table` platform caveat                                               |
| 32–37         | The never-select rulings written after the last run. **Every one names a component that looks like the right answer** |
| 41–43         | **Built outside the design system.** The component alone is not the whole answer — the run must report the selection  |
| 52–53, 59, 64 | Rules whose answer includes a declaration, not only a component                                                       |
| 35–37, 56–58  | Rules whose correct answer is that there is nothing to place                                                          |

| #   | Intent                                                                                                               | Expected                                                                                                                                                                                 | Tests                                                                                                                                                                                                                                    |
| --- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | "A control that takes the user to the pricing page"                                                                  | `Link`                                                                                                                                                                                   | **Which component** — action vs navigation                                                                                                                                                                                               |
| 2   | "A 'Read more' control under a truncated description"                                                                | `Text button`                                                                                                                                                                            | **Which component** — button weight                                                                                                                                                                                                      |
| 3   | "Let the user pick one of 12 property types in a form"                                                               | `Dropdown`                                                                                                                                                                               | **Which component** — the 10-option ceiling                                                                                                                                                                                              |
| 4   | "Let the user pick one of 3 property types in a form"                                                                | `Radio button group`                                                                                                                                                                     | **Which component** — same ceiling, other side                                                                                                                                                                                           |
| 5   | "Switch the results between map view and list view"                                                                  | `Segmented control`                                                                                                                                                                      | **Which component** — view mode vs form value                                                                                                                                                                                            |
| 6   | "Switch between the Description, Photos and Location sections of a listing"                                          | `Tabs`                                                                                                                                                                                   | **Which component** — full content sections                                                                                                                                                                                              |
| 7   | "Let the user tick several amenities inside the listing-creation form"                                               | `Checkbox group`                                                                                                                                                                         | **Which component** — structured form                                                                                                                                                                                                    |
| 8   | "Quick inline filters above search results, no dropdown panels"                                                      | `Chip group` — **not** `Filter bar`                                                                                                                                                      | **Highest tier first vs Which component precedence.** **Highest tier first** names filter rows, but **Which component** routes the lighter case here                                                                                     |
| 9   | "Show 'New' on a listing — not clickable"                                                                            | `Tag`                                                                                                                                                                                    | **Which component** — holds its own place in the flow, vs `Badge` anchored to a host                                                                                                                                                     |
| 10  | "Narrow a SERP by price, surface and rooms with structured panels"                                                   | `Filter bar`                                                                                                                                                                             | **Which component** — structured criteria                                                                                                                                                                                                |
| 11  | "Let the user write a 3-paragraph description of their property"                                                     | `Text area`                                                                                                                                                                              | **Which component** — multi-line                                                                                                                                                                                                         |
| 12  | "Let the user type a city and pick from matching suggestions"                                                        | `Autocomplete`                                                                                                                                                                           | **Which component** — type to filter                                                                                                                                                                                                     |
| 13  | "Pick a number of bedrooms with + and − controls"                                                                    | `Counter field`                                                                                                                                                                          | **Which component** — numeric with controls                                                                                                                                                                                              |
| 14  | "A budget range across a continuous scale"                                                                           | `Slider`                                                                                                                                                                                 | **Which component** — range, approximate                                                                                                                                                                                                 |
| 15  | "Turn email notifications on, effective immediately"                                                                 | `Toggle`                                                                                                                                                                                 | **Which component** — immediate vs submitted                                                                                                                                                                                             |
| 16  | "Contextual actions on a listing card, on a phone"                                                                   | `Modal bottom sheet menu`                                                                                                                                                                | **Which component** + **Platform limits** — mobile                                                                                                                                                                                       |
| 17  | "Confirm before deleting a listing, blocking, **on web**"                                                            | `Modal bottom sheet` — **never** `Alert`, **never** `Pop-up`                                                                                                                             | **Platform limits overrides Which component.** `Alert` is not built on web and is assembled from `Modal bottom sheet`, keeping its fixed shape; `Pop-up` is apps only. **Corrected 2026-09-23** — see the note under *Scoring*           |
| 18  | "A card summarising a property: photo carousel, price, surface, tags"                                                | `Listing Card` (Experience)                                                                                                                                                              | **Highest tier first.** Fails if it composes Card + Image slider + Tag                                                                                                                                                                   |
| 19  | "An input for a phone number with a country prefix"                                                                  | `Phone Number Field` (Experience)                                                                                                                                                        | **Highest tier first.** Fails if it composes Text field + Dropdown                                                                                                                                                                       |
| 20  | "A row inside a list, with a title, subtitle and trailing icon"                                                      | A list you lay out yourself, of `Cell content` rows — never `Cell Content` as the answer to "which component"                                                                            | **Never select + **Which component**.** There is no `List` component; laying it out yourself is the intended pattern                                                                                                                     |
| 21  | "Show all search results at once in a grid rather than a carousel"                                                   | A grid layout of `Card`s — **no** `Card grid` component exists                                                                                                                           | **Platform limits.** Fails if it searches for a Card grid component                                                                                                                                                                      |
| 22  | "The bar at the very top of the phone showing battery and signal"                                                    | Nothing — the OS draws it                                                                                                                                                                | **Never select.** Fails if it selects `Status Bar`                                                                                                                                                                                       |
| 23  | "An unread-message count sitting on a navigation icon"                                                               | `Badge`                                                                                                                                                                                  | **Which component** — anchored to a host, vs `Tag`                                                                                                                                                                                       |
| 24  | "A settings list where each row has a label and an on/off control taking effect immediately"                         | `Toggle group`                                                                                                                                                                           | **Which component** — the composite, not hand-built rows of toggles                                                                                                                                                                      |
| 25  | "A step-by-step property-valuation flow where step 3 depends on step 2"                                              | `Wizard`                                                                                                                                                                                 | **Highest tier first** / **Which component** — sequential dependency                                                                                                                                                                     |
| 26  | "A brief hint explaining what the DPE field means, on hover of the info icon"                                        | `Tooltip`                                                                                                                                                                                | **Which component** — single clarification, vs `Coach mark`                                                                                                                                                                              |
| 27  | "Tell the user their saved-search limit is reached, inline, and keep it visible"                                     | `Feedback message`                                                                                                                                                                       | **Which component** — persistent and inline, vs `Snackbar`                                                                                                                                                                               |
| 28  | "An empty state for a saved-search list with nothing in it yet"                                                      | `Info State`                                                                                                                                                                             | **Highest tier first, container kind.** Fails if it assembles an illustration + text + a button                                                                                                                                          |
| 29  | "A data grid of leads, sortable, **on web**"                                                                         | `Table` — but **flag it**: Figma-ready, web in progress                                                                                                                                  | **Platform limits.** Fails if it returns `Table` with no platform caveat                                                                                                                                                                 |
| 30  | "A map view of listings with clickable pins"                                                                         | `Map template`                                                                                                                                                                           | **Highest tier first, all-or-nothing.** Fails if it selects `mapPinsV2_SL` or builds a container plus pins                                                                                                                               |
| 31  | "A list of settings rows, each with a label and a trailing chevron"                                                  | A list you lay out yourself, of `Cell content` rows                                                                                                                                      | **Never select + **Which component**.** Tests that Cell content is reachable as a part but never as the answer                                                                                                                           |
| 32  | "A whole panel that is itself one action — tap anywhere on it to start the valuation flow"                           | `Card`, with the whole container as the action                                                                                                                                           | **Never select.** Fails if it selects `Button Card`, which is available on no platform. **It has a usage doc, and a doc is not permission**                                                                                              |
| 33  | "The mobile menu for a consumer-content site, opened from the icon in the top bar"                                   | `Burger menu`                                                                                                                                                                            | **Never select.** Fails if it selects `Burger menu (profil)`, whose name reads as the better fit for consumer content and is forbidden                                                                                                   |
| 34  | "A panel letting the user switch the site's language and reach their profile"                                        | `Navigation bar`, whose own controls include the language menu                                                                                                                           | **Never select**, provisional entry. Fails if it selects `Menus`, which is exactly this and is withheld                                                                                                                                  |
| 35  | "Hold every listing photo to a 4:3 ratio across the results grid"                                                    | Nothing to place. Hold the image to its ratio in the layout itself                                                                                                                       | **Never select.** Fails if it selects `Image Ratio`, a Figma-internal helper for designers                                                                                                                                               |
| 36  | "Add one more filter control beside the existing filter row on the results page"                                     | Select `Filter bar`, then configure its filter buttons inside it                                                                                                                         | **Never select.** Fails if it places `Filter button` or `Filter dropdown container` beside the bar. They are its parts, never components placed next to it                                                                               |
| 37  | "Reuse the small colour-and-label key from inside the donut chart, on its own, beside a table"                       | Nothing. It is an internal part of the chart                                                                                                                                             | **Platform limits**, *Figma*. A dot-prefixed name is never placed, never rebuilt by hand, never copied out of its parent                                                                                                                 |
| 38  | "Let the user move between Search, Favourites, Messages and Profile **in the iOS app**"                              | `Navigation Bar (App)`                                                                                                                                                                   | **Which component** + **Platform limits.** Two separate components, not one with two platforms. Fails if it reaches the web bar first, or answers `Tabs`                                                                                 |
| 39  | "On the desktop site, the Buy entry in the top navigation opens a full panel of sub-links"                           | `Mega menus`, together with `Navigation bar`                                                                                                                                             | **Which component**, the web navigation as one system. From 1024 up. Fails if it returns only the bar                                                                                                                                    |
| 40  | "The same site at 375 wide — the navigation collapses behind an icon"                                                | `Burger menu`, together with `Navigation bar`                                                                                                                                            | **Which component.** The width decides, and it is never a free choice between the two panels                                                                                                                                             |
| 41  | "Ask the user whether this search result was useful — a thumbs up or thumbs down"                                    | `Feedback thumb buttons`, **and the run reports the selection**                                                                                                                          | **Built outside the design system.** Fails if it returns the component with no report line. Web only                                                                                                                                     |
| 42  | "Show how strong a seller lead is, on the agent's dashboard"                                                         | `Score tag`, **and the run reports the selection**                                                                                                                                       | **Built outside the design system** + **Which component** — the seller-lead-scoring case, vs `Tag` for any other label                                                                                                                   |
| 43  | "A control in the site footer for downloading the mobile app from the App Store"                                     | `Badge store`                                                                                                                                                                            | **Which component** — vs `Link` for any other link, and vs `Badge`, a different component one word away                                                                                                                                  |
| 44  | "The email address is filled in wrongly, and the message must sit under that field"                                  | `State message`                                                                                                                                                                          | **Which component** — attached to one form field, vs `Feedback message` for a whole section                                                                                                                                              |
| 45  | "The saved-search list is being fetched, and the area needs to show the wait"                                        | `Loading state`                                                                                                                                                                          | **Which component** — waiting, vs `Info state` for empty, failed or succeeded                                                                                                                                                            |
| 46  | "Step through the twelve photos of a property, photos and nothing else"                                              | `Image slider`                                                                                                                                                                           | **Which component** — images only, vs `Carousel` for slides of mixed content                                                                                                                                                             |
| 47  | "Ask the user to rate the valuation flow from one to five"                                                           | `Feedback bar`                                                                                                                                                                           | **Which component**, *Asking the user for something* — a notation on a scale, vs `Feedback thumb buttons` for a like                                                                                                                     |
| 48  | "Show the average score this agency has received from past clients"                                                  | `Rating`                                                                                                                                                                                 | **Which component** — displaying results that already exist, vs the two components that ask for an opinion                                                                                                                               |
| 49  | "The user types their move-in date, and no calendar is offered"                                                      | `Date field`                                                                                                                                                                             | **Which component** — typed, vs `Date picker` where a calendar view is wanted                                                                                                                                                            |
| 50  | "Save and Cancel, anchored at the foot of a long listing-creation form"                                              | `Button bar`                                                                                                                                                                             | **Which component** — up to two actions at the foot of a form or flow, vs `Button group` in normal page flow                                                                                                                             |
| 51  | "Share and Favourite, floating over the photo at the top of a listing"                                               | `Floating button group`                                                                                                                                                                  | **Which component** — floating above scrolling content, vs `Button group` in normal page flow                                                                                                                                            |
| 52  | "A mortgage simulator: the user adjusts amount, rate and duration, and the monthly payment updates in front of them" | **No component is this block.** Compose the controls from `Slider`, `Counter field` or `Text field`, present the result with `KPI`, **and declare it**                                   | **Which component**, *Computing a figure from user input* + **When nothing fits.** Fails if it selects `Estimation card` or `Wizard`, and fails if it composes without declaring                                                         |
| 53  | "The same simulator, where the figure it produces is the property's estimated price"                                 | **Two halves.** `Estimation card` for the result, composed and **declared** controls for the adjustment                                                                                  | **Highest tier first** + **When nothing fits.** Fails if it hand-builds the result block, and fails if using the Experience for one half is treated as exempting the other                                                               |
| 54  | "Confirm before deleting a listing, blocking, **in the iOS app**"                                                    | `Pop-up` for a short confirmation                                                                                                                                                        | **Which component** + **Platform limits.** `Pop-up` is apps only. Its overlap with `Modal bottom sheet` is unsettled, so `Modal bottom sheet` also passes; a web answer fails. Pairs with row 17                                         |
| 55  | "Show what share of the leads came from each of four channels"                                                       | `Donut chart`                                                                                                                                                                            | **Which component**, the chart branch — parts of a whole, vs `Bar graph` across categories and `Line chart` over a continuous axis                                                                                                       |
| 56  | "That donut has four segments and the reader needs to know which is which"                                           | Switch the chart's **legend** on. There is no legend component to place                                                                                                                  | **Which component**, *Legend* + **Platform limits**, *not components*. **Mandatory at two or more segments.** Fails if it searches for a legend to place                                                                                 |
| 57  | "Put that key underneath the donut rather than beside it"                                                            | Not possible. Beside is the only placement the library offers, and it is correct output                                                                                                  | **Platform limits**, *Where a chart's legend sits*. Fails if it composes a below-placed legend by hand, and fails if it reports this as a finding                                                                                        |
| 58  | "A small info icon beside the DPE label that the user can press for an explanation"                                  | The icon sits inside a control that carries states, a hit area and an accessible name — `Button`, `Text Button`, `Link`, `Chip`, `Floating Button Group`, or a component's own icon slot | **Icons.** A bare icon is never interactive, and **a tooltip may never be triggered by one**                                                                                                                                             |
| 59  | "An onboarding step asking which of 14 property types the user is looking for, with nothing else on the screen"      | `Radio button group`, **and the count recorded in the run's `## Declarations`**                                                                                                          | **Which component** — the 10-option ceiling's one named exception. Fails if it routes to `Dropdown`, and fails if it returns the group without recording why                                                                             |
| 60  | "Let the user pick which floor of the building their apartment is on, ground floor included"                         | `Floor selection` (Experience)                                                                                                                                                           | **Highest tier first, all-or-nothing.** Fails if it composes a list or a dropdown of floor numbers                                                                                                                                       |
| 61  | "A property summary needing a layout the standard summary card cannot produce"                                       | `Listing summary` (Experience)                                                                                                                                                           | **Highest tier first.** Fails if it composes `Card` + `Image slider` + `Tag` because `Listing Card` did not fit                                                                                                                          |
| 62  | "A count of unread messages sitting beside a section title, not attached to any control"                             | `Badge`, standing alone                                                                                                                                                                  | **Which component.** The anchored use is the common one; **the standalone use is open, not exceptional.** Fails if it rules `Badge` out for having no host                                                                               |
| 63  | "A control in the middle of a paragraph of body copy that opens the full terms"                                      | `Link`                                                                                                                                                                                   | **Which component.** `Text button` stands on its own and is **never inline**. Fails if the "less weight than a button" reading wins over the placement                                                                                   |
| 64  | "A page frame stacking a hero, a results list and a footer, where every block inside it is already declared"         | **No declaration for the frame itself**                                                                                                                                                  | **When nothing fits**, *what needs declaring*. A frame that only stacks does no job of its own. Fails if it writes a declaration nobody can review — no problem heading covers stacking, and there is no container component to rule out |

## Scoring

| Band | Meaning |
| --- | --- |
| 64/64 | The ruleset is doing its job |
| 56–63 | Usable. Fix the missed rows before extending **Which component** |
| ≤55 | The ruleset is not yet the single entry point. Do not point agents at it |

**Intents 28–64 were first run on 2026-09-23, in run 4.** Rows 28–31 were added on 2026-09-08 with
**Highest tier first**'s parts list, to probe the container and all-or-nothing
kinds and the `Table` platform caveat. **Rows 32–64 were drafted on 2026-09-23**,
one per rule written after the last run and reached by no existing intent — the
never-select rulings, the navigation family, the built-outside-the-design-system
flag, the nine components documented on 21 and 22 September, the two Experiences
runs 1–3 never reached, and the chart, legend, icon and declaration rules.

Runs 1–3 scored against the first 27 only, so **their scores are not comparable
to a 64-intent run.** Run 4 is the first 64-intent score, and the only one a
later 64-intent run may be compared against.

**Row 17 was corrected on 2026-09-23, and its old expected answer would have
scored a pass on an answer the ruleset forbids.** It accepted `Pop-up` for a
short blocking confirmation **on web**. `Pop-up` became apps-only on 21 September
2026, and **Which component** now sends a web confirmation to `Modal bottom
sheet`. Row 54 tests `Pop-up`'s own case, in an app.

Record each run below.

## Runs

| Date | Score | Misses | Fix applied |
| --- | --- | --- | --- |
| 2026-09-08 · run 1 | **22/22** | None. Two answers reached at low confidence (#2, #20), one at medium (#9) | Four ruleset defects the score did not catch — all fixed, see below |
| 2026-09-08 · run 2 | **27/27** (5 new intents added) | None. Run 1's fixes moved #2 and #9 to high confidence | Five more defects, including a **Highest tier first** / **Which component** contradiction introduced by run 1 — all fixed |
| 2026-09-08 · run 3 | **10/10** focused | None. Both run-2 fixes confirmed working, quoted back by the agent | Three more defects — `Pop-up` missing from **Which component**, `Charts` unbranched, **Highest tier first** threshold qualitative — all fixed |
| 2026-09-23 · run 4 | **60/64** — first run of all 64 | #29, #41, #42, #54. Two are the ruleset's fault, two are this file's | **None applied.** Three ruleset defects found and still open on 2026-10-08, see below |

### Run 1 — 2026-09-08

A cold agent given only `components-rules-ai.md` answered all 22 correctly, with
the correct rule each time, including the three traps (17 Alert-on-web, 20 Cell
Content, 21 Card grid) and both **Highest tier first** tier cases (18, 19).

**The score hid four real defects.** A perfect score reached by forcing an answer
is not a working ruleset — these came from the agent's own friction report:

| Defect | Fix |
| --- | --- |
| **`Badge` was absent from **Which component** entirely.** It sat in the **The inventory** inventory with no routing to it, so "New" on a listing had two plausible answers (`Tag`, `Badge`) and zero criteria between them | Added a `Badge` row under *Providing feedback and status*, split from `Tag` on whether the marker is attached to a host or stands alone in the layout |
| **No case for revealing content in place.** "Read more" under truncated text — an extremely common listing pattern — had no anchor; the agent forced it into the button-weight branch | Added a `Text button` row under *Grouping and structuring content* |
| **Never select told the agent to "select the Card or list", but no `List` component exists** in any of the four libraries | Rewrote the `Cell Content` row: names `Card` and `Table` as the real containers, states plainly that there is no `List` component, and reframes Cell content as what you build rows *from* rather than something banned |
| **No precedence when an intent matched several rows.** "Long list" appears as the *Otherwise* of three different rows | Added a five-step precedence order at the top of **Which component** |

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
| **Highest tier first contradicted Which component.** **Highest tier first**'s table said "a filter row from Chips or Buttons → Filter bar", while **Which component**'s Filter bar row says "lightweight inline filters without dropdown panels → Chip group". Since **Highest tier first** "wins whenever both apply", an agent following precedence literally reached the *wrong* component | Narrowed the **Highest tier first** row to a **structured, multi-criteria** filter panel, and added a "What **Highest tier first** does not cover" table: when **Which component** routes to a **lighter** component for a smaller version of the same job, that is not a **Highest tier first** violation |
| **No container existed for a plain list.** **Never select** offered only `Card` or `Tables`, neither of which is a settings screen or an index list, while stating no `List` component exists | Added a **Which component** row for **a list you lay out yourself, of `Cell content` rows**, stating explicitly that this is the intended pattern rather than a workaround, and softened **Never select** to match |
| **`Toggle group` vs. hand-built rows of toggles was unresolved** — two paths producing identical UI from different components | `Toggle group`'s row now names the settings-screen case and forbids hand-building the rows |
| **`Tag` vs `Badge` was example-driven, not rule-driven.** It resolved only because the word "New" appeared in Tag's row; "Verified" would have been ambiguous | Replaced the examples with a structural test — does the marker **hold its own place in the layout flow** (Tag) or is it **anchored to a host component's geometry** and meaningless without it (Badge) |
| **`Tooltip` had no first-class row**, reachable only via Coach mark's *Otherwise* | Given its own row under *Providing feedback and status* |

Still open, and tracked in the audit rather than the ruleset: seven components
are marked *Undescribed* in **The inventory**, so for those the ruleset knowingly points
outside itself. See [components-rules-ai-audit.md](components-rules-ai-audit.md)
open question 2.

### Run 3 — 2026-09-08 · focused

Ten intents targeting only what Run 2's fixes changed, plus two direct questions
asking the agent to quote the rule that decides a contested case.

**10/10.** Both fixes confirmed working, in the agent's own words:

- On the **Highest tier first** / **Which component** precedence — the inline-filter case is *"pre-adjudicated,
  not left to inference"*.
- On `Tag` vs `Badge` — *"the test is general, not word-matching"*. It noted that
  an agent pattern-matching on the example words would still pass, but would
  misclassify a "Verified" marker overlapping a card corner, which the geometry
  test correctly sends to `Badge`.

Three further defects found and fixed:

| Defect | Fix |
| --- | --- |
| **`Pop-up` had no **Which component** row.** It existed only in the **Highest tier first** exception table and the inventory, so an agent reading **Which component** as the flat decision table — which is how the ruleset describes itself — would never find it. Nothing separated a short web confirmation between `Pop-up` and `Modal bottom sheet` | Gave `Pop-up` its own row under *Overlaying content*, and rewrote `Alert`'s web fallback to split on content size rather than sending everything to `Modal bottom sheet` |
| **`Charts` was one row for three chart types**, with no branching. The Bar / Line / Donut distinction existed only in **The inventory**'s inventory strings, which **Which component** never pointed to | Split into four rows — `Bar graph`, `Line chart`, `Donut chart`, `Legend` — each with its own trigger and redirects |
| **The **Highest tier first** threshold was qualitative** — "the full job" vs "a lighter version" gave no operational test, so two agents could disagree and both cite the text | Added **count the parts**: two or more of the higher-tier component's own moving parts means **Highest tier first**; one part means **Which component**. With a worked table for `Filter bar` and `Wizard` |

Accepted, not fixed: the five-step precedence ladder is stated once at the top of
**Which component** rather than repeated per row. Repeating it 51 times would bloat the table
for a reader that always has the whole file in context.

### Run 4 — 2026-09-23

The first run of all 64 intents. A cold agent on **Sonnet**, given the 64 intents
with the Expected column removed and told to read `components-rules-ai.md` and
nothing else. **It made one tool call and read one file**, which is the evidence
that the run was cold and not merely instructed to be.

**Sonnet was chosen on purpose.** A stronger reader silently repairs an ambiguous
rule, which is the weakest version of a test built to find ambiguity.

**60/64 — band: usable.** Four misses, and they are not four faults of one kind:

| Row | Expected | Answered | Whose fault |
| --- | --- | --- | --- |
| 41 | `Feedback thumb buttons`, and the run reports the selection | `Feedback thumb buttons`, no report line | **The ruleset.** The obligation is written — *"Select it. Report that you did"* — but in the separate **Built outside the design system** section, never in the component's own **Which component** row. The agent found the row, named the component and stopped |
| 42 | `Score tag`, and the run reports the selection | `Score tag`, no report line | **The ruleset.** Same cause as row 41 |
| 29 | `Table`, flagged as *Figma-ready, web in progress* | `Table`, no caveat | **This file.** *"Web in progress"* appears nowhere in the ruleset, so the row expects a fact the agent cannot have. **Row 29 is defective as written** |
| 54 | `Pop-up`, or `Modal bottom sheet` | `Alert` | **This file, and the ruleset behind it.** The intent says *"Confirm before deleting"*. `Alert`'s row says *"expecting a decision back — an answer, a confirmation, a choice"*, and `Pop-up`'s row says *"a short confirmation"*. Both rows claim the case, so the intent cannot isolate `Pop-up`. **Row 54 is defective as written** |

**Rows 29 and 54 are left unchanged, on purpose.** Neither can be rewritten
correctly yet:

- **Row 29** waits on where availability lives. Gabriel decided on 2026-09-24
  that it lives in each component doc's readiness table and not in the ruleset.
  A run that reads only the ruleset therefore cannot be asked about availability
  at all, so this row is rewritten or removed once the ruleset's **Platform
  limits** section follows that decision.
- **Row 54** waits on a rule that separates `Pop-up` from `Alert`. No such rule
  exists, and it is Gabriel's to write.

**Score a later run against 62, not 64, until both rows are repaired** — and say
so beside the score.

**Three ruleset defects, none of them fixed. Verified still present on
2026-10-08:**

| Defect | Found by |
| --- | --- |
| **The report obligation for a component built outside the design system is not in that component's own row.** It is in a separate section the agent did not reach | Rows 41 and 42 |
| **`Info state` and `Loading state` both claim full-area loading.** `Info state`'s row lists *"empty, error, success, loading"*; `Loading state`'s Otherwise sends *"empty, failed or succeeded rather than waiting"* to `Info state`. Nothing says which one owns full-area waiting | The agent, unprompted, in its own friction report. It answered row 45 correctly and flagged that the two rows overlap |
| **`Pop-up` and `Alert` both claim a confirmation**, and both are available in apps | Scoring row 54 |

**Three things the agent looked for and could not find.** None is a
contradiction:

- A rule for a panel that switches language **and** reaches the profile. `Menus`
  is never-select and reroutes to `Navigation bar` for the language menu; the
  profile half is addressed nowhere. Row 34, answered correctly at medium
  confidence.
- Which control the info icon beside a bare label sits inside. The **Icons**
  section lists the kinds of control and not which applies here. Row 58.
- The widths behind the breakpoint names `XXS`, `XS` and `SM`, which the ruleset
  uses and does not define.

**What this run does not prove.** It proves the ruleset can be followed to the
expected answer on 60 intents by one reader on one day. It proves nothing about
whether a rule is true of the design system — every expected answer here was
written from the ruleset itself.

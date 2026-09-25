# Component rules for AI generation

_The authoritative ruleset for choosing **which component** when generating a GSL
interface. Read this before opening any component page — the component pages say
how to use a component, this says which one to reach for. Evidence and rejected
options are in `components-rules-ai-audit.md`, which a generating agent must
not read. Full inventory: [components-index.md](components-index.md)._

This page is written for machine consumption. Each section maps a design
decision to one component.

**The six rules, in precedence order.** Apply them in this order and stop at the
first that decides your case. The rules have names rather than numbers, because a
number encoded nothing this list does not already state.

**Precedence order is not page order.** **Which component** appears second on
the page because it is the bulk of the ruleset, but **Platform limits** is
checked before it: a component unavailable on your target platform is not a
candidate, however well it fits the problem.

| Rule | Decides |
| --- | --- |
| **Highest tier first** | Am I about to rebuild something that already exists one tier up? |
| **Platform limits** | Is this component available on my target platform? |
| **Which component** | Which control solves this problem? |
| **Never select** | Is this even mine to place? |
| **The inventory** | Does the component I have in mind exist at all? |
| **When nothing fits** | Nothing fits — what now? |

---

## Highest tier first

*Reach for the highest tier that fits.*

GSL is four Figma libraries, in increasing order of assembly:

```
Foundations  →  Components  →  Patterns  →  Experiences
   tokens,        Button,       Filter bar,   Listing Card,
   icons          Chip          Wizard        Map template
```

**Search from the right.** Before composing anything out of Components, check
whether a Pattern or an Experience already is the thing you are about to build.

| You are about to build | Stop — this already exists | Kind |
| --- | --- | --- |
| A property summary card | `Listing Card` (Experience) | composed |
| A **structured, multi-criteria** filter panel | `Filter bar` (Pattern) | composed |
| A step-by-step flow | `Wizard` (Pattern) | composed |
| A phone input with a country prefix | `Phone Number Field` (Experience) | composed |
| An empty / error / success / loading screen | `Info State` (Pattern) | container |
| A map screen | `Map template` (Experience) | all-or-nothing |
| A data grid | `Table` (Experience) | container |
| A floor picker | `Floor selection` (Experience) | all-or-nothing |
| A more flexible property summary than Listing Card allows | `Listing summary` (Experience) | composed |
| A price estimation block | `Estimation card` (Experience) | unresolved |

### The Kind column, and what each kind asks of you

**The Kind column tells you how to use the component, not how to build one.**
Every row above is a component you place; none of them is ever assembled by hand.

| Kind | What it is | What it asks of you |
| --- | --- | --- |
| **Composed** | Assembled from public components | Place it whole. Assembling the same thing from `Card`, `Chip` or `Tabs` yourself is the failure this rule exists to stop |
| **Container** | A shell you place content into. `Info State` is closer to a modal with prescribed content than to an assembly | Place the shell, then fill its slots. `Table` takes `Cell Content` rows; do not build the shell around them |
| **All-or-nothing** | Used whole or not at all. A partial `Map template` is not a realistic build | Take the whole thing or nothing. `Map template`'s own pin sets are on the **Never select** list and are reached by placing it |
| **Unresolved** | Nobody has established which of the other three it is | Treat it as all-or-nothing and place it whole. If it will not do what you need, follow **When nothing fits** rather than guessing at its parts |

**Highest tier first applies to every kind, unresolved included.** The Kind
changes how you place the component; it never changes whether you must reach for
it.

Composing from a lower tier when a higher-tier component exists is the single
most common compliance failure. **Which component** below is flat by design — it answers
"which control", not "which tier". **Highest tier first wins over Which
component whenever both apply.**

**What Highest tier first does not cover.** It fires when you would be rebuilding the
higher-tier component *in full*. It does not fire when **Which component** deliberately routes
you to a **lighter** component for a smaller version of the same job. These are
not violations:

| **Which component** sends you to | Rather than | Because |
| --- | --- | --- |
| `Chip group` | `Filter bar` | Inline filters with no dropdown panels — not a structured multi-criteria panel |
| `Pop-up` | `Modal bottom sheet` | A small amount of content |
| `Tabs` | `Wizard` | Independent sections, not sequential steps |

When **Highest tier first**'s table and a **Which component** *Otherwise* branch both match, and the **Which component**
branch names a **simpler** component for an explicitly **lighter** case, follow
**Which component**.

**The operational test — count the parts.** **Highest tier first** fires when your build would
need **two or more** of the higher-tier component's own moving parts. One part
alone is the lighter case, and **Which component** wins.

**This test applies to the composed kind only.** For a container, an
all-or-nothing or an unresolved component there are no parts to count, and
**Highest tier first** applies regardless of how much of it you were about to
rebuild.

**The parts counted here are capabilities, not components.** *Filter controls*,
*dropdown panels* and *applied-state handling* are three things the thing you are
building would have to do. Never try to count which library components an
imitation would contain — that list is not written anywhere, on purpose.

| You would build | Parts | Rule |
| --- | --- | --- |
| Filter controls **and** dropdown panels **and** applied-state handling | 3 | **Highest tier first** → `Filter bar` |
| A row of filter chips, nothing else | 1 | **Which component** → `Chip group` |
| Sequential steps **and** progress **and** step gating | 3 | **Highest tier first** → `Wizard` |
| Switchable sections, no sequence | 1 | **Which component** → `Tabs` |

---

## Which component

*Choose by the problem being solved.*

Find the row whose **When** matches your situation. If your situation differs,
follow **Otherwise**. Organised by problem, not by component category.

**When an intent matches more than one row**, apply in this order and stop at the
first that decides it:

1. **Highest tier first** — a Pattern or Experience already is the whole thing. Wins outright.
2. **Platform limits** — a platform limit forbids the obvious answer.
3. **The narrower trigger wins.** "Filtering a SERP with structured panels"
   beats "multi-select outside a form"; "a date" beats "single-line input".
4. **Inside a form beats outside it.** Form context selects the form component
   (`Checkbox group` over `Chip group`, `Radio button group` over
   `Segmented control`).
5. Still tied → pick either and **declare the tie** under **When nothing fits**.

### Triggering actions

| Choose | When | Otherwise |
| --- | --- | --- |
| **Button** | The user triggers an immediate action — save, submit, share, open a modal | Navigation → **Link** · Full button weight is visually too heavy → **Text button** · Prominent navigational entry point with icon or illustration → **Card**, with the whole container as the action · Choosing from a set of related options → **Button group** |
| **Button bar** | Up to two buttons anchored at the foot of a form or flow, sticky or not | The buttons sit in normal page flow → **Button group** · Two or three actions floating over content → **Floating button group** · A single action → **Button** |
| **Floating button group** | Two or three actions that float above scrolling content, typically overlaying media or a map | The actions sit in normal page flow → **Button group** · A dropdown list of contextual actions → **Action menu** · A single action → **Button**, floating |
| **Link** | The intent is navigation to another page or section — not action | An action is triggered → **Button** · Navigation needs button weight, e.g. an empty-state CTA → **Button**, tertiary |

### Selecting a single value

| Choose                 | When                                                                                                                                                                                                                                                    | Otherwise                                                                                                                                                                                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Radio button group** | Mutually exclusive choices in a form. **The limit is label readability, not a count**: up to 5 options in one column; 6 to 10 in two columns, when every label fits 2 lines or fewer on mobile. In one column a label may run to 3 lines, 2 recommended | More than 10 options, or labels too long for the column count → **Dropdown** · Prominent visual treatment preferred → **Button group** (single-select) · Options benefit from icons or illustrations → **Select card group** (single-select) · Switching views rather than submitting a value → **Segmented control** |
| **Dropdown**           | Single-select from a list in a form, or space too constrained to show options inline                                                                                                                                                                    | 10 options or fewer, and the labels are short enough for the column count → **Radio button group** · Long list where typing to filter helps → **Autocomplete** · Items trigger actions rather than set a value → **Action menu**                                                                                      |
| **Segmented control**  | Switching between mutually exclusive view modes or display options — not a form value                                                                                                                                                                   | The choice is a form value → **Button group** · Switching full content sections → **Tabs** · Standard form styling needed → **Radio button group**                                                                                                                                                                    |

**The 10-option ceiling on a radio button group has one exception.** When the choice is the whole screen, with no competing content — an onboarding step, for example — the count may go higher. **Record it in the run's report**, in the same `## Declarations` section **When nothing fits** uses, stating the count and why the screen carries nothing else. **Anywhere the screen holds other content, the ceiling holds.**

### Selecting multiple values

| Choose | When | Otherwise |
| --- | --- | --- |
| **Checkbox group** | Multi-select in a structured form | Few options and prominent visual treatment preferred → **Button group** (multi-select) · Options benefit from card layout → **Select card group** (multi-select) · Long list or constrained space → **Dropdown** · Lightweight selections outside a form → **Chip group** |
| **Chip group** | Lightweight multi-select filtering or input outside a structured form | Inside a structured form with labels and helper text → **Checkbox group** · Constrained space or numerous options → **Dropdown** · Filtering a SERP or data table with structured panels → **Filter bar** · The element is non-interactive → **Tag** |
| **Select card group** | Form selection benefits from a visual, card-based layout with icons or illustrations | Simpler single-select → **Radio button group** · Simpler multi-select → **Checkbox group** · The intent is navigation, not selection → **Card**, with the whole container as the action |

### Filtering content

| Choose | When | Otherwise |
| --- | --- | --- |
| **Filter bar** | Narrowing search results or table content using structured criteria — SERP or data page | Lightweight inline filters without dropdown panels → **Chip group** · A single filter criterion inside a form → **Dropdown** · Triggering filter-related actions rather than setting criteria → **Action menu** |

### Entering text

| Choose | When | Otherwise |
| --- | --- | --- |
| **Text field** | Short, single-line free-form input | Multi-line or longer than a sentence → **Text area** · Suggestions appear as the user types → **Autocomplete** · Numeric with increment/decrement controls → **Counter field** · A date, picked from a calendar → **Date picker** · A date the user types, with no calendar → **Date field** |
| **Text area** | Multi-line free-form text — descriptions, comments, messages | Single-line → **Text field** · Attaching a file → **Media upload** |
| **Autocomplete** | The user types to filter and select from a large or dynamic dataset | No suggestions needed → **Text field** · Fixed options selected without typing → **Dropdown** |
| **Date field** | The user types a date and no calendar is offered | A calendar view is wanted → **Date picker** · Free-form text that is not a date → **Text field** |

### Entering numeric values

| Choose | When | Otherwise |
| --- | --- | --- |
| **Counter field** | Numeric values adjusted with +/− controls | Range selection where an approximate value is acceptable → **Slider** · Direct numeric text entry without controls → **Text field** · Only a small fixed set of values → **Dropdown** |
| **Slider** | Selecting a value or range along a continuous scale | Precision and exact entry matter → **Counter field** · Only discrete values available → **Dropdown** |

### Computing a figure from user input

| Choose | When | Otherwise |
| --- | --- | --- |
| **No component is this block — compose it, and declare it** | The user adjusts a set of controls and a figure recalculates in front of them: a mortgage or affordability simulator, a yield estimator, a fee calculator. **No Pattern and no Experience is this block** — the libraries were searched. Build the controls from **Slider**, **Counter field** or **Text field**, present the result with **KPI**, and follow **When nothing fits** to the end, including its declaration step | The figure is shown and the user cannot change it → **KPI** · That figure is a property price estimate → **Estimation card**, see **Highest tier first** · The user advances through ordered steps rather than adjusting freely → **Wizard** · The controls narrow a list of results rather than produce a figure → **Filter bar** |

**`Estimation card` is the near miss. It is not this.** It presents a completed
estimate — price range, confidence, selling or renting — and carries no controls
to adjust. A simulator whose result happens to be a property price estimate is
**two halves**: the result half is `Estimation card` and **Highest tier first**
applies to it normally; the controls half has no component and is composed and
declared. Using the Experience for the half it covers is not a reason to skip
declaring the half it does not.

**Composing here is still invention.** Assembling existing components into a
block the libraries do not have is exactly what **When nothing fits** governs, so
work its order rather than jumping to the build: re-check the higher tiers,
re-check **The inventory**, then compose, then declare. An undeclared simulator
is a compliance failure even when every part inside it is a real component.

### Binary choices and toggles

| Choose | When | Otherwise |
| --- | --- | --- |
| **Toggle** | A binary on/off setting that takes effect immediately — settings, preferences | The setting is submitted as part of a form → **Checkbox** |
| **Toggle group** | Multiple independent on/off settings, grouped — including a settings screen where every row is one immediate setting. **Use the group; never hand-build rows of individual toggles**, which looks identical and is not the component | Settings are part of a form submitted later → **Checkbox group** · Switching between views rather than toggling settings → **Segmented control** · Only some rows carry a setting, the rest are navigation → a list you lay out yourself, of **Cell content** rows |

### Showing context-specific actions

| Choose | When | Otherwise |
| --- | --- | --- |
| **Action menu** | A dropdown list of contextual actions, primarily on desktop | Mobile (XXS/XS) or in apps → **Modal bottom sheet menu** · Selecting a form value rather than triggering actions → **Dropdown** · All options always visible, ≤7 → **Button group** |
| **Modal bottom sheet menu** | A list of contextual actions on mobile or in apps | Desktop, SM and above → **Action menu** · Content richer than a simple action list → **Modal bottom sheet** |

### Overlaying content

| Choose | When | Otherwise |
| --- | --- | --- |
| **Modal bottom sheet** | Contextual content must overlay the screen and block interaction | Content is a simple action list → **Modal bottom sheet menu** · Content should persist on the page → **Card** · An immediate, blocking decision is required → **Alert** |
| **Pop-up** | A **small** amount of blocking content — a short confirmation, a brief message, one or two buttons. **Apps only — iOS and Android.** Gabriel, 21 September 2026 | The screen is on the web → **Modal bottom sheet** · The content is long, scrollable, or rich → **Modal bottom sheet** · It is a plain list of actions → **Modal bottom sheet menu** · It is not blocking → **Snackbar** or **Feedback message** |
| **Alert** | **Alerting the user and expecting a decision back** — an answer, a confirmation, a choice. It is a modal with a fixed design, so that **every alert in the product looks the same**. Gabriel, 21 September 2026 | Transient, non-blocking feedback → **Snackbar** · Inline, non-blocking contextual guidance → **Feedback message** · The content is rich rather than a single decision → **Modal bottom sheet** |

**`Alert` is not built on web, and can be replicated there.** Gabriel,
21 September 2026. Until it is built, a web alert is assembled from `Modal
bottom sheet`, keeping the alert's fixed shape: the message, and the buttons
that answer it. **Replicating a component this rule sends you to is not an
invention** and does not need declaring under **When nothing fits** — say which
component you assembled it from, and move on.

**`Pop-up` is for apps only, and is under investigation.** Gabriel,
21 September 2026. It overlaps `Modal bottom sheet`, which carries a `Type`
property whose options are `Modal` and `Bottom Sheet` and covers iOS and Android
already. **Which of the two is right for an app is not settled**, and there is no
`Pop-up` doc on purpose until it is. On web the question does not arise: use
`Modal bottom sheet`.

### Grouping and structuring content

| Choose | When | Otherwise |
| --- | --- | --- |
| **Card** | Visually grouping related content in a cohesive container | Content should be collapsible → **Accordion** · Content overlays the screen → **Modal bottom sheet** · The whole container is a single navigational action → that is **Card**'s own job; build it as a Card |
| **Accordion** | Content needs progressive disclosure in a persistent expandable list | Content should always be visible → **Card** · Sections are mutually exclusive views → **Tabs** |
| **Divider** | Visually separating content sections or list items where spacing alone is insufficient | — |
| **Text button** | An action needing less weight than a button, standing on its own and **never inline**. **Built for an alignment constraint** — `Button` carries horizontal padding, so a tertiary button below a block of text does not line up with it, and a text button has no horizontal padding. Revealing more content in place — "Read more", "Show all 12 photos" — is one common use, not the whole job | The control leaves the page → **Link**, which is underlined and so reads as taking the user somewhere · The control sits inside a sentence or in body copy → **Link** · The content collapses back into a persistent expandable list → **Accordion** · Submitting or resetting a form → **Button**, primary emphasis for the submit |
| **A list you lay out yourself, of `Cell content` rows** | A plain list — settings, an index, a menu — that is neither one grouped visual block nor tabular data. **There is no `List` component in any library; laying the rows out yourself is the intended pattern, not a workaround** | The rows are tabular and comparable → **Tables** · The rows belong inside one visual container → **Card** · The whole block is a single action → **Button card** · Every row carries an immediate on/off setting → **Toggle group** |
| **Carousel** | Users browse a horizontal collection of items one by one. **Web only** | All items should be visible simultaneously → a grid layout, **not a component** — see **Platform limits** |

`Cell content` is **not a choice** — it is a composition slot inside Cards and
lists. See **Never select**.

### Navigating between pages and sections

| Choose | When | Otherwise |
| --- | --- | --- |
| **Tabs** | Organising related content at the same hierarchy level into switchable views | Switching view modes within a single content area → **Segmented control** · Steps must be completed in sequence → **Wizard** · Switching between top-level destinations → **Navigation bar** |
| **Wizard** | Guiding users through a sequential multi-step process | Sections are independent and non-sequential → **Tabs** · Showing task completion without step-by-step input → **Progress bar** |
| **Breadcrumb** | Showing hierarchical location and allowing navigation up the hierarchy. **Web only** | The primary need is page title and actions → **Top bar** · Top-level global navigation → **Navigation bar** |
| **Pagination** | Dividing large result sets into numbered pages. **Web only** | Mobile and apps → infinite scroll, a **behaviour, not a component** — see **Platform limits** |
| **Top bar** | Page-specific title, context, and actions | Global site navigation → **Navigation bar** |
| **Mega menus** | Top-level navigation on the main B2C or B2B websites, or staying compliant with what the real product ships | Global navigation inside a product screen → **Navigation bar** · The mobile menu behind the burger icon → **Burger menu** |
| **Burger menu** | The mobile navigation menu opened from the navigation bar's burger icon | Navigation stays visible across the top → **Navigation bar** · A list of contextual actions rather than navigation → **Action menu** on desktop, **Modal bottom sheet menu** on mobile |
| **Navigation bar** | Global navigation to top-level site destinations (web) | Top-level navigation on the main B2C or B2B websites → **Mega menus** · Sub-pages and flows → **Top bar** · In-app navigation → **Navigation Bar (App)**, mobile only |
| **Navigation Bar (App)** | **The main way a user navigates an app** — moving between its top-level destinations, on iOS and Android. That is the whole of it. Gabriel, 21 September 2026 | The screen is on the web → **Navigation bar** · Switching between views of one screen's content → **Tabs** · One screen's title and its actions → **Top bar** · A list of contextual actions rather than navigation → **Action menu** |

**The web navigation is three components, and choosing one means choosing the others.** Gabriel, 21 September 2026. `Navigation bar` is the bar; **`Mega menus` is what an entry opens on desktop**; **`Burger menu` is what replaces the mega menu on mobile**. An entry in the bar that opens nothing is half a design, so reach for the whole set. The width decides which of the two panels applies — mega menus from 1024 up, burger menu at 320 and 768 — and it is never a free choice between them.

**`Navigation bar` and `Navigation Bar (App)` are two components, not one with two platforms.** The web one is the row above; the app one is its own row. **Reaching the app component must not require considering the web one first** — an agent designing an app screen never looks at a web row. Gabriel, 21 September 2026.

**`Mega menus` is moving into the design system, not sitting outside it.** Gabriel, 21 September 2026, correcting the 18 September note. **The Figma was built by the design system team**, the component is **not stored here today**, and **the transfer is ongoing**. It is not built or maintained by the team on the development side. **Provisional** — 18 September 2026, to be confronted with the real product, as `Menus` is.

### Providing feedback and status

| Choose | When | Otherwise |
| --- | --- | --- |
| **Snackbar** | Brief, transient feedback confirming the outcome of a user action | Persistence and inline placement needed → **Feedback message** · Critical and blocking → **Alert** |
| **Feedback message** — the Figma library names this set `Feedback Messages` | Persistent inline contextual guidance or status within a section | Transient, action-triggered feedback → **Snackbar** · Full-area or page-level states → **Info state** · Feedback belonging to one form field → **State message** |
| **State message** — the Figma library names this set `state_message`, lowercase and underscored | Inline feedback **attached to a single form field** — guiding entry, correcting an error, or adding information under that field | Guidance for a section rather than one field → **Feedback message** · Transient confirmation of an action → **Snackbar** · Full-area state → **Info state** |
| **Info state** | Full-area states — empty, error, success, loading | Inline section-level messages → **Feedback message** · A blocking decision is required → **Alert** |
| **Tag** | A non-interactive status label or category that **occupies its own place in the layout flow** and would still make sense if the thing beside it were removed — "New", "Sold", "Exclusive", "Verified" | Seller lead scoring → **Score tag** · The element is interactive — selectable, filterable, removable → **Chip** · Status needs supporting text → **Feedback message** · The marker is anchored to another component's geometry → **Badge** |
| **Score tag** | A Tag specialised for seller lead scoring | Any other status or category label → **Tag** · An energy-efficiency rating → **Energy tag** |
| **Badge** | A marker — typically a count or a dot — **normally anchored to a host component's geometry**, overlapping or pinned to a button, tab label, menu entry or cell row. **It may also stand alone**, for a case no other component covers — a count beside a title, for example. The anchored use is the common one; the standalone use is open, not exceptional. Gabriel, 18 September 2026 | The marker is a status or category word rather than a count or a dot → **Tag** · It is interactive → **Chip** |
| **Loading state** | Content is being fetched and the wait needs its own element on the page — a spinner with an optional title and description | The area is empty, failed or succeeded rather than waiting → **Info state** · The wait belongs inside a control already on screen, such as a dropdown fetching its options → that component's own loading state, not this |
| **Tooltip** | A brief clarification of one UI element, shown on hover or tap — a single explanation, not a sequence | Persistent inline guidance not tied to a control → **Feedback message** · A guided, multi-step tour → **Coach mark** |
| **Coach mark** | Contextual onboarding overlays pointing at specific UI elements | Persistent inline guidance not tied to onboarding → **Feedback message** · A single brief clarification rather than a guided tour → **Tooltip** |

**A Tag's style comes from its role, never from how loud it should look.** Gabriel, 25 September 2026, from how the iOS and Android apps use tags today. The same table is in the Tag doc, under **Style by role**:

| What the tag says | Example labels | Style | Hierarchy | Icon |
| --- | --- | --- | --- | --- |
| **The item is new** — a listing just published | "New" | `Primary` | `Strong` | Yes — `fire` |
| **A feature is on trial** | "Beta" | `Information` | `Weak` | No rule. Add one only when it makes the meaning clearer |
| **The user's own history with this item** | "Seen", "Contacted" | `Light` | — | Yes. Choose it by the icon rules |
| **A neutral attribute of the item** | "Furnished", "3 rooms" | `Subdued` | — | No rule. Add one only when it makes the meaning clearer |
| **A system state** — something the system decided about the item | "Sold out", "Expired" | The status that matches the meaning: `Error`, `Success`, `Information` or `Warning` | `Strong` or `Weak`. No rule decides between them yet | No rule. Add one only when it makes the meaning clearer |

**`Dark` and `Secondary` have no role in this table.** If no row matches the tag's role, do not reach for either. Stop and report the tag's role as unmatched. **The surface behind the tag never chooses the style.** Swap to another style only when the role's style fails contrast on that surface, and report the swap with the reason.

### Asking the user for something

*The rows above tell the user something. These two ask.*

| Choose | When | Otherwise |
| --- | --- | --- |
| **Feedback bar** | Asking the user to **rate** something — a notation on a scale | A like or dislike rather than a score → **Feedback thumb buttons** · Telling the user something rather than asking → **Feedback message** or **Snackbar** |
| **Feedback thumb buttons** | Asking the user to **like or dislike** — a binary opinion, thumbs up or thumbs down | A score on a scale → **Feedback bar** · Telling the user something rather than asking → **Feedback message** or **Snackbar** |

**A notation against a like is the whole distinction.** Gabriel, 18 September 2026. They are separate
components and **the thumbs are not inside the bar**, though `Feedback bar` does carry its own button
group, an illustration slot and a pre-title.

**Neither is built on web**, and **no usage rules exist for the thumb buttons**. Use them when the
user's opinion is needed, until something better replaces them. Gabriel, 18 September 2026.

**`Feedback thumb buttons` is selectable, and selecting it is a signal.** The component was built
by a team outside the design system, kept because others might want it, and never brought in.
Gabriel, 21 September 2026. **An agent may still choose it** — the rule above decides when.
**What follows from choosing it:** more than one team needs the component, which is the condition
for adopting it into the design system properly. A run that selects it should say so in its report,
so the adoption question reaches Gabriel. **This is the only component in the design system on these
terms**, so far as Gabriel knows.

**`Feedback thumb buttons` is web only — never iOS, never Android.** Gabriel, 21 September 2026.
Checked live in the Components library the same day: the component set carries **no `Platform`
property**, its only axis is `Device` with `Desktop` and `Mobile`, and the page titles it
*"Feedback Thumb Buttons (Web)"*. `Desktop` and `Mobile` there are **web breakpoints**, not native
platforms. The component is also **not in the web code repo**, so it exists in Figma and nowhere
else.

**`Rating` is not in this section and is not an alternative to either.** It displays results that
already exist, from Opinion System, and is non-interactive. These two collect an opinion; `Rating`
shows one.

### Showing progress and data

| Choose | When | Otherwise |
| --- | --- | --- |
| **Progress bar** | Linear task or goal completion | A compact circular format fits better → **Progress circle** · Progress involves sequential user-input steps → **Wizard** |
| **Progress circle** | A single completion percentage in a compact circular format | A linear format fits the layout better → **Progress bar** |
| **KPI** | A single key metric value needs prominent standalone display | Trends, comparisons or distributions → **Charts** |
| **Bar graph** | Comparing quantities **across categories**, or ranking them | A single metric is more informative → **KPI** · The axis is continuous, usually time → **Line chart** · The point is each part's share of a whole → **Donut chart** |
| **Line chart** | Following a value **over a continuous axis**, usually time | Categories are discrete, not a continuum → **Bar graph** · Each part's share of a whole → **Donut chart** · A single metric is more informative → **KPI** |
| **Donut chart** | Showing how a total **divides into parts of a whole** | Comparing values across categories → **Bar graph** · A trend over time → **Line chart** · There is only one value → **KPI** |
| **Legend** | **Never placed on its own — it is a property of the chart.** Place `Bar graph`, `Line chart` or `Donut chart`, then switch its legend on. **Mandatory when two or more data series or segments are shown.** The Figma library places the legend beside the chart and offers no below option — see **Where a chart's legend sits**, below | A single data set → leave it off; the chart title and axis labels carry the meaning · Looking for a legend component to place → there isn't one, and that is correct |

### Identity and media

| Choose | When | Otherwise |
| --- | --- | --- |
| **Avatar** | Representing a user, agent, agency, or seeker. Circle for individuals, square for agencies | — |
| **Media upload** | The user uploads files by drag-and-drop or file picker | The user provides a URL or file path instead → **Text field** |
| **Image slider** | A sequence of images the user swipes or steps through — **images only**, and the whole slider may link to one destination | The slides carry mixed content, not only images → **Carousel** |
| **Rating** | Displaying user rating results — non-interactive, from Opinion System | — |
| **Energy tag** | Property energy efficiency ratings **only**. Use the correct country/region variant | — |
| **Badge store** | **Offering the user a download of the app** — the App Store or Google Play button. Our replicas of the official badges, kept here so they can be maintained. **Mostly a footer or a landing page.** Gabriel, 21 September 2026 | Any other link → **Link** · A count or marker pinned to a component → **Badge**, which is a different component one word away |

---

### Built outside the design system

*Some components in the libraries were not built by the design system. They are
still yours to select. What changes is what selecting one means.*

**These components are usable by any team.** They are in the libraries precisely
so that a second team need not rebuild them.

**Selecting one is a signal.** If a component built for one team's case is
picked by another, more than one team needs it — which is the condition for
adopting it into the design system properly. **A run that selects one should say
so in its report**, so the adoption question reaches Gabriel.

| Component | Where it actually lives | What a design agent may do |
| --- | --- | --- |
| `Score tag` | Built on web, in the **patterns** package rather than the core UI one. Very specific case — seller lead scoring | Select it. Report that you did |
| `Feedback thumb buttons` | Built by a team outside the design system and **never brought in**. Figma only — no web, iOS or Android build exists | Select it. Report that you did |
| `Badge store` | **Figma only, and deliberately so.** Nobody built it on our side, because it is a replica of two badges Apple and Google publish | Place it. There is nothing to generate on any platform |

**This is not the same as Never select.** A never-selectable component is not
yours to place at all. These are yours to place, and worth telling someone
about. Gabriel, 21 September 2026.

---

## Platform limits

*Platform limits override **Which component**.*

**Availability is always answered for one target platform.** Name the platform,
then read that platform's section below. A component is available there or it is
not — there is no partial state.

**Which component** assumes web unless stated. These limits win over it.

### Figma

**Every name in `figma/*-registry.json` is available in Figma.** All 98 entries
were verified live, so there is no Figma availability limit — if **Which
component** or **The inventory** names it, you may place it. **The one exception
is the short list in *Three things Which component names that are not
components*, below.** Those three are not components at all, so nothing grants
permission to place them.

A name that appears in **neither *Which component* nor *The inventory*** is not
a GSL component. Go to **When nothing fits**.

**A name starting with a dot is the exception.** It is not missing — it is an
internal part of another component, deliberately unregistered and unpublished:
`.Legend`, `.Header`, `.Grid`, `.Bar graph vertical` and their like. Never place
one, never rebuild it by hand, never copy it out of its parent. You reach it
through the component that contains it — as a property to switch on, or as a
slot already exposed on it. Only a name that is neither registered nor
dot-prefixed sends you to **When nothing fits**.

#### Where a chart's legend sits

**`Donut chart`'s legend sits beside the chart, and that is the only placement
the library offers.** Its graph frame is laid out horizontally and **carries no
alignment property**, so switching the legend on puts it to the side. Do not
compose a below-placed legend by hand.

**The legend's own `Alignment` is a different property, and it works.** The
internal `.Legend` supports horizontal and vertical, which controls how its rows
stack inside the legend. Setting it is allowed. It does not move the legend below
the chart — the graph frame is what would have to change. Gabriel, 15 September
2026, after run-003 set it and the run had to ask whether that was permitted.

The component documentation allows two placements, below **or to the left**, and
forbids above. The library can produce only one of the two. **Recorded as a
library defect on 14 September 2026**, from run-002: the alignment property
missing from the **graph frame** is a Figma gap, not a documentation error.
Until it is added, beside is correct output and is not a finding.

**Never change the gap between a chart and its legend on an instance.** That gap
is a library component's internal spacing, and **Components first** forbids
overriding it — the rule is stated in every token ruleset. If the legend does
not fit the width you have, say so in the run report. Do not reshape the
component to make it fit.

> **The intended gap is `Spacing/16` at minimum and `Spacing/48` at maximum, and
> this rule is unverified.** Sixteen is the floor, so the legend never reads as
> sitting on top of the graph. Forty-eight is the ceiling, so it always reads as
> belonging to the graph. Within that range the amount is chosen for the
> context, by the designer or the agent. Gabriel's definition, recorded
> 14 September 2026. **Not checked against web code, and not what the Figma
> library does today** — the library uses a fixed 56, above the ceiling. Follow
> it as documented intent, exactly as you would spacing's **Container padding**
> and **Page rhythm**, which carry the same unverified label.

**Do not read a component doc's `Figma` cell.** It is a hand-maintained
duplicate of the registries and has drifted in six of 52 docs — saying `Not
documented`, holding a link instead of a status, or saying `To Do` for a
component the registry verified live. The registry wins, every time.

### Web, iOS and Android

**Not answered yet. If your target platform is web, iOS or Android, ask before
selecting.**

**Do not read a component doc's `Figma | Web | iOS | Android` readiness row, on
any platform.** It looks like the answer and is not. Checked against the web
source code on 10 September 2026: of thirteen components the docs call
unavailable on web, **five are shipping today** — `Bar graph`, `Coachmark`,
`Line chart`, `Segmented Control` and `Slider`. Three more components have no
row at all — `Tabs`, `Date Picker`, `Phone Number Field` — and all three are
live on web. The iOS and Android columns have not been checked against anything.

A stale row that reads as authoritative is worse than no row: it produces a
confident wrong answer, and nothing downstream catches it.

The few platform limits confirmed independently of that row:

| Component | Limit |
| --- | --- |
| `Carousel` | Web only |
| `Breadcrumb` | Web only |
| `Pagination` | Web only. On mobile and in apps, use infinite scroll |
| `Navigation Bar (App)` | iOS and Android only — **not** the same component as `Navigation bar`, which is web |
| `Feedback Thumb Buttons` | Web only. No `Platform` property exists on the set; its `Device` axis is web breakpoints. Gabriel, 21 September 2026 |

**`Navigation Bar (App)` is placeable in Figma and will never ship on web.** Gabriel,
21 September 2026. A design agent working in Figma **may** select it for an app screen. A web
generating agent **may not**, because there is nothing on web to generate. The two are separate
questions and the answer differs.

**This table is not the full picture and must not be read as one.** A component's
absence from it means nothing has been established, not that it is available.

### Where a component exists but does not apply at every width

Availability and form factor are different questions. These components are
available, and constrained to part of the range:

| Component | Applies at |
| --- | --- |
| `Action Menu` | Desktop, SM breakpoint and above |
| `Modal Bottom Sheet Menu` | Mobile breakpoints (XXS/XS) |

### Three things **Which component** names that are not components

Do not search the libraries for them:

| Named as | What it actually is |
| --- | --- |
| "Card grid" | A grid layout of `Card`s. Lay it out yourself — there is no Card grid component |
| "Infinite scroll" | A loading behaviour, not a component |
| "Legend" | A property of the chart, not a component. Place `Bar graph`, `Line chart` or `Donut chart` and switch its legend on — see the **Legend** row in **Which component**. The underlying piece is an internal part and is never placed |

---

## Icons

*An icon is never interactive on its own.*

_**Stated here and in full in [icons-rules-ai.md](../icons/icons-rules-ai.md)**,
which is the authority on icons — which one, which variant, and what exists. It is
repeated here because this is the page you are on when you decide what the user
presses._

A bare icon has **no states, no hit area and no accessible name.** If the user
can press it, it sits inside something that carries those: `Button`,
`Text Button`, `Link`, `Chip`, `Floating Button Group`, or a component's own icon
slot.

**A tooltip may be triggered by any component. It may never be triggered by a
bare icon.** `Text Field` shows the pattern — the icon beside its label sits in a
control, not loose on the canvas.

**A decorative or purely informative icon needs none of this**, because nothing
presses it. The test is whether the user can act on it, never how it looks.

**455 icons exist and none of them was documented before 14 September 2026.**
Go to [icons-index.md](../icons/icons-index.md) for what exists, and
[icons-rules-ai.md](../icons/icons-rules-ai.md) before choosing a variant — every
variant axis defaults to `Off`, which is how run-002 placed a bare `info` where
the circled form was wanted.

## Never select

*Never select these.*

Present in the libraries, but never a design decision. Selecting one puts
platform chrome, a brand asset, or another component's internals into a product
screen.

| Never select | Why | Do this instead |
| --- | --- | --- |
| `Status Bar` · `Home Indicator` · `Webview` | Platform chrome — the OS draws it | Nothing. It is not yours to place |
| `Cell Content` | A composition slot — what you build rows *from*. Never the answer to "which component solves this problem" | Decide the container first: `Card` for one grouped block, `Tables` for tabular data, or — for a plain list — a layout you lay out yourself. **There is no `List` component in any library.** Once the container is settled, Cell content is the correct row, and using it there is not a violation of this rule |
| `Content Placeholder` | A slot, instantiated once then swapped for local content | Select the parent, put your content in the slot |
| `Filter dropdown container` · `Filter button` | Internal to `Filter bar`. The bar is built **from** filter buttons — they are its parts, never a component you place beside it. Gabriel, 18 September 2026 | Select `Filter bar`, then configure its filter buttons inside it |
| `Map Polygon` · `Map Polygon backdrop` · `mapPinsV2_SL` · `mapPinsV2_IWT` | Internal to `Map template`; the two pin sets are brand-specific | Select `Map template` |
| `Brand Logo` · `Favicon` · `Brand App Icons` · `Flag` | Brand assets, determined by brand configuration | Nothing. Brand config places them |
| `Programmatic Ads` | Commercial ad slot | Nothing |
| `Burger menu (profil)` | Already adapted to consumer-content needs, and never to be used. Gabriel, 18 September 2026 | Use `Burger menu` |
| `Menus` | Built to cover international content needs, and nothing requires it to build anything today. **Provisional** — Gabriel, 18 September 2026, to be revisited once real product usage shows whether it is used | Use `Navigation bar`, whose own controls include the language menu |
| `Button Card` · `Button Card Group` | **Neither is available on any platform** — not web, not iOS, not Android. Never developed. Gabriel, 18 September 2026 for the group and 21 September 2026 for `Button Card` itself. **Removal from Figma waits on an investigation** and is not settled here; selectability is. **`Button Card` has a doc, and a doc is not permission** — the same situation as `Cell Content` above | Use `Card`, with the whole container as the action. **Which component**'s `Button`, `Card` and `Select card group` rows were rerouted there on 21 September 2026, so no rule now points at either of these |
| `Image Ratio` | A Figma-internal helper, built so a designer need not hold an image to its aspect ratio by hand. Never a component in a product screen. Gabriel, 21 September 2026 | Nothing to place. Hold the image to its ratio in the layout itself |
| `Tab Bar` | Mid-refactor, unclassified | Use `Tabs` |
| `Footer` | Figma only, owned by the Header/Footer team, not built | Nothing |

---

## The inventory

*The full inventory of every component in the four libraries.*

Every component in the four libraries. **A name absent from this table does not
exist** — do not invent one. A row marked *no doc* exists in Figma but has no
usage documentation yet; you may still select it if **Which component** or **Highest tier first** points there.

#### Components library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Accordion` | Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of… | [accordion](accordion/accordion.md) |
| `Action Menu` | Action menus display context-specific actions in a dropdown list. | [action-menu](action-menu/action-menu.md) |
| `Alert` | Alerts are modals that provide users with critical information they need immediately. | [alert](alert/alert.md) |
| `Autocomplete` | Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more… | [autocomplete](autocomplete/autocomplete.md) |
| `Avatar` | Avatars represent user profiles of agencies, agents, private sellers and seekers. | [avatar](avatar/avatar.md) |
| `Badge` | Attention marker attached to a host component. | [badge](badge/badge.md) |
| `Badge Store` | Our replicas of the official App Store and Google Play badges, kept here so they can be maintained. | [badge-store](badge-store/badge-store.md) |
| `Brand Logo` ⚠︎ *also in Foundations* | 🚫 **Never select** — asset — brand config | — *no doc* |
| `Button` | Buttons are used to trigger an immediate action. | [button](button/button.md) |
| `Button Bar` | Holds the actions that close a form or a flow, anchored at its foot. | [button-bar](button-bar/button-bar.md) |
| `Button Card` | 🚫 **Never select** — withheld — never developed, available on no platform | [button-card](button-card/button-card.md) |
| `Button Card Group` | 🚫 **Never select** — withheld — never developed, should leave Figma | — *no doc* |
| `Button Group` | Button groups display multiple related choices in a horizontal row, allowing users to select one or more options. | [button-group](button-group/button-group.md) |
| `Card` | Cards are flexible containers used to visually group content. | [card](card/card.md) |
| `Carousel` | Carousels are used to display a collection of items that the users can slide through. | [carousel](carousel/carousel.md) |
| `Cell Content` | 🚫 **Never select** — composed-only — a slot inside Cards and lists | [cell-content](cell-content/cell-content.md) |
| `Checkbox` | Checkboxes are used to select one or more options from a list. | [checkbox](checkbox/checkbox.md) |
| `Checkbox Group` | Checkbox groups are used to select multiple options from grouped checkboxes. | [checkbox-group](checkbox-group/checkbox-group.md) |
| `Chip` | Chips are used to filter content, make selections, display input information or trigger actions. | [chip](chip/chip.md) |
| `Chip Group` | Chip groups are collections of chips that allow users to filter, select, or manage multiple related options simultaneously. | [chip-group](chip-group/chip-group.md) |
| `Coachmark` | Coach marks are temporary overlay messages that provide contextual information about user interface elements. | [coach-mark](coach-mark/coach-mark.md) |
| `Content Placeholder` | 🚫 **Never select** — composed-only — a slot, swapped for local content | — *no doc* |
| `Counter Field` | Counter fields are used to enter or select numeric values. | [counter-field](counter-field/counter-field.md) |
| `Divider` | Dividers are horizontal lines that separate content. | [divider](divider/divider.md) |
| `Dropdown` | Dropdowns are used to select one option from a list. | [dropdown](dropdown/dropdown.md) |
| `Energy Tag` | Energy tags are used to indicate the energy efficiency of properties. | [energy-tag](energy-tag/energy-tag.md) |
| `Feedback Messages` | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. | [feedback-message](feedback-message/feedback-message.md) |
| `Feedback Thumb Buttons` | Asks the user for a binary opinion — thumbs up or thumbs down. | [feedback-thumb-buttons](feedback-thumb-buttons/feedback-thumb-buttons.md) |
| `Floating Button Group` | The floating button group is used to display icon-only actions on top of images and maps. | [floating-button-group](floating-button-group/floating-button-group.md) |
| `Image Ratio` ⚠︎ *also in Foundations* | 🚫 **Never select** — withheld — a Figma-internal ratio helper for designers | — *no doc* |
| `Image Slider` | Horizontally sliding image sequence. | [image-slider](image-slider/image-slider.md) |
| `Link` | Links are navigational elements that are used to direct users to another location or resource. | [link](link/link.md) |
| `Loading State` | Signals data or content is being fetched. | [loading-state](loading-state/loading-state.md) |
| `Modal Bottom Sheet` | Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen. | [modal-bottom-sheet](modal-bottom-sheet/modal-bottom-sheet.md) |
| `Modal Bottom Sheet Menu` | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. | [modal-bottom-sheet-menu](modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) |
| `Navigation Bar (App)` | Persistent in-app navigation between top-level destinations. | [navigation-bar-app](navigation-bar-app/navigation-bar-app.md) |
| `Pagination` | Pagination divides content into smaller, numbered pages, making it easier for users to navigate through large amounts of content. | [pagination](pagination/pagination.md) |
| `Pop-up` | Small-content alternative to a Modal bottom sheet. | — *no doc* |
| `Programmatic Ads` | 🚫 **Never select** — withheld — commercial ad slot | — *no doc* |
| `Progress Bar` | A progress bar shows a task's progress. | [progress-bar](progress-bar/progress-bar.md) |
| `Progress Circle` | A progress circle shows a task's progress. | [progress-circle](progress-circle/progress-circle.md) |
| `Radio Button Group` | Radio button groups are used to select one option from a group of mutually exclusive choices. | [radio-button-group](radio-button-group/radio-button-group.md) |
| `Rating` | The rating is used to display the result of user ratings. | [rating](rating/rating.md) |
| `Score Tag` | A Tag specialised for seller lead scoring. | [score-tag](score-tag/score-tag.md) |
| `Segmented Control` | Segmented controls are used to select one option from a group of mutually exclusive choices. | [segmented-control](segmented-control/segmented-control.md) |
| `Select Card Group` | Select cards are used for single- or multi-selection inside forms. | [select-card-group](select-card-group/select-card-group.md) |
| `Slider` | A range slider can be used to select a single value or a range between minimum and maximum values. | [slider](slider/slider.md) |
| `Snackbar` | Snackbars are used to provide quick feedback after an action is taken. | [snackbar](snackbar/snackbar.md) |
| `State Message` | Inline feedback inside a form field. | [state-message](state-message/state-message.md) |
| `Tab Bar` | 🚫 **Never select** — withheld — mid-refactor, use Tabs | — *no doc* |
| `Tabs` | Tabs are used to organize related content into different views and allow users to seamlessly switch between them. | [tabs](tabs/tabs.md) |
| `Tag` | Tags are used to label, categorize and highlight items to help users quickly identify content. | [tag](tag/tag.md) |
| `Text Area` | Text areas are used to enter and edit multi-line text content. | [text-area](text-area/text-area.md) |
| `Text Button` | A distinct component from Button, for when full button weight is too heavy. | [text-button](text-button/text-button.md) |
| `Text Field` | Text fields are used to enter and edit single-line text content. | [text-field](text-field/text-field.md) |
| `Toggle` | Toggles are used to switch between on and off states. | [toggle](toggle/toggle.md) |
| `Toggle Group` | Toggle groups are used to organize related options, allowing users to switch between multiple settings, with each toggle independently… | [toggle-group](toggle-group/toggle-group.md) |
| `Tooltip` | Brief overlay clarifying one UI element. | [tooltip](tooltip/tooltip.md) |
| `Webview` | 🚫 **Never select** — chrome — an embedded browser container | — *no doc* |
| `Home Indicator` | 🚫 **Never select** — chrome — the OS draws it | — *no doc* |
| `Status Bar` | 🚫 **Never select** — chrome — the OS draws it | — *no doc* |

#### Patterns library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Burger menu` | Mobile menu opened from the navigation bar burger icon. | [burger-menu](burger-menu/burger-menu.md) |
| `Burger menu (profil)` | 🚫 **Never select** — withheld — adapted to consumer content, use Burger menu | — *no doc* |
| `Bar graph` | Compare quantities across categories. | [charts/bar-chart](charts/bar-chart.md) |
| `Donut chart` | Show a distribution across parts of a whole. | [charts/donut-chart](charts/donut-chart.md) |
| `Line chart` | Show a trend over a continuous axis. | [charts/line-chart](charts/line-chart.md) |
| `KPI` | Key Performance Indicators (KPIs) are measurable values that demonstrate how effectively a key objective is achieved. | [kpi](kpi/kpi.md) |
| `Breadcrumb` | Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. | [breadcrumb](breadcrumb/breadcrumb.md) |
| `Date Field` | Date input — distinct from the Date Picker calendar view. | [date-field](date-field/date-field.md) |
| `Date Picker` | Date pickers are used to select a date using text input or a calendar view. | [date-picker](date-picker/date-picker.md) |
| `Feedback Bar` | Asks the user to rate something — a notation on a scale. | [feedback-bar](feedback-bar/feedback-bar.md) |
| `Filter bar` | Filter bars are used to narrow down search results or displayed content based on selected criteria. | [filter-bar](filter-bar/filter-bar.md) |
| `Filter button` | 🚫 **Never select** — composed-only — inside Filter bar | — *no doc* |
| `Filter dropdown container` | 🚫 **Never select** — composed-only — inside Filter bar | — *no doc* |
| `Footer` | 🚫 **Never select** — withheld — Figma only, not built | — *no doc* |
| `Info State` | Info states are placeholders used to inform users about success, error and empty states. | [info-state](info-state/info-state.md) |
| `Media Upload` | Media upload components allow users to upload, view, and manage media files such as images, videos and documents. | [media-upload](media-upload/media-upload.md) |
| `Mega menus` | Top-level navigation on the main B2C and B2B websites. The Figma was built by the design system team; the component is not stored here yet and the transfer is ongoing. | [mega-menus](mega-menus/mega-menus.md) |
| `Menus` | 🚫 **Never select** — withheld, provisional — nothing requires it today, use Navigation bar | [menus](menus/menus.md) |
| `Navigation bar` | Navigation bars provide quick access to key pages within the site, helping users to navigate efficiently. | [navigation-bar](navigation-bar/navigation-bar.md) |
| `Top Bar` | Top bars display navigation elements, titles and actions such as buttons or icons at the top of the screen. | [top-bar](top-bar/top-bar.md) |
| `Wizard` | Wizards guide users through step-by-step processes to achieve their goal. | [wizard](wizard/wizard.md) |

#### Experiences library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Estimation card` | Presents a completed price estimate — range, confidence, selling or renting. Carries no controls to adjust it. | [estimation-card](estimation-card/estimation-card.md) |
| `Floor selection` | Picking an apartment floor, including ground floor. | [floor-selection](floor-selection/floor-selection.md) |
| `Listing Card` | Listing cards are actionable cards that summarize the details of a property listed on any AVIV Group website. | [listing-card](listing-card/listing-card.md) |
| `Listing summary` | Higher-flexibility alternative to Listing card. | [listing-summary](listing-summary/listing-summary.md) |
| `Map template` | The map experience container. | [map-template](map-template/map-template.md) |
| `mapPinsV2_SL` | 🚫 **Never select** — composed-only — inside Map template, SeLoger | — *no doc* |
| `mapPinsV2_IWT` | 🚫 **Never select** — composed-only — inside Map template, Immowelt | — *no doc* |
| `Map Polygon` | 🚫 **Never select** — composed-only — inside Map template | — *no doc* |
| `Map Polygon backdrop` | 🚫 **Never select** — composed-only — inside Map template | — *no doc* |
| `Phone Number Field` | The phone number field is used to input and format phone numbers. | [phone-number-field](phone-number-field/phone-number-field.md) |
| `Table` | Tables are used to organize and display all information from a data set. | [tables](tables/tables.md) |

#### Foundations library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Flag` | 🚫 **Never select** — asset — brand config | — *no doc* |
| `Favicon` | 🚫 **Never select** — asset — brand config | — *no doc* |
| `Image Ratio` ⚠︎ *also in Components* | 🚫 **Never select** — withheld — a Figma-internal ratio helper for designers | — *no doc* |
| `Brand Logo` ⚠︎ *also in Components* | 🚫 **Never select** — asset — brand config | — *no doc* |
| `Brand App Icons` | 🚫 **Never select** — asset — brand config | — *no doc* |

---

## When nothing fits

*What to do when nothing fits.*

Compliance means **reuse before invention**, not never inventing.

1. Re-check **Highest tier first**. Most "nothing fits" cases are a Pattern or Experience that
   was not searched for.
2. Re-check **The inventory** for a component with no doc — 25 selectable components exist
   in Figma with no usage page, and absence of a doc is not absence of the
   component.
3. If nothing still fits, **compose from existing Components** using the token
   rulesets — [colour](../tokens/color/color-rules-ai.md),
   [typography](../tokens/typography/typography-rules-ai.md),
   [spacing](../tokens/spacing/spacing-rules-ai.md). Never hand-style something
   a component already does.
4. **Declare it.** Write the declaration into the `## Declarations` section of
   this run's report — `compliance/briefs/brief-<NNN>/run-<NNN>/report-run-<NNN>.md`, where
   `<NNN>` is this run's three-digit number. One block per element you built by
   hand, each stating all three of:
   - **What you built.**
   - **Which problem it belongs under** — a heading from **Which component**.
   - **Which existing components you ruled out, and why.**

   Write each block as a `###` heading naming what you built, followed by the
   three parts. If you invented nothing, the section still gets written, reading
   `_None._`.

**What needs declaring, and what does not.** A declaration describes something
you **composed** — an element assembled from components, frames and text that
together do a job no single component does. It is not a receipt for every node
on the screen.

| Built by hand | Declare it? | Why |
| --- | --- | --- |
| A composed block — a container plus components plus text, doing one job | **Yes** | Nobody can review whether composing it was right unless you say you did |
| A layout container holding **one** declared thing | **Yes**, inside that content's own declaration | It is part of the thing you composed |
| **A frame that only stacks other elements and does no job of its own** — a page frame, a section stack, a container holding content from several declarations at once | **No** | It is layout, not an element. The job is done by the things inside it, and every one of those is declared on its own. The three-part declaration cannot be written for it either: no problem heading in **Which component** covers stacking things, and there is no container component to rule out. Gabriel, 15 September 2026, from run-003 |
| **Plain text set in a published GSL text style** — a section title, a field label, a caption, a unit | **No** | Typography's **Components first** tells you to set type on your own markup. No text, heading or label component exists to rule out, and no problem heading in **Which component** covers writing a label. The three-part declaration cannot be written for it, and a declaration missing a part counts as absent |

**Content you author to fill a component's own slot still counts as composed.**
`Card`'s `Content Placeholder` is documented as taking local content, so building
something to go in it is correct. It is still an element you built by hand, so it
still gets its own declaration, with all three parts. **Using a sanctioned slot
is permission to compose — never an exemption from declaring.**

**The report file is the only place a declaration counts.** Not a note on the
Figma frame, not a comment in the code, not your reply to whoever asked — a
reply is not an artefact and is gone when the session closes. The place is the
same on every platform, because a run folder is the same on every platform.

**Write it before the output is scored, and never revise it afterwards.** A
declaration reworded once the verdict is known is not a declaration.

**A declaration missing any of the three parts counts as absent**, and an
absent declaration is a failure. Two of the three is not a partial pass; it is a
declaration nobody can review.

An undeclared new component is a compliance failure even when it looks right.

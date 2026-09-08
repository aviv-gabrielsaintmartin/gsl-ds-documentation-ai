# Component rules for AI generation

_The authoritative ruleset for choosing **which component** when generating a GSL
interface. Read this before opening any component page — the component pages say
how to use a component, this says which one to reach for. Evidence and rejected
options: [components-audit.md](components-audit.md). Full
inventory: [components.md](components.md)._

This page is written for machine consumption. Each section maps a design
decision to one component.

---

## Rule 0 — Reach for the highest tier that fits

GSL is four Figma libraries, in increasing order of assembly:

```
Foundations  →  Components  →  Patterns  →  Experiences
   tokens,        Button,       Filter bar,   Listing Card,
   icons          Chip          Wizard        Map template
```

**Search from the right.** Before composing anything out of Components, check
whether a Pattern or an Experience already is the thing you are about to build.

| You are about to build | Stop — this already exists | Kind | Parts a hand-built version would contain |
| --- | --- | --- | --- |
| A property summary card | `Listing Card` (Experience) | composed | `Card` · `Image Slider` · `Tag` |
| A **structured, multi-criteria** filter panel | `Filter bar` (Pattern) | composed | `Chip` · `Button` |
| A step-by-step flow | `Wizard` (Pattern) | composed | `Tabs` · `Progress Bar` |
| A phone input with a country prefix | `Phone Number Field` (Experience) | composed | `Text Field` · `Dropdown` |
| An empty / error / success / loading screen | `Info State` (Pattern) | **container** | — it is a shell with content slots, not an assembly of components |
| A map screen | `Map template` (Experience) | **all-or-nothing** | — used whole or not at all. Its pin sets are Rule 3 never-select |
| A data grid | `Table` (Experience) | **container** | `Cell Content` rows inside a shell. **Figma-ready, web in progress** — see Rule 2 |
| A floor picker | `Floor selection` (Experience) | unresolved | `Counter Field` — one part only. Open question |
| A more flexible property summary than Listing Card allows | `Listing summary` (Experience) | unresolved | — ⚠︎ undescribed, see audit |
| A price estimation block | `Estimation card` (Experience) | unresolved | — ⚠︎ undescribed, see audit |

**The Parts column is for a checker, not for you.** It lists what a hand-built
imitation would be assembled *from*, so a compliance check can detect one. Never
read it as a recipe — the whole point of Rule 0 is that you use the higher-tier
component instead of assembling anything.

Part names are exact inventory names from Rule 4. A part may be a Rule 3
never-select component: Rule 3 governs what you may **choose**, while this column
describes what an imitation would **contain**. Different questions.

### Two kinds of higher-tier component

The distinction matters because only the first kind can be detected by counting
parts.

| Kind | What it is | Rule 0 still applies? | Detectable by counting parts? |
| --- | --- | --- | --- |
| **Composed** | Assembled from public components | yes | **yes** — the four rows above |
| **Container** | A shell you place content into. `Info State` is closer to a modal with prescribed content than to an assembly | yes | no — there is no characteristic set of parts to count |
| **All-or-nothing** | Used whole or not at all. A partial `Map template` is not a realistic build | yes | no — there is no partial composition to detect |

For the container and all-or-nothing kinds, **Rule 0 is still the rule** — you
must still reach for the existing component. It simply cannot be enforced by a
parts count, and `C2 · Tier ceiling` says so rather than passing them silently.

Composing from a lower tier when a higher-tier component exists is the single
most common compliance failure. Rule 1 below is flat by design — it answers
"which control", not "which tier". **Rule 0 wins over Rule 1 whenever both
apply.**

**What Rule 0 does not cover.** It fires when you would be rebuilding the
higher-tier component *in full*. It does not fire when Rule 1 deliberately routes
you to a **lighter** component for a smaller version of the same job. These are
not violations:

| Rule 1 sends you to | Rather than | Because |
| --- | --- | --- |
| `Chip group` | `Filter bar` | Inline filters with no dropdown panels — not a structured multi-criteria panel |
| `Pop-up` | `Modal bottom sheet` | A small amount of content |
| `Tabs` | `Wizard` | Independent sections, not sequential steps |

When Rule 0's table and a Rule 1 *Otherwise* branch both match, and the Rule 1
branch names a **simpler** component for an explicitly **lighter** case, follow
Rule 1.

**The operational test — count the parts.** Rule 0 fires when your build would
need **two or more** of the higher-tier component's own moving parts. One part
alone is the lighter case, and Rule 1 wins.

**This test applies to the composed kind only.** For a container or
all-or-nothing component there are no parts to count, and Rule 0 applies
regardless of how much of it you were about to rebuild.

| You would build | Parts | Rule |
| --- | --- | --- |
| Filter controls **and** dropdown panels **and** applied-state handling | 3 | **Rule 0** → `Filter bar` |
| A row of filter chips, nothing else | 1 | **Rule 1** → `Chip group` |
| Sequential steps **and** progress **and** step gating | 3 | **Rule 0** → `Wizard` |
| Switchable sections, no sequence | 1 | **Rule 1** → `Tabs` |

---

## Rule 1 — Choose by the problem being solved

Find the row whose **When** matches your situation. If your situation differs,
follow **Otherwise**. Organised by problem, not by component category.

**When an intent matches more than one row**, apply in this order and stop at the
first that decides it:

1. **Rule 0** — a Pattern or Experience already is the whole thing. Wins outright.
2. **Rule 2** — a platform limit forbids the obvious answer.
3. **The narrower trigger wins.** "Filtering a SERP with structured panels"
   beats "multi-select outside a form"; "a date" beats "single-line input".
4. **Inside a form beats outside it.** Form context selects the form component
   (`Checkbox group` over `Chip group`, `Radio button group` over
   `Segmented control`).
5. Still tied → pick either and **declare the tie** under Rule 5.

### Triggering actions

| Choose | When | Otherwise |
| --- | --- | --- |
| **Button** | The user triggers an immediate action — save, submit, share, open a modal | Navigation → **Link** · Full button weight is visually too heavy → **Text button** · Prominent navigational entry point with icon or illustration → **Button card** · Choosing from a set of related options → **Button group** |
| **Link** | The intent is navigation to another page or section — not action | An action is triggered → **Button** · Navigation needs button weight, e.g. an empty-state CTA → **Button**, tertiary |

### Selecting a single value

| Choose | When | Otherwise |
| --- | --- | --- |
| **Radio button group** | Mutually exclusive choices in a form, ≤5 options, enough vertical space | \>5 options, long labels, or constrained space → **Dropdown** · Prominent visual treatment preferred → **Button group** (single-select) · Options benefit from icons or illustrations → **Select card group** (single-select) · Switching views rather than submitting a value → **Segmented control** |
| **Dropdown** | Single-select from a list in a form, or space too constrained to show options inline | ≤5 options and space allows → **Radio button group** · Long list where typing to filter helps → **Autocomplete** · Items trigger actions rather than set a value → **Action menu** |
| **Segmented control** | Switching between mutually exclusive view modes or display options — not a form value | The choice is a form value → **Button group** · Switching full content sections → **Tabs** · Standard form styling needed → **Radio button group** |

### Selecting multiple values

| Choose | When | Otherwise |
| --- | --- | --- |
| **Checkbox group** | Multi-select in a structured form | Few options and prominent visual treatment preferred → **Button group** (multi-select) · Options benefit from card layout → **Select card group** (multi-select) · Long list or constrained space → **Dropdown** · Lightweight selections outside a form → **Chip group** |
| **Chip group** | Lightweight multi-select filtering or input outside a structured form | Inside a structured form with labels and helper text → **Checkbox group** · Constrained space or numerous options → **Dropdown** · Filtering a SERP or data table with structured panels → **Filter bar** · The element is non-interactive → **Tag** |
| **Select card group** | Form selection benefits from a visual, card-based layout with icons or illustrations | Simpler single-select → **Radio button group** · Simpler multi-select → **Checkbox group** · The intent is navigation, not selection → **Button card** |

### Filtering content

| Choose | When | Otherwise |
| --- | --- | --- |
| **Filter bar** | Narrowing search results or table content using structured criteria — SERP or data page | Lightweight inline filters without dropdown panels → **Chip group** · A single filter criterion inside a form → **Dropdown** · Triggering filter-related actions rather than setting criteria → **Action menu** |

### Entering text

| Choose | When | Otherwise |
| --- | --- | --- |
| **Text field** | Short, single-line free-form input | Multi-line or longer than a sentence → **Text area** · Suggestions appear as the user types → **Autocomplete** · Numeric with increment/decrement controls → **Counter field** · A date → **Date picker** |
| **Text area** | Multi-line free-form text — descriptions, comments, messages | Single-line → **Text field** · Attaching a file → **Media upload** |
| **Autocomplete** | The user types to filter and select from a large or dynamic dataset | No suggestions needed → **Text field** · Fixed options selected without typing → **Dropdown** |

### Entering numeric values

| Choose | When | Otherwise |
| --- | --- | --- |
| **Counter field** | Numeric values adjusted with +/− controls | Range selection where an approximate value is acceptable → **Slider** · Direct numeric text entry without controls → **Text field** · Only a small fixed set of values → **Dropdown** |
| **Slider** | Selecting a value or range along a continuous scale | Precision and exact entry matter → **Counter field** · Only discrete values available → **Dropdown** |

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
| **Pop-up** | A **small** amount of blocking content — a short confirmation, a brief message, one or two buttons | The content is long, scrollable, or rich → **Modal bottom sheet** · It is a plain list of actions → **Modal bottom sheet menu** · It is not blocking → **Snackbar** or **Feedback message** |
| **Alert** | Critical, blocking information requiring immediate action | **On web → Pop-up** for a short confirmation, **Modal bottom sheet** for richer content (Alert is not yet available on web) · Transient, non-blocking feedback → **Snackbar** · Inline, non-blocking contextual guidance → **Feedback message** |

### Grouping and structuring content

| Choose | When | Otherwise |
| --- | --- | --- |
| **Card** | Visually grouping related content in a cohesive container | Content should be collapsible → **Accordion** · Content overlays the screen → **Modal bottom sheet** · The whole container is a single navigational action → **Button card** |
| **Accordion** | Content needs progressive disclosure in a persistent expandable list | Content should always be visible → **Card** · Sections are mutually exclusive views → **Tabs** |
| **Divider** | Visually separating content sections or list items where spacing alone is insufficient | — |
| **Text button** | Revealing more content in place — "Read more" under truncated text, "Show all 12 photos" | The control leaves the page → **Link** · The content collapses back into a persistent expandable list → **Accordion** |
| **A list you lay out yourself, of `Cell content` rows** | A plain list — settings, an index, a menu — that is neither one grouped visual block nor tabular data. **There is no `List` component in any library; laying the rows out yourself is the intended pattern, not a workaround** | The rows are tabular and comparable → **Tables** · The rows belong inside one visual container → **Card** · The whole block is a single action → **Button card** · Every row carries an immediate on/off setting → **Toggle group** |
| **Carousel** | Users browse a horizontal collection of items one by one. **Web only** | All items should be visible simultaneously → a grid layout, **not a component** — see Rule 2 |

`Cell content` is **not a choice** — it is a composition slot inside Cards and
lists. See Rule 3.

### Navigating between pages and sections

| Choose | When | Otherwise |
| --- | --- | --- |
| **Tabs** | Organising related content at the same hierarchy level into switchable views | Switching view modes within a single content area → **Segmented control** · Steps must be completed in sequence → **Wizard** · Switching between top-level destinations → **Navigation bar** |
| **Wizard** | Guiding users through a sequential multi-step process | Sections are independent and non-sequential → **Tabs** · Showing task completion without step-by-step input → **Progress bar** |
| **Breadcrumb** | Showing hierarchical location and allowing navigation up the hierarchy. **Web only** | The primary need is page title and actions → **Top bar** · Top-level global navigation → **Navigation bar** |
| **Pagination** | Dividing large result sets into numbered pages. **Web only** | Mobile and apps → infinite scroll, a **behaviour, not a component** — see Rule 2 |
| **Top bar** | Page-specific title, context, and actions | Global site navigation → **Navigation bar** |
| **Navigation bar** | Global navigation to top-level site destinations (web) | Sub-pages and flows → **Top bar** · In-app navigation → **Navigation Bar (App)**, mobile only |

### Providing feedback and status

| Choose | When | Otherwise |
| --- | --- | --- |
| **Snackbar** | Brief, transient feedback confirming the outcome of a user action | Persistence and inline placement needed → **Feedback message** · Critical and blocking → **Alert** |
| **Feedback message** | Persistent inline contextual guidance or status within a section | Transient, action-triggered feedback → **Snackbar** · Full-area or page-level states → **Info state** |
| **Info state** | Full-area states — empty, error, success, loading | Inline section-level messages → **Feedback message** · A blocking decision is required → **Alert** |
| **Tag** | A non-interactive status label or category that **occupies its own place in the layout flow** and would still make sense if the thing beside it were removed — "New", "Sold", "Exclusive", "Verified" | The element is interactive — selectable, filterable, removable → **Chip** · Status needs supporting text → **Feedback message** · The marker is anchored to another component's geometry → **Badge** |
| **Badge** | A marker **anchored to a host component's geometry** — overlapping or pinned to a button, tab label, menu entry or cell row, and meaningless without that host. Typically a count or a dot | The marker holds its own place in the layout flow → **Tag** · It is interactive → **Chip** |
| **Tooltip** | A brief clarification of one UI element, shown on hover or tap — a single explanation, not a sequence | Persistent inline guidance not tied to a control → **Feedback message** · A guided, multi-step tour → **Coach mark** |
| **Coach mark** | Contextual onboarding overlays pointing at specific UI elements | Persistent inline guidance not tied to onboarding → **Feedback message** · A single brief clarification rather than a guided tour → **Tooltip** |

### Showing progress and data

| Choose | When | Otherwise |
| --- | --- | --- |
| **Progress bar** | Linear task or goal completion | A compact circular format fits better → **Progress circle** · Progress involves sequential user-input steps → **Wizard** |
| **Progress circle** | A single completion percentage in a compact circular format | A linear format fits the layout better → **Progress bar** |
| **KPI** | A single key metric value needs prominent standalone display | Trends, comparisons or distributions → **Charts** |
| **Bar graph** | Comparing quantities **across categories**, or ranking them | A single metric is more informative → **KPI** · The axis is continuous, usually time → **Line chart** · The point is each part's share of a whole → **Donut chart** |
| **Line chart** | Following a value **over a continuous axis**, usually time | Categories are discrete, not a continuum → **Bar graph** · Each part's share of a whole → **Donut chart** · A single metric is more informative → **KPI** |
| **Donut chart** | Showing how a total **divides into parts of a whole** | Comparing values across categories → **Bar graph** · A trend over time → **Line chart** · There is only one value → **KPI** |
| **Legend** | Two or more data series or segments are shown on any chart — then it is **mandatory** | A single data set → omit it; the chart title and axis labels carry the meaning |

### Identity and media

| Choose | When | Otherwise |
| --- | --- | --- |
| **Avatar** | Representing a user, agent, agency, or seeker. Circle for individuals, square for agencies | — |
| **Media upload** | The user uploads files by drag-and-drop or file picker | The user provides a URL or file path instead → **Text field** |
| **Rating** | Displaying user rating results — non-interactive, from Opinion System | — |
| **Energy tag** | Property energy efficiency ratings **only**. Use the correct country/region variant | — |

---

## Rule 2 — Platform limits override Rule 1

Rule 1 assumes web unless stated. These constraints win over it.

**The policy: use a component on a platform where it exists.** Where it does not
exist on your target platform, it is not available to you, whatever Rule 1 says.

Where to find out whether it exists:

| Target platform | Source of truth | State today |
| --- | --- | --- |
| **Figma** | `figma/*-registry.json` — every entry verified live in Figma | **All 98 exist.** No Figma availability constraint |
| Web · iOS · Android | The component's own doc, its `Figma \| Web \| iOS \| Android` row | Hand-maintained free text. **Read the doc; do not rely on the table below** |

**Do not read a doc's Figma cell as authority.** It is a hand-maintained
duplicate of the registries and has drifted — six of 52 docs say `Not
documented`, hold a link instead of a status, or say `To Do` for a component the
registry verified live in Figma. The registry wins.

**The table below is the curated set of platform limits, not the whole picture.**
Nine doc entries are not production-ready on web while this table names two.
Reconciling that data needs a controlled vocabulary first — the docs currently
use `To Do`, `To-do`, `WIP`, `In progress`, `Partially available` and
`Non-gemini component` interchangeably. See
[components-audit.md](components-audit.md).

| Component | Constraint |
| --- | --- |
| `Alert` | **Not yet available on web.** On web, use `Modal bottom sheet` |
| `Carousel` | Web only |
| `Breadcrumb` | Web only |
| `Pagination` | Web only. On mobile and in apps, use infinite scroll |
| `Action menu` | Desktop, SM breakpoint and above |
| `Modal bottom sheet menu` | Mobile (XXS/XS) and apps |
| `Navigation Bar (App)` | Mobile (iOS/Android) only |
| `Table` | **Figma ready, web in progress.** Not yet production on web; iOS and Android not started. Safe for Figma output, not for web |
| `Footer` | Figma only — not built. Do not generate it |
| `Tab Bar` | Mid-refactor. Use `Tabs` |

**Two things Rule 1 names that are not components.** Do not search the libraries
for them:

| Named as | What it actually is |
| --- | --- |
| "Card grid" | A grid layout of `Card`s. Lay it out yourself — there is no Card grid component |
| "Infinite scroll" | A loading behaviour, not a component |

---

## Rule 3 — Never select these

Present in the libraries, but never a design decision. Selecting one puts
platform chrome, a brand asset, or another component's internals into a product
screen.

| Never select | Why | Do this instead |
| --- | --- | --- |
| `Status Bar` · `Home Indicator` · `Webview` | Platform chrome — the OS draws it | Nothing. It is not yours to place |
| `Cell Content` | A composition slot — what you build rows *from*. Never the answer to "which component solves this problem" | Decide the container first: `Card` for one grouped block, `Tables` for tabular data, or — for a plain list — a layout you lay out yourself. **There is no `List` component in any library.** Once the container is settled, Cell content is the correct row, and using it there is not a violation of this rule |
| `Content Placeholder` | A slot, instantiated once then swapped for local content | Select the parent, put your content in the slot |
| `Filter dropdown container` | Internal to `Filter bar` | Select `Filter bar` |
| `Map Polygon` · `Map Polygon backdrop` · `mapPinsV2_SL` · `mapPinsV2_IWT` | Internal to `Map template`; the two pin sets are brand-specific | Select `Map template` |
| `Brand Logo` · `Favicon` · `Brand App Icons` · `Flag` | Brand assets, determined by brand configuration | Nothing. Brand config places them |
| `Programmatic Ads` | Commercial ad slot | Nothing |
| `Tab Bar` | Mid-refactor, unclassified | Use `Tabs` |
| `Footer` | Figma only, owned by the Header/Footer team, not built | Nothing |

---

## Rule 4 — The full inventory

Every component in the four libraries. **A name absent from this table does not
exist** — do not invent one. A row marked *no doc* exists in Figma but has no
usage documentation yet; you may still select it if Rule 1 or Rule 0 points there.

#### Components library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Accordion` | Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of… | [accordion](accordion/accordion.md) |
| `Action Menu` | Action menus display context-specific actions in a dropdown list. | [action-menu](action-menu/action-menu.md) |
| `Alert` | Alerts are modals that provide users with critical information they need immediately. | [alert](alert/alert.md) |
| `Autocomplete` | Autocomplete components suggest possible matches for user input in real time as they type, helping them complete text fields more… | [autocomplete](autocomplete/autocomplete.md) |
| `Avatar` | Avatars represent user profiles of agencies, agents, private sellers and seekers. | [avatar](avatar/avatar.md) |
| `Badge` | Attention marker attached to a host component. | — *no doc* |
| `Badge Store` | ⚠︎ **Undescribed** — see audit | — *no doc* |
| `Brand Logo` ⚠︎ *also in Foundations* | 🚫 **Never select** — asset — brand config | — *no doc* |
| `Button` | Buttons are used to trigger an immediate action. | [button](button/button.md) |
| `Button Bar` | ⚠︎ **Undescribed** — see audit | — *no doc* |
| `Button Card` | Button cards are prominent calls to action that can be used alone or in a group, with icons or pictograms. | [button-card](button-card/button-card.md) |
| `Button Card Group` | ⚠︎ **Undescribed** — see audit | — *no doc* |
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
| `Feedback Thumb Buttons` | ⚠︎ **Undescribed** — see audit | — *no doc* |
| `Floating Button Group` | The floating button group is used to display icon-only actions on top of images and maps. | [floating-button-group](floating-button-group/floating-button-group.md) |
| `Image Ratio` ⚠︎ *also in Foundations* | Enforces an image aspect ratio. | — *no doc* |
| `Image Slider` | Horizontally sliding image sequence. | — *no doc* |
| `Link` | Links are navigational elements that are used to direct users to another location or resource. | [link](link/link.md) |
| `Loading State` | Signals data or content is being fetched. | — *no doc* |
| `Modal Bottom Sheet` | Modal bottom sheets are containers that appear above the content and block interaction with the rest of the screen. | [modal-bottom-sheet](modal-bottom-sheet/modal-bottom-sheet.md) |
| `Modal Bottom Sheet Menu` | Modal bottom sheet menus display a list of context-specific actions on mobile screens or on apps. | [modal-bottom-sheet-menu](modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) |
| `Navigation Bar (App)` | Persistent in-app navigation between top-level destinations. | — *no doc* |
| `Pagination` | Pagination divides content into smaller, numbered pages, making it easier for users to navigate through large amounts of content. | [pagination](pagination/pagination.md) |
| `Pop-up` | Small-content alternative to a Modal bottom sheet. | — *no doc* |
| `Programmatic Ads` | 🚫 **Never select** — withheld — commercial ad slot | — *no doc* |
| `Progress Bar` | A progress bar shows a task's progress. | [progress-bar](progress-bar/progress-bar.md) |
| `Progress Circle` | A progress circle shows a task's progress. | [progress-circle](progress-circle/progress-circle.md) |
| `Radio Button Group` | Radio button groups are used to select one option from a group of mutually exclusive choices. | [radio-button-group](radio-button-group/radio-button-group.md) |
| `Rating` | The rating is used to display the result of user ratings. | [rating](rating/rating.md) |
| `Score Tag` | A Tag specialised for seller lead scoring. | — *no doc* |
| `Segmented Control` | Segmented controls are used to select one option from a group of mutually exclusive choices. | [segmented-control](segmented-control/segmented-control.md) |
| `Select Card Group` | Select cards are used for single- or multi-selection inside forms. | [select-card-group](select-card-group/select-card-group.md) |
| `Slider` | A range slider can be used to select a single value or a range between minimum and maximum values. | [slider](slider/slider.md) |
| `Snackbar` | Snackbars are used to provide quick feedback after an action is taken. | [snackbar](snackbar/snackbar.md) |
| `State Messages` | Inline feedback inside a form field. | — *no doc* |
| `Tab Bar` | 🚫 **Never select** — withheld — mid-refactor, use Tabs | — *no doc* |
| `Tabs` | Tabs are used to organize related content into different views and allow users to seamlessly switch between them. | [tabs](tabs/tabs.md) |
| `Tag` | Tags are used to label, categorize and highlight items to help users quickly identify content. | [tag](tag/tag.md) |
| `Text Area` | Text areas are used to enter and edit multi-line text content. | [text-area](text-area/text-area.md) |
| `Text Button` | A distinct component from Button, for when full button weight is too heavy. | — *no doc* |
| `Text Field` | Text fields are used to enter and edit single-line text content. | [text-field](text-field/text-field.md) |
| `Toggle` | Toggles are used to switch between on and off states. | [toggle](toggle/toggle.md) |
| `Toggle Group` | Toggle groups are used to organize related options, allowing users to switch between multiple settings, with each toggle independently… | [toggle-group](toggle-group/toggle-group.md) |
| `Tooltip` | Brief overlay clarifying one UI element. | — *no doc* |
| `Webview` | 🚫 **Never select** — chrome — an embedded browser container | — *no doc* |
| `Home Indicator` | 🚫 **Never select** — chrome — the OS draws it | — *no doc* |
| `Status Bar` | 🚫 **Never select** — chrome — the OS draws it | — *no doc* |

#### Patterns library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Burger menu` | Mobile menu opened from the navigation bar burger icon. | — *no doc* |
| `Burger menu (profil)` | Distinct sibling of Burger menu, separate definition. | — *no doc* |
| `Bar graph` | Compare quantities across categories. | [charts/bar-chart](charts/bar-chart.md) |
| `Donut chart` | Show a distribution across parts of a whole. | [charts/donut-chart](charts/donut-chart.md) |
| `Line chart` | Show a trend over a continuous axis. | [charts/line-chart](charts/line-chart.md) |
| `KPI` | Key Performance Indicators (KPIs) are measurable values that demonstrate how effectively a key objective is achieved. | [kpi](kpi/kpi.md) |
| `Breadcrumb` | Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. | [breadcrumb](breadcrumb/breadcrumb.md) |
| `Date Field` | Date input — distinct from the Date Picker calendar view. | — *no doc* |
| `Date Picker` | Date pickers are used to select a date using text input or a calendar view. | [date-picker](date-picker/date-picker.md) |
| `Feedback Bar` | ⚠︎ **Undescribed** — see audit | — *no doc* |
| `Filter bar` | Filter bars are used to narrow down search results or displayed content based on selected criteria. | [filter-bar](filter-bar/filter-bar.md) |
| `Filter button` | The individual filter control inside a Filter bar. | — *no doc* |
| `Filter dropdown container` | 🚫 **Never select** — composed-only — inside Filter bar | — *no doc* |
| `Footer` | 🚫 **Never select** — withheld — Figma only, not built | — *no doc* |
| `Info State` | Info states are placeholders used to inform users about success, error and empty states. | [info-state](info-state/info-state.md) |
| `Media Upload` | Media upload components allow users to upload, view, and manage media files such as images, videos and documents. | [media-upload](media-upload/media-upload.md) |
| `Mega menus` | ⚠︎ **Undescribed** — see audit | — *no doc* |
| `Menus` | Profile and language menus. | — *no doc* |
| `Navigation bar` | Navigation bars provide quick access to key pages within the site, helping users to navigate efficiently. | [navigation-bar](navigation-bar/navigation-bar.md) |
| `Top Bar` | Top bars display navigation elements, titles and actions such as buttons or icons at the top of the screen. | [top-bar](top-bar/top-bar.md) |
| `Wizard` | Wizards guide users through step-by-step processes to achieve their goal. | [wizard](wizard/wizard.md) |

#### Experiences library

| Name | Purpose | Doc |
| --- | --- | --- |
| `Estimation card` | ⚠︎ **Undescribed** — see audit | — *no doc* |
| `Floor selection` | Picking an apartment floor, including ground floor. | — *no doc* |
| `Listing Card` | Listing cards are actionable cards that summarize the details of a property listed on any AVIV Group website. | [listing-card](listing-card/listing-card.md) |
| `Listing summary` | Higher-flexibility alternative to Listing card. | — *no doc* |
| `Map template` | The map experience container. | — *no doc* |
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
| `Image Ratio` ⚠︎ *also in Components* | Enforces an image aspect ratio. | — *no doc* |
| `Brand Logo` ⚠︎ *also in Components* | 🚫 **Never select** — asset — brand config | — *no doc* |
| `Brand App Icons` | 🚫 **Never select** — asset — brand config | — *no doc* |

---

## Rule 5 — When nothing fits

Compliance means **reuse before invention**, not never inventing.

1. Re-check Rule 0. Most "nothing fits" cases are a Pattern or Experience that
   was not searched for.
2. Re-check Rule 4 for a component with no doc — 25 selectable components exist
   in Figma with no usage page, and absence of a doc is not absence of the
   component.
3. If nothing still fits, **compose from existing Components** using the token
   rulesets — [colour](../tokens/color/color-rules-ai.md),
   [typography](../tokens/typography/typography-rules-ai.md),
   [spacing](../tokens/spacing/spacing-rules-ai.md). Never hand-style something
   a component already does.
4. **Declare it.** State, in the output: what you built, which problem in Rule 1
   it belongs under, and which existing components you ruled out and why.

An undeclared new component is a compliance failure even when it looks right.

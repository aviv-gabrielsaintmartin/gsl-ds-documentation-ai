# Component selection audit

_The evidence behind [components-rules-ai.md](components-rules-ai.md). This file
records where each selection rule came from, what was rejected, and what is
still unresolved. **Never read this as rules** — read the ruleset._

Same relationship as `tokens/*/​*-usage-audit.md` has to `*-rules-ai.md`.

---

## Method

Every claim in the ruleset traces to one of four sources, named per row:

| Source | What it is | Trust |
| --- | --- | --- |
| `registry` | The four `figma/*-registry.json` files — names, tiers, keys, variant properties, audit status | Highest. Verified live via the Figma Desktop Bridge |
| `doc` | Prose already in a `components/<name>/<name>.md` — its `Usage` narrative or a `Related Components` row | High. Human-written, but inherited from Zeroheight and never re-checked |
| `confluence` | The "Component selection guide" page, migrated into this repo | High |
| `inferred` | Derived from variant properties or sibling structure, with **no** confirming prose | **Low — must be confirmed before it becomes a rule** |

Nothing in the ruleset is marked `inferred` without also appearing in
[Open questions](#open-questions) below.

---

## Inventory reconciliation

Counted from the four registries on 2026-09-07.

| Figure | Count |
| --- | --- |
| Registry entries across all four tiers | **98** |
| — Components / Patterns / Experiences / Foundations | 61 / 21 / 11 / 5 |
| Unique names | 96 |
| Names appearing in **two** tiers | 2 — `Image Ratio`, `Brand Logo` |
| Local doc folders under `components/` | 53 |
| Registry entries that have a doc | **55** |
| Registry entries with **no doc at all** | **43** |
| Doc folders with no registry entry | 0 |

Five docs cover a registry entry under a different name. These aliases are real,
not sloppiness, and the ruleset must resolve them:

| Registry name | Tier | Doc |
| --- | --- | --- |
| `Feedback Messages` | Components | `feedback-message/` |
| `Table` | Experiences | `tables/` |
| `Bar graph` | Patterns | `charts/bar-chart.md` |
| `Donut chart` | Patterns | `charts/donut-chart.md` |
| `Line chart` | Patterns | `charts/line-chart.md` |

### The two cross-tier duplicates

`Image Ratio` and `Brand Logo` each exist in **both** the Components library and
the Foundations library, with **identical variant counts but different keys** —
so they are two distinct Figma components, not one component listed twice.

| Name | Components library key | Foundations library key | Variants |
| --- | --- | --- | --- |
| `Image Ratio` | `62e17467…3686` | `00f0402e…0d4f5` | 11 both |
| `Brand Logo` | `c2dc9cee…03c4` | `2655d153…6452` | 136 both |

An agent told only "use Brand Logo" cannot know which library to instantiate
from. Unresolved — see [Open questions](#open-questions).

---

## Triage — what an agent may choose from

Not every registry entry is a design decision. Offering all 98 as choices would
be actively harmful: an agent would place a `Status Bar` or a `Favicon` into a
product screen because the inventory said it existed.

Five classes:

| Class | Meaning | May the agent select it? |
| --- | --- | --- |
| **Selectable** | A real design decision | Yes |
| **Composed-only** | Exists only inside a parent; the agent selects the parent | No — select the parent |
| **Chrome** | The OS or the app shell renders it | No |
| **Asset** | Brand asset, determined by brand config, not by design intent | No |
| **Withheld** | Internal, in-progress, or not implemented | No — see the reason |

### Not selectable, and why

| Item | Tier | Class | Evidence |
| --- | --- | --- | --- |
| `Home Indicator` | Components | Chrome | `registry` — iOS system affordance |
| `Status Bar` | Components | Chrome | `registry` — OS-rendered; live `Plattform` typo preserved |
| `Webview` | Components | Chrome | `registry` — "iOS/Android only"; an embedded browser container |
| `Cell Content` | Components | Composed-only | `confluence` — "a composition slot inside Cards and lists. Not a component to choose — a container you compose into." **This one has a full doc**, so it is the only not-selectable item an agent could otherwise have reached through the normal docs |
| `Content Placeholder` | Components | Composed-only | `registry` — "design-intent is a slot: instantiated once and swapped/replaced with local content"; `doc` (card) — "available with 1 to 5 slots" |
| `Filter dropdown container` | Patterns | Composed-only | `registry` — 1 variant, no properties, "sibling pattern to Filter bar" |
| `Map Polygon` | Experiences | Composed-only | `registry` — lives on the "Map experience" page beside `Map template` |
| `Map Polygon backdrop` | Experiences | Composed-only | `registry` — same page, same parent |
| `mapPinsV2_SL` | Experiences | Composed-only | `registry` — brand-specific (SeLoger), successor to a deprecated set |
| `mapPinsV2_IWT` | Experiences | Composed-only | `registry` — brand-specific (Immowelt), sibling of the above |
| `Programmatic Ads` | Components | Withheld — internal | `registry` — commercial ad slot, not a product design choice |
| `Tab Bar` | Components | Withheld — in progress | `registry` — "newly discovered, undocumented, no pattern classification… inside a 'Refacto' section, likely an in-progress refactor". Agents must use `Tabs` until this settles |
| `Footer` | Patterns | Withheld — not implemented | `doc` (navigation-bar) — "Figma only (owned by Header/Footer team)… shows a future version of the component that has not yet been developed" |
| `Favicon` | Foundations | Asset | `registry` — "instantiated as a fixed asset", no properties of its own |
| `Brand App Icons` | Foundations | Asset | `registry` — "flat asset family… per-platform/per-brand app icon exports" |
| `Brand Logo` | Foundations + Components | Asset | `registry` — configured by brand, not chosen by design intent |
| `Flag` | Foundations | Asset | `registry` — country flag family |

Counted by **unique name** rather than registry entry, because `Brand Logo`
occupies two entries: that removes **17 of the 96 names**, leaving **79
selectable**.

### Selectable but undocumented

Of the 43 entries with no doc, 17 are among the not-selectable set above
(`Brand Logo` accounting for two of them), leaving **25 selectable names with no
doc**. The ruleset must still name
them, or an agent will rebuild them from primitives. Purposes recovered by
mining the existing docs for cross-references:

| Item | Tier | Purpose | Source |
| --- | --- | --- | --- |
| `Tooltip` | Components | Temporary short overlay clarifying a UI element; a single brief clarification, not a guided tour | `doc` (coach-mark) |
| `State Messages` | Components | Inline feedback in forms — guide, correct errors, add information | `doc` (alert, text-area, text-field) |
| `Text Button` | Components | A distinct component from Button; used for "Read more", inside action menus and autocomplete dropdowns | `doc` (button, action-menu, autocomplete) |
| `Pop-up` | Components | The small-content alternative to a Modal bottom sheet | `doc` (modal-bottom-sheet) — "If you have a small amount of content, please use the pop-up component instead" |
| `Loading State` | Components | Signals that data or content is being fetched | `doc` (autocomplete, dropdown, info-state) |
| `Image Slider` | Components | A horizontally sliding image sequence; used inside Listing card with the slider disabled | `doc` (listing-card, carousel) |
| `Score Tag` | Components | A Tag specialised for seller lead scoring | `doc` (tag) |
| `Navigation Bar (App)` | Components | Persistent in-app navigation between high-level destinations. Mobile only | `doc` (tabs); `registry` — "mobile (iOS/Android) only" |
| `Badge` | Components | Dynamic attention-grabbing marker attached to a host (button, tab label, cell content, menu entry) | `doc` (button, tabs, cell-content, modal-bottom-sheet-menu) |
| `Image Ratio` | Components + Foundations | Enforces an image aspect ratio | `registry` (11 variants) |
| `Date Field` | Patterns | Date **input**, distinct from the Date Picker's calendar view | `doc` (date-picker, text-area) |
| `Filter button` | Patterns | The individual filter control; Filter bar "consists of filter buttons" | `doc` (filter-bar, charts) |
| `Burger menu` | Patterns | Mobile menu opened from the navigation bar's burger icon | `doc` (navigation-bar) |
| `Burger menu (profil)` | Patterns | A distinct component from `Burger menu`, same variant axes, separate definition | `registry` — confirmed by the design owner as not a duplicate |
| `Menus` | Patterns | Profile and language menus | `registry` — props `Type` (Default/Simple), `Content` (Profil/Language) |
| `Floor selection` | Experiences | Picking an apartment floor, including "GF" for ground floor | `doc` (counter-field) — "Instead, use the floor selection component" |
| `Listing summary` | Experiences | The higher-flexibility alternative to Listing card | `doc` (listing-card) |
| `Map template` | Experiences | The map experience container; parent of the map pin and polygon sets | `registry` — 243 exposed sub-instances |
| `Badge Store` | Components | — | **none** |
| `Button Bar` | Components | — | **none** |
| `Button Card Group` | Components | — | **none** |
| `Feedback Thumb Buttons` | Components | — | **none** |
| `Feedback Bar` | Patterns | — | **none** |
| `Mega menus` | Patterns | — | **none** |
| `Estimation card` | Experiences | — | **none** |

Seven of those have **no evidence anywhere in the repo**. They will appear in the
ruleset's inventory as named-but-undescribed rather than being given an invented
purpose.

---

## Reconciling the Confluence guide

The "Component selection guide" page was migrated on 2026-09-07 and became
[**Which component**](components-rules-ai.md#which-component).
Its 14 problem-type sections were adopted as-is — the organising principle
("by the type of problem being solved, not by category") was already correct and
was not second-guessed. Its `Use X when` / `Use Y instead when` shape became the
`Choose · When · Otherwise` table columns.

**Four things the migration changed or added.**

### 1. `Cell Content` was reclassified

The guide states it plainly — "Not a component to choose — a container you
compose into." It has a full doc, so it was the one not-selectable item an agent
could reach through the normal docs. It is now in the never-select list.

### 2. Coverage — the guide reaches 51 of 79 selectable components

| | Count |
| --- | --- |
| Selectable components | 79 |
| Covered by the guide | **51** |
| Not covered | **28** |

Four of the 28 **have a full usage doc** but no selection guidance, so an agent
cannot find them by intent:

| Component | Tier |
| --- | --- |
| `Floating Button Group` | Components |
| `Listing Card` | Experiences |
| `Phone Number Field` | Experiences |
| `Table` | Experiences |

The other 24 have neither a doc nor a guide entry — listed under
[Selectable but undocumented](#selectable-but-undocumented) above.

### 3. The Experiences tier has zero coverage

**Not one Experience appears in the guide** — not `Listing Card`, the flagship
component, nor `Table`, `Map template`, `Estimation card`, `Floor selection`,
`Listing summary` or `Phone Number Field`. The guide is written entirely at the
Components layer with some Patterns mixed in.

This is the exact failure `CLAUDE.md` warns about: an agent following the guide
faithfully will rebuild a Listing Card from `Card` + `Image slider` + `Tag`,
because nothing told it `Listing Card` exists. It is why
[**Highest tier first**](components-rules-ai.md#highest-tier-first) was
added above **Which component** rather than folded into it — **Which component** is flat and tier-blind by
construction, and no amount of editing its rows fixes that.

### 4. Two guide entries name things that are not components

| Named in the guide | Reality |
| --- | --- |
| "Use **Card grid** when all items should be visible simultaneously" (under Carousel) | No `Card grid` exists in any library. It is a grid layout of `Card`s |
| "Use **Infinite scroll** on mobile and apps" (under Pagination) | A loading behaviour, not a component |

Both are now called out explicitly in
[**Platform limits**](components-rules-ai.md#platform-limits) rather
than silently dropped, because an agent told to "use Card grid" will otherwise
search the libraries, fail, and invent something.

### What the guide resolved

`Text Button`'s purpose — "when full button weight is visually too heavy" — came
from the guide, closing one gap that repo evidence had only partially covered.

### Migration note

The pasted content ends mid-word in the `Energy tag` row ("Use the correct
country/region varian…"). The row was transcribed to that point. **Unverified:
whether any section follows "Identity and media" on the live page.**

---

## Open questions

Each needs Gabriel's answer before the affected rule can be written.

1. **`Image Ratio` and `Brand Logo` exist in two libraries with different keys.**
   Which one does a generating agent instantiate — Components or Foundations? Is
   one deprecated?
2. **Seven selectable components have no description anywhere**: `Badge Store`,
   `Button Bar`, `Button Card Group`, `Feedback Thumb Buttons`, `Feedback Bar`,
   `Mega menus`, `Estimation card`. What is each one for, in one line?
3. **Is `Badge` selectable on its own, or only ever attached to a host
   component?** All five pieces of evidence show it attached.
4. **Is `Filter button` selectable on its own, or only inside `Filter bar`?**
   The registry registers it as a sibling pattern, but the Filter bar doc
   describes it as a constituent.
5. **`Tab Bar` is withheld as an in-progress refactor.** Confirm agents should
   use `Tabs` until it settles, and say who owns the decision to promote it.
6. **`Footer` is Figma-only, owned by the Header/Footer team.** Confirm it stays
   withheld from generation until it is built.
7. **Is `Flag` genuinely an asset**, or is it selectable for locale/country
   pickers?
8. **Four documented components are absent from the guide** —
   `Floating Button Group`, `Listing Card`, `Phone Number Field`, `Table`.
   Deliberate, or an oversight? Each needs a **Which component** row under some problem type;
   `Listing Card` most urgently.
9. **Does anything follow "Identity and media" on the live Confluence page?**
   The paste ended mid-word inside the `Energy tag` row.
10. **Should **Which component** gain rows for the 24 selectable components that have neither
    a doc nor a guide entry?** They are named in **The inventory**'s inventory, so an agent
    knows they exist, but nothing routes it there by intent. This is the largest
    remaining gap after Phase 1.

11. **`Floor selection`'s second part.** It has one (`Counter Field`), and
    `C2 · Tier ceiling` needs two. Is a floor picker a counter plus ground-floor
    handling, or is it genuinely a one-part component and therefore a **Which component** case?
12. **What controlled vocabulary should the platform rows use?** Answered in
    principle — *use a component where it exists* — but the docs express
    existence as `Ready`, `To Do`, `To-do`, `WIP`, `In progress`, `Partially
    available`, `N/A`, `Non-gemini component`, a bare link, or `Not documented`.
    Which of those mean "exists"? `Partially available` (7 Android entries) is
    the genuinely ambiguous one. Blocks **Block 2c · Platform availability**.
13. **How is a rebuilt container detected?** Nothing catches an agent that
    hand-builds an empty state instead of using `Info State`. Parts counting
    cannot work for the container kind, and no alternative is designed.

---

## Decisions taken while filling the component docs

### `Priority` was ambiguous and is now pinned

The inherited `Related Components` tables used `Priority` with **two different
meanings**. In `alert.md` it encoded message severity — `Snackbar` Low rising to
`Alert` High. In `chip.md` it encoded how likely the neighbour was the better
choice — `Chip group` High, `Button` Med. Normalising the table shape without
fixing this would have propagated an ambiguous column into every doc.

**Pinned to the second meaning: how likely this neighbour is the better choice.**
It is the reading a generating agent can act on. Values are `High`, `Medium`,
`Low`, or `—` for the component's own row. `Med` and `Not documented` were
normalised away.

A **forward redirect in Which component** — the anchor's own *Otherwise* column — is
always `High`. A **reverse redirect** — another component pointing here — is
`Medium` unless hand-written content said otherwise.

### Related Components is generated from **Which component**, hand-written content preserved

Tables are the union of what was already written and what **Which component** implies, so the
two can't drift. Existing rows keep their hand-written `Usage` and
`Example Scenario`; only empty cells and `—` placeholders were filled from the
matching **Which component** condition. Rows **Which component** implies but the doc lacked were appended.

### Three components have no neighbour at all

`Avatar`, `Divider` and `Rating` are solo in **Which component** — their *Otherwise* column is
empty. Rather than a one-row table that says nothing, each carries an explicit
**"No alternative"** statement. A stated absence is machine-readable; a
one-row table is just noise.

### Decision trees are grounded, and say so when they are not

Every `Variant Selection Flow` derives from that component's own
`Variants & Modifiers` section, or — where the doc has none (`Info State`,
`Phone Number Field`) — from the variant properties recorded in
`figma/*-registry.json`. Where neither source documents a further axis, the tree
says so outright (`Donut chart`, `Legend`) rather than inventing one.

`Pagination` and `Modal bottom sheet` trees come from their `Behavior &
Responsiveness` sections, which is where their real variant logic had been
written.

---

## **Highest tier first**'s parts list, and what it exposed

Added 2026-09-08 so `C2 · Tier ceiling` of the compliance scorecard can run. It
compares a hand-built element against the parts of each **Highest tier first** row, and **Highest tier first**
stated those parts only as prose.

Turning the prose into data was not a transcription job. **Four rows worked as
written; six did not.**

### Clerical — every part name was unmatchable

Checked against the four registries. Every name in the prose failed an exact
match:

| In the prose | Actual inventory name |
| --- | --- |
| `Image slider` | `Image Slider` |
| `Progress bar` | `Progress Bar` |
| `Counter field` | `Counter Field` |
| `Text field` | `Text Field` |
| `Cell content` | `Cell Content` |
| `Chips` · `Buttons` | `Chip` · `Button` |

Unambiguous, and fixed. A checker matching on inventory names would have found
nothing at all before this.

### Substantive — five named things are not components

| Named | What it actually is | Resolution |
| --- | --- | --- |
| `Price` | Nothing in any inventory. `Listing Card` has a private `.listing_price_tag` slot | **Dropped.** Confirmed by Gabriel as the internal slot. `Card` · `Image Slider` · `Tag` already clear the threshold |
| `container` · `pins` | Descriptions, not names. The real pin sets are `mapPinsV2_SL` / `mapPinsV2_IWT`, both **Never select** never-select | **Row reclassified.** Gabriel: `Map template` is *"full usage or nothing"* — a designer might want a pin as an illustration but will find another solution. There is no partial build to detect |
| `Illustration` · `Text` | An illustration is real but lives under the Foundations registry's separate `illustrations` key, not the component inventory. Text is a token-styled primitive | **Row reclassified.** Gabriel: `Info State` is *"more a content component like a modal with specific content inside"* — a shell, not an assembly |

### The finding that mattered — **Highest tier first** has two kinds of row

Three rows named exactly one part, which contradicts **Highest tier first**'s own operational
test: *two or more of the higher-tier component's own moving parts.* Read
literally, `Info State`, `Floor selection` and `Table` could never fire **Highest tier first**.

Gabriel's answers resolved this, and the resolution is better than the question.
Those rows are not under-documented — **they are not parts-composed things at
all**:

| Kind | Meaning | Rows | Countable? |
| --- | --- | --- | --- |
| **Composed** | Assembled from public components | `Listing Card` · `Filter bar` · `Wizard` · `Phone Number Field` | **yes** |
| **Container** | A shell you place content into | `Info State` · `Table` | no |
| **All-or-nothing** | Used whole or not at all | `Map template` | no |
| **Unresolved** | Undescribed, or one part with no second identified | `Floor selection` · `Listing summary` · `Estimation card` | no |

**Highest tier first still governs all ten.** Six cannot be *enforced by counting parts*,
which is a limit on the checker, not a gap in the rule. The scorecard states
coverage as 4 of 10 and names the six it skips.

**Still open**: `Floor selection` has one part (`Counter Field`) and no second
part identified. A floor picker is plausibly a counter plus ground-floor
handling, but no document says so, and inferring it would be the guessing this
audit already rejected.

**Detecting a rebuilt container is unsolved.** Nothing catches an agent that
hand-builds an empty state rather than using `Info State`. It needs a mechanism
that is not parts-based, and none is designed.

## **Platform limits**, platform availability, and where that data belongs

Found 2026-09-08 while confirming Gabriel's note that *"table is not even dev,
only figma"*. His `Table` doc says `Figma: Ready ✅ · Web: In progress 🚧`, and
it turned out not to be alone.

**52 of the 57 component docs carry their own per-platform readiness row** —
`Figma | Web | iOS | Android`. **Platform limits** had nine hand-written rows, only one about
web readiness.

| State | Figma | Web | iOS | Android |
| --- | --- | --- | --- | --- |
| Ready | 46 | 39 | 30 | 21 |
| In progress | 0 | 2 | 0 | 0 |
| Partially available | 0 | 0 | 0 | 7 |
| To do | 1 | 7 | 15 | 16 |
| N/A | 0 | 1 | 6 | 6 |
| **Not a status** — blank, a link, or free text | **5** | **3** | **1** | **2** |

### The Figma column is unreliable, and redundant

The first reading of this data — *"46 of 52 are Figma-ready, so six are not"* —
was wrong, and was corrected the same day. **All six non-Ready Figma cells are
data-quality problems, not missing components:**

| Figma cell | Docs | Reality |
| --- | --- | --- |
| `Not documented` | `snackbar` · `select-card-group` · `bar-chart` | All three exist in Figma. Snackbar's doc links to its Figma node two lines below the table |
| A link instead of a status | `energy-tag` · `modal-bottom-sheet` | The component exists; the cell simply is not a status |
| `To Do 🚧` | `donut-chart` | `Donut chart` is in the Patterns registry, verified live |

**Every one of the 98 registry entries was verified live in Figma.** So the
authoritative answer to "does this exist in Figma" is the registry, and the
doc's Figma cell is a hand-maintained duplicate that has drifted in six of 52
cases.

### Where each kind of availability data belongs

Gabriel's question was whether this content belongs in the docs or in a skill.
Neither, for the Figma part — it already has a better home.

| Content | Home | Maintained by | Why there |
| --- | --- | --- | --- |
| Does it exist **in Figma**? | `figma/*-registry.json` | the `figma-sync-*` skills | Machine-verifiable, verified live, complete, and it changes when Figma changes rather than when someone edits a doc |
| Does it exist on **web / iOS / Android**? | the component's own doc | a human | Nothing in this repo can verify it, so a human record is the only option |
| **The rule** — use a component where it exists | `components-rules-ai.md` **Platform limits** | a human, from this audit | It is a rule, not data. Duplicating 52 × 4 values into the ruleset would create a second source of truth, which is exactly how the Figma column drifted |

The general principle, since the question raised it: **a skill reads docs and
writes registries. A skill is never a source of truth for knowledge.** The
`figma-sync-*` skills own registry *data*; they own no rules. The
`component-web-ai-docs` skill reads code and docs; it owns neither.

### The policy, and why **Platform limits** states it rather than tabulating it

**Decided 2026-09-08 by Gabriel:** *"Components existing on a platform should be
used on it. Figma first. When working on web or android, we will work on the
status and synchronisation."*

So **Platform limits** now states the policy and names its source of truth per platform,
instead of duplicating the matrix. Two consequences:

- **For Figma there is no availability constraint at all.** All 98 registry
  entries exist. The current milestone is unconstrained on these grounds, which
  is the opposite of what the first reading suggested.
- **For web and native, reconciliation is deferred** — and its first job is not
  reconciliation but a **controlled vocabulary.** The docs currently use `To Do`,
  `To-do`, `WIP`, `In progress`, `Partially available` and `Non-gemini
  component` interchangeably, plus 11 cells that hold no status at all. Nothing
  can be scored or ruled on until those mean fixed things.

`Table` was added to **Platform limits**'s curated table because Gabriel named it directly.
The other web-unready components were not, because the vocabulary question comes
first.

## Rejected approaches

| Rejected | Why |
| --- | --- |
| Publishing the inventory as JSON alongside the Figma registries | JSON in this repo is reserved for Figma identity data written by the `figma-sync-*` skills. A selection ruleset is hand-authored prose-and-tables; putting it in JSON would imply a sync skill owns it. |
| Offering all 98 registry entries as choices | Would let an agent place `Status Bar`, `Favicon` or `Programmatic Ads` into a product screen. Hence the triage above. |
| Deriving purposes for the nine undescribed components from their variant properties | Variant axes say how a component varies, never what it is for. `Feedback Bar` having an `Orientation` property tells you nothing about when to reach for it. Guessing here would put `inferred` content into a ruleset that agents treat as authoritative. |

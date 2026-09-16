Seeded from Confluence pages 3423797434, 3423338655 on 2026-08-26 — this file is now the append-only local audit log; Confluence is no longer read or written by the skill. All entries below predate the 2026-08-26 generalization from Components-only `figma-sync-components` to the multi-tier `figma-sync-component-sets`; new entries for Patterns/Experiences work get tagged `[Patterns / <page>]` / `[Experiences / <page>]`.

---

# Section 1 — Figma Components pattern overview (source page 3423797434)

## Flagged Audit Discrepancies (For Review)

> **Discrepancy 1: Pattern 2 Component Count**
>
> * **Details:** Document #1 states there are **17 Pattern 2 components** (33% of 51 total components audited). However, Document #2's Quick Reference table lists only **16 components**.
> * **Action Required:** Verify if one Pattern 2 component was omitted from the August 2026 table or if a component was reclassified as Pattern 1 during the audit.

> **Discrepancy 2: Scope & Naming Discrepancy (Checkbox vs. Checkbox Group)**
>
> * **Details:** Document #1 audits `Checkbox` as a Pattern 1 self-contained component. Document #2 lists `Checkbox group` as a Pattern 2 component exposing `.header_form` and `.checkboxes`.
> * **Action Required:** Confirm whether `Checkbox` (single atom) and `Checkbox group` (container) are maintained as two separate components with distinct component keys, or if `Checkbox` was superseded by `Checkbox group`.

## Methodology & System Architecture

This documentation covers the research and methodology for enabling an AI agent to design in Figma using Gemini DS components across all 51 audited components.

### Key Finding: `isExposedInstance` Signal

When a component author exposes a nested instance to the Figma properties panel (*Right-click → "Expose properties from nested instances"*), the Figma Plugin API sets `isExposedInstance: true` on that node. This is the native, machine-readable signal for whether a sub-component is intentionally surfaced for configuration:

* `isExposedInstance: true`: Visible in properties panel → agent may configure this sub-component.
* `isExposedInstance: false`: Hidden from properties panel → agent must not interact with it directly.

### Operational Rules

* **Nested Propagation:** Exposure does not propagate automatically. If an exposed sub-component contains deeper nested instances, those deeper instances remain `false` unless explicitly re-exposed by the author.
* **Layer Naming Conventions:** The `.` or `..` prefix convention serves as a human-readable layer-panel signal for DS authors; the agent must rely exclusively on `isExposedInstance` as the authoritative signal.

## Pattern Classification

* **Pattern 1 — Self-contained (67% / 34 components):** `isExposedInstance: false` on all nested instances. The agent configures the parent component exclusively via its variant properties, BOOLEANs, and INSTANCE_SWAP slots. Internal sub-components are off-limits.
* **Pattern 2 — Composed (33% / 17 components):** One or more nested instances set `isExposedInstance: true`. The agent configures the parent, then configures the exposed sub-components appearing as named sections in the Figma properties panel.

## Shared Sub-Components Reference

These private components appear as exposed sub-components across multiple parent components.

### `.header_form` (Shared)

* **Type:** Standalone COMPONENT (not a component set)
* **Key:** `2fd26bdf7fa1968e9a1ad3155f546011e2914095` (confirmed live via exposed-instance trace)
* **Used in:** Checkbox group, Radio button group, Text area

| Property | Type | Default |
| --- | --- | --- |
| Required | BOOLEAN | true |
| Optional | BOOLEAN | true |
| Tooltip | BOOLEAN | true |
| Helper text | BOOLEAN | true |

* **Agent Rules:** Configure via parent component's exposed Header form / Header layer. `Required` and `Optional` are mutually exclusive. Tooltip shows the Info icon touch zone.

### `.header_form` (Slider-Only Variant)

* **Type:** Standalone COMPONENT
* **Key:** `10ffb513884b5e0e56cba53a53131f9e50b57e10` | **Node ID:** `11:219041`
* **Used in:** Slider only (nested inside `.header_slider`, key `944a1ac9a96992532ff1f19539176626f223ff62`)
* **Agent Rules:** Same property schema as shared `.header_form`, but uses a distinct key. Do not conflate keys.

## Pattern 2 Quick Reference Table

| Component | Exposed Sub-components |
| --- | --- |
| Action menu | Button (`.button_type`), Menu (`.action_list`) |
| Button group | Button group items 1–5 (`.base_button_group`) |
| Card | Content placeholder (standalone component, not a variant set) |
| Checkbox group | Header form (shared `.header_form`), Checkboxes (`.checkboxes - Vertical` / `.checkboxes - Horizontal`) |
| Coachmark | `.coachmarkContent` |
| Floating button group | Item 1 & 2 (`.base_floating_button_group`) |
| Image slider | `.views_tags` |
| Loading state | Spinner (`.spinner`) |
| Navigation bar (app) | `.base_tab` ×3–5 |
| Radio button group | Header form (shared `.header_form`), Radio (`.radio - Vertical` / `.Horizontal`) |
| Rating | Star 1–5 (`.star`), `.rating` |
| Select card group | `.content select card` |
| Slider | `.header_slider` (nests private `.header_form`) |
| Tabs | `.base_tabs` → Tab items (`.item_tabs`), plus nested Action menu (`.button_type`, `.action_list`) |
| Text area | Header (shared `.header_form`), State message + counter (`.State message + counter`) |
| Toggle | `.states` → `.side` |

## Sample Component Audits

### 1. Accordion (Pattern 1)

* **Key:** `623d4962ee8ec936f4602d6d4a03db615cbad543` | **Node ID:** `59919:147` | **Variants:** 16
* **Properties:** State (VARIANT), Expanded (VARIANT), Border (VARIANT), Body (BOOLEAN), Description (BOOLEAN), Small title (BOOLEAN), Large title (Web only) (BOOLEAN), Icon (BOOLEAN), Content (INSTANCE_SWAP), ↳ select icon (INSTANCE_SWAP).
* **Exposed Sub-components:** None.
* **Rules:** Configure parent only. Chevron direction is controlled automatically by Expanded variant. `Large title` and `Small title` are mutually exclusive.
* Note: this key/node predates the 2026-08-11 live re-verification — see Section 2 and the components registry for the current confirmed key (`12bad17c5323ed7d55361e6e9a7d159dcd1179d5`, node `11:136048`).

### 2. Checkbox (Pattern 1)

* **Key:** `13e54941d3d7de40a7c70bd3ae069c4ecfe1648b` | **Node ID:** `59920:42205` | **Variants:** 144
* **Properties:** Platform (VARIANT), State (VARIANT), Selection state (VARIANT), Error (VARIANT), Border (VARIANT), Label (VARIANT), State message (BOOLEAN), Tooltip (BOOLEAN), Required (BOOLEAN), Optional (BOOLEAN).
* **Exposed Sub-components:** None (`.checkbox atom`, `Info icon`, `State message` are `isExposedInstance: false`).
* **Rules:** Configure parent only. `Required` and `Optional` are mutually exclusive.

### 3. Pop-up (Pattern 1)

* **Key:** `b7d6a891475cdf75e0dd6e47356f601f6858c231` | **Node ID:** `59920:61441` | **Variants:** 12
* **Properties:** Device (VARIANT), Type (VARIANT), Orientation (VARIANT), Padding content (VARIANT), Header (BOOLEAN), Button Bar (BOOLEAN), Content (INSTANCE_SWAP).
* **Exposed Sub-components:** None.
* **Rules:** Configure parent only. `Landscape` orientation is only valid when `Device=Tablet`.

### 4. Segmented control (Pattern 1)

* **Key:** `2993b71e3479860edcaed2a71531e076ec767f54` | **Node ID:** `59920:64852` | **Variants:** 2
* **Properties:** Content (VARIANT), Button 3–7 (BOOLEANs).
* **Exposed Sub-components:** None (`.segment_button` instances are `isExposedInstance: false`).
* **Rules:** Configure parent only. Buttons 1 and 2 are always visible; Button 3–7 BOOLEANs add optional slots (min 2, max 7).

### 5. Action menu (Pattern 2)

* **Key:** `4312fcfdefa847e4ff847148aed185ae4dc5f514` | **Node ID:** `59920:9595` | **Variants:** 2
* **Properties:** Active (VARIANT: YES, NO).
* **Exposed Sub-components (`isExposedInstance: true`):**
  * **Button** (`.button_type` | Key: `7c2374d3fbabd1b0fde9efe933b3e16b9a8d4f33`): Properties: Type (Floating Button, Text Button, Tertiary Button).
  * **Menu** (`.action_list` | Key: `76ce81ff0ec8cf1403ff57bcaaa3301d973727e8`): Properties: Rows (2–6), Platform (Web/Android, iOS Light).
* **Rules:** Button and Menu are both configurable post-instantiation. `Active=NO` renders an inactive state — use `Active=YES` for interactive state.
* Note: this key predates the 2026-08-11 live re-verification — see Section 2 and the components registry for the current confirmed key (`598c5fcb9e0f4d78a5de1d9806eb2f24505564a5`).

### 6. Carousel (Pattern 1)

* **Key:** `1d9b6638b3f24ef0fc2b970cf2df3a044a5b26dd` | **Node ID:** `59920:37097` | **Variants:** 48
* **Properties:** Step, Arrows position, Dots position, Clip content, Alignment, Title (BOOLEAN), Dots (BOOLEAN), Description (BOOLEAN), Content (INSTANCE_SWAP).
* **Exposed Sub-components:** None.
* **Rules:** Configure parent only. Step controls active arrow states.

### 7. Dropdown (Pattern 1)

* **Key:** `786b2d3b5fd2d4a2f277778d3893758ef1f6a1a9` | **Node ID:** `59920:50493` | **Variants:** 48
* **Properties:** Platform, State, Content, Error, Optional, Tooltip, Required, Icon Leading, State Message, Suffix, Helper Text, ↳ select icon lead (INSTANCE_SWAP).
* **Exposed Sub-components:** None.
* **Rules:** Configure parent only. `Required` and `Optional` are mutually exclusive.

## Documentation Templates

### Template 1 — Self-contained Component (Pattern 1)

```
## [Component name]

### Figma identity
- Component set key: `[key]`
- Node ID: `[nodeId]`
- Variant count: [n]

### Variant properties
| Property | Type | Values | Default |
|---|---|---|---|
| `[name]` | VARIANT | [val1, val2] | [default] |
| `[name]` | BOOLEAN | true / false | [default] |
| `[name]` | INSTANCE_SWAP | [accepted component description] | — |

### Internal sub-components (isExposedInstance: false — not agent-accessible)
| Sub-component | Component set | Notes |
|---|---|---|
| `[name]` | `[componentSetName]` | [notes] |

### Instantiation
figma_instantiate_component(
  componentKey: "[key]",
  nodeId: "[nodeId]",
  variant: { "[Property]": "[value]" },
  overrides: { "[Text layer]": "[content]" }
)

### Agent rules
- [constraints, mutual exclusions, known quirks]
```

### Template 2 — Composed Component with Exposed Sub-components (Pattern 2)

```
## [Component name]

### Figma identity
- Component set key: `[key]`
- Node ID: `[nodeId]`
- Variant count: [n]

### Variant properties
| Property | Type | Values | Default |
|---|---|---|---|
| `[name]` | VARIANT | [val1, val2] | [default] |

### Exposed sub-components (isExposedInstance: true — agent-accessible)
| Sub-component | Component set key | Node ID | Properties panel label |
|---|---|---|---|
| `[name]` | `[key]` | `[nodeId]` | "[label]" |

#### [Sub-component name] — [component set name]
| Property | Type | Values | Default |
|---|---|---|---|
| `[name]` | VARIANT | [...] | [...] |

### Internal sub-components (isExposedInstance: false — not agent-accessible)
| Sub-component | Component set | Notes |
|---|---|---|
| `[name]` | `[componentSetName]` | [notes] |

### Instantiation
// Step 1: instantiate parent
figma_instantiate_component(
  componentKey: "[key]",
  nodeId: "[nodeId]",
  variant: { "[Property]": "[value]" }
)

// Step 2: configure exposed sub-components by targeting layer names post-instantiation

### Agent rules
- [constraints, ordering rules, known quirks]
```

*Page History:* Created: 2026-03-24 | Updated Pass: 2026-08-07

---

# Section 2 — Figma Component Props Audit (source page 3423338655)

* **The entire library was regenerated, not renamed.** The source file key changed from `xxqSJcKOphrgimxRQbvtfe` ("2. Gemini Components Library") to `ABqcGx0cmJWozuJ8OoW6f2` ("2. GSL Components Library"). Every Component Set Key below changed as a result — variant counts were spot-checked and are unchanged, so structure is intact, only identity changed.
* **RESOLVED — Avatar found live (2026-08-11).** The prior "could not be found live" flag is closed: Avatar exists at node `11:146259`, key `dcc57df93537a70ccc49221904d31bac911fdcc8` (changed from the previously documented `578a1fb775333cdd4d9175aea12536960e5774b1`, consistent with the library-wide regeneration noted above). 103 variants confirmed, matching the last-known count.
* **RETRACTED — "Avatar Type=Rectangle removed" and "Circle missing Size=120" were both false, from a stale bridge read.** A single-pass scan right after the Avatar re-discovery above missed 3 live variants (`Type=Rectangle`, all at `Size=120`, `Logo available=Yes`). A follow-up pass with a forced `figma.loadAllPagesAsync()` reload confirmed Rectangle is still live, and Circle/Square size support is actually symmetric (Rectangle-only owns `Size=120`, not an asymmetry between Circle and Square). User-flagged and corrected 2026-08-11. **Takeaway: never conclude an option was removed from a single-pass query on this file — force a full reload and re-query at least twice before reporting removal.**
* **Avatar — unexposed INSTANCE_SWAP slots (confirmed still accurate).** `↳ Select picture` and `↳ Select icon` are defined as INSTANCE_SWAP component properties, but the underlying bound instances (`Content placeholder`, `placeholder`) have `isExposedInstance: false` across all 103 variants. Per the Pattern Classification rule (exposed instance required for Pattern 2), Avatar classifies as **Pattern 1** despite having instance-swap properties.
* **Avatar — Padding gating (confirmed accurate, user-verified 2026-08-11).** `Padding=No` never co-occurs with `Logo available=No`, for any `Type` (Square, Circle, Rectangle) — verified with a forced reload plus an exhaustive filter across all 103 variants (zero counterexamples). When `Logo available=No`, `Padding` is always `Yes`; when `Logo available=Yes`, both `Padding=Yes` and `Padding=No` exist.
* **Avatar — inconsistent internal naming.** The picture-content wrapper is a capitalized `Placeholder` frame when `Logo available=Yes`, but a lowercase `placeholder` instance (no wrapping frame) when `Logo available=No`. Code that walks the layer tree by name should account for this.
* **Accordion — no structural drift (2026-08-11).** Re-verified with forced reload: key `12bad17c5323ed7d55361e6e9a7d159dcd1179d5`, node `11:136048`, 16 variants — unchanged from last capture. Pattern 1 confirmed (`isExposedInstance: false` on every bound instance across all 16 variants, despite the `Content` and `↳ select icon` INSTANCE_SWAP properties).
* **Accordion — property key casing inconsistent with Avatar.** Accordion's exposed instance-swap property is `↳ select icon` (lowercase "select"); Avatar's equivalent is `↳ Select icon` (capitalized). Preserved verbatim per the exact-string-literal rule — flagged as a cross-component naming drift, not corrected in either file.
* **Accordion — one-off title layer rename miss.** The `State=Hover, Expanded=No, Border=No` variant has its title text node named `Title`, while all 15 other variants name the equivalent node `App title`. Looks like a missed rename on that single variant.
* **NEW — Home Indicator documented (2026-08-11).** Pattern 1, 2 variants (`Device=Phone/Tablet`), key `e1504d5c1604c910b2634885863052b0110b3497`, node `11:219584`. No anomalies.
* **NEW — Status Bar documented (2026-08-11).** Pattern 1, 7 variants across `Plattform`/`Device`/`Camera`, key `7a7c90730cc1928f21d4746ee959d03cab7d8691`, node `13894:42307`. Lives nested under the "Toggle" page, not its own top-level page — easy to miss in a page-by-page sweep. Has a live typo: property is `Plattform` (double "t"), preserved verbatim.
* **CORRECTED — Coachmark's "canonical" node no longer exists live (2026-08-11).** The previously documented canonical node `20666:2051` (key `24bf71f6f5a08d9195c1b4098d7502365a62805e`) now times out on every `getNodeByIdAsync` call while all other node lookups resolve instantly — it has been deleted or is otherwise unreachable. A full-file scan finds exactly one Coachmark component set: the one previously flagged as the "buried stale duplicate" (key `d1274e9f9474365783926ee5330e10f93b96a1af`, node `13450:129981`, Pattern 2, 12 variants). **Takeaway: "duplicate" and "canonical" labels can flip between passes — always re-resolve both candidates before trusting a prior pass's labeling.**
* **Cursor components — likely reference material, not real design-system components.** 13 COMPONENT_SET nodes (Arrow/Hand/Zoom/Size/"Move to"/Text/Misc. Cursor) live inside a frame named "Documentation Cursor" on the Cursor page. Six of the seven cursor types are duplicated (two component sets with the identical name, different keys, different variant counts — e.g. "Arrow Cursor" has one copy with 8 variants and another with 6, missing "Poof"/"Poof old"). One duplicate ("Move to Cursor", key `ababec3c7b700f3b398d8620f9924dae0c7f36fc`) has a variant literally named `Type=Type7` — an unfinished placeholder label. Given the "Documentation" framing and the duplication, these read as an OS-cursor reference sheet rather than consumable components — not documented as individual registry entries pending design-team confirmation of intent.
* **Brand Logo and Image Ratio (Foundations-sourced) were not re-verified this pass** — the Foundations Library file (`utQzIdpY7RaHMTmu068e5r`, "0. GSL Foundations Library") did not have the Desktop Bridge plugin open during this audit. Their entries are left as-is with a flag; re-run with that file connected to confirm.
* **Cell Content and Text Field are reclassified from Pattern 2 to Pattern 1.** Live inspection (`isExposedInstance` walk) found no exposed nested instances on either — their "Icon Right" / "Icon Trailing" slots are `INSTANCE_SWAP` component properties, not exposed sub-component instances. The Pattern legend requires an actual exposed instance for Pattern 2.
* **Two distinct `.header_form` components exist.** The shared one used by Checkbox group, Radio button group, and Text area resolves to key `2fd26bdf7fa1968e9a1ad3155f546011e2914095`. A second, Slider-only `.header_form` (nested inside `.header_slider`) is the one at key `10ffb513884b5e0e56cba53a53131f9e50b57e10` — the key the previous version of this page flagged as "unverified." That flagged key was correct but belongs to the Slider-only variant, not the shared component. Both are documented separately in Section 1.
* `.Select card AI test` (key `9f5da93a5cc007775037fd1d16c70115f32703b9`) is a 28-variant sibling of the real "Select card" frame, dot-prefixed and named "AI test" with no description — treated as an internal experiment per this library's dot-prefix-is-private convention, and excluded from the registry.
* **Minor cleanup items (not blocking):** the "Badge Figma Props" page title has a stray trailing "2" (`Badge Figma Props 2`) — cosmetic, content is correct (`badge`, lowercase, key `ac3a83569347cde8300494ded82054462631b717`, 28 variants). `Title + Badge` was intentionally flagged pending fuller review, not an error.
* **Tabs' exposed `.item_tabs` key was wrong in the previous version of this page** (`798bd467ca0f855c3bc17ef95dac71c5e89160c2`). Live tracing confirms the actual wired key is `a4da24bf61ba063c2908bcfec894c5e13c19a13d` (nodeId `11:70529`). Tabs' top-level properties were previously undocumented ("discover via API") — now filled in.
* **Action Menu verified live (2026-08-11).** Pattern 2, 2 variants, key `598c5fcb9e0f4d78a5de1d9806eb2f24505564a5`. Live data matched the existing page exactly (Button/.button_type, Menu/.action_list). No anomalies.
* **Alert verified live (2026-08-11).** Pattern 1, 3 variants, key `6fe94d63e6cfed7576d199dedf7823f55c04b368`. Live data matched the existing page exactly (Buttons/Icon/Illustration/Description + two INSTANCE_SWAP slots, both unexposed). No anomalies.
* **Autocomplete reclassified Pattern 1 → Pattern 2 (2026-08-11).** The existing page documented Autocomplete as self-contained, but a live `isExposedInstance` walk (verified twice with a forced reload) found 40 exposed instances across two distinct layer names — `Icon Trailing` (bound to `.icon_button`, key `cf23b2354ac9b30711a69dcefab9664ebc18ef6d`) and `.base_rows` (key `94d4df40d37779061e3e0353f20a6804069e0c08`). Key and 24-variant count unchanged.
* **`Title + Badge` removed from the registry (2026-08-26) — it is not a component.** Live inspection via Desktop Bridge (`2. GSL Components Library`, page "Cell content") confirms `Title + badge` is a `FRAME`, five levels deep inside the `Cell Content` `COMPONENT_SET` (`Title + badge` → `Title` → `Placeholder + Title` → `Content` → a `Cell Content` variant component). It was never an independently instantiable component; the Confluence-era entry (key `62783a08e3db17fd89929a62617fd14577a679b7`, nodeId `11:175742`) was a false positive, likely from `figma_search_components` matching the frame's name rather than a real `COMPONENT_SET`. `Cell Content` itself was already correctly registered separately (Pattern 1, 20 variants) and needs no change.
* **`Content Placeholder` re-extracted live and corrected (2026-08-26).** Its Confluence source page (3424124990) held only stale, unrelated master-index data — the backfill left a `needs re-extraction` placeholder. Live inspection (page "Content placeholder", node `11:178535`) confirms it's a single `COMPONENT` (key `08ba36d263c9777d4616a752d6e9a90f3ccae666`), not a `COMPONENT_SET` — no variants, no `componentPropertyDefinitions`, no children, no exposed instances. Its own description field: *"Content Placeholder is used to swap with local components."* Confirmed by design owner as an intentional slot component — instantiated once and replaced wholesale, not configured via props/variants. Registered as Pattern 1, variantCount 1.
* **`Chip` / `Chip Group` duplication resolved as documentation-only (2026-08-26).** Both live on the "Chip" page as distinct `COMPONENT_SET`s — `Chip` (nodeId `11:10848`, 15 variants: `Type`×`State`×`Selected`, plus `Icon Left` boolean and a nested `Select Icon` instance-swap prop) and `Chip Group` (nodeId `11:10915`, 3 variants: `Type` only). Neither has exposed instances — both Pattern 1. The Confluence-era "identical merged content on both pages" issue never affected the registry's own key/variantCount values, which were already correct; only the `status` field's warning note needed clearing.
* **[Patterns / Burger menu] First multi-tier run of the generalized skill (2026-08-26).** Found two distinct `COMPONENT_SET`s on the "Burger menu" page with identical variant/prop shape (`Bottom bar` Off/On × `Breakpoint` 320px/768px, 4 variants each, both Pattern 1, no exposed instances) but different keys: `Burger menu` (key `1441ae904fca5422489654112cf2eae951511ac6`, nodeId `2213:93218`, nested inside a "Documentation burger menu (web)" frame) and `Burger menu (profil)` (key `14e3da3a77641ad18114325386e3a264526c0a21`, nodeId `2213:94048`, sits at page root). Confirmed by design owner: both are real, separate components — the nesting inside a "Documentation" frame is a presentation-only convention used across this library, not a staleness signal (see `known-traps.md`). Both registered separately in `figma-patterns-registry.json`.
* **[Patterns] Bulk sweep of remaining pages (2026-08-26).** Surveyed all 21 pages in `3. GSL Patterns Library` (excluding Cover/Index/`---`/Burger menu, already handled). Registered 19 public (non-dot-prefixed) `COMPONENT_SET`/`COMPONENT` entries across 15 pages: `Bar graph`, `Donut chart`, `Line chart`, `KPI`, `Breadcrumb`, `Date Field`, `Date Picker`, `Feedback Bar`, `Filter bar`, `Filter button`, `Filter dropdown container`, `Footer`, `Info State`, `Media Upload`, `Mega menus`, `Menus`, `Navigation bar`, `Top Bar`, `Wizard`. Private `.`-prefixed helper sets on each page (e.g. `.base_footer`, `.Legend`, `.item_entry_l2`) were left unregistered per the dot-prefix-is-private convention. Two pages legitimately hold multiple sibling public patterns rather than one — `Date picker` page (`Date Field` + `Date Picker`) and `Filter bar` page (`Filter bar` + `Filter button` + `Filter dropdown container`) — registered as separate entries, not merged. `Navigation bar` is a single-variant set (`Property 1=Default`), reads as an early-stage/placeholder definition, not flagged further. Two verbatim-preserved typos carried into prop tables per the "preserve string typos" trap: `Loadiing` (Media Upload State variant) and `Plattform` (Top Bar prop name).
  - **Deferred, not registered:** `(WIP) Menu anchor widget` page — page name itself flags it as work-in-progress per the WIP/Refacto trap; its `Menu anchor widget` component was left out pending confirmation it's finished.
* **[Experiences] Full sweep, first run on this tier (2026-08-26).** Surveyed all 11 pages in `4. GSL Experiences Library` (excluding Cover/`---`×2). Registered 11 public entries: `Estimation card`, `Floor selection`, `Listing Card`, `Listing summary`, `Map template`, `mapPinsV2_SL`, `mapPinsV2_IWT`, `Map Polygon`, `Map Polygon backdrop`, `Phone Number Field`, `Table`. `Listing Card` is the largest composed pattern found across any tier so far (602 exposed sub-instances, 79 variants, ~12 private helper sets on its page). One typo preserved verbatim: `Plateform` (Map template prop name).
  - **Deliberately excluded:** `(❌ OUTDATED) mapPins` (nodeId `3458:11043`, "Map experience" page) — explicitly marked outdated by the design owner in its own name; superseded by the two registered brand-specific successors `mapPinsV2_SL` / `mapPinsV2_IWT`. New known-trap added for this marker convention.
  - **`exposedSubComponents` backfilled across all three registries (2026-08-26).** Added the structured `exposedAs`/`key`/`name`/`properties` array to every pre-existing Pattern-2 entry that didn't yet have one: 18 in `figma-components-registry.json` (Action Menu, Autocomplete, Button Group, Card, Checkbox Group, Coachmark, Floating Button Group, Image Slider, Loading State, Modal Bottom Sheet, Navigation Bar (App), Radio Button Group, Rating, Select Card Group, Slider, Tabs, Text Area, Toggle), 10 in `figma-patterns-registry.json` (Bar graph, Donut chart, Line chart, KPI, Feedback Bar, Filter bar, Info State, Media Upload, Top Bar, Wizard), 3 in `figma-experiences-registry.json` (Estimation card, Map template, Phone Number Field) — plus `Listing Card`/`Listing summary` done just before this sweep. Queried all three library files in one session via `figma_execute`'s `fileKey` parameter, without switching Figma Desktop's active tab (see new known-trap). Most Components-tier entries had no `nodeId` recorded from the original Confluence backfill — resolved by exact name search, then a fuzzy fallback search for the 3 that didn't match on first try (`Checkbox goup`, `Navigation Bar`, `Select card` — all confirmed correct by key match despite display-name mismatches with the registry's existing names, see new known-trap). `Map template`'s exposed slots include one private helper explicitly named `❌ .base_floating_button_group (outdated)` live in Figma — preserved verbatim in its data since it's an internal slot reference, not flagged for separate action.
  - **Resolved same day: `.Listings` page components confirmed private, and confirmed genuinely in use.** Design owner renamed all 7 sets on `.Listings` with a `.` prefix live in Figma (`.listing_tags_list`, `.listing_actions`, `.listing_price_tag`, `.listing_title`, `.listing_property_features`, `.listing_property_location`, `.listing_helper_text`) — there is no separate Figma "hidden from publishing" API flag for components (that only exists for variables/styles, see `architecture.md`); the dot-prefix naming convention IS this library's actual privacy mechanism. Cross-referenced by `mainComponent` key (not display name, since instances get renamed on use) against `Listing Card`'s and `Listing summary`'s exposed instances: all 7 are genuinely composed into one or both — 6 into `Listing Card`, all 7 into `Listing summary` (`.listing_helper_text` only there). None registered as standalone entries, per the private-helper convention; the mapping is recorded in `Listing Card`/`Listing summary`'s own `status` fields in `figma-experiences-registry.json` instead.
* **[Foundations] First run of the generalized skill on the `foundations` tier (2026-08-27).** Foundations is mixed-content — Tokens (`figma-sync-tokens`), Icons (~600+ entries on the "Icons" page, deferred to a future dedicated skill), Illustrations (100+ COMPONENT_SETs, deliberately out of scope for now — too large for this pass), and this run's target: the real named components. Registered 5 entries into the new `figma-foundations-components-registry.json`: `Flag` (11 variants), `Favicon` (standalone COMPONENT, built on private `.Brand Favicon` 6-variant helper but exposes no properties of its own), `Image Ratio` (11 variants), `Brand Logo` (136 variants, built on private `.Logo` 34-variant helper), and `Brand App Icons` (new shape — 31 standalone COMPONENTs with no shared COMPONENT_SET, registered as one entry with an `assets` array instead of variant fields). All four variant-bearing sets confirmed Pattern 1 (`isExposedInstance` walk found zero exposed instances on any of them, despite two being built internally on private helper sets — composition without exposure). `" ", ".",` `UX Writing checklist`, and the stray single COMPONENTs on `Index`/`Colors`/`Breakpoint & Grids` were confirmed as documentation/WIP artifacts per design-owner call and excluded entirely, not registered.
* **[Foundations] Illustrations run (2026-08-28).** Previously deferred as out of scope (too large); revisited on request. Foundations' "Illustrations" page holds 10 real category frames (Empty, Error, Success, Loading, Teaser, Onboarding, Property type, Selection, Info, `Placeholder &  Templates`) plus a `Title section` label frame per category (excluded, not a component) and ~10 private dot-prefixed helper sets at page root (`.Header`, `.Player`, `.Variable`, `.Alerts - Tag`, `.Watermark`, four `.Icon - <style>` sets) — none registered individually, per the standing private-helper convention. Registered 173 illustration `COMPONENT_SET`s under a new top-level `illustrations` key in `figma-foundations-components-registry.json`, grouped by category. Every illustration carries exactly one variant property, `Size` (`Banner`/`Hero`/`Picto`/`Spot`) — 100% uniform across all 173, no exceptions. 172/173 are Pattern 2, composing exactly one exposed instance ("Variable tag" → private `.Alerts - Tag` set, itself varying `Style`×`Size`×`Type`) — this is where the library's per-brand multibranding actually lives, one level below the illustration's own variant (see new known-trap). One illustration (`Info Reset Password Email`) has zero exposed instances (Pattern 1) — flagged, not silently normalized. The `HP` category has no `COMPONENT_SET`s at all — instead 2 standalone `HeroIllus` COMPONENTs with no distinguishing properties found yet — registered as a flat asset family (same shape as `Brand App Icons`) and flagged for the design owner to clarify what differentiates them. No Figma "export" page and no local exported-illustration assets exist yet in this repo — confirmed before choosing to register live component metadata over building a new export pipeline.
* **[Foundations] Illustrations anomalies resolved (2026-08-28).** Design owner confirmed both flagged items are intentional, not errors: `Info Reset Password Email`'s missing Alerts-tag composition is deliberate (it's meant to differ from the rest of the catalog), and the `HP` category's two standalone `HeroIllus` components are intentionally standalone — Home Page illustrations don't follow the shared Size/Alerts-tag structure the rest of the catalog uses. Both left registered as-is (no structural change needed) with their `note` fields updated to record the confirmation; `HP` is out of scope for further modeling for now.
* **[Components / Cell content] Re-synced after a live component change (2026-09-16).** Gabriel added two axes to `Cell Content` and asked for the registry and the usage doc to follow. Live read via FigCli on `2. GSL Components Library`, node `18359:17763`. **20 variants before, 33 after.** New variant property `Placeholder left alignement` (`Middle`/`Top`, misspelling preserved) and a third `Padding` option, `0`. Three combination limits are enforced by the variant set itself and were read off the 33 variant names rather than taken from the brief: `Top` exists only with `Alignment=Horizontal`; `Padding=0` exists only with `Clickable=OFF`, covering all three non-clickable combinations; `Clickable=OFF` only ever pairs with `State=Default`, at every padding. **Reclassified Pattern 1 → Pattern 2**, reversing the previous entry, which stated a live trace had found no nested exposed instances — the walk on 2026-09-16 found `.placeholder left` (key `d7ba36d47a5c5fe30aed4e528aa89bea3c6407d4`, node `18359:18070`, `Type=Image/Icon`) exposed on all 33 variants. **Gabriel confirmed the same day that the earlier entry was simply wrong** — the slot was not newly exposed. It carried no `nodeId` and no `auditedDate`, which is the tell for a classification never verified against the current file. The other half of its note held — `Icon Right` is still a BOOLEAN plus an `↳ Icon Right` INSTANCE_SWAP, never an exposed sub-component. Two new traps logged.

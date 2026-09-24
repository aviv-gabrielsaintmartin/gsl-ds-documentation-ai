<!-- Generated from `tokens/color/surface.md` on 2026-09-24 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

_Which token to use inside this colour family. The value tables are left out: a spec never holds a raw value._

## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/base` | The default starting point for most components — cards, sheets, standard containers | Anything with a more specific match below | see below |
| `Surface/Brand` | CTAs and primary/secondary brand-identity fills | Non-branded interactive elements (→ `Interactive`) | `badge`, `button`, `card`, `progressBar` +2 |
| `Surface/Status` | Feedback messages, inline alerts, validation states (error/warning/success/info) | Persistent quality tiers (→ `Score`) | `button`, `checkbox`, `feedbackMessage`, `mediaUpload` +6 |
| `Surface/Score` | Advertiser/listing quality tier badges (Diamond–Bronze) | Status/feedback states (→ `Status`) | **not used** |
| `Surface/Interactive & Active` | Generic hover/pressed/selected/active states with no other semantic role | Elements with a dedicated family already (Status, Brand, Score) | see below |
| `Surface/Constant` | Fixed black/white fills that must ignore brand and light/dark mode entirely | Anything that should re-theme (→ `base`, `Default/Inverted`) | `badge`, `button`, `imageSlider`, `mediaUpload` +1 |
| `Surface/Transparent` | See-through washes with no solid colour, for subtle interaction feedback | Visible/solid state changes (→ `Interactive`) | `actionMenu`, `badge`, `button`, `cellContent` +12 · direct: `Chip`, `DateCalendar` |
| `Surface/On-Brand / On-Primary / On-Secondary` | An element's own fill when it sits on top of a brand/primary/secondary surface | The brand/primary/secondary surface itself | see below |
| `Surface/Data visualisation` | Charts and graphs only | Product UI, ever — even if a colour looks right | see below |
| `Surface/Decorative` | **One documented exception only** (the `rating` star). Brand- and mode-invariant accent with no state meaning and no general usage rule — see the Decorative section. | New work of any kind (→ use `<Rating>`, or raise the need for `Content/Decorative/*`) | `rating` |

## Semantic usage

> **Pick the sub-family by what the element *is*.** The three hover/pressed
> sub-families are not interchangeable — each has a consistent meaning in real
> usage:
>
> | The element is… | Default | Hover | Pressed |
> | --- | --- | --- | --- |
> | A **container or row** that reacts to pointer | `Default/Default` | `Default/Hover` | `Default/Pressed` |
> | An **interactive control** with a fill | `Default/Default` | `Interactive/Hover` | `Interactive/Pressed` |
> | A **ghost control** — no fill, still needs feedback | `Transparent/Default` | `Transparent/Hover` | `Transparent/Pressed` |
>
> Container: `accordion`, `cellContent`, `topBar`, `tabs`. Control: `chip`,
> `actionMenu`, `buttonGroup`, `selectableList`, `slider`. Ghost: `button`
> (tertiary), `pagination`, `toggleButton`.
>
> **A fill is always a `Surface/*` token, and a `Surface/*` token is always a
> fill.** Never bind a border or an icon to one — `button`, `badge` and `chip`
> currently do, and those are recorded defects. (`rating` also does, but as a
> documented exception — see `Decorative` below.)


### Brand

| Token | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Brand/Primary` | Main brand-coloured CTA fill — primary buttons, key actions, one per screen/section | Secondary or supporting fills (→ `Surface/Brand/Secondary`) | `badge`, `button`, `card`, `progressBar` +2 |
| `Surface/Brand/Secondary` | **Not used.** Only `Brand/Primary` has consumers. | Everything, until a real case appears | **not used** |

### Status

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Status/Error` | Light error background — feedback message body, inline validation banner | Solid/high-contrast error fills (→ `Error-Strong`) | `feedbackMessage`, `mediaUpload`, `selectCardGroup`, `statusTag` +1 |
| `Surface/Status/Error-Strong` | Solid, high-contrast error fill — error badges, icon containers, anything needing strong emphasis | Banner/message backgrounds (→ `Error`) | `button`, `checkbox`, `radio`, `tag` |
| `Surface/Status/Information` | Light informational background — tips, neutral announcements | Solid info fills (→ `Information-Strong`) | `feedbackMessage`, `statusTag`, `tag` |
| `Surface/Status/Information-Strong` | Solid, high-contrast info fill | Banner/message backgrounds (→ `Information`) | `tag` |
| `Surface/Status/Success` | Light success background — confirmation banners | Solid success fills (→ `Success-Strong`) | `feedbackMessage`, `statusTag`, `tag` |
| `Surface/Status/Success-Strong` | Solid, high-contrast success fill | Banner/message backgrounds (→ `Success`) | `progressBar`, `progressCircle`, `tag` |
| `Surface/Status/Warning` | Light warning background | Solid warning fills (→ `Warning-Strong`) | `feedbackMessage`, `statusTag`, `tag` |
| `Surface/Status/Warning-Strong` | Solid, high-contrast warning fill | Banner/message backgrounds (→ `Warning`) | `tag` |

*General rule across all four: `-Strong` is a contrast/weight choice (solid fill vs. light wash), not a severity escalation — don't reach for `-Strong` just because a message feels more urgent.*

### Score

| Token | When to use | Used by |
| --- | --- | --- |
| `Surface/Score/Diamond` | Highest advertiser/listing quality tier | **not used** |
| `Surface/Score/Gold` | Second-highest tier | **not used** |
| `Surface/Score/Silver` | Third tier | **not used** |
| `Surface/Score/Bronze` | Lowest tier | **not used** |

*Score tag backgrounds only. Never substitute for `Surface/Status/*` — Score is a tier ranking, not a state.*

### Data visualisation

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Data/Categorical` | Distinct, unordered categories in a chart (up to 5 series) | Ordered/magnitude data (→ Sequential) | dynamic |
| `Surface/Data/Categorical/Disabled` | A categorical series that's toggled off/inactive in a legend | Any in-use series | dynamic |
| `Surface/Data/Sequential` | Data with a single ordered magnitude, low to high (e.g. a heatmap of one metric) | Data with a meaningful zero-crossing (→ Diverging) | dynamic |
| `Surface/Data/Diverging` | Data with a meaningful midpoint — deviation above/below a baseline (e.g. profit/loss) | Simple ordered magnitude (→ Sequential) | dynamic |

*Charts and graphs only — never product UI, regardless of how well a colour happens to fit.*

### Constant

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Constant/Black` | Fixed black fill and its interaction states, ignoring brand and light/dark mode | Anything that should re-theme (→ `Surface/Default/Inverted`) | `imageSlider`, `mediaUpload`, `tag` |
| `Surface/Constant/Black/Transparent/Strong` | Strong black scrim/overlay, fixed opacity regardless of mode | Subtle overlays (→ `Transparent/Subdued`) | `mediaUpload` |
| `Surface/Constant/Black/Transparent/Subdued` | **Not used.** `Transparent/Strong` is the only scrim with consumers (`mediaUpload`). | Scrims (→ `Transparent/Strong`) | **not used** |
| `Surface/Constant/White` | Fixed white fill and its interaction states, ignoring brand and light/dark mode | Anything that should re-theme (→ `Surface/Default`) | `badge`, `button`, `tag` |

### Transparent

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Transparent` | A see-through fill over a light/default-mode background — subtle hover/press wash with no solid colour | Fills over dark/inverted content (→ `Transparent-Inverted`) | `actionMenu`, `badge`, `button`, `cellContent` +12 · direct: `Chip`, `DateCalendar` |
| `Surface/Transparent-Inverted` | A see-through fill over a dark/inverted background | Fills over standard-mode content (→ `Transparent`) | `button`, `progressBar`, `progressCircle` |

### On-Brand / On-Primary / On-Secondary

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/On-Brand` | An element's interaction-state fill when it sits directly on a brand-coloured surface | Elements on the default page background | `button` |
| `Surface/On-Primary/Transparent` | A transparent interaction wash for an element on a primary-coloured fill (e.g. hover on an icon inside a primary button) | Solid on-primary fills — this family is transparency-only | `button` |
| `Surface/On-Secondary/Transparent` | Same, on a secondary-coloured fill | Solid on-secondary fills | `button` · direct: `unsafe` |

### Interactive & Active

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Accent/Light` | A light, brand-tinted accent fill for highlighting content without implying selection | Selected/active state (→ `Active`) — see flag below | `card`, `progressBar`, `progressCircle`, `tag` |
| `Surface/Active` | **Legacy — `tabs` only.** `Active/Default` is unused; `Hover`/`Pressed` are bound by `tabs`, and `progressBar`/`progressCircle` borrow `Active/Pressed` as a static fill (a recorded defect). Do not use for new work. | Anything outside `tabs` (→ `Interactive/Selected`) | `progressBar`, `progressCircle`, `tabs` |
| `Surface/Interactive` | Generic hover/pressed fill for any interactive element with no other semantic role | Elements with a dedicated state family (Status, Active, Selected) | `actionMenu`, `buttonGroup`, `checkbox`, `chip` +10 · direct: `DateCalendar`, `SegmentedControl` |
| `Surface/Interactive/Selected` | The fill for an item in a persisted selected state (e.g. a chosen radio card, toggled filter) | Momentary active/highlight (→ `Active`) | `actionMenu`, `buttonGroup`, `checkbox`, `chip` +9 · direct: `DateCalendar`, `SegmentedControl` |

> **Resolved — use `Accent/Light`.** The two do resolve to the same hex in both
> modes and all six brands, but usage settles it: `Accent/Light/Default` has four
> consumers (`card`, `progressBar`, `progressCircle`, `tag`) while
> `Active/Default` has **none**. The `Active` family is a fast-iteration artifact
> whose only real consumer is `tabs` — see
> color-usage-audit.md § B4. For a new tinted accent
> fill, use `Accent/Light`.

### Decorative

| Token | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Decorative/Red` | **Not used.** No consumer. | Everything, until a real case appears | **not used** |
| `Surface/Decorative/Yellow` | The `rating` star fill — a **documented exception**, brand- and mode-invariant by design. Not a precedent: reach for `<Rating>`, not this token. | Any new element (→ `<Rating>`, or raise the need for `Content/Decorative/*`) | `rating` |

*Decorative tokens carry brand/visual accent, not state. If an element's colour is meant to communicate something (error, active, tier), that's a missed semantic case, not a Decorative one.*

> **Still open — and the two tokens don't behave alike.** `Decorative/Yellow` is
> mode-invariant (`#FFB868` in light *and* dark, all six brands);
> `Decorative/Red` flips (`#DC3741` → `#E26C71`) and has no consumer. If
> `Decorative` means "a fixed accent that ignores the theme", Red contradicts it.
> The family has no settled definition, so no usage rule can be written for it.
>
> Its one live binding — `rating.color.starIcon` — is a **documented exception**,
> not a defect: no Content-family decorative token exists, and a rating star is
> amber by cross-product convention rather than by brand, so mode-invariance is
> correct. The structurally right home is `Content/Decorative/*`; that token
> should be created only once a second use case justifies it. See
> color-usage-audit.md § A5.
>
> Until then: **do not use `Decorative` in new work.** Use `<Rating>` for a
> rating display.

### base

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Default` | The default fill for most components — cards, sheets, standard containers. Start here. | Page-level canvas (→ `Background/Default`) | `accordion`, `actionMenu`, `avatar`, `button` +21 · direct: `CoachMark`, `DateCalendar` |
| `Surface/Default/Inverted` | A component fill that should flip against the page's light/dark mode (e.g. a dark card in light mode) | Fixed-colour needs regardless of mode (→ `Constant`) | `snackbar`, `tooltip` · direct: `CoachMark`, `unsafe` |
| `Surface/Light` | A lighter component fill for subtle recessed containers within a component | Page-level background (→ `Background/Light`) | `avatar`, `card`, `counterField`, `mediaUpload` +2 · direct: `SegmentedControl` |
| `Surface/Light/Transparent` | A translucent, very subtle wash — barely-visible hover/press feedback | Visible state changes (→ `Surface/Interactive`) | `wizard` |
| `Surface/Subdued` | A muted component fill — de-emphasised containers | Disabled state (→ `Surface/Disabled`) | `accordion`, `carousel`, `selectCardGroup`, `tag` · direct: `Chip` |
| `Surface/Disabled` | The fill for a disabled component | Muted-but-interactive containers (→ `Subdued`) | `accordion`, `badge`, `button`, `buttonGroup` +14 |
| `Surface/Dark` | **A neutral fill that must stay distinguishable from a white or light foreground.** Brand-invariant grey; white on it gives exactly 3.0:1, the WCAG non-text floor (`Surface/Subdued` would give 1.16:1 and fail). Use for an unselected control track, an active indicator dot, or a thumbnail scrim. | A general dark background (→ `Default/Inverted`) | `buttonGroup`, `carousel`, `mediaUpload`, `toggle` |

<!-- Generated from `tokens/color/border.md` on 2026-09-24 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

_Which token to use inside this colour family. The value tables are left out: a spec never holds a raw value._

## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for | Used by |
| --- | --- | --- | --- |
| `Border/base` | Standard strokes and outlines on components — the default starting point | Anything with a more specific match below | see below |
| `Border/Status` | Strokes on error, warning, success, or information states (validation, alerts) | General interactive borders (→ `Interactive`) | `checkbox`, `counterField`, `datePicker`, `dropdown` +5 |
| `Border/Active` | The stroke on a currently active/selected element (e.g. a focused input, selected chip) | Focus ring (→ `Focus`) | `tabs` |
| `Border/Focus` | **Nothing — not used on web.** Focus rings use the platform system colours (`Highlight`, `-webkit-focus-ring-color`) so they honour the user's OS settings. | Everything — never bind this | **not used** |
| `Border/Interactive` | Generic hover/pressed stroke on an interactive element with no other semantic role | Elements with a dedicated border family (Active, Focus, Status) | `buttonGroup`, `checkbox`, `chip`, `counterField` +8 · direct: `DateCalendar` |
| `Border/On-Primary / On-Secondary` | A stroke on an element that sits on top of a primary or secondary background | Strokes on default/light backgrounds | see below |
| `Border/Constant` | Fixed black or white stroke that must ignore brand and light/dark mode entirely | Anything that should re-theme | `badge`, `mapPin` (no component) |
| `Border/Transparent` | A **faint but real** edge — 10% opaque, for subtle structural separation. Not invisible. | Visible borders needing contrast; a truly invisible border | `avatar`, `button`, `floatingButtonGroup`, `slider` +1 · direct: `CoachMark` |

## Semantic usage

> **`Border/Transparent` is a faint edge, not an invisible one.** It is 10%
> opaque (`#3232321a`) — a subtle separation line, used by `button`'s floating
> variant and by `avatar`, `tooltip` and `floatingButtonGroup`.
>
> The system has **no fully-transparent border token**. `button` (20 bindings),
> `badge` (4) and `chip` (3) therefore bind `Surface/Transparent` (alpha `00`) or
> their own fill token to get a border that occupies space but renders
> invisibly — so filled and outlined variants share an outer size. That is a
> deliberate component-internal idiom, not a defect: see
> color-usage-audit.md § A1–A3.


### Status

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Border/Status/Error` | Stroke on an input, card, or container in an error state — validation failure, failed action | Warning states (→ `Warning`) | `checkbox`, `counterField`, `datePicker`, `dropdown` +5 |
| `Border/Status/Information` | **Not used.** No component borders a control for information — only `Error` is interactive. | Any control border | **not used** |
| `Border/Status/Success` | **Not used.** No component borders a control for success — only `Error` is interactive. | Any control border | **not used** |
| `Border/Status/Warning` | **Not used.** No component borders a control for warning — only `Error` is interactive. | Any control border | **not used** |

### base

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Border/Default` | Standard stroke on a high-contrast outlined control — outlined button, badge. **Ships `Default` only: there is no `Hover` or `Pressed` leaf** — for those use `Interactive`. | Form controls (→ `Subdued`), structural containers (→ `Light`), disabled (→ `Disabled`), inverted backgrounds (→ `Default-Inverted`) | `badge`, `button`, `toggleButton` · direct: `Checkbox`, `unsafe` |
| `Border/Default-Inverted` | Standard stroke on a component sitting on a dark/inverted background | Standard-mode components (→ `Default`) | `badge`, `button`, `slider` |
| `Border/Subdued` | The standard stroke on a **form control** — input, checkbox, radio, toggle, select. The most-used border in the system. | Interactive borders needing contrast (→ `Interactive`) | `buttonGroup`, `checkbox`, `counterField`, `datePicker` +9 · direct: `SegmentedControl` |
| `Border/Light` | The stroke on a **structural container** — card, modal, accordion, top bar, divider. | Anything needing visible contrast | `accordion`, `buttonBar`, `card`, `divider` +3 · direct: `unsafe` |
| `Border/Surface` | A stroke that matches the surface level — nearly invisible separation between adjacent fills | Visible structural borders (→ `Default`, `Subdued`) | `datePicker` · direct: `unsafe` |
| `Border/Disabled` | Stroke on a disabled component | Interactive states (→ `Interactive`) | `badge`, `button`, `checkbox`, `counterField` +9 · direct: `DateCalendar` |
| `Border/Focus` | **Nothing — not used on web.** Every focusable component sets `outlineColor={['Highlight', '-webkit-focus-ring-color']}` instead, deliberately deferring to the platform. | Everything — never bind this | **not used** |
| `Border/Active` | **Legacy — `tabs` only.** The `Active` family is a fast-iteration artifact; the rest of the system expresses selected states with `Interactive/Default`. Do not use for new work. | Anything outside `tabs` (→ `Interactive/Default`) | `tabs` |
| `Border/Interactive` | Generic hover/pressed stroke with no other semantic role | Elements with a dedicated border family | `buttonGroup`, `checkbox`, `chip`, `counterField` +8 · direct: `DateCalendar` |
| `Border/On-Primary` | Stroke on an element sitting on a primary-coloured fill | Strokes on default backgrounds | `badge`, `button` |
| `Border/On-Secondary` | Stroke on an element sitting on a secondary-coloured fill | Strokes on default backgrounds | `badge`, `button` |
| `Border/Constant/Black` | Fixed black stroke, ignores brand and mode | Anything that should re-theme | `badge` |
| `Border/Constant/White` | Fixed white stroke, ignores brand and mode. **Its only consumer, `mapPin`, has no component in code** — treat as effectively unused. | Anything that should re-theme | `mapPin` (no component) |
| `Border/Accent/Light` | **Not used.** `Surface/Accent/Light` is used by four components; this border twin has no consumer. | Everything, until a real case appears | **not used** |
| `Border/Transparent` | A **faint but real** edge — 10% opaque. Separates a light floating surface from the page. Not invisible. | A truly invisible border (no token exists — see the note above); visible structural borders | `avatar`, `button`, `floatingButtonGroup`, `slider` +1 · direct: `CoachMark` |
| `Border/Transparent/Strong` | A slightly more visible transparent stroke — stronger ghost container edges | Solid borders needing colour contrast | `slider` |

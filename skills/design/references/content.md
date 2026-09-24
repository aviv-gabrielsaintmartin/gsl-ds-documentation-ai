<!-- Generated from `tokens/color/content.md` on 2026-09-24 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

_Which token to use inside this colour family. The value tables are left out: a spec never holds a raw value._

## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for | Used by |
| --- | --- | --- | --- |
| `Content/base` | Text and icon fills for standard UI — the default starting point for all text colour decisions | Anything with a more specific match below | see below |
| `Content/Status` | Text and icon colour inside or alongside a status state (error, warning, success, info) | Score tier labels (→ `Score`) | `feedbackMessage`, `mediaUpload`, `stateMessage`, `statusTag` +3 |
| `Content/Score` | Text colour inside a Score tag (Diamond–Bronze tier labels) | Status/feedback text (→ `Status`) | **not used** |

## Semantic usage

### base

*Bind all text and icon fills to these — never hardcode a colour value.*

> **Icons take Content tokens, not `Symbol/*`.** `Icon` renders with `fill: currentcolor` and a `color` prop, so an icon is painted by whatever Content token it inherits or is given. The `Symbol/*` family is Figma-only — see symbols.md.

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Content/Default` | Primary body text, labels, headings — the default for most text. Start here. | De-emphasised or disabled text (→ `Subdued`, `Light`, `Disabled`) | `accordion`, `actionMenu`, `avatar`, `badge` +31 · direct: `CoachMark`, `DateCalendar` |
| `Content/Default/Inverted` | Text on a dark/inverted background | Text on standard-mode backgrounds (→ `Default`) | `actionMenu`, `badge`, `button`, `buttonGroup` +12 · direct: `CoachMark`, `DateCalendar` |
| `Content/Subdued` | Supporting text — helper text under a field, metadata, captions. Note it is *darker* than `Light` (`#4B4B4B` vs `#646464`). | Placeholders (→ `Light`); disabled text (→ `Disabled`); body text (→ `Default`) | `accordion`, `cellContent`, `mediaUpload`, `stateMessage` +1 · direct: `Carousel`, `unsafe` |
| `Content/Light` | **Placeholders and optional markers** — every `placeholder` (5 of 5) and `optional` (3 of 3) binding in the system uses this. Also field affordance icons. | Body or supporting text (→ `Default`, `Subdued`) | `buttonGroup`, `checkbox`, `datePicker`, `dropdown` +5 · direct: `DateCalendar`, `Dropdown` |
| `Content/Disabled` | Text or icon on a disabled component | De-emphasised but interactive text (→ `Subdued`) | `accordion`, `actionMenu`, `badge`, `button` +21 · direct: `DateCalendar`, `SegmentedControl` |
| `Content/Active` | **Legacy — `tabs` only** (the selected tab label). The `Active` family is a fast-iteration artifact; the rest of the system uses `Interactive` or `Default/Inverted`. Do not use for new work. | Anything outside `tabs` | `tabs` |
| `Content/Interactive` | Text or icon colour responding to hover/pressed/selected states with no other semantic role | Elements with a dedicated content family (Status, On-Primary, On-Secondary) | `chip`, `field`, `imageSlider`, `link` +1 · direct: `CoachMark` |
| `Content/Interactive/Inverted` | Interactive-state text on a dark/inverted background | Standard-mode interactive text (→ `Interactive`) | `textButton` · direct: `CoachMark` |
| `Content/On-Brand/Disabled` | Disabled text sitting directly on a brand-coloured surface | Enabled text on brand surfaces (→ `On-Primary`) | `button` |
| `Content/On-Primary` | Text or icon on a primary brand-coloured fill (e.g. label inside a primary button) | Text on secondary fills (→ `On-Secondary`) | `badge`, `button`, `link`, `tag` |
| `Content/On-Secondary` | Text or icon on a secondary brand-coloured fill | Text on primary fills (→ `On-Primary`) | `badge`, `button`, `link` |
| `Content/Constant/Black` | Fixed near-black text that must **not** flip in dark mode. ⚠️ Identical to `Content/Default` in light mode (`#323232`) but does not flip — mistaking the two gives 1.31:1 in dark. | Any text that should re-theme (→ `Default`) | `badge`, `button`, `tag` |
| `Content/Constant/White` | Fixed white text that must **not** flip in dark mode — a fixed scrim or image overlay. ⚠️ Identical to `Content/Default/Inverted` in light mode (`#FFFFFF`) but does not flip — mistaking the two gives 1.26:1 in dark. | Text on an inverted surface (→ `Default/Inverted`, which flips) | `imageSlider`, `mediaUpload`, `tag` |
| `Content/Constant/White/onDark` | **Not used.** No component binds it. | Everything, until a real case appears | **not used** |

### Status

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Content/Status/Error` | Error text or icon — validation messages, failed states, inline field errors | Warning text the user should notice but not fix immediately (→ `Warning`) | `feedbackMessage`, `mediaUpload`, `stateMessage`, `statusTag` +2 |
| `Content/Status/Error-Strong` | Stronger error emphasis — error text on a light error surface needing higher contrast | Standard error labels (→ `Error`) | `tag` |
| `Content/Status/Error/Inverted` | Error text on a dark/error-strong surface | Error text on standard backgrounds (→ `Error`) | **not used** |
| `Content/Status/Warning` | Warning text — prompts the user to review before continuing | Confirmed failures (→ `Error`) | `feedbackMessage`, `stateMessage`, `statusTag` |
| `Content/Status/Warning-Strong` | Higher-contrast warning text on a light warning surface | Standard warning labels (→ `Warning`) | `tag` |
| `Content/Status/Warning/Inverted` | Warning text on a dark/warning-strong surface | Warning text on standard backgrounds (→ `Warning`) | **not used** |
| `Content/Status/Success` | Confirmation text — action completed, saved, uploaded | Ongoing neutral info (→ `Information`). Note `wizard` binds this as a circle **fill**, which is a recorded defect (→ `Surface/Status/Success-Strong`) | `feedbackMessage`, `stateMessage`, `statusTag`, `wizard` |
| `Content/Status/Success-Strong` | Higher-contrast success text on a light success surface | Standard success labels (→ `Success`) | `tag` |
| `Content/Status/Success/Inverted` | Success text on a dark/success-strong surface | Success text on standard backgrounds (→ `Success`) | **not used** |
| `Content/Status/Information` | Informational text — tips, announcements, non-urgent notes | Actionable states (→ `Warning`, `Error`) | `feedbackMessage`, `stateMessage`, `statusTag` |
| `Content/Status/Information-Strong` | Higher-contrast information text on a light info surface | Standard info labels (→ `Information`) | `tag` |
| `Content/Status/Information/Inverted` | Information text on a dark/info-strong surface | Info text on standard backgrounds (→ `Information`) | **not used** |

*General rule: `-Strong` is a contrast choice (higher emphasis on a light wash background), not a severity escalation.*

> **The four `/Inverted` status tokens are unused.** Status text never sits on a
> solid status-coloured fill anywhere in the system. Do not reach for them.
>
> **Only `Error` is interactive.** `Error` has `Hover` and `Pressed` leaves and
> appears on form controls and danger actions. Information, Success and Warning
> appear **only** in messaging and display components (`FeedbackMessage`,
> `StateMessage`, `StatusTag`, `Tag`) — never on an interactive element.

### Score

| Token | When to use | Used by |
| --- | --- | --- |
| `Content/Score/Diamond` | Text label inside a Diamond-tier Score tag | **not used** |
| `Content/Score/Gold` | Text label inside a Gold-tier Score tag | **not used** |
| `Content/Score/Silver` | Text label inside a Silver-tier Score tag | **not used** |
| `Content/Score/Bronze` | Text label inside a Bronze-tier Score tag | **not used** |

*Paired with the matching `Surface/Score/*` background. Never use for general status text — Score is a tier ranking label only.*

> **Corrected 21 September 2026 — all eight are used, and the scan could not see it.**
> `ScoreTag` **is** implemented, in `@gsl-core-web/design-system-patterns-tag`
> (`libraries/patterns/tag/src/ScoreTag`). It binds one `Surface/Score/*` and one
> `Content/Score/*` per tier, exactly as the table above describes.
> **The earlier note said the opposite** — *"no scoring UI exists in `libraries/ui`;
> `scoreTag.json` defines tokens for a component that has no implementation"* —
> and it was right about `libraries/ui` and wrong about the conclusion. **The
> usage scan reads `libraries/ui` only**, so every component built in
> `libraries/patterns` reads as zero. `Score tag`, `Floor selection`,
> `Phone number field`, `Map pin`, the charts and the energy class slider all
> live there. **A zero in this file means "not used in `libraries/ui`", never
> "not used".** Gabriel approved the correction the same day.

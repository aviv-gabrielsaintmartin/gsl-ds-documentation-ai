> **This page is evidence-based.** The **Used by** column lists the components
> that actually bind each token in `gsl-core-web-design-system`, generated from
> [color/color-usage-ledger.md](color-usage-ledger.md). **not used** means no
> component binds it — do not reach for it.
> Rules for generating UI: [color-rules-ai.md](color-rules-ai.md).
> Evidence and verdicts: [color-usage-audit.md](color-usage-audit.md).

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

> **Icons take Content tokens, not `Symbol/*`.** `Icon` renders with `fill: currentcolor` and a `color` prop, so an icon is painted by whatever Content token it inherits or is given. The `Symbol/*` family is Figma-only — see [symbols.md](symbols.md).

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

## Tokens

### base (27)

*Text and icon fills. Bind text fills to these — never hardcode.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Content/Active/Default` | `#323232` | `#F8F8FA` | |
| `Color/Content/Active/Pressed` | `#323232` | `#F8F8FA` | |
| `Color/Content/Constant/Black/Default` | `#323232` | `#292D3B` | |
| `Color/Content/Constant/White/Default` | `#FFFFFF` | `#FFFFFF` | |
| `Color/Content/Constant/White/onDark/Default` | `#E0E0E0` | `#E3E5ED` | |
| `Color/Content/Default/Default` | `#323232` | `#F8F8FA` | |
| `Color/Content/Default/Inverted/Default` | `#FFFFFF` | `#15171E` | |
| `Color/Content/Default/Inverted/Hover` | `#E0E0E0` | `#525A76` | |
| `Color/Content/Default/Inverted/Pressed` | `#C7C7C7` | `#68708C` | |
| `Color/Content/Disabled` | `#959595` | `#7F87A0` | |
| `Color/Content/Interactive/Default` | `#323232` | `#F8F8FA` | |
| `Color/Content/Interactive/Hover` | `#4B4B4B` | `#AFB5C8` | |
| `Color/Content/Interactive/Inverted/Default` | `#EEEEEE` | `#292D3B` | |
| `Color/Content/Interactive/Inverted/Hover` | `#E0E0E0` | `#AFB5C8` | |
| `Color/Content/Interactive/Inverted/Pressed` | `#C7C7C7` | `#525A76` | |
| `Color/Content/Interactive/Pressed` | `#000000` | `#E3E5ED` | |
| `Color/Content/Light/Default` | `#646464` | `#AFB5C8` | |
| `Color/Content/On-Brand/Disabled` | `#32323280` | `#292D3B80` | |
| `Color/Content/On-Primary/Default` | `#FFFFFF` | `#F8F8FA` | Brand-variant — see below |
| `Color/Content/On-Primary/Disabled` | `#FFFFFF99` | `#F8F8FA80` | Brand-variant — see below |
| `Color/Content/On-Primary/Hover` | `#FFFFFFcc` | `#F8F8FAcc` | Brand-variant — see below |
| `Color/Content/On-Primary/Pressed` | `#FFFFFFb2` | `#F8F8FAb2` | Brand-variant — see below |
| `Color/Content/On-Secondary/Default` | `#FFFFFF` | `#F8F8FA` | |
| `Color/Content/On-Secondary/Disabled` | `#FFFFFF99` | `#F8F8FA99` | |
| `Color/Content/On-Secondary/Hover` | `#FFFFFFcc` | `#F8F8FAcc` | |
| `Color/Content/On-Secondary/Pressed` | `#FFFFFFb2` | `#F8F8FAb2` | |
| `Color/Content/Subdued/Default` | `#4B4B4B` | `#C9CDDB` | |

<details>
<summary>Brand variance — 4 of 27 tokens vary across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Content/On-Primary/Default` | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#323232` | `#FFFFFF` | `#FFFFFF` |
| `Content/On-Primary/Disabled` | `#FFFFFF99` | `#FFFFFF99` | `#FFFFFF99` | `#32323280` | `#FFFFFF99` | `#FFFFFF99` |
| `Content/On-Primary/Hover` | `#FFFFFFcc` | `#FFFFFFcc` | `#FFFFFFcc` | `#323232cc` | `#FFFFFFcc` | `#FFFFFFcc` |
| `Content/On-Primary/Pressed` | `#FFFFFFb2` | `#FFFFFFb2` | `#FFFFFFb2` | `#323232b2` | `#FFFFFFb2` | `#FFFFFFb2` |

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Content/On-Primary/Default` | `#F8F8FA` | `#15171E` | `#15171E` | `#15171E` | `#15171E` | `#F8F8FA` |
| `Content/On-Primary/Disabled` | `#F8F8FA80` | `#15171E99` | `#15171E99` | `#15171E99` | `#15171E99` | `#F8F8FA99` |
| `Content/On-Primary/Hover` | `#F8F8FAcc` | `#15171Ecc` | `#15171Ecc` | `#15171Ecc` | `#15171Ecc` | `#F8F8FAcc` |
| `Content/On-Primary/Pressed` | `#F8F8FAb2` | `#15171Eb2` | `#15171Eb2` | `#15171Eb2` | `#15171Eb2` | `#F8F8FAb2` |

</details>

### Status (14)

*Text and icon colours for status states.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Content/Status/Error-Strong/Default` | `#5E1519` | `#F6DCDD` | |
| `Color/Content/Status/Error/Default` | `#B32730` | `#E89597` | |
| `Color/Content/Status/Error/Hover` | `#881E24` | `#EFB9BB` | |
| `Color/Content/Status/Error/Inverted/Default` | `#E89597` | `#B32730` | |
| `Color/Content/Status/Error/Pressed` | `#5E1519` | `#F6DCDD` | |
| `Color/Content/Status/Information-Strong/Default` | `#00344B` | `#DAE4ED` | |
| `Color/Content/Status/Information/Default` | `#006591` | `#8DAFCE` | |
| `Color/Content/Status/Information/Inverted/Default` | `#8DAFCE` | `#006591` | |
| `Color/Content/Status/Success-Strong/Default` | `#00391A` | `#DAE5DC` | |
| `Color/Content/Status/Success/Default` | `#006D31` | `#8DB596` | |
| `Color/Content/Status/Success/Inverted/Default` | `#8DB596` | `#006D31` | |
| `Color/Content/Status/Warning-Strong/Default` | `#422C0E` | `#FFDCBE` | |
| `Color/Content/Status/Warning/Default` | `#7F561C` | `#E69B33` | |
| `Color/Content/Status/Warning/Inverted/Default` | `#E69B33` | `#7F561C` | |

### Score (4)

*Text colours for the Score tag only.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Content/Score/Bronze` | `#604015` | `#FFEEE0` | |
| `Color/Content/Score/Diamond` | `#005A78` | `#E3F8FF` | |
| `Color/Content/Score/Gold` | `#5E4E12` | `#FFF6D6` | |
| `Color/Content/Score/Silver` | `#3B3F4A` | `#E9EEF5` | |

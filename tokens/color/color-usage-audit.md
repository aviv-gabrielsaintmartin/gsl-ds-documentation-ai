# Colour usage audit

_Human-facing audit only — this is **not** the AI-facing ruleset. It records how
colour tokens are **actually** used in `gsl-core-web-design-system`, where that
disagrees with the written definitions, and the verdict reached on each
disagreement. An AI agent should read [color-rules-ai.md](color-rules-ai.md) for
the rules to apply — this file exists so the evidence and the reasoning don't
bloat that doc._

## Why this exists

The colour token set was built quickly, then extended to cover product requests.
Documentation followed late, so the family pages ([surface.md](surface.md),
[border.md](border.md), [content.md](content.md)) describe what each token is
*nominally* for, written top-down from the token names. Nothing in them was
derived from, or checked against, what components actually bind.

That gap is the blocker for AI-generated interfaces: an agent reading only the
family pages cannot tell an authorised token from an unused one, or a
system-wide convention from a one-component workaround.

This audit closes the gap by extracting the real binding graph and adjudicating
every place it disagrees with the docs.

## Method

Fully mechanical extraction, then human adjudication. The extractor
([scripts/extract_color_usage.py](../scripts/extract_color_usage.py)) reads three
sources and writes [color/color-usage-ledger.md](color-usage-ledger.md) and
`color-usage.json`:

1. `libraries/tokens/src/brands/<BRAND>/figma/colors.{light,dark}.json` — the
   semantic colour set, 6 live brands × 2 modes (AVIV excluded, see below)
2. `libraries/tokens/src/shared/components/*.json` — component-token bindings
3. `libraries/{ui,patterns,core,icons,illustrations,logos,…}/src/**.{ts,tsx}` —
   direct usage, excluding stories and tests

It makes no judgement; it records what is bound to what. Re-run it to refresh —
the generated files are not hand-edited.

**Code is the source of truth for this audit.** Where a token exists in Figma but
not in code, it is logged as Figma drift (see [Figma reconciliation](#figma-reconciliation)),
not as a code defect.

State of the code repo at time of extraction: 3 September 2026.

## The architecture the docs were missing

The single most important structural fact, and the reason usage looked opaque:

**Components do not choose semantic colour tokens.**

```
brands/<BRAND>/figma/colors.{light,dark}.json     218 semantic tokens
        │                                          (identical key set in all 6 brands × 2 modes)
        ▼
shared/components/*.json                           60 files · 631 colour bindings
        │   component.toggle.color.borderHover
        │       = {color.border.interactive.hover}
        ▼
libraries/ui/src/*.tsx                             53 components
            borderColor="unsafe_component.toggle.color.borderHover"
```

Every colour decision in the system lives in that middle layer. No doc mentioned
it before this audit; [color-tokens.md](color-tokens.md) now does.

Two things follow. First, "which component uses which token" was never unknown —
it is a declarative table, and this audit is mostly a matter of reading it.
Second, the *interesting* question is not the mapping but whether each mapping is
intentional.

## What the extraction found

| Metric | Value |
| --- | --- |
| Semantic colour tokens defined | 218 |
| Brands × modes | 6 × 2 — identical 218-key set in every one |
| Component token files | 60 (48 declare colour, 12 do not; 4 describe a component that does not exist) |
| Component → semantic bindings | 631 |
| Tokens with **no consumer at all** | 73 (33%) |
| Tokens consumed **only dynamically** | 22 (`surface.data.*`, chart series) |
| Tokens used **directly in `.tsx`**, bypassing the component tier | 28 |
| Bindings whose **role disagrees with the semantic family** | 32 (27 are the documented border-parity idiom, A1–A3) |
| Public props typed to accept **any** token in a family | 2 |

## Verdicts

| Verdict | Meaning for the ruleset |
| --- | --- |
| **canonical** | This is the token for this job. |
| **restricted** | Allowed only in the named situation, for the named reason. |
| **do-not-use** | Never reach for it. Reason recorded. |
| **fix-code** | Usage is wrong; the binding should change. Ruleset documents the target. |
| **needs-verification** | Real deviation, cause not yet established. Not authorised in the meantime. |
| **exception** | Deliberate, understood, and correct for its one case — but not generalisable into a rule. Recorded so it is neither copied nor "fixed". |

---

## A. Role / family mismatches

_A component token named for one paint role, bound to a semantic token from
another family. 32 bindings, five patterns._

### A1–A3 · Borders bound to `Surface/*` — **exception** (corrected)

**This finding was wrong in the first two drafts of this audit. The correction is
recorded here in full, because the original recommendation would have caused a
visual regression.**

27 bindings across `button` (20), `badge` (4) and `chip` (3) bind a *border* role
to a `Surface/*` token. I first called this "the clearest inconsistency in the
set" and recommended repointing `button`'s twenty to
`color.border.transparent.default` as a "zero-risk rename, same resolved value".

**The values are not the same:**

| Token | Light | Alpha |
| --- | --- | --- |
| `surface.transparent.default` | `#32323200` | **00 — fully invisible** |
| `border.transparent.default` | `#3232321a` | 1a — **10% opaque, a visible tint** |

Repointing would have put a faint dark edge on every primary, tertiary and
danger button.

#### What the pattern actually is

Confirmed by Gabriel (the designer): nothing in Figma looks like this, and it is
dev-specific. The code bears that out — it is a deliberate, consistent idiom:

> **Every variant carries a 1px border so filled and outlined variants have
> identical outer dimensions.** A variant that should show an edge binds a real
> `Border/*` token. A variant that should not binds whatever renders invisibly.

`button` follows it exactly:

| Variant | Fill | Border | Why |
| --- | --- | --- | --- |
| `secondary.default` (outlined) | transparent | `border.default.default` | a real edge |
| `secondary.floating` (white, floating) | `surface.default.default` | `border.transparent.default` | a deliberate faint edge |
| `primary.default` (filled) | brand primary | `surface.transparent.default` | invisible — parity only |
| `tertiary.default` (ghost) | transparent | `surface.transparent.default` | invisible — parity only |

`badge` splits the same way: its filled `primary` variants bind border = fill
(invisible against itself); all nine outlined `secondary` variants bind real
`Border/*` tokens. `chip` likewise — the unselected border is
`border.interactive.default`; only the *filled* selected state binds border =
fill.

**In all seven `badge`/`chip` cases the border token is literally the same token
as the fill.** That is what makes it invisible.

So there is no inconsistency, and `button.secondary.floating` is not the "correct
one" the earlier draft claimed — it is a different job.

#### The real finding

**The border family has no truly-transparent token.** `Border/Transparent` is a
subtle 10% edge, not "no edge". Devs reach into `Surface/*` because nothing in
`Border/*` renders invisibly.

→ **Verdict: exception.** The bindings are correct and should not be changed.
The gap is in the token set, not the code.

→ **Proposal for the DS team:** add a fully-transparent border token (e.g.
`Border/Transparent/None` at alpha `00`) so the "invisible border for box-model
parity" idiom can be expressed in the border family. Until then these bindings
are the only way to say it.

#### Why this matters beyond the finding

This one was caught because a designer said "nothing in Figma looks like that."
Code-only extraction established *what* is bound; it could not establish *why*,
and the plausible-looking story — wrong family, easy fix — was wrong. **A binding
that looks like a mistake needs someone who knows the intent before it is called
one.** B1 and B3 were then put to the designer: B3 came back confirmed wrong, B1
came back as something larger than a token choice.

### A4 · `wizard` fills step icons with content tokens — **fix-code**

`wizard.color.icon.bgCurrent` → `color.content.default.default`,
`bgError` → `color.content.status.error.default`,
`bgCompleted` → `color.content.status.success.default`.

A filled circle taking its fill from the text palette. The correct targets are
the **saturated** status fills, and they resolve to byte-identical values:

| Current binding | Correct binding | Light | Dark |
| --- | --- | --- | --- |
| `content.status.error.default` | `surface.status.errorStrong.default` | `#b32730` | `#e89597` |
| `content.status.success.default` | `surface.status.successStrong.default` | `#006d31` | `#8db596` |

The values are byte-identical, so repointing is visually risk-free. Note the
target is `…Strong`, **not** `surface.status.<status>.default`: those are the
pale message-background tints (`#edf2ee`, `#fbeeee`) and would give 1.13:1
against a white glyph.

**Confidence: cosmetic only.** After the A1–A3 correction this is worth stating
plainly — the two tokens resolve identically, so nothing renders differently
either way. The case for changing it is that the family label should match the
role, not that anything is broken. If there is a reason `wizard` was written this
way that is not visible in the token files, that reason wins. Low priority.

### A5 · `rating` paints the star with a surface token — **exception**

`rating.color.starIcon` → `color.surface.decorative.yellow.default`.

Confirmed with Gabriel: **this is not a defect.** No Content-family decorative
token exists, and this was the only way to get a semantic token for the case at
the time. The colour itself is right; only the family label is off.

The token's behaviour supports that reading. `Decorative/Yellow` is **both
brand-invariant and mode-invariant** — `#FFB868` in all six brands and in both
light and dark:

| Token | Brand-varies | Light | Dark | Mode-invariant |
| --- | --- | --- | --- | --- |
| `Surface/Decorative/Yellow` | no | `#FFB868` | `#FFB868` | **yes** |
| `Surface/Decorative/Red` | no | `#DC3741` | `#E26C71` | no |

That is `Constant/*` behaviour, and it is correct here: a rating star is amber by
cross-product convention, not by brand, so it should not re-theme. Gabriel's
point that it sits outside the brand guidelines is borne out by the values.

**Where it is genuinely wrong is the family, not the choice.** It paints an
*icon*, and icons render through `fill: currentcolor` from a `color` prop
(C2/B5), so Content is the structurally correct family.
`Content/Decorative/Yellow` is what this wants to be.

**Recommendation: do not create that token yet.** One consumer and no writable
usage definition is exactly the pressure that produced the sprawl this audit is
documenting — 73 of 218 tokens with no consumer. Creating a family for a single
component repeats it. Better to leave the binding, record the exception, and set
a trigger: **create `Content/Decorative/*` when a second use case appears**, and
migrate `rating` with it.

**The contrast question softens too.** The star gives 1.71:1 against the default
surface in light mode, but `rating` also binds `ratingText` →
`content.default.default`, so the star is not the sole carrier of the value. It
is reinforcement alongside a readable number — decorative in the real sense.
Worth a designer's eye, not a blocker.

**Open, and more interesting than the binding itself:** the two Decorative
tokens do not behave alike. Yellow is mode-invariant, Red flips. If `Decorative`
means "fixed accent that ignores the theme", Red contradicts it — and Red has no
consumer to settle the question. The family has no coherent definition yet, which
is precisely why no usage rule can be written for it.

---

## B. State drift

### B1 · `toggleButton` — the border itself diverges from the design — **needs-verification**

My original finding was narrow: `toggleButton.color.borderSelected` binds
`color.border.default.default` while five other components use
`color.border.interactive.default` for a selected border. Gabriel's answer
reframes it into something larger.

**Per the design (Figma), `ToggleButton` shows a border only in the *unselected*
hover and pressed states.** The code does something different, and not in one
way but three:

`ToggleButton.tsx:71-72` sets the border unconditionally —

```tsx
borderWidth="unsafe_component.toggleButton.borderWidth"   // borderWidth.1
borderStyle="solid"
```

— and `mapButtonStateToBoxProps` supplies a colour in every state:

| State | Border in code | Value (SL light) |
| --- | --- | --- |
| Unselected, resting | `border.subdued.default` | `#959595` |
| Unselected, hover | `border.subdued.default` — **unchanged** | `#959595` |
| Unselected, pressed | `border.subdued.default` — **unchanged** | `#959595` |
| Selected | `border.default.default` | `#323232` |
| Disabled | `border.disabled` | `#E0E0E0` |

So in code:

1. **The border is always visible**, in every state — not only on unselected
   hover/pressed.
2. **Hover and pressed do not change the border at all.** `getBorderColor()`
   branches only on `isDisabled` and `isSelected`; hover and pressed change the
   *background* only.
3. **A `borderSelected` token exists and is used** — which the design implies
   should not be visible.

Because Storybook renders this component from this code, Storybook necessarily
shows the border in every state too. That part is a logical consequence, not an
observation — worth re-checking against a live story before anyone acts, since
it conflicts with the recollection that prompted this finding.

**The question is no longer "which token".** It is whether `ToggleButton` should
carry a resting and selected border at all. If the design is right, the fix is in
the component's state logic, and `borderSelected` / the resting `border` binding
may need to become transparent or be removed — not repointed.

→ Needs a Figma/Storybook comparison on the component itself. The token choice
(`border.default.default` vs `border.interactive.default`) is downstream of that
answer and not worth resolving first.

### B2 · `buttonGroup` disabled states — **restricted, justified**

| Component token | Bound to | Everyone else |
| --- | --- | --- |
| `buttonGroup.color.borderDisabled` | `color.border.subdued.default` | `color.border.disabled` (13) |
| `buttonGroup.color.textDisabledSelected` | `color.content.light.default` | `color.content.disabled` (22) |
| `buttonGroup.color.bgDisabledSelected` | `color.surface.dark.default` | `color.surface.disabled` (14) |

**This should not be "fixed" reflexively.** A disabled-*selected* segment sits on
a darker fill than a normal disabled surface. Using `content.disabled` on it
would give **1.0:1 in light mode — literally invisible**. The current
`content.light.default` gives 1.98:1: still low, but disabled controls are
exempt from WCAG 1.4.3, and the alternative is strictly worse.

→ Documented as a general rule: a **selected + disabled** pairing needs a
foreground chosen against the selected fill, not the disabled fill.

### B3 · Pressed-state tokens used as static fills — **fix-code, and forbid**

- `skeleton.color.bg` → `color.surface.light.pressed`
- `skeleton.color.bgGradient` → `color.background.subdued`
- `progressBar.color.onDark.bgProgress` → `color.surface.active.pressed`
- `progressCircle.color.onDark.bgProgress` → `color.surface.active.pressed`

None of these elements has a pressed state. Confirmed by Gabriel: **this is
wrong, and it was done to avoid creating a new style.** It should be fixed, and
the practice forbidden going forward.

Unlike A1–A3, there is no forced-choice defence here. A skeleton shimmer and an
on-dark progress fill are their own things; borrowing an interaction-state token
for its hex value hides that a token is missing, and couples two unrelated
elements — change `Surface/Light/Pressed` for a real pressed state and the
skeleton changes with it.

**The fix needs one decision, because no existing token is a clean match:**

| Binding | Nearest existing token | Problem |
| --- | --- | --- |
| `skeleton.color.bg` (`#E0E0E0` / `#7F87A0`) | `surface.disabled` (`#E0E0E0` / `#525A76`) | same in light, **differs in dark** |
| `progress onDark.bgProgress` | — | the other three `bgProgress` variants use brand, selected and status fills; none fits on-dark |

→ Either create the missing tokens (`Surface/Skeleton/*`, an on-dark progress
fill) or accept a deliberate repoint with the dark-mode difference reviewed.
Creating them is the honest option: this is a case where the token genuinely does
not exist, as opposed to A1–A3 where the borrowing is the only way to express
something.

→ **Forbidden in the ruleset:** never bind a `hover` or `pressed` leaf to an
element that has no such state.

### B4 · The `Active` family is a fast-iteration artifact — **restricted (legacy)**

Confirmed by Gabriel: the family is the result of fast iteration, during which
hover and pressed states were sourced from whichever family was to hand. The
extraction shows the consequence precisely — **`Active` is, in practice, the
tabs family**:

| Token | Consumer |
| --- | --- |
| `color.border.active.default` | `tabs.color.line` |
| `color.content.active.default` | `tabs.color.tab.colorSelected` |
| `color.surface.active.hover` | `tabs.color.tab.bgHover` |
| `color.surface.active.pressed` | `tabs.color.tab.bgPressed`, `progressBar`, `progressCircle` |
| `color.surface.active.default` | — orphan |
| `color.border.active.pressed` | — orphan |
| `color.content.active.pressed` | — orphan |

Meanwhile the rest of the system expresses the same concept through
`interactive.selected.*` — 7 components for the default state alone.

So two parallel vocabularies cover one idea, and the newer one is half-populated
(3 of 7 leaves orphaned).

→ `Interactive/Selected/*` is **canonical** for selected/active states.
`Active/*` is **restricted to `tabs`** and must not be used for new work. The
`progressBar`/`progressCircle` borrowings are a B3 fix, not an endorsement.

### B5 · Icons have no family of their own — **resolved**

Icon-role bindings resolve to `content.light.default` (3),
`content.default.default`, `content.default.inverted.default`,
`content.interactive.default` and `surface.decorative.yellow.default` (A5).
Meanwhile the whole 22-token `color.symbol.*` family has **zero references
anywhere in the monorepo source**.

That looked like neglect. It is not — see [C2](#c2--symbol-is-a-design-authoring-palette--do-not-use-in-web).

---

## C. Conventions and restricted tokens

### C1 · `Surface/Dark` — a contrast floor, not an oddity

Believed to be toggle-only and possibly an accessibility choice. Both halves
check out, with a correction.

**Four consumers, not one:**

| Component | Token | What it paints |
| --- | --- | --- |
| `toggle` | `bgDefault` | the track in the off state |
| `buttonGroup` | `bgDisabledSelected` | a selected-but-disabled segment |
| `carousel` | `indicatorCurrent` | the active pagination dot |
| `mediaUpload` | `bgImageEdit` | the edit scrim over a thumbnail |

**Brand-invariant** — `#959595` light, `#979eb5` dark, identical in all 6 brands.
A neutral, not a brand colour.

**The accessibility hypothesis is correct, with a number.** A white knob on
`Surface/Dark` gives exactly **3.0:1** in light mode — the WCAG 1.4.11 non-text
contrast floor. The intuitive alternative, `Surface/Subdued`, gives **1.16:1**, a
clear fail.

→ `Surface/Dark` is the token for *a neutral fill that must stay distinguishable
from a white or light foreground*. All four consumers fit. It gets a **positive
rule**, not a prohibition — and explicitly **not** a general-purpose dark
background, which is `Surface/Default/Inverted`.

### C2 · `Symbol/*` is a design-authoring palette — do-not-use in web

The 22-token family is referenced nowhere in `ui`, `patterns`, `core`, `icons`,
`illustrations` or `logos`. Two pieces of evidence explain why, and they are
structural rather than accidental:

**Icons** are painted through `currentcolor`. `libraries/core/src/Icon/Icon.tsx:73`
sets `fill: 'currentcolor'`, with a `color` prop defaulting to `inherit`. An icon
takes whatever **Content** token it is given. There is no path by which a Symbol
token reaches an icon in web.

**Illustrations are raster.** All 362 illustration components render a
pre-rendered `.webp` through `<img srcSet>` — no inline SVG, no `fill`
attribute, no runtime colour anywhere in the library.

Confirmed with Gabriel: **`Symbol/*` is used only in Figma.**

So [symbols.md](symbols.md) is not wrong: it is a real, correctly documented
palette — applied at asset-authoring time and baked into exported bitmaps. It is
a designer-facing palette with no web runtime.

→ **do-not-use in generated web code**, while `symbols.md` remains valid for
designers. `symbols.md` now carries a note saying so.

### C3 · The status convention — all four statuses vs. error only

Confirmed with Gabriel and borne out by the bindings: status colour belongs to
messaging. But the extraction shows the real convention has **two tiers**, and
the narrower rule alone would forbid things the system does deliberately.

**Tier 1 — all four statuses.** Messaging and display components only:

| Component | Status bindings | Uses |
| --- | --- | --- |
| `feedbackMessage` | 8 of 8 | `surface.status.<s>.default` background + `content.status.<s>.default` icon |
| `stateMessage` | 4 of 5 | `content.status.<s>.default` — this is the message under a text field. The fifth binding is its non-status `helper` text (`content.subdued.default`). |
| `statusTag` | 8 of 8 | surface + content, all four |
| `tag` | 16 of 46 | weak/strong variants, all four |

**Tier 2 — error only.** Every other status use in the system is error, and only
error:

| Purpose | Components | Tokens |
| --- | --- | --- |
| Form control in an error state | all nine: `textField`, `textArea`, `dropdown`, `datePicker`, `counterField`, `mediaUpload`, `selectCardGroup`, `checkbox`, `radio` | `border.status.error.default` · `.hover` · `.pressed` |
| Selected control in an error state | `checkbox`, `radio` (in addition to their error border) | `surface.status.errorStrong.*` |
| Destructive action | `button` (danger), `textButton` (danger) | `surface.status.errorStrong.*`, `content.status.error.*` |

No component uses information, success, or warning on an interactive element.

**This single rule explains 13 of the 73 orphans** — they are not gaps:

| Orphaned | Count | Because |
| --- | --- | --- |
| `surface.status.{information,success,warning}Strong.{hover,pressed}` | 6 | only error is interactive |
| `border.status.{information,success,warning}.default` | 3 | only error borders a control |
| `content.status.*.inverted.default` | 4 | status text never sits on an inverted surface |

→ **canonical**, stated as: *all four statuses in messaging and display
components; error alone on interactive elements; status never inverted.*

The one genuine exception is `progressBar` / `progressCircle` binding
`surface.status.successStrong.default` for a success progress fill — a display
use of a saturated status colour outside a messaging component. Reasonable;
recorded so it is not mistaken for drift.

---

## D. Tokens with no consumer — 73 of 218 (33%)

Flagged, not triaged, by decision. Grouped, with the apparent reason:

| Cluster | Count | Reason |
| --- | --- | --- |
| `symbol.*` — brand, disabled, skinColors | 22 | Figma-only design-authoring palette (C2) |
| `scales.energy` | 2 | **corrected 10 Sep 2026** — only `Blue100` and `Red300`. The other ten are bound by `EnergyScale.tsx`; this audit first recorded all 12 as unconsumed |
| `scales.co2` | 7 | no GSL-component consumer — checked again 10 Sep 2026, still true |
| `surface.constant.*` hover/pressed/disabled/transparent | 9 | fixed black/white fills; only the `.default` leaves have consumers |
| `surface.status.{info,success,warning}Strong.{hover,pressed}` | 6 | only error is interactive (C3) |
| `content.status.*.inverted.default` | 4 | status text is never inverted (C3) |
| `border.status.{information,success,warning}.default` | 3 | only error borders a control (C3) |
| `content.score` / `surface.score` — bronze, silver, gold, diamond | 8 | scoring UI not built in `libraries/ui` |
| `background.constant.{black,white}` | 2 | no consumer |
| One-offs — the ten below | 10 | see table |

The ten one-off orphans, each the only unused leaf in an otherwise-used group:

| Token | Note |
| --- | --- |
| `border.focus` | orphaned by design — focus rings use platform system colours (F3) |
| `surface.active.default` | `Active` is a fast-iteration artifact (B4) |
| `border.active.pressed` | same |
| `content.active.pressed` | same |
| `surface.light.hover` | `surface.light.default` and `.pressed` are both used |
| `surface.brand.secondary.default` | only `brand.primary.*` has consumers |
| `surface.decorative.red.default` | only `decorative.yellow` is used, by `rating` (A5) |
| `border.accent.light.default` | `surface.accent.light.default` is used; the border twin is not |
| `content.constant.white.onDark.default` | no consumer |
| `background.light` | referenced only from a Storybook story, never production code |

→ **do-not-use** in the ruleset, phrased as "no component consumes this", with
`border.focus`, `symbol.*`, `scales.*` and the status clusters carrying their own
reasons.

**An orphan is not automatically dead.** Only two of these ten clusters are
unexplained (`score`, `background.constant`). The rest are orphaned for a
recorded, sound reason — the status clusters especially: 13 tokens that look like
gaps are simply the unreachable corners of a convention (C3).

**Corrected 10 September 2026.** This section previously said all 19 `scales.*`
tokens were consumed by an external team with no GSL-component consumer, and
told an agent not to generate with them. That was wrong.
`libraries/patterns/energyclassslider/src/EnergyScale.tsx` — a GSL component in
the GSL web repo — binds ten of the twelve `scales.energy` leaves. The colour
ruleset now carries the French DPE class mapping and permits both families.

Genuinely unconsumed: `scales.energy.blue100`, `scales.energy.red300`, and all
seven `scales.co2`. Do not delete any of them.

---

## E. Component-tier bypasses — 28 tokens

28 semantic tokens are referenced straight from `.tsx`, skipping the
`unsafe_component.*` layer. Storybook stories and tests are excluded — counting
them inflates this figure to 35 and adds eight phantom "offenders" (`Box`,
`Overlay`, `usePopover`, `useSafeArea`, `usePreventScroll`, `useResizeObserver`,
`useFocusable`, `StatusTag`) whose only token references are in demo code.

| Owner | Tokens | Has a colour token file? |
| --- | --- | --- |
| `DateCalendar` | 11 | **no** |
| `SegmentedControl` | 10 | **no** |
| `CoachMark` | 4 | **no** |
| `unsafe` (charts) | 9 | n/a |
| `Chip` | 4 | yes — genuine bypass |
| `ImageSlider`, `GeminiProvider` | 2 each | mixed |
| `Checkbox`, `Dropdown`, `SelectableList`, `Carousel`, `TopBar` | 1 each | yes — genuine bypass |

**The bypass is not sloppiness.** The three largest are exactly three of the
twelve components whose token file declares no colour at all. They colour
themselves in code because they were never given a colour layer.

The other nine colourless files: `barChart`, `brandLogo`, `chartTooltip`,
`checkboxGroup`, `chipGroup`, `icon`, `infoState`, `radioGroup`, `scoreTag`.

→ Documented finding, no code change in this pass. The ruleset records that
`DateCalendar`, `SegmentedControl` and `CoachMark` do not follow the standard
tier, so their source is not a model to copy.

### E2 · Four token files describe a component that does not exist

`barChart.json`, `brandLogo.json`, `mappin.json` and `scoreTag.json` define
component tokens for components with no implementation anywhere in the
monorepo — not in `ui`, `ui/unsafe`, `core`, `patterns` or `logos`.
(`checkboxGroup`, `chipGroup`, `radio` and `icon` look similar but are real; they
are nested inside `Checkbox/`, `Chip/`, `RadioGroup/` and `core/Icon`.)

Only `mappin` declares colour: `mappin.color.border` →
`color.border.constant.white`. That token therefore has exactly one consumer, and
that consumer is a phantom — treat `border.constant.white` as effectively unused.

→ Recorded, no action. Relevant to any future "is this token used?" question:
the component-token layer is not a reliable proxy for shipped UI on its own.

### E1 · Two public props accept any token in a family

`ChartReferenceArea` types a prop as `` `color.content.${string}` |
`color.surface.${string}` `` — any consumer can pass any of ~144 tokens. Flagged
for the DS team as a hole in the type surface; out of scope here beyond "do not
rely on this prop being constrained."

---

## F. Resolved non-issues

_Recorded so they are not re-investigated._

### F1 · `Border/Default/Hover` does not exist in code

`Border/Default` ships **`Default` only** — no hover, no pressed, in any of the 7
brands or either mode. Components using `border.interactive.hover` for hover
strokes are not deviating; it is the only hover border in the system, and
[border.md:11](border.md) already authorises it ("generic hover/pressed stroke on
an interactive element"). **Zero violations.**

If `Border/Default/Hover` exists in Figma, that is Figma-side drift — see below.

### F2 · The `border/hover` role is near-perfectly consistent

Every border+hover binding resolves to `color.border.interactive.hover` (10
components) or `color.border.status.error.hover` (9 components, error variants of
the same fields). The only exception is `chip` (A3).

### F3 · `Border/Focus` is orphaned by design

`color.border.focus` has zero consumers, and [border.md:37](border.md) calls it
"keyboard focus ring — accessibility indicator only". That reads as a defect
until you look at the code: every focusable component sets

```tsx
outlineColor={['Highlight', '-webkit-focus-ring-color']}
```

— CSS **system colours**, deliberately bypassing the design system so the focus
ring honours the user's OS and browser settings. That is the correct
accessibility choice.

Separately, the six `borderFocus` component tokens (`textField`, `textArea`,
`dropdown`, `datePicker`, `counterField`, `mediaUpload`) all bind
`color.border.interactive.default` — but those paint the *field's* focus border,
a different thing from the keyboard focus ring.

→ **do-not-use**, reason recorded: "focus rings use platform system colours;
`Border/Focus` is not used on web."

### F4 · AVIV is not a live brand — excluded

An `AVIV` token set ships in `libraries/tokens/src/brands/`, structurally
identical to the six live brands (same 218 keys, its own values). Confirmed by
Gabriel: **it is not in use.** It is excluded from this audit, from the ledger,
and from the ruleset; the extractor skips it by default
(`--include-inactive-brands` overrides).

Recorded here so future audits do not re-raise it as a documentation gap — the
docs are correct to describe six brands.

Its exclusion changes none of the findings: AVIV has no component bindings of its
own, and the brand-variance counts are **21 light / 23 dark either way**. The one
real correction to `color-tokens.md` was the token total, 221 → 218.

---

## G. Light-mode collisions — where Figma drift hides

The single most useful output of this audit for Figma reconciliation, and the
reason the `constant` check was worth running.

**21 groups of tokens resolve to the same value in light mode but different
values in dark.** Inside such a group the tokens are visually indistinguishable
in light mode, so a wrong pick in Figma looks perfect on the canvas and only
breaks when dark mode renders. **10 of the 21 groups contain two or more live
tokens**, which is where a realistic mistake can occur.

The worst offender: **ten live tokens all resolve to `#ffffff` in light mode**,
and they split into five different dark values.

| Token | Consumers | Dark |
| --- | --- | --- |
| `content.default.inverted.default` | 37 | `#15171e` |
| `surface.default.default` | 26 | `#292d3b` |
| `content.onPrimary.default` | 9 | `#f8f8fa` |
| `surface.constant.white.default` | 8 | `#f8f8fa` |
| `content.constant.white.default` | 4 | `#ffffff` |
| `content.onSecondary.default` | 4 | `#f8f8fa` |
| `border.defaultInverted.default` | 3 | `#292d3b` |
| `background.default` | 2 | `#15171e` |
| `border.onPrimary.default` | 2 | `#f8f8fa` |
| `border.constant.white` | 1 | `#f8f8fa` |

The other nine live-risk groups, by light value: `#323232` (9 live tokens),
`#e0e0e0` (8), `#000000` (5), `#eeeeee` (5), `#4b4b4b` (4), `#ffffff99` (3),
`#959595` (3), `#c7c7c7` (3), `#ffffff33` (2). Full tables in
[color/color-usage-ledger.md](color-usage-ledger.md).

### G1 · Worked example — the inverted `Link`

Confirmed by Gabriel: in Figma and Storybook an inverted `Link` variant exists,
and Figma binds it to **constant** content. The code binds something else:

```
link.color.inverted.default  =  {color.content.default.inverted.default}
```

Both are `#ffffff` in light mode, so the two are indistinguishable on a light
canvas. In dark mode they diverge, and only one survives:

| | Light | Dark |
| --- | --- | --- |
| Inverted surface it sits on | `#323232` | `#e3e5ed` |
| **Code** — `content.default.inverted.default` | `#ffffff` → **12.82:1** | `#15171e` → **14.23:1** |
| **Figma** — `content.constant.white.default` | `#ffffff` → 12.82:1 | `#ffffff` → **1.26:1** |

The inverted surface flips with the mode (`#323232` → `#e3e5ed`); constant white
does not. So the Figma binding renders white text on a near-white surface in
dark mode.

**Code is correct. This is a live Figma bug**, invisible in light mode.

→ Add to the Figma reconciliation backlog. It also generalises: any Figma
binding that names a `Constant/*` token where the code names an `Inverted/*` or
`On-Primary/*` one is the same bug, and the `#ffffff` group above lists every
place it can occur.

### G2 · Method note

This check is now part of the extractor and regenerates with the ledger. It
needs no Figma access — it identifies the *risk surface* from code alone, so a
designer can audit the Figma pages that matter instead of all of them.

---

### G3 · `Surface/Dark` and `Active/*` checked the same way

Run against the two families most likely to diverge. One is safe, the other has
two live traps.

**`Surface/Dark` — low risk.** It shares `#959595` with `content.disabled` (42
consumers) and `border.subdued.default` (15). A wrong pick on the toggle track:

| Knob on… | Light | Dark |
| --- | --- | --- |
| `surface.dark.default` (correct) | 3.0:1 | **5.14:1** |
| `content.disabled` | 3.0:1 | 3.83:1 |
| `border.subdued.default` | 3.0:1 | 3.83:1 |

All three clear the 3:1 non-text floor in both modes. A wrong pick degrades
contrast but does not break it — and note the correct token has the most
headroom in dark, which is a further argument that C1 is deliberate.

**`Active/*` — two live traps, both in `tabs`, both invisible in light mode.**

*The selected tab label.* `content.active.default` shares `#323232` with six
divergent live tokens. Against the page background:

| Token | Light | Dark |
| --- | --- | --- |
| `content.active.default` (correct) | 12.82:1 | **16.88:1** |
| `content.constant.black.default` | 12.82:1 | **1.31:1** ❌ |

*The tab hover background.* `surface.active.hover` shares `#f8c3c6` with
`symbol.brand.primary.subdued`. With the selected label on top:

| Token | Light | Dark |
| --- | --- | --- |
| `surface.active.hover` (correct) | 8.31:1 | **16.2:1** |
| `symbol.brand.primary.subdued` | 8.31:1 | **1.45:1** ❌ |

The second is the more likely mistake: `Symbol/*` is a Figma-only family (C2),
so it sits in the designer's picker with no code counterpart to contradict it.

The rest of `Active/*` is low risk — `border.active.default` collides only with
an unused Symbol token whose dark value barely differs, and
`surface.active.default` / `.pressed` have unique light values.

### G4 · The rule behind all of it

**The dangerous collisions are where a mode-fixed token shares a light value
with a mode-flipping one.** `Constant/*` and `Symbol/*` hold their value across
modes by design; everything else flips. When the two coincide in light mode,
picking the fixed one looks perfect and fails in dark.

**6 of the 10 live-risk groups contain a `Constant/*` or `Symbol/*` token** —
`#ffffff`, `#323232`, `#e0e0e0`, `#000000`, `#eeeeee`, `#4b4b4b`. Those are the
high-severity groups: Link (G1), the tab label and the tab hover (G3) are all
instances.

The other four groups — `#ffffff99`, `#959595`, `#c7c7c7`, `#ffffff33` — diverge
only among mode-flipping tokens, so a wrong pick still adapts to dark mode and
degrades rather than breaks. `Surface/Dark` sits in this benign category.

→ **For the Figma audit, start with any binding that names a `Constant/*` or
`Symbol/*` token.** That is where the invisible bugs are.

---

## Figma reconciliation

Code is the source of truth for this audit, so anything that exists only in
Figma is listed here rather than treated as a code defect. This list needs a
Figma-side pass to complete — it cannot be derived from the code repo.

| Item | Status |
| --- | --- |
| `Border/Default/Hover` | Believed to exist in Figma; absent from code in all 6 brands (F1) |
| `Corner radius/*` semantic layer | Known Figma-only layer, already noted in [radius-usage-audit.md](../radius/radius-usage-audit.md) |
| `Symbol/*` | Exists in both, but is applied at asset-authoring time only (C2) |
| Inverted `Link` bound to `Content/Constant/White` | **Figma bug** — unreadable in dark mode (1.26:1). Code is correct. (G1) |
| `Select card group` showing `Constant` | **Figma bug**, confirmed by Gabriel. No code equivalent; resolved Figma-side. |
| `Link`, `Carousel` showing `Constant` | `Carousel` still unexplained — code uses `surface.dark` / `surface.subdued`, no constant anywhere |
| Selected tab label | Check it is not bound to `Content/Constant/Black` — 1.31:1 in dark (G3) |
| Tab hover background | Check it is not bound to `Symbol/Brand/Primary/Subdued` — 1.45:1 in dark (G3) |
| Any `Constant/*` or `Symbol/*` binding | The six high-severity collision groups (G4) — audit these first |
| `ToggleButton` border | Design shows a border only on unselected hover/pressed; code draws one in every state and never changes it on hover/pressed (B1) |

## Open questions

1. **A truly-transparent border token.** Should `Border/*` gain an alpha-`00`
   leaf so the border-parity idiom (A1–A3) stops borrowing from `Surface/*`?
   A DS-team call, not a design one.
2. **The `Decorative` family's definition.** `Yellow` is mode-invariant, `Red`
   flips, and `Red` has no consumer. Is `Decorative` meant to ignore the theme or
   not? Until that is settled the family cannot carry a usage rule. (A5)
3. **Figma reconciliation.** The table above needs completing from the Figma
   side.

### Answered since first draft

- **`scales.energy` / `scales.co2`** — **answer corrected 10 Sep 2026.**
  `scales.energy` is consumed by `EnergyScale.tsx` inside this design system, not
  by an external team. Both families are now permitted, with rules. (D)
- **`Symbol/*`** — Figma-only. (C2)
- **`Active/*`** — fast-iteration artifact. (B4)
- **`surface.status.*` and `feedbackMessage`** — confirmed; the full convention
  is recorded in C3, and it explains 13 orphans that looked like gaps.
- **A1–A3, border-mirrors-fill** — not a defect: a deliberate box-model-parity
  idiom, forced by the absence of a fully-transparent border token. My original
  "zero-risk rename" was wrong and would have regressed every filled button. (A1)
- **`rating` / `Decorative/Yellow`** — an exception, not a defect. Reclassified;
  the token to create is `Content/Decorative/*`, but only once a second use case
  justifies it. (A5)

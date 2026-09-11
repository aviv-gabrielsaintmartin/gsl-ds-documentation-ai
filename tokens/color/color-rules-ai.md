# Colour rules for AI generation

_The authoritative ruleset for choosing colour when generating a GSL interface.
Every rule here is derived from real bindings in `gsl-core-web-design-system`, not
from token names. Evidence and reasoning:
[color-usage-audit.md](color-usage-audit.md). Exact values:
[background](background.md) · [surface](surface.md) · [border](border.md) ·
[content](content.md) · [symbols](symbols.md) · [scale](scale.md)._

---

## Components first

*Do not choose colours. Choose components.*

_**This rule precedes every other rule on this page.** The spacing and typography rulesets open with the same rule, under the same name — it is one rule stated where each ruleset needs it._

Colour in this system is decided by a component-token layer, not by the person
writing the UI:

```
semantic token  →  component.<name>.color.<role><State>  →  component
```

A `<Button>` is already correct in every brand, both modes, and all five
interaction states. A hand-built `<div>` styled to look like a button is correct
in none of them.

**So: reach for a component first, every time.** See
[../../components/components-index.md](../../components/components-index.md) for the
inventory. Only colour something yourself when no component covers it — a custom
layout surface, a one-off container, a page background.

Everything below applies **only** to that remainder.

---

## No raw colour

*Never write a raw colour.*

No hex, `rgb()`, `hsl()`, named CSS colour, or opacity-shifted variant. Every
colour comes from a token. There are no exceptions in product UI.

---

## Pick the family

*Pick the family by what you are painting.*

| Painting | Family |
| --- | --- |
| The page/screen canvas behind everything | `Background/*` |
| A component or container fill | `Surface/*` |
| A stroke or outline | `Border/*` |
| Text **and icons** | `Content/*` |
| DPE / CO₂ domain data | `Scales/Energy/*` · `Scales/CO2/*` — see [**Energy and CO2 scales**](#energy-and-co2-scales) |
| Error, information, success, warning | see [**Status is messaging**](#status-is-messaging) |

`Symbol/*` and `Native/*` never appear in generated web code — see [Never use](#never-use).

---

## Surface sub-family

*Surface: pick the sub-family by what the element *is*.*

The three hover/pressed sub-families are not interchangeable. Each has a
distinct, consistent meaning in real usage:

| The element is… | Default | Hover | Pressed | Real consumers |
| --- | --- | --- | --- | --- |
| A **container or row** that reacts to pointer | `surface.default.default` | `surface.default.hover` | `surface.default.pressed` | accordion, cellContent, topBar, tabs |
| An **interactive control** with a fill | `surface.default.default` | `surface.interactive.hover` | `surface.interactive.pressed` | chip, actionMenu, buttonGroup, selectableList, slider |
| A **ghost control** — no fill, still needs feedback | `surface.transparent.default` | `surface.transparent.hover` | `surface.transparent.pressed` | button (tertiary), pagination, toggleButton |

Then:

| State / context | Token |
| --- | --- |
| Selected | `surface.interactive.selected.default` · `.hover` · `.pressed` |
| Disabled | `surface.disabled` |
| A subtle raised or inset panel | `surface.light.default` |
| A dark panel or inverted region | `surface.default.inverted.default` |
| Sitting on a brand-primary fill | `surface.onPrimary.*` |
| Sitting on a secondary fill | `surface.onSecondary.*` |
| Must ignore brand and mode entirely | `surface.constant.{black,white}.*` |
| Status fill | see [**Status is messaging**](#status-is-messaging) — the tint/Strong distinction matters |

**Selected states use `Interactive/Selected/*`.** Do not use `Surface/Active/*` —
see [Restricted](#restricted).

---

## Border by owner

*Border: pick by what the stroke belongs to.*

| The stroke is on… | Token |
| --- | --- |
| A **form control** — input, checkbox, radio, toggle, select | `border.subdued.default` |
| A **structural container** — card, modal, accordion, top bar, divider | `border.light.default` |
| A **high-contrast outlined control** — outlined button, badge | `border.default.default` |
| Something on a dark/inverted background | `border.defaultInverted.default` |

State, on any of the above:

| State | Token |
| --- | --- |
| Hover | `border.interactive.hover` |
| Pressed | `border.interactive.pressed` |
| Selected / active | `border.interactive.default` |
| Disabled | `border.disabled` |
| Error (and its hover/pressed) | `border.status.error.default` · `.hover` · `.pressed` |
| A faint edge on a floating light surface | `border.transparent.default` (10% opaque) |

**`Border/Default` has no hover or pressed leaf.** It ships `Default` only, in
every brand and mode. `border.interactive.hover` is the system's only hover
stroke and is the correct choice — this is not a workaround.

**`Border/Transparent` is a faint edge, not an invisible one** — it is 10%
opaque (`#3232321a`). For a genuinely invisible border the system has only
`surface.transparent.default` (alpha `00`), which is why `button`, `badge` and
`chip` bind it for box-model parity. That is a documented exception, not a
pattern to copy: you should not be hand-building a control that needs it.

**Keyboard focus rings are not a token.** Use the platform default:

```tsx
outlineColor={['Highlight', '-webkit-focus-ring-color']}
```

This is deliberate — it honours the user's OS and browser settings. Do not
substitute `Border/Focus`.

---

## Content covers text and icons

*Content covers text *and* icons.*

| Element | Token |
| --- | --- |
| Body and heading text | `content.default.default` |
| Secondary text, placeholders, optional markers | `content.light.default` |
| Muted supporting text | `content.subdued.default` |
| Disabled text | `content.disabled` |
| Text on a dark, inverted, or filled surface | `content.default.inverted.default` |
| Links and interactive text | `content.interactive.default` · `.hover` · `.pressed` |
| Text on a brand-primary fill | `content.onPrimary.*` |
| Status text | `content.status.<status>.default` — see [**Status is messaging**](#status-is-messaging) |

**Icons take Content tokens.** `Icon` renders with `fill: currentcolor` and a
`color` prop, so an icon is painted by whatever Content token it inherits or is
given. Match the icon to its adjacent text: `content.light.default` for a field
affordance, `content.default.default` for a standalone icon.

---

## Status is messaging

*Status colour belongs to messaging, and only error is interactive.*

Two tiers. Do not mix them.

**Tier 1 — all four statuses** (error, information, success, warning). Only in
messaging and display components, and always via the component:

| Need | Component | Tokens it binds |
| --- | --- | --- |
| A message block | `<FeedbackMessage>` | `surface.status.<s>.default` background + `content.status.<s>.default` icon |
| A message under a field | `<StateMessage>` | `content.status.<s>.default` |
| A status label or pill | `<StatusTag>`, `<Tag>` | `surface.status.<s>.default` + `content.status.<s>.default` |

**Tier 2 — error only.** Every other status use in the system is error:

| Need | Tokens |
| --- | --- |
| A form control in an error state | `border.status.error.default` · `.hover` · `.pressed` |
| A selected control in an error state | `surface.status.errorStrong.*` |
| A destructive action | `<Button variant="danger">`, `<TextButton variant="danger">` |

**Never put information, success, or warning on an interactive element.** No
component does, and the tokens for it do not exist —
`surface.status.{information,success,warning}Strong.hover` and `.pressed` are all
unused, by design.

**Never invert status text.** `content.status.*.inverted.default` has no
consumer.

**`<status>.default` vs `<status>Strong.default`:**

| | Example (error, light) | Use for |
| --- | --- | --- |
| `surface.status.error.default` | `#fbeeee` — pale tint | A message background behind dark text |
| `surface.status.errorStrong.default` | `#b32730` — saturated | A filled element carrying a white glyph or label |

Picking the tint for a filled element gives 1.13:1 against white. Picking Strong
for a message background makes the text unreadable.

---

## Never pick by light mode

*Never pick a token by its light-mode colour.*

**21 groups of tokens are identical in light mode and different in dark.** Ten of
those groups contain multiple live tokens. Choosing by appearance — "I need
white here" — picks the right pixel in light mode and the wrong one in dark.

Ten live tokens resolve to `#ffffff` in light mode alone, splitting into five
different dark values:

| If you need white for… | Use | Dark |
| --- | --- | --- |
| Text or an icon on a dark/inverted surface | `content.default.inverted.default` | `#15171e` — flips with the mode |
| A default component fill | `surface.default.default` | `#292d3b` |
| Text on a brand-primary fill | `content.onPrimary.default` | `#f8f8fa` |
| White that must stay white in both modes | `content.constant.white.default` | `#ffffff` |
| The page canvas | `background.default` | `#15171e` |

The same trap exists for `#323232` (9 live tokens), `#e0e0e0` (8), `#000000` (5),
`#eeeeee` (5), `#4b4b4b` (4), `#959595` (3), `#c7c7c7` (3), `#ffffff99` (3) and
`#ffffff33` (2).

**Choose by role, never by colour.** "Text on an inverted surface" has exactly
one right answer; "white" has ten wrong ones.

**`Constant/*` means *ignores the mode*.** Use it only when the colour must not
flip in dark mode — a logo lockup, a fixed scrim. Text on an inverted surface is
**not** that case: it needs `Inverted/*`, which flips. Binding `Constant/White`
there gives 1.26:1 in dark mode.

**The whole trap in one line: a mode-fixed token sharing a light value with a
mode-flipping one.** `Constant/*` and `Symbol/*` hold their value across modes;
everything else flips. Six of the ten dangerous collision groups contain one of
those two families. Measured failures:

| Correct | Wrong but identical in light | Dark |
| --- | --- | --- |
| `content.default.inverted.default` | `content.constant.white.default` | 14.23:1 → **1.26:1** |
| `content.active.default` | `content.constant.black.default` | 16.88:1 → **1.31:1** |
| `surface.active.hover` | `symbol.brand.primary.subdued` | 16.2:1 → **1.45:1** |

Not every collision is dangerous. `surface.dark.default` shares `#959595` with
`content.disabled` and `border.subdued.default`, but all three flip, so a wrong
pick degrades (5.14:1 → 3.83:1) rather than breaks. **The severity comes from
mode-fixed families, not from the collision itself.**

---

## Never borrow a state token

*Never borrow a state token for its colour.*

**A `hover`, `pressed`, `selected` or `disabled` leaf may only be used for that
state.** If an element has no pressed state, it must not bind a `.pressed`
token — however well the value happens to fit.

Borrowing hides the fact that a token is missing, and couples unrelated things:
change `Surface/Light/Pressed` for a real pressed interaction and every element
that borrowed it changes too.

Known offenders, all confirmed wrong and slated for fixing — never copy them:

| Element | Wrongly binds |
| --- | --- |
| `skeleton` shimmer fill | `surface.light.pressed` |
| `skeleton` shimmer gradient | `background.subdued` |
| `progressBar` / `progressCircle` on-dark fill | `surface.active.pressed` |

If nothing in the palette fits a static element, that is a **missing token to
raise**, not a neighbouring state to borrow.

---

## Never use

The agent must never emit these.

| Token / family | Count | Why |
| --- | --- | --- |
| `Symbol/*` — brand, disabled, skinColors | 22 | A design-authoring palette. Icons paint via `currentcolor` from Content; illustrations ship as pre-rendered `.webp` raster. No web runtime consumes it. |
| `Border/Focus` | 1 | Focus rings use platform system colours (**Border by owner**). |
| `Native/*` | — | iOS/Android only. |
| `Surface/Decorative/*` | 2 | One live binding (`rating`), a documented exception with no general rule. For a rating display use `<Rating>`. |
| Status leaves unreachable under **Status is messaging** | 13 | `…Strong.{hover,pressed}` for information/success/warning, `border.status.{information,success,warning}.default`, `content.status.*.inverted.default`. Only error is interactive; status is never inverted. |
| Everything else with no consumer | 28 | No component uses it and no rule explains it — there is no precedent for what it means. |

**73 of the 218 tokens have no consumer**: 22 `Symbol/*`, 13
status leaves, 1 `Border/Focus`, 9 unused `Scales/*` leaves, and 28 others — `surface.active.default`,
`border.active.pressed`, `content.active.pressed`,
`surface.brand.secondary.default`, `surface.decorative.red.default`,
`surface.light.hover`, `border.accent.light.default`,
`content.constant.white.onDark.default`, `background.light`, the `score` families, the
`surface.constant.*` interaction states, and `background.constant.{black,white}`.

**This figure was 83 and was wrong.** The audit counted all 19 `Scales/*` tokens
as having no consumer. Ten of them are bound by `EnergyScale.tsx` in the web
design-system repo — checked 10 September 2026. The nine genuinely unused are
`Scales/Energy/Blue100`, `Scales/Energy/Red300` and the seven `Scales/CO2/*`.
Corrected everywhere on 10 September 2026.

---

## Restricted

Allowed only as described.

### Energy and CO2 scales

`Scales/Energy/*` and `Scales/CO2/*` are the **only** correct colours for
energy-performance and CO₂ data. Never substitute a `Surface/*`, `Content/*` or
status colour. A grey or neutral energy ladder is wrong output, not a safe
fallback — the colour carries the meaning, and on a French listing it is
regulated information.

**France only.** Other country scales exist on the token page and are legacy.

#### Energy class colours — France

*Match the token to the DPE class in the listing data. Never estimate a class,
and never pick by appearance.*

| DPE class | Token |
| --- | --- |
| A | `Scales/Energy/Green100` |
| B | `Scales/Energy/Green200` |
| C | `Scales/Energy/Green400` |
| D | `Scales/Energy/Yellow100` |
| E | `Scales/Energy/Orange100` |
| F | `Scales/Energy/Red100` |
| G | `Scales/Energy/Red200` |

**The French scale runs green to red across all seven classes.** `Green300`,
`Yellow200`, `Orange200`, `Red300` and `Blue100` are **not part of it** — do not
reach for them to fill a gap, and do not assume the classes walk the palette in
order. They do not.

A French ladder that ends yellow or orange at G is wrong. G is the worst rating
and must read red.

**Text on a selected segment**, as the energy filter slider does it: white on
**A** and **G** only; the default content colour on B through F. Those two fills
are the darkest in the scale.

#### CO2 scale

Sequential blue palette, for CO₂ emission data only.

| Step | Token |
| --- | --- |
| Lowest emission | `Scales/CO2/Blue100` |
| Intermediate | `Scales/CO2/Blue200`–`Blue600`, assigned in order |
| Highest emission | `Scales/CO2/Blue700` |

**Never reverse the scale.** Never use CO₂ blues for an energy class, or energy
colours for CO₂.

#### Where these rules come from

| | |
| --- | --- |
| Energy class mapping | **Verified against web source code** — `libraries/patterns/energyclassslider/src/EnergyScale.tsx`, 10 September 2026 |
| CO₂ ordering | **Not verified against code.** Nothing in the web codebase consumes `Scales/CO2/*`; the rule comes from the token page |
| Both | **Never checked against Figma.** `Energy Tag` carries 48 Figma variants that have not been read. If they assign classes differently, that is a finding to raise — not a difference to resolve on your own |

### `Surface/Dark`

A neutral fill that must stay distinguishable from a white or light foreground.
Brand-invariant (`#959595` light, `#979eb5` dark). White on it gives exactly
**3.0:1**, the WCAG 1.4.11 non-text floor; `Surface/Subdued` would give 1.16:1
and fail.

Use for: an unselected control track, an active indicator dot, a scrim over a
thumbnail. Real consumers: `toggle`, `buttonGroup`, `carousel`, `mediaUpload`.

Do **not** use it as a general dark background — that is
`surface.default.inverted.default`.

### `Active/*` — `surface`, `border`, `content`

Legacy. The family is a fast-iteration artifact and is, in practice, the `tabs`
family; three of its seven leaves have no consumer at all. The system expresses
the same idea through `Interactive/Selected/*`.

Use `interactive.selected.*` for selected and active states. Do not introduce
`Active/*` into new work.

### Selected **and** disabled together

Choose the foreground against the *selected* fill, not the disabled fill.
`content.disabled` on a selected-disabled surface resolves to **1.0:1 —
invisible**. `buttonGroup` uses `content.light.default` here for exactly this
reason.

---

## Do not copy these patterns

Real bindings in the current codebase that are known-wrong. If generated output
resembles them, it is wrong even though shipped code does it.

| Pattern | Where | Correct form |
| --- | --- | --- |
| A border bound to `surface.transparent.default` or to its own fill | `button` (20), `badge` (4), `chip` (3) | **Not a defect** — a deliberate box-model-parity idiom. Never reproduce it by hand; use the component. |
| A circle fill taken from `content.status.*` | `wizard` (3) | `surface.status.<s>Strong.default` — identical value, correct family |
| An icon painted with `surface.decorative.yellow.default` | `rating` | **Exception, not a defect** — but never reproduce it. Use `<Rating>`. |
| A selected border bound to `border.default.default` | `toggleButton` | `border.interactive.default` |
| A pressed-state token used as a static fill | `skeleton`, `progressBar`, `progressCircle` | A default-state token |

`DateCalendar`, `SegmentedControl` and `CoachMark` colour themselves directly in
`.tsx`, bypassing the component-token layer, because they were never given one.
Their source is not a model to copy.

`Surface/Constant/*` and `Content/Constant/*` are used **only in their `.default`
form**, by `button`, `badge`, `tag`, `imageSlider` and `mediaUpload`. Every
hover, pressed and disabled leaf of the constant family is unused — do not
invent interaction states for a constant colour.

---

## Brand and mode

- **6 brands** — SL, SLN, LI, LIN, MA, BD — × light and dark. All 12
  combinations define the **same 218 token keys**, so a token that exists is
  safe to use in every brand and mode.
- An `AVIV` token set also ships in the source tree. **It is not a live brand —
  ignore it.** Never generate for it or count it as a brand.
- Only **21 tokens vary by brand in light mode, 23 in dark** — concentrated in
  `Surface/Brand`, a few accent/active states, and the `On-Primary` families.
- Never hardcode a brand's resolved value, and never branch on brand. Bind the
  token and let the theme resolve it.
- Both modes are always live. Never assume a light background: text on a custom
  surface must use a Content token, never a literal dark colour.

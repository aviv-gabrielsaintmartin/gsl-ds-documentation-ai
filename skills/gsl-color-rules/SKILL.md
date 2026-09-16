---
name: gsl-color-rules
description: Use when designing or editing any screen in Figma that must follow the GSL (Gemini) design system. Covers colour only — which variable to bind for page backgrounds, component surfaces, borders, text and icons, status messaging, and the regulated energy and CO2 scales. Apply it before choosing any colour. Never pick a colour by how it looks.
---

# GSL colour rules

**These rules decide every colour in a GSL screen.** They come from real
bindings in the design system's own code, not from token names.

## How these rules read in Figma

**The rules below write a token in dot notation, the way the code does.** In
Figma the same token is a variable, written with slashes and capitals.

| Written here | The Figma variable |
| --- | --- |
| `surface.default.default` | `Surface/Default/Default` |
| `content.status.error.default` | `Content/Status/Error/Default` |
| `Scales/Energy/Green100` | `Scales/Energy/Green100` — already in Figma form |

Four rules about applying them:

- **Bind a variable. Never type a hex value**, and never use the colour picker
  to match something by eye.
- **Reach for a library component before you colour anything.** An instance is
  already correct in every brand and both modes.
- **Never detach an instance to change its colour.** If the component cannot do
  what you need, say so in your output rather than working around it.
- **If nothing in this page fits what you are painting, say so.** A missing
  token is something to raise. It is not a licence to pick a near one.

---

## Components first

**Do not choose colours. Choose components.**

Colour in this system is decided by a component layer, not by the person drawing
the screen. A button from the library is already correct in every brand, both
modes, and all five interaction states. A frame styled to look like a button is
correct in none of them.

**So reach for a component first, every time.** Only colour something yourself
when no component covers it — a custom layout surface, a one-off container, a
page background.

Everything below applies **only** to that remainder.

---

## No raw colour

**Never write a raw colour.** No hex, no picked value, no opacity-shifted
variant of a token. Every colour comes from a variable. There are no exceptions.

---

## Pick the family

**Pick the family by what you are painting.**

| Painting | Family |
| --- | --- |
| The page or screen canvas behind everything | `Background/*` |
| A component or container fill | `Surface/*` |
| A stroke or outline | `Border/*` |
| Text **and icons** | `Content/*` |
| Energy or CO2 data | `Scales/Energy/*` · `Scales/CO2/*` — see **Energy and CO2 scales** |
| Error, information, success, warning | see **Status is messaging** |

`Symbol/*` and `Native/*` are never used — see **Never use**.

---

## Surface sub-family

**Pick the sub-family by what the element *is*.** The three hover and pressed
sub-families are not interchangeable.

| The element is… | Default | Hover | Pressed |
| --- | --- | --- | --- |
| A **container or row** that reacts to pointer | `surface.default.default` | `surface.default.hover` | `surface.default.pressed` |
| An **interactive control** with a fill | `surface.default.default` | `surface.interactive.hover` | `surface.interactive.pressed` |
| A **ghost control** — no fill, still needs feedback | `surface.transparent.default` | `surface.transparent.hover` | `surface.transparent.pressed` |

Then:

| State or context | Token |
| --- | --- |
| Selected | `surface.interactive.selected.default` · `.hover` · `.pressed` |
| Disabled | `surface.disabled` |
| A subtle raised or inset panel | `surface.light.default` |
| A dark panel or inverted region | `surface.default.inverted.default` |
| Sitting on a brand-primary fill | `surface.onPrimary.*` |
| Sitting on a secondary fill | `surface.onSecondary.*` |
| Must ignore brand and mode entirely | `surface.constant.{black,white}.*` |
| Status fill | see **Status is messaging** |

**Selected states use `Interactive/Selected/*`.** Never `Surface/Active/*` — see
**Restricted**.

---

## Border by owner

**Pick the border by what the stroke belongs to.**

| The stroke is on… | Token |
| --- | --- |
| A **form control** — input, checkbox, radio, toggle, select | `border.subdued.default` |
| A **structural container** — card, modal, accordion, top bar, divider | `border.light.default` |
| A **high-contrast outlined control** — outlined button, badge | `border.default.default` |
| Something on a dark or inverted background | `border.defaultInverted.default` |

State, on any of the above:

| State | Token |
| --- | --- |
| Hover | `border.interactive.hover` |
| Pressed | `border.interactive.pressed` |
| Selected or active | `border.interactive.default` |
| Disabled | `border.disabled` |
| Error, and its hover and pressed | `border.status.error.default` · `.hover` · `.pressed` |
| A faint edge on a floating light surface | `border.transparent.default` — 10% opaque |

**`Border/Default` has no hover or pressed value.** It ships `Default` only.
`border.interactive.hover` is the system's only hover stroke and is the correct
choice. This is not a workaround.

**`Border/Transparent` is a faint edge, not an invisible one** — it is 10%
opaque. For a genuinely invisible border the system has only
`surface.transparent.default`.

**Do not draw a keyboard focus ring.** Focus is a platform behaviour, not a
design decision, and `Border/Focus` is never used.

---

## Content covers text and icons

| Element | Token |
| --- | --- |
| Body and heading text | `content.default.default` |
| Secondary text, placeholders, optional markers | `content.light.default` |
| Muted supporting text | `content.subdued.default` |
| Disabled text | `content.disabled` |
| Text on a dark, inverted or filled surface | `content.default.inverted.default` |
| Links and interactive text | `content.interactive.default` · `.hover` · `.pressed` |
| Text on a brand-primary fill | `content.onPrimary.*` |
| Status text | `content.status.<status>.default` — see **Status is messaging** |

**Icons take Content tokens, not Surface ones.** Match an icon to the text
beside it: `content.light.default` for a field affordance,
`content.default.default` for a standalone icon.

---

## Status is messaging

**Status colour belongs to messaging, and only error is interactive.** Two
tiers. Do not mix them.

**Tier one — all four statuses**, error, information, success and warning. Only
in messaging and display components, and always through the component:

| Need | Component | What it binds |
| --- | --- | --- |
| A message block | Feedback Message | `surface.status.<s>.default` fill + `content.status.<s>.default` icon |
| A message under a field | State Message | `content.status.<s>.default` |
| A status label or pill | Status Tag, Tag | `surface.status.<s>.default` + `content.status.<s>.default` |

**Tier two — error only.** Every other status use in the system is error:

| Need | Tokens |
| --- | --- |
| A form control in an error state | `border.status.error.default` · `.hover` · `.pressed` |
| A selected control in an error state | `surface.status.errorStrong.*` |
| A destructive action | The Button or Text Button danger variant |

**Never put information, success or warning on an interactive element.** No
component does, and the tokens for it do not exist.

**Never invert status text.** `content.status.*.inverted.default` is never used.

**The tint against the strong value:**

| | Example — error, light mode | Use for |
| --- | --- | --- |
| `surface.status.error.default` | pale tint | A message background behind dark text |
| `surface.status.errorStrong.default` | saturated | A filled element carrying a white glyph or label |

Picking the tint for a filled element gives 1.13:1 against white. Picking the
strong value for a message background makes the text unreadable.

---

## Never pick by light mode

**Never pick a token by its light-mode colour.**

**21 groups of tokens are identical in light mode and different in dark.**
Choosing by appearance — "I need white here" — picks the right pixel in light
mode and the wrong one in dark.

Ten live tokens look white in light mode alone, and split into five different
dark values:

| If you need white for… | Use | What it becomes in dark |
| --- | --- | --- |
| Text or an icon on a dark or inverted surface | `content.default.inverted.default` | Dark — it flips with the mode |
| A default component fill | `surface.default.default` | Dark grey |
| Text on a brand-primary fill | `content.onPrimary.default` | Near-white |
| White that must stay white in both modes | `content.constant.white.default` | Still white |
| The page canvas | `background.default` | Dark |

The same trap exists for nine other shared values, including the system's dark
grey, its mid greys and its blacks.

**Choose by role, never by colour.** "Text on an inverted surface" has exactly
one right answer. "White" has ten wrong ones.

**`Constant/*` means it ignores the mode.** Use it only when a colour must not
flip in dark mode — a logo lockup, a fixed scrim. Text on an inverted surface is
**not** that case: it needs `Inverted/*`, which flips. Using `Constant/White`
there gives 1.26:1 in dark mode.

Three measured failures, all invisible in light mode:

| Correct | Wrong, but identical in light | Contrast in dark |
| --- | --- | --- |
| `content.default.inverted.default` | `content.constant.white.default` | 14.23:1 → **1.26:1** |
| `content.active.default` | `content.constant.black.default` | 16.88:1 → **1.31:1** |
| `surface.active.hover` | `symbol.brand.primary.subdued` | 16.2:1 → **1.45:1** |

---

## Never borrow a state token

**A hover, pressed, selected or disabled token may only be used for that state.**
If an element has no pressed state, it must not use a pressed token — however
well the value happens to fit.

Borrowing hides the fact that a token is missing. If nothing fits a static
element, that is a **missing token to raise**, not a neighbouring state to
borrow.

---

## Never use

**Never bind any of these.**

| Token or family | Why |
| --- | --- |
| `Symbol/*` — brand, disabled, skin colours | A design-authoring palette. Nothing in the product consumes it |
| `Border/Focus` | Focus rings are a platform behaviour |
| `Native/*` | iOS and Android only |
| `Surface/Decorative/*` | One documented exception. For a rating display use the Rating component |
| Status values unreachable under **Status is messaging** | Only error is interactive, and status is never inverted |
| Anything else with no consumer | No component uses it and no rule explains it, so there is no precedent for what it means |

**73 of the 218 colour tokens have no consumer at all.** If a token is not named
somewhere on this page, treat that as a reason to stop and ask, not as a free
choice.

---

## Restricted

Allowed only as described here.

### Energy and CO2 scales

`Scales/Energy/*` and `Scales/CO2/*` are the **only** correct colours for energy
performance and CO2 data. Never substitute a `Surface/*`, `Content/*` or status
colour.

**A grey or neutral energy ladder is wrong output, not a safe fallback.** The
colour carries the meaning, and on a French listing it is regulated information.

**France only.** Other country scales exist and are legacy.

#### Energy class colours, France

**Match the token to the DPE class in the listing data. Never estimate a class,
and never pick by appearance.**

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

**Text on a selected segment:** white on **A** and **G** only, the default
content colour on B through F. Those two fills are the darkest in the scale.

#### CO2 scale

A sequential blue palette, for CO2 emission data only.

| Step | Token |
| --- | --- |
| Lowest emission | `Scales/CO2/Blue100` |
| Intermediate | `Scales/CO2/Blue200` to `Blue600`, assigned in order |
| Highest emission | `Scales/CO2/Blue700` |

**Never reverse the scale.** Never use CO2 blues for an energy class, or energy
colours for CO2.

**The letter or label colour on a CO2 step.** The CO2 scale does **not** flip
with theme. Text sitting on it must therefore use a theme-stable content token.
Never `Content/Default/Default` and never `Content/Default/Inverted` — both flip
against a fill that does not, and invert the contrast.

| Step | Token |
| --- | --- |
| `Blue100` · `Blue200` · `Blue300` | `Content/Constant/Black` |
| `Blue400` · `Blue500` · `Blue600` · `Blue700` | `Content/Constant/White` |

`Blue300` is the fragile step: it clears the 4.5:1 floor by 0.08 in light and
0.06 in dark.

**Where these rules come from, so you know how far to trust them:** the energy
class mapping is verified against the design system's own code. The CO2 ordering
comes from the token documentation and is not verified against code. The CO2
letter colour is computed from the token values, not observed anywhere.
**Neither scale has been checked against the Figma library.** If the Figma
components assign classes differently, that is a finding to raise — not a
difference to resolve on your own.

### `Surface/Dark`

A neutral fill that must stay distinguishable from a white or light foreground.
White on it gives exactly 3.0:1, the non-text contrast floor.

Use for an unselected control track, an active indicator dot, or a scrim over a
thumbnail. **Do not use it as a general dark background** — that is
`surface.default.inverted.default`.

### `Active/*` — surface, border and content

Legacy. The system expresses the same idea through `Interactive/Selected/*`.

Use `interactive.selected.*` for selected and active states. **Never introduce
`Active/*` into new work.**

### Selected and disabled together

Choose the foreground against the **selected** fill, not the disabled fill.
`content.disabled` on a selected-disabled surface resolves to **1.0:1, which is
invisible.** Use `content.light.default` here.

---

## Brand and mode

- **Six brands** — SL, SLN, LI, LIN, MA, BD — each in light and dark. All twelve
  combinations define the **same 218 token keys**, so a token that exists is safe
  to use in every brand and mode.
- An `AVIV` token set also exists. **It is not a live brand. Ignore it.**
- Only about twenty tokens vary by brand, concentrated in `Surface/Brand`, a few
  accent and active states, and the on-primary families.
- **Never hardcode a brand's resolved value, and never branch on brand.** Bind
  the variable and let the theme resolve it.
- **Both modes are always live.** Never assume a light background: text on a
  custom surface must use a Content token, never a literal dark colour.

---

## What to do when you are stuck

**Say so in your output.** Name what you were painting, say that no rule on this
page covers it, and stop.

An invented colour is worse than an unfinished screen, because nothing flags it
later.

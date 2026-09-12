# Spacing rules for AI generation

_The authoritative ruleset for spacing and sizing when generating a GSL
interface. Every rule is derived from real bindings and mechanically verified
where possible. Evidence is in `spacing-usage-audit.md`, which a generating
agent must not read. Values:
[spacing-tokens.md](spacing-tokens.md) · [sizing-tokens.md](../sizing/sizing-tokens.md).
Colour: [color-rules-ai.md](../color/color-rules-ai.md).
Type: [typography-rules-ai.md](../typography/typography-rules-ai.md)._

---

## Components first

*Use a component; it carries its own spacing.*

_**This rule precedes every other rule on this page.** The colour and typography rulesets open with the same rule, under the same name — it is one rule stated where each ruleset needs it._

A `<Card>`, `<Modal>` or `<CellContent>` already has correct internal padding in
every viewport. Reach for the component first. Everything below applies to the
layout *between* components, and to custom containers.

**Never override a component's internal padding via CSS.**

---

## No pixel literals

*Never write a pixel literal.*

No `gap: 10px`, `margin: 15px`, `width: 200px`. Every spacing value resolves to
a `Spacing/*` token; every fixed dimension to a `Sizing/*` token.

---

## Spacing vs sizing

*Spacing is distance. Sizing is dimension.*

| Property | Family |
| --- | --- |
| `padding`, `gap`, `margin`, offsets | `Spacing/*` |
| `width`, `height`, `min-width`, `max-width` | `Sizing/*` |

They are not interchangeable. `Sizing` is not a rhythm scale — it is a catalogue
of concrete dimensions (`142` and `294` sit alongside `144` and `288`), so never
interpolate a "next step up" from it.

---

## Component spacing stops at 32

*Component spacing stops at 32.*

**Verified: 0 violations across all 60 component token files.**

| Range | Use for |
| --- | --- |
| `Spacing/None` – `Spacing/32` | anything inside a component or card |
| `Spacing/48`, `56`, `64`, `80`, `128`, `256` | **page rhythm only** — section separation, hero space, viewport margins |

**Never put a page-rhythm token inside a component or card.** No component in
the system does, and that is the single most reliably-followed rule in the
spacing docs.

`Spacing/40` is the boundary: documented for page-level separation, so treat it
as page-level.

---

## Containment

*A gap never exceeds its container’s padding.*

**Verified: 0 violations across the 24 components that have both.**

If a card pads at `Spacing/16`, the gaps between its children must be `16` or
less. Breaking this makes children look like they belong to the page rather than
the card — it is the most common way generated layouts read as "off" without an
obvious cause.

---

## Start from real usage

*Start from what components actually use.*

| Token | px | Components |
| --- | --- | --- |
| `Spacing/None` | 0 | 3 |
| `Spacing/2` | 2 | 5 |
| `Spacing/4` | 4 | 23 |
| `Spacing/6` | 6 | 4 |
| `Spacing/8` | 8 | 36 |
| `Spacing/12` | 12 | 14 |
| `Spacing/16` | 16 | 27 |
| `Spacing/20` | 20 | 1 |
| `Spacing/24` | 24 | 4 |
| `Spacing/32` | 32 | 9 |

`Spacing/8`, `Spacing/16` and `Spacing/4` cover most component spacing. Reach
for `Spacing/20` only with a reason — one component uses it.

---

## Container padding

*Standard container padding.*

| Container | Mobile (XS–SM) | Desktop (MD–XXXL) |
| --- | --- | --- |
| Listing / product card | `Spacing/16` | `Spacing/24` |
| Dropdown / popover | `Spacing/12` | `Spacing/16` |
| Modal / dialog body | `Spacing/16` | `Spacing/24`–`32` |
| Embedded filter box | `Spacing/16` | `Spacing/16` |

## Page rhythm

*Page rhythm by viewport.*

| Tier | Outer margin | Section gap | Card grid gap | Form field gap |
| --- | --- | --- | --- | --- |
| XS / Mobile | `Spacing/16` | `Spacing/48` | `Spacing/16` | `Spacing/16` |
| SM / Tablet portrait | `Spacing/32` | `Spacing/48` | `Spacing/16` | `Spacing/16` |
| MD–LG / Tablet landscape | `Spacing/32` | `Spacing/48` | `Spacing/24` | `Spacing/16` |
| XL–XXXL / Desktop | `Spacing/80` | `Spacing/64` | `Spacing/24` | `Spacing/16` |

Outer margin and grid gutter must match the [grid tokens](../grid/grid-tokens.md)
`Margin`/`Gutter` for the same tier.

> **Container padding and Page rhythm are unverified.** They describe
> product-page composition, which lives outside the component library and could
> not be checked. Follow them as the documented intent — but unlike **Component
> spacing stops at 32** and **Containment**, each of which was checked against
> every component that could break it, nothing has confirmed these two.

---

## Do not use

| Token | Why |
| --- | --- |
| `Spacing/56` | No documented purpose anywhere — not in any usage note, layer, or rhythm table, and no consumer. |
| `Sizing/14`, `36`, `142`, `204`, `288`, `294` | No component consumer, and no page-level explanation available for a dimension scale. |

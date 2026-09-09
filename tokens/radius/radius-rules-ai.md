# Radius rules for AI generation

_The authoritative ruleset for corner radius when generating a GSL interface.
Every rule is derived from real bindings and live spot-checks. Evidence:
[radius-usage-audit.md](radius-usage-audit.md). Values:
[radius-tokens.md](radius-tokens.md).
Spacing: [spacing-rules-ai.md](../spacing/spacing-rules-ai.md).
Shadow: [shadow-rules-ai.md](../shadow/shadow-rules-ai.md).
Border: [border-width-rules-ai.md](../border-width/border-width-rules-ai.md)._

---

## Components first

*Use a component; it carries its own radius.*

_**This rule precedes every other rule on this page.** The colour, typography and
spacing rulesets open with the same rule, under the same name — it is one rule
stated where each ruleset needs it._

A `<Card>`, `<Button>` or `<TextField>` already has the correct corner radius.
Reach for the component first. Everything below applies to custom containers, and
to choosing between a component's own radius variants.

**Never override a component's radius**, with one exception: `Card` exposes it as
a variant — see **Card chooses by variant**.

---

## No pixel literals

*Never write a corner-radius literal.*

Every corner radius resolves to one of the five `Radius/*` tokens. No
`border-radius: 6px`, no `12`, no value invented between tiers. The five tokens
are the complete set — there is no sixth value and nothing to interpolate.

---

## Shape before size

*What kind of thing it is decides the tier, before how big it is.*

This is the rule an agent gets wrong. Radius is **not** a size ladder.

| Shape category | Tier | Why |
| --- | --- | --- |
| **Filled or interactive control** — Button, Tag, Chip | `Radius/Rounded` | Always a full capsule, **at every size**. A small Button is not `Radius/4` |
| **Rectangular container** — Card, Text Field, Accordion, Snackbar | tier by size, see below | These are the only things that scale with size |

`Text Button` is the case that proves it: it is small, and it is `Radius/8` —
because it is rectangular, not because of its size. `Button` at the same size is
`Radius/Rounded`.

**Decide the shape category first. Only then, if it is a rectangular container,
pick the tier by size.**

---

## The five tiers

*What each token is for.*

| Token | Value | Use for |
| --- | --- | --- |
| `Radius/None` | 0 | Square corners — flush and full-bleed surfaces, edge-docked elements. The borderless "floating banner" variant of Feedback message |
| `Radius/4` | 4 | Small rectangular surfaces — compact cards, and the fixed corner radius on chart bars |
| `Radius/8` | 8 | Mid-size rectangular containers and controls — standard cards, Text Field, Snackbar, Text Button |
| `Radius/16` | 16 | Larger containers — large cards, Accordion, Coach mark |
| `Radius/Rounded` | 10000 | Fully rounded — every filled or interactive control, at any size. Icon-only Button becomes a full circle |

All five are in real use. None is orphaned.

---

## Card chooses by variant

*Do not set a radius on a Card — pick the variant.*

`Card` exposes radius as a component variant: `Radius=4`, `Radius=8`,
`Radius=16`. Confirmed directly in Figma, not inferred.

Select the variant. Never apply a radius on top of a `Card` instance. The
size-to-radius mapping lives in [Card](../../components/card/card.md#radius).

---

## Rounded is a clamp, not a measurement

*`Radius/Rounded` is 10000 and is meant to be.*

It is a clamp value, not a literal corner radius. It resolves to a full capsule
whatever the element's height, which is why one token covers Button, Tag, Chip
and a circular icon button alike.

In Figma, pill components bind their own component-level value (`96`–`100`)
rather than referencing `Radius/Rounded` literally. Both clamp to the same
visual capsule. **This is expected, not a discrepancy** — do not "fix" it.

---

## Figma applies radius as a number

*Corner radius is not a bound variable in Figma. Set the value.*

Unlike colour and typography, radius is applied as a plain number on the node in
every case checked — across the component library and across three real product
screens. There is no variable to bind.

**A generating agent must set the numeric value** from the table above, and
**must not** report this as an unbound-token violation. It is how the system is
built, not a defect.

Figma also contains an unimplemented, undocumented intermediate layer of
per-component variables (`Corner radius/Accordion` and similar). **Ignore it.**
It is not built in code, and nothing should be generated against it.

---

## Do not use

| What | Why |
| --- | --- |
| Any value not in the five-token table | There is no sixth tier. Nothing may be interpolated between tiers |
| `Corner radius/*` per-component variables | An unbuilt Figma layer. Not in code, not documented, not to be generated against |

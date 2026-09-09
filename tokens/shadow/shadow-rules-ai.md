# Shadow rules for AI generation

_The authoritative ruleset for elevation when generating a GSL interface. Every
rule is derived from real code bindings and live spot-checks. Evidence:
[shadow-usage-audit.md](shadow-usage-audit.md). Values:
[shadow-tokens.md](shadow-tokens.md).
Radius: [radius-rules-ai.md](../radius/radius-rules-ai.md).
Border: [border-width-rules-ai.md](../border-width/border-width-rules-ai.md)._

---

## Components first

*Use a component; it carries its own elevation.*

_**This rule precedes every other rule on this page.** The colour, typography and
spacing rulesets open with the same rule, under the same name._

A `<Modal>`, `<Snackbar>` or `<ActionMenu>` already carries the right shadow.
Reach for the component first. Everything below applies to custom containers.

**Never add a shadow to a component instance.**

---

## Flat by default

*If it does not float above the page, it has no shadow.*

This is the rule an agent gets wrong in both directions — inventing elevation for
a card, or applying none at all because nothing told it to.

**The default is `none`.** A surface earns a shadow only by floating *above* the
page: overlaying other content, or detached from the flow. Being visually
set apart is not floating.

| Surface | Shadow | How it is set apart instead |
| --- | --- | --- |
| Listing / product card | **`none`** | A border — see [border-width-rules-ai.md](../border-width/border-width-rules-ai.md) |
| Sticky bottom call-to-action bar | **`none`** | A border |
| Full-screen Modal | **`none`** | Nothing is behind it to separate from |
| Button in its normal on-page style | **`none`** | — |
| Non-floating Feedback message | **`none`** | — |

Both the listing card and the sticky bar were checked on real product screens.
**A card is not elevated. Give it a border.**

---

## The four tiers

*What each level is for, once something does float.*

| Tier | Blur / Y offset | Use for |
| --- | --- | --- |
| `none` | — | Everything above. The default |
| `4` | 4 / 1 | Minimal lift, anchored tightly to a trigger or another surface — floating button group, selectable list, slider handle, coach mark, small decorative badges |
| `8` | 8 / 2 | Overlays and page furniture that sit above content — action menu, date picker, top bar, a floating-variant button, the floating Feedback message |
| `16` | 16 / 4 | Transient overlays at the top of the stack — snackbar, tooltip, mobile bottom sheet |

All are drop shadows: no spread, no horizontal offset, fixed colour `#00000029`
(black at 16%). Never author a custom shadow colour, spread or X offset.

---

## When the tier is unresolved, ask

*Nothing distinguishes `8` from `16`. Do not invent a reason.*

The floating Feedback message uses `8` and Snackbar uses `16`. Both are floating,
temporary, similarly-sized notification components, and **no property of either
explains the difference** — not size, not anchoring, not persistence. A
stacking-order rationale is plausible but was never verified.

So:

| Situation | What to do |
| --- | --- |
| You are using a **named component** from the table above | Use exactly the tier listed. It is what that component uses |
| You need elevation for something **new**, above tier `4` | **Raise it as an open question.** Do not pick between `8` and `16` |

Choosing between them by taste produces output nobody can defend. Saying the
rule is missing is the correct answer.

---

## The blur you see may be half the token

*A rendering artifact, not token drift.*

Several components render elevation via CSS `filter: drop-shadow(...)` rather
than `box-shadow`. When rendered that way the **blur reads as exactly half** the
token's value — tier `16` renders as `8px` blur. The offset is unchanged.

Confirmed consistent across every instance checked. **Never report this as a
mismatch, and never compensate for it** by picking a higher tier.

---

## Do not use

| What | Why |
| --- | --- |
| `24` and `32` | **No consumer.** Confirmed from code, not merely unsampled: no component token and no component binds either. The scale in real use tops out at `16` |
| A custom shadow — any other colour, spread, or X offset | Every GSL shadow is a drop shadow with no spread, no X offset, at `#00000029` |
| The mobile bottom navigation bar's shadow (`0px -4px 2px rgba(0,0,0,0.04)`) | Known Figma debt. Matches no tier and is excluded from the rules — do not copy it |

---

## Known gap

`8` versus `16` has no rule, only precedent. Recorded in
[shadow-usage-audit.md](shadow-usage-audit.md). Until it is answered, follow
**When the tier is unresolved, ask**.

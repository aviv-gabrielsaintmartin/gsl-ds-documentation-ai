<!-- Generated from `icons/icons-rules-ai.md` on 2026-09-25 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

# Icon rules for AI generation

_The authoritative ruleset for icons when generating a GSL interface. What exists
is [icons-index.md](icons-index.md). The evidence, the defective names and the
open questions are in `icons-audit.md`, **which a generating agent must not
read**. Components: [components-rules-ai.md](components-rules-ai.md).
Colour: [color-rules-ai.md](color-rules-ai.md)._

---

## Components first

*Use a component; it carries its own icons.*

_**This rule precedes every other rule on this page.** The colour, typography and
spacing rulesets open with the same rule, under the same name — it is one rule
stated where each ruleset needs it._

A `Button`, `Text Field`, `Cell Content`, `Feedback Messages` or `Top Bar`
already places its own icons, in the right size, the right colour and the right
position. Reach for the component first. Everything below applies only when you
are placing an icon into a slot a component exposes, or into something you are
composing yourself.

**Never restyle an icon inside a component instance.** Its fill, its size and its
position belong to the component.

---

## An icon is never interactive on its own

*An icon alone is never the thing the user presses.*

**This is the rule most likely to be broken, and it was broken in run-002.**

A bare icon has **no states, no hit area and no accessible name**. A sighted
mouse user may be able to hit it; a keyboard user cannot reach it, a screen
reader has nothing to announce, and nothing shows hover, focus, pressed or
disabled.

**If the user can press it, the icon sits inside something.** One of:

| Put the icon in | When |
| --- | --- |
| `Button` | Any triggered action, including icon-only ones |
| `Text Button` | The same, where full button weight is too heavy |
| `Link` | Navigation |
| `Chip` | An interactive filter or selection |
| `Floating Button Group` | Icon-only actions over an image or a map |
| A component's own icon slot | The component carries the states for it |

**A tooltip may be triggered by any component. It may never be triggered by a
bare icon.** The trigger needs the states and the hit area, so the icon goes
inside a `Button` — the way `Text Field` does it beside its label.

**A decorative or purely informative icon needs none of this**, because nothing
presses it. The test is whether the user can act on it, never how it looks.

---

## Match the exact name

*The name in the index is the whole of the match.*

Names are reproduced in [icons-index.md](icons-index.md) exactly as the library
holds them. **Fifteen break the lowercase-kebab convention, and three carry a
trailing space.** `eye slash`, `smart fill`, `Save`, `RDC` and `assistance `
are the real strings — an approximate match, a tidied match or a guessed
hyphenation finds nothing.

**Two near-identical pictures are two different icons. The category decides:**

| What you want to say | The icon |
| --- | --- |
| **An idea, a tip, a hint** | `light-bulb`, in **Alert & Feedback**, beside `info` and `question` |
| **A physical light** | `lightbulb`, in **Furnitures** |

They look almost the same and mean different things, so **never pick between
them by appearance** — pick by what you are saying. See
[icons-index.md](icons-index.md) for both rows.

**One name is a typo, and the typo is still the name today:**

| What you may want | What the library actually holds |
| --- | --- |
| A magnifying glass with a spark | `maginifying-glass-spark` — **the typo is the name.** Match it as written |

**Never invent a name that is not in the index**, and never reach for a name
because it resembles one that is.

---

## Two icons are France-only

*`file-cdd` and `file-cdi` are French employment contract types.*

**CDD** is a fixed-term contract, **CDI** a permanent one. They are meaningful on
a French listing and meaningless anywhere else. **Confirmed by Gabriel,
14 September 2026: use them only in a French context**, and never as a generic
document or contract icon — `file-lines`, `file-signature` and `file-certificate`
are the general ones.

The two names differ by one letter. Read it before you place it.

---

## Variants

*Every axis defaults to `Off`. Setting nothing gives the plain outline glyph.*

An icon carries up to four axes beyond its name — `Filled`, `Circle`, `Square`,
and in a handful of cases `Triangle`, `Half` or `Platform`. All of them default
to `Off`.

| Icons | Choice to make |
| --- | --- |
| 133 | **None.** A single variant |
| 276 | `Filled` on or off, and nothing else |
| 45 | More than that — listed in the index |

**What each axis is for is not documented, and this ruleset does not guess.**
The axes were added over several years to cover different cases, and the
reasoning was not written down. **No variant is a wrong choice by any rule that
exists today.**

So:

- **Pick the variant that matches the components around it.** If a nearby
  design-system component uses the circled form of an icon, use the circled form.
  Consistency with what is already on the screen is the only guidance there is.
- **Say which variant you chose, and why, in the run report** whenever the icon
  carries a real choice. A later reader cannot tell a decision from a default,
  because the default is what an unset instance gives.
- **Never report a variant choice as compliant or non-compliant.** Nothing
  authorises either verdict yet.

---

## When no icon fits

*Reuse before invention, exactly as for components.*

1. **Re-read the category.** The index groups all icons into 17 categories, and
   most "there is no icon for this" cases are a name in a category that was not
   looked at.
2. **Check whether a component already carries it.** `Cell Content` shows a
   chevron by default when the row links, and an external-link icon when it
   leaves the site. You do not place those.
3. **If nothing fits, stop and say so.** Do not compose an icon out of shapes,
   do not scale a different icon into service, and do not copy one out of another
   component.
4. **Never place a dot-prefixed name.** `.Legend`, `.Header` and their like are
   internal parts of other components, deliberately unpublished. This holds for
   icons exactly as it holds for components.

---

## Never place

| What | Why |
| --- | --- |
| A bare icon the user can press | No states, no hit area, no accessible name. See **An icon is never interactive on its own** |
| An icon with a name not in the index | It is not a GSL icon |
| A dot-prefixed name | An internal part of another component |
| An icon you drew, traced or composed from shapes | Invention where reuse was available, and it will not re-theme |
| A brand icon as a general-purpose glyph | The **Brands** category is brand marks — `facebook`, `linkedin`, `apple` the company. They are not decoration |

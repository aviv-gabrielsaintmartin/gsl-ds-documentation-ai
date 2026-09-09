# Border width rules for AI generation

_The authoritative ruleset for stroke width when generating a GSL interface.
Every rule is derived from real component bindings. Values:
[border-width-tokens.md](border-width-tokens.md).
Radius: [radius-rules-ai.md](../radius/radius-rules-ai.md).
Shadow: [shadow-rules-ai.md](../shadow/shadow-rules-ai.md).
Border colour: [color-rules-ai.md](../color/color-rules-ai.md)._

---

## Components first

*Use a component; it carries its own border.*

_**This rule precedes every other rule on this page.** The colour, typography and
spacing rulesets open with the same rule, under the same name._

A `<Card>`, `<TextField>` or `<Chip>` already has the correct stroke. Reach for
the component first. Everything below applies to custom containers.

**Never override a component's border width.**

---

## One is the default

*Any bordered surface at rest is `Border Width/1`.*

There are only three tokens, and this one covers almost everything. It is **not**
limited to interactive controls — it applies equally to static containers and
separators.

| At rest | Token |
| --- | --- |
| Card | `Border Width/1` |
| Divider | `Border Width/1` |
| Text Field, default | `Border Width/1` |
| Outlined Chip | `Border Width/1` |
| Checkbox tick-box, and its optional bordered wrapper | `Border Width/1` |
| Button Group items | `Border Width/1` |

If you are choosing a stroke width and the element is at rest, the answer is `1`.

---

## Two means focus, and nothing else

*Double the stroke only for an interactive control's active or focused state.*

`Border Width/2` is the single narrow exception to `1`. It signals focus
independently of colour, so focus survives for a user who cannot rely on the
colour change.

**Confirmed on Text Field:** it applies at `Active`, and it applies there
**regardless of the error state**.

| State | Width | Colour |
| --- | --- | --- |
| Rest | `1` | default border colour |
| Active / focused | **`2`** | default border colour |
| Error, at rest | `1` | **error colour** |
| Error, active | **`2`** | **error colour** |

**Error changes the colour, not the width.** Never widen a border to signal an
error, and never widen one for emphasis, hover, or selection.

---

## None means a fill replaced the outline

*Use `Border Width/None` only where a surface fill does the border's job.*

`Border Width/None` is an explicit value, not the absence of a decision. It is
for a surface that stands in for an outline — a selected or subdued Chip, where
the fill carries the shape that a stroke would otherwise carry.

Do not use it as a way of saying "no border here". If an element simply has no
border, do not author a border property at all.

---

## The three tokens

*The complete set.*

| Token | Value | Used by |
| --- | --- | --- |
| `Border Width/None` | 0 | 2 components — modal, pagination |
| `Border Width/1` | 1 | 27 components |
| `Border Width/2` | 2 | 10 components |

All three are in use. None is orphaned. **There is no fourth value**, and nothing
may be interpolated.

---

## Do not use

| What | Why |
| --- | --- |
| Any value other than `0`, `1` and `2` | The scale is complete. No `1.5`, no `3` |
| `Border Width/2` for anything but active or focused | Its only confirmed meaning. Using it for emphasis destroys the focus signal |
| A widened border to signal an error | Error is a colour change. Width is unaffected |

---

## Known gap

`Energy tag`'s border has never been confirmed. It renders as a flattened SVG
with no exposed stroke, and the Figma link raised to check it resolved to
`Checkbox` instead. If you need `Energy tag`'s border, **raise it as an open
question** rather than assuming `1`.

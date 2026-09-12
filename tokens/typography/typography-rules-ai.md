# Typography rules for AI generation

_The authoritative ruleset for choosing text styles when generating a GSL
interface. Derived from real bindings in `gsl-core-web-design-system`, not from
token names. Evidence is in `typography-usage-audit.md`, which a generating
agent must not read. Values: [typography-tokens.md](typography-tokens.md).
Colour: [color-rules-ai.md](../color/color-rules-ai.md)._

---

## Components first

*Use a component; it already carries its type.*

_**This rule precedes every other rule on this page.** The colour and spacing rulesets open with the same rule, under the same name — it is one rule stated where each ruleset needs it._

Same rule as colour. A `<Button>`, `<Tag>`, `<FeedbackMessage>` or `<CellContent>`
binds its own text style, correct in every brand. Reach for the component first.
Everything below applies only when you are setting type on your own markup.

---

## No hand-set fonts

*Never set font properties by hand.*

No `font-size`, `font-weight`, `line-height`, `font-family`, or `text-decoration`
literals. Apply a **style token** — the properties travel together, and a
mismatched size/line-height pair is the most common way generated type looks
wrong.

**Never name a typeface.** The font family is the *only* property that varies by
brand, and it varies in all 32 styles: `Cera SL sys` (SL, SLN), `Open Sans` (LI,
LIN), `Poppins` (MA), `Gotham` (BD). Hardcoding one breaks four of six brands.
Everything else — size, weight, line height, letter spacing — is identical across
brands, so a style token is safe everywhere.

---

## Size by context

*There is no hierarchy ladder. Size by context.*

No H1→H5 mapping holds. Audited against real screens, a page's own title can
render *smaller* than a section header further down the same page.

Size is chosen per block, from two things:

1. **Local emphasis** — what must dominate its immediate neighbours (a price
   outranking the title above it).
2. **Container size** — the same role goes larger in a full-width page, smaller
   in a compact card.

Observed pairings on real screens, to copy rather than derive:

| Context | Element | Style |
| --- | --- | --- |
| Detail page (full width) | Price, primary | `headline/28/bold` |
| Detail page | Section header | `headline/22/bold` |
| Detail page | Property title | `body/16/bold` |
| Detail page | Key facts, address, card copy | `body/14/regular` |
| Search result card | Price | `headline/24/bold` |
| Search result card | Listing title | `body/16/bold` |
| Search result card | Provider tag | `body/12/regular` |
| Homepage module | Module title | `body/16/bold` |
| Homepage carousel | Widget label / sub-label | `body/14/bold` / `body/12/regular` |

**Bold vs Regular within a size is emphasis, not hierarchy.**

---

## The eleven used styles

*Start from the eleven styles components actually use.*

These are the styles the design system exercises in real components. Prefer them:

| Style | Size/LH | Components | Bound by |
| --- | --- | --- | --- |
| `body/16/bold` | 16/24 | 16 | `accordion`, `button`, `cellContent`, `datePicker`, `feedbackMessage` +11 |
| `body/16/regular` | 16/24 | 22 | `accordion`, `actionMenu`, `avatar`, `cellContent`, `checkbox` +17 |
| `body/16/regular underlined` | 16/24 | 1 | `link` |
| `body/14/bold` | 14/20 | 7 | `badge`, `field`, `mediaUpload`, `rating`, `snackbar` +2 |
| `body/14/regular` | 14/20 | 19 | `accordion`, `buttonGroup`, `cellContent`, `checkbox`, `chip` +14 |
| `body/12/bold` | 12/16 | 3 | `badge`, `datePicker`, `mediaUpload` |
| `body/12/regular` | 12/16 | 4 | `avatar`, `mediaUpload`, `slider`, `tag` |
| `headline/32/bold` | 32/40 | 1 | `progressCircle` |
| `headline/24/bold` | 24/32 | 1 | `progressCircle` |
| `headline/22/bold` | 22/28 | 6 | `accordion`, `infoState`, `loadingState`, `mediaUpload`, `selectableList` +1 |
| `headline/20/bold` | 20/26 | 0 | direct: `unsafe` |

`body/16/regular`, `body/14/regular` and `body/16/bold` alone cover most text.

---

## Headline is bold-only

*Headline is bold-only.*

Every `regular` headline weight — 22, 24, 28, 32 — exists solely to size
`avatar`'s initials. None expresses a heading anywhere in the system.

**Use `headline/*/bold` for a heading. Never `headline/*/regular`.**

The same applies to `body/11/regular` and `display/45/regular` — avatar's ramp,
not text styles.

---

## No Display

*Do not use Display.*

**No component binds a Display style**, and none of three sampled product screens
used one. If you reach for Display you are outside every precedent in the system.

For a large heading use `headline/32/bold`, the largest style with real use.

---

## Inline link decoration

*For an inline link, use the decoration longhand.*

| Need | Token |
| --- | --- |
| Underline at the surrounding text's size | `typography.css.textDecoration.underline` |
| A standalone 16px underlined link | `body/16/regular underlined` |

The longhand adds underline while **inheriting size and weight**, so an inline
link matches whatever copy it sits in. That is why seven of the eight
`underlined` styles have no consumer — do not reach for them to underline text at
another size; use the longhand.

**Never underline text that is not a link.**

---

## What "no component" means on the token page

It does **not** mean unused. Product pages set type directly, outside the
component library: `headline/28/bold` is the detail-page price on a real screen
yet no component binds it.

Read the `Used by` column as *"do I get this style for free from a component"* —
not as a list of dead tokens. **The eleven used styles** tells you which to
prefer; it is about precedent, not about deletion.

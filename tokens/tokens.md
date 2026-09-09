Design tokens for the GSL Design System, generated from the Figma Foundations Library where applicable. One page per category — each is just the tokens and how to use them.

## For AI generation

Six categories have been audited against real component usage and carry a
dedicated, evidence-based ruleset. **Read the ruleset, not just the token page** —
it says which tokens are actually authorised and which have no precedent.

| Category | Ruleset | Evidence |
| --- | --- | --- |
| Colour | [color-rules-ai.md](color/color-rules-ai.md) | [color-usage-audit.md](color/color-usage-audit.md) |
| Typography | [typography-rules-ai.md](typography/typography-rules-ai.md) | [typography-usage-audit.md](typography/typography-usage-audit.md) |
| Spacing & sizing | [spacing-rules-ai.md](spacing/spacing-rules-ai.md) | [spacing-usage-audit.md](spacing/spacing-usage-audit.md) |
| Corner radius | [radius-rules-ai.md](radius/radius-rules-ai.md) | [radius-usage-audit.md](radius/radius-usage-audit.md) |
| Shadow | [shadow-rules-ai.md](shadow/shadow-rules-ai.md) | [shadow-usage-audit.md](shadow/shadow-usage-audit.md) |
| Border width | [border-width-rules-ai.md](border-width/border-width-rules-ai.md) | inline in [border-width-tokens.md](border-width/border-width-tokens.md) |

**Every token category has now been checked against real component usage.** The
six above carry a full ruleset; the rest carry a `Used by` column and their
findings inline:

| Category | Headline finding |
| --- | --- |
| [Breakpoint](breakpoint/breakpoint-tokens.md) | Used via responsive object keys, not token names — mechanism now documented |
| [Grid](grid/grid-tokens.md) | **No component uses it.** Figma and product pages only. `Grid/Width` derivation verified |
| [Z-Index](z-index/z-index-tokens.md) | Applied through `Overlay`'s context, which sums when nested; level `2` unused |
| [Opacity](opacity/opacity-tokens.md) | Only 3 of 11 used — prefer an alpha colour token over an opacity |
| [Motion](motion/motion-tokens.md) | All four easings used and split by purpose; `500 ms` unused |
| [Sizing](sizing/sizing-tokens.md) | Not a Figma property; a code-side dimension ledger. 6 dead tokens |

## Categories

| Page | Covers | Count |
| --- | --- | --- |
| [Color tokens](color/color-tokens.md) | Semantic colour, Light + Dark, 6 brands — drills into 7 family pages | 218 |
| [Typography tokens](typography/typography-tokens.md) | Text styles — 32 per brand, +1 shared decoration longhand | 33 |
| [Spacing tokens](spacing/spacing-tokens.md) | Padding, gaps, margins | 17 |
| [Sizing tokens](sizing/sizing-tokens.md) | Fixed widths and heights — control sizes, avatars, thumbnails, panel widths | 43 |
| [Radius tokens](radius/radius-tokens.md) | Corner radius | 5 |
| [Border width tokens](border-width/border-width-tokens.md) | Stroke widths | 3 |
| [Shadow tokens](shadow/shadow-tokens.md) | Elevation | 6 |
| [Breakpoint tokens](breakpoint/breakpoint-tokens.md) | Viewport tiers and the responsive-prop mechanism | 8 |
| [Grid tokens](grid/grid-tokens.md) | Column grid — Figma and product pages only, no component uses it | 4 |
| [Opacity tokens](opacity/opacity-tokens.md) | Opacity scale — code only | 11 |
| [Motion tokens](motion/motion-tokens.md) | Animation durations and easings — code only | 11 |
| [Z-Index tokens](z-index/z-index-tokens.md) | Stacking order — code only | 5 |

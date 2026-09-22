Tracks the category-by-category documentation review for `tokens/`. Read this before starting a review session, update it before ending one.

## What "review" means here

Values are already exported from Figma and trusted — no spot-check against Figma needed. A review checks:

1. The file follows the shared template: `Overview` (which family/layer — omit if there's only one), `Semantic usage` (when to use each specific token), `Tokens` (exact values).
2. `Semantic usage` is actually complete — every token has a "when to use" note, not just a bare value table.
3. Anything flagged as open/unconfirmed in the file itself is still accurate, or gets escalated here.
4. If `Semantic usage` guidance can't be confirmed from the file or a naming convention alone, sample real screens live via Figma before writing it — don't infer a hierarchy or rule from convention and present it as settled.
5. Where any learning beyond the confirmed rule needs storing, use the same three-tier split everywhere, not an ad hoc format per session:
   - **Confirmed rule** → stated as plain prose/table in `Semantic usage`. No label needed for a settled fact.
   - **A short, self-contained caveat about the token data itself** — doesn't need methodology or evidence to understand (e.g. "these two tokens resolve to the same value, unclear if intentional") — gets a one-line inline flag directly in the token doc, using a standard label: `**Open question:**` for something genuinely unresolved, `**Note:**` for a resolved non-issue worth a heads-up (e.g. a rendering artifact that looks like a bug but isn't).
   - **Anything that needs methodology, a component/screen list, or produced multiple findings** — whether it settled into a confirmed rule (supporting evidence) or stayed exploratory (no rule could be confirmed) — goes into a sibling `<category>-usage-audit.md` file, human-facing only, flagged not-AI-facing in its own header (see `typography-usage-audit.md` and `radius-usage-audit.md` for the pattern, itself modelled on `color/surface-border-combination-audit.md`). The main doc keeps only a one-line pointer to it. This keeps the split about the *shape* of the content (self-contained fact vs. researched evidence), not its size or whether it's "confirmed" — a confirmed rule can still have audit-file-worthy supporting evidence (radius, shadow), and a short caveat doesn't need a whole file just because it's unresolved (border-width, grid, surface).

## Status

| Category | File | Status | Last reviewed | Notes |
| --- | --- | --- | --- | --- |
| Surface | `color/surface.md` | Reviewed | 2026-09-03 | Full template. Two `**Open question:**` flags in the file itself (relabeled during the 2026-09-03 audit-storage consistency pass, content unchanged): `Accent/Light` vs `Active` resolve identically, `Decorative` family boundary still too vague. Both short, self-contained caveats — no sibling audit file needed per the updated methodology. |
| Border | `color/border.md` | Reviewed | 2026-09-03 | Full template. |
| Content | `color/content.md` | Reviewed | 2026-09-03 | Full template. |
| Symbols | `color/symbols.md` | Reviewed | 2026-09-03 | Full template. |
| Scale | `color/scale.md` | Reviewed | 2026-09-03 | Full template. |
| Native | `color/native.md` | Reviewed | 2026-09-03 | Single family, no Overview needed. |
| Background | `color/background.md` | Reviewed | 2026-09-03 | Single family, no Overview needed. |
| Spacing | `spacing-tokens.md` | Reviewed | 2026-09-03 | Rebuilt this session — merged two prior files, added Overview + Semantic usage. |
| Typography | `typography-tokens.md` | Reviewed | 2026-09-03 | Rewritten after auditing 3 real screens in Figma — no H1–H5 mapping exists in practice; size is a per-block choice (local emphasis + container size), not a lookup. Exploratory findings live in the sibling `typography-usage-audit.md` (the original model for the sibling-audit-file pattern, now formalized in the methodology above). Its inline pointer flag was relabeled `**Open question:**` during the 2026-09-03 consistency pass; content unchanged. |
| Radius | `radius-tokens.md` | Reviewed | 2026-09-03 | Confirmed rule (size/shape-tiered: `4`/`8`/`16` scale with container size, pill covers filled/interactive controls regardless of size) unchanged. During the 2026-09-03 audit-storage consistency pass, moved the supporting evidence — the 9-component and 3-screen live spot-checks, the pill-value non-issue, and two out-of-scope findings (Figma's unimplemented "Corner radius" layer; a custom-built sort control masquerading as a real component) — out of the doc's `Semantic usage` prose and into a new sibling file, `radius-usage-audit.md`, per the same pattern typography already used. Nothing lost, just relocated. |
| Shadow | `shadow-tokens.md` | Reviewed | 2026-09-03 | Confirmed tiers (`none`, `4`, `8`, `16`) and the drop-shadow rendering note stay inline (relabeled `**Note:**`) since they're either the rule itself or a short self-contained caveat. During the 2026-09-03 consistency pass, moved the `8` vs `16` open question's full reasoning, the 8-component + 5-page-element spot-check method, and the two resolved anomalies (mobile nav bar shadow, autocomplete dropdown) into a new sibling file, `shadow-usage-audit.md` — the doc itself now keeps only a short actionable `**Open question:**` flag pointing there. Nothing lost, just relocated. |
| Border width | `border-width-tokens.md` | Reviewed | 2026-09-03 | Confirmed rule unchanged: `1` is the default stroke weight for basically any bordered surface at rest — static containers/separators (Card, Checkbox's `Border=ON` wrapper, Divider) as much as interactive controls at rest (Text Field default, outlined Chip, Checkbox's tick-box, Button Group items); `2` is the one narrow exception, reserved for an interactive control's active/focused state (confirmed on Text Field, where it applies at `Active` regardless of `Error`); `None` covers filled surfaces that substitute for a stroke entirely. During the 2026-09-03 consistency pass, added the previously-tracker-only Energy tag open thread as an inline `**Open question:**` flag in the doc itself (a Figma link meant to show Energy tag's border resolved to Checkbox instead; Energy tag's real border, if any, is baked into flattened SVG artwork and unverified) — short and self-contained enough that no sibling audit file is needed for it. |
| Opacity | `opacity-tokens.md` | Not started | — | Same. |
| Z-Index | `z-index-tokens.md` | Not started | — | Already merges usage into the Tokens table via a "Use for" column — check if that's sufficient or needs a dedicated Semantic usage section. |
| Breakpoint | `breakpoint-tokens.md` | Not started | — | Same. |
| Grid | `grid-tokens.md` | Not started | — | Has an existing flag about no live grid layout system — re-check it's still accurate. Relabeled to `**Open question:**` during the 2026-09-03 audit-storage consistency pass for label consistency only; this doesn't count as a full review pass. |
| Motion | `motion-tokens.md` | Not started | — | Has an existing note that duration/easing pairing tokens don't exist yet — re-check it's still accurate. |

## Out of scope for now

- The `color/surface-border-combination-audit.md` draft — left alone deliberately, not part of this review track.
- Figma value spot-checks — tokens are already exported and trusted; only revisit if something looks structurally wrong.

---
paths:
  - "tokens/**"
---

# Token docs

One folder per token category, mirroring how `components/` is organised.

- **Start at `tokens/README.md`** — it explains every file's role.
  `tokens/tokens.md` is the content index.
- Only `README.md`, `tokens.md` and `review-progress.md` sit at the top level.
  Everything else lives in a category folder — `color/`, `typography/`,
  `spacing/`, `sizing/`, `radius/`, `shadow/`, `border-width/`, `breakpoint/`,
  `grid/`, `motion/`, `opacity/`, `z-index/` — or in `scripts/`.

## The filename suffix states the file's role

| File | Role |
| --- | --- |
| `<category>-tokens.md` | The token page: values and usage, with a **Used by** column naming the components that really bind each token. |
| `<category>-rules-ai.md` | The AI ruleset — what an agent may actually use, derived from the audit. **These, not the token pages, are what a generating agent reads.** Seven exist: `color`, `typography`, `spacing` (which also covers `sizing`), `radius`, `shadow` and `border-width`, plus `components`. The five without one — `breakpoint`, `grid`, `motion`, `opacity`, `z-index` — have no contract yet, so an agent has nothing authorised to reach for in those categories. |
| `<category>-usage-audit.md` | Human-facing evidence and verdicts, including rejected options and open questions. **Never read as rules.** |
| `<category>-usage-ledger.md` | **Generated, never hand-edited** — the raw table the audit was built from (every token, every component that binds it). Only `color`, `typography` and `spacing` have one; the `.json` twin is gitignored. |

## Token page template

Every token page follows one shape:

1. `Overview` table — which family or layer to use. Omitted where there's only one.
2. `Semantic usage` table — which specific token, when.
3. `Tokens` table — exact values.

No tool-specific source annotations, so the docs stay usable regardless of what
pipes them into Confluence, Figma, or elsewhere.

## `color/`

The only category with more than three files:

- `color-tokens.md` — family index
- seven family pages: `background.md`, `surface.md`, `border.md`, `content.md`,
  `symbols.md`, `scale.md`, `native.md`
- its ruleset and audit
- a draft `surface-border-combination-audit.md` — human-facing only, see the
  file's own header

## `tokens/scripts/`

Four read-only Python extractors that regenerate the usage evidence from
`gsl-core-web-design-system`, each writing its `-usage-ledger.{md,json}` into the
matching category folder.

This is the one deliberate exception to "no tooling in this repo": without it
the **Used by** columns go stale the first time a component changes. The `.md`
ledgers are committed as the evidence the audits link to; the `.json` twins are
gitignored and regenerated on demand.

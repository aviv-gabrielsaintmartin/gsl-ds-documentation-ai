---
name: figma-sync-tokens
description: Extract design tokens, text styles, and effect styles from the GSL Foundations Figma library into the local tokens registry, resolving per-brand and light/dark values. Triggers on requests to update/sync/refresh Figma design tokens (colors, spacing, radius, breakpoints, grid, border-width, effect styles, text styles) for a given category.
metadata:
  author: Aviv
  version: "2.0.0"
  status: production
---

# Figma Tokens Sync

Local-only version of a skill formerly run against 8 separate Confluence "Keys" pages under "Figma Variables Keys" (space `ADS`). Confluence is dropped entirely — that output was read by AI agents reconciling state, not by humans, so `figma-tokens-registry.json` (repo root) is now the sole source of truth and the only output. Static background reading on how tokens resolve across brand/mode/primitive layers is cached in `architecture.md` (this skill's folder) — read it once per session if unsure how a category resolves, not per token.

## Objective

Extract design tokens, text styles, and effect styles from `0. GSL Foundations Library` in Figma Desktop for a targeted category, resolve light/dark and per-brand values where relevant, and update `figma-tokens-registry.json` for that category only.

## Prerequisites & Mappings

| Item | Value / Configuration |
|---|---|
| **App & Plugin** | Figma Desktop with `0. GSL Foundations Library` open. Plugin: `Plugins → Development → **FigCli** → Run` (keep the plugin window open). **Only Gabriel can start it** — ask, then wait. |
| **How Figma is driven** | **`figma-cli`, at `~/figma-cli`. It is not on PATH** — run everything as `cd ~/figma-cli && node src/index.js <cmd>`. `run <file>` executes a script in the plugin context; `eval <code>` handles one-liners. **Do not use the Desktop Bridge (`figma-console-mcp`)** — Gabriel retired it as unmaintained, and the `figma_execute` / `figma_get_variables` tools this skill used to call no longer exist. |
| **Foundations Key** | Read from `figma-libraries-registry.json` under `foundations`. |
| **Registry** | `figma-tokens-registry.json` (repo root). Read and write directly — never Confluence. |
| **Architecture reference** | `architecture.md` (this folder) — resolution model, collection/mode IDs, scope rules. Static; only re-cache if the owner says the token architecture itself changed. |
| **Audit log** | `audit-log.md` (this folder) — append a short entry after each run instead of writing to a Confluence audit page. |

### Category → collection mapping

| Category | Collection Source |
|---|---|
| **border-width** | `1 - Primitive` |
| **breakpoints** | `4 - Breakpoint` |
| **colors** | `3 - Brand` |
| **effect-styles** | Local effect styles (not a variable collection) |
| **grid** | `4 - Breakpoint` |
| **radius** | `1 - Primitive` |
| **spacing** | `1 - Primitive` |
| **text-styles** | Local text styles (not a variable collection) — added during the 2026-08 Confluence backfill; wasn't part of the original skill's scope but the source data existed, so it's kept as its own category. |

## Steps

**STEP 0: Scope selection**
1. Check whether a category was named in the prompt.
2. If not, ask: "Which category was updated? (border-width, breakpoints, colors, effect-styles, grid, radius, spacing, text-styles)"

**STEP 1: Target resolution & connection check**
1. Map the target category to its collection source above.
2. Verify the plugin is attached, and treat this as two separate checks:
   - `cd ~/figma-cli && node src/index.js status` → the daemon only. `✓ Daemon running` says **nothing** about the plugin.
   - `node src/index.js eval 'JSON.stringify({name: figma.root.name})'` → the plugin, and which file it is on. It must read `0. GSL Foundations Library`.
   - **`Error: fetch failed` means the plugin is not attached, not that the daemon is down.** The usual cause is Figma switching files, which stops the plugin. Ask Gabriel to run `Plugins → Development → FigCli`. You cannot do it.
3. Read the `foundations` key from `figma-libraries-registry.json`. **Do not try to read it from Figma: `figma.fileKey` is `undefined` through FigCli** (proved 2026-09-14). The registry is the source for it.
4. Ignore expired REST tokens — all extraction runs in the plugin context, through `node src/index.js run <file>`.

**STEP 2: Targeted extraction rules**
- Exclude variables containing 🔒 (component-internal).
- Exclude raw `Color/*` primitives in `1 - Primitive` (hidden from publishing).
- **colors** → extract `3 - Brand` (6 brand modes). Resolve Dark mode by walking the alias chain `3 - Brand → 2 - Mode → 1 - Primitive` with the mode pinned — the plugin's variable API resolves against Light by default (see `architecture.md`).
- **spacing / radius / border-width** → extract `1 - Primitive`.
- **breakpoints / grid** → extract `4 - Breakpoint` (7 modes).
- **effect-styles / text-styles** → extract local styles, not variables.
- Read publish keys with a script run through `node src/index.js run <file>`: `await figma.variables.getLocalVariablesAsync()`, then `v.key` on each. Have it `return JSON.stringify(...)` and capture stdout. Paginate at 100 items per request.
- Round-trip one publish key per collection via `importVariableByKeyAsync` before saving, to confirm it's live.

**STEP 3: Diff against the local registry**
Compare live Figma tokens against the existing `figma-tokens-registry.json` entry for this category only:
- **ADDED** — in Figma, missing in registry.
- **REMOVED** — in registry, missing in Figma.
- **RECREATED** — key changed (delete + recreate).
- **VALUE UPDATED** — value or alias path changed.
- **VALUE/NAME DRIFT** — name suggests one value, holds another (e.g. `Radius/16` = 17px). Record the real value; don't flag as an anomaly.

**STEP 4: Write the registry**
Merge the updated category into `figma-tokens-registry.json`, preserving every other category untouched.

**STEP 5: Log & report**
1. Append one line to `audit-log.md`: date, category, structural delta counts, value-update count.
2. Print a chat summary: category updated, deltas, registry write confirmation.

## Known Traps & Resolutions

See `known-traps.md` in this folder — append new ones there, not here.

---
name: figma-sync-component-sets
description: Extract component/pattern/experience/foundations-component identity, keys, node IDs, variant properties, and Pattern 1/2 classification from any GSL Figma library (Components, Patterns, Experiences, or the real components inside Foundations) into the matching local registry. Triggers on requests to document/update/sync/audit a component, pattern, or experience's Figma props, in any of the four GSL library tiers.
metadata:
  author: Aviv
  version: "1.1.0"
  status: production
---

# Figma Component / Pattern / Experience Sync

Generalized 2026-08-26 from the original Components-only `figma-sync-components` skill, after confirming live that the Patterns library uses identical Figma primitives — `COMPONENT_SET`/`COMPONENT` nodes, variant properties, and the same public/private dot-prefix convention already seen in Components (e.g. Patterns' "Burger menu" page: a public `Burger menu` set built from private `.base_burger menu` and `.base_profil` helper sets). One skill, one `known-traps.md`, covering all node-bearing GSL library tiers — `components`, `patterns`, `experiences`, and (added 2026-08-27) `foundations` — instead of tripling near-identical logic. Confluence is never read or written; the matching `figma-*-registry.json` file (repo root) is the sole source of truth for each tier.

**Foundations is a mixed-content library** — it also holds Tokens (variables/styles, `figma-sync-tokens`'s territory) and Icons (a separate flat inventory, `figma-sync-icons`'s territory — leaf components, no composition to track). This skill's `foundations` tier covers the real, named components (`Flag`, `Favicon`, `Image Ratio`, `Brand Logo`, `Brand App Icons`) plus, as of 2026-08-28, Illustrations: 173 `COMPONENT_SET`s across 10 category frames on the "Illustrations" page, each a self-contained Pattern 1/2 entity with real composition (unlike Icons) — stored under the registry's `illustrations` key, grouped by category, rather than mixed into the flat `components` key. See `known-traps.md` for the illustrations-specific multibranding pattern (Style lives on an exposed sub-component, not the parent's own variant).

## Objective

Extract identity, parent property definitions (`VARIANT`, `BOOLEAN`, `INSTANCE_SWAP`, `TEXT`), variant counts, and exposed sub-components (`isExposedInstance`) for a named component/pattern/experience from whichever GSL library is open in Figma Desktop, and keep that tier's registry in sync.

## Prerequisites & Mappings

| Item | Value / Configuration |
|---|---|
| **App & Plugin** | Figma Desktop with the target library open. Plugin: `Plugins → Development → **FigCli** → Run` (keep the plugin window open). **Only Gabriel can start it** — ask, then wait. |
| **How Figma is driven** | **`figma-cli`, at `~/figma-cli`. It is not on PATH** — run everything as `cd ~/figma-cli && node src/index.js <cmd>`. `run <file>` executes a script in the plugin context; `eval <code>` handles one-liners. **Do not use the Desktop Bridge (`figma-console-mcp`)** — Gabriel retired it as unmaintained, and the `figma_get_status` / `figma_execute` tools this skill used to call no longer exist. |
| **Library tiers → registry files** | `components` → `figma-components-registry.json` · `patterns` → `figma-patterns-registry.json` · `experiences` → `figma-experiences-registry.json` · `foundations` → `figma-foundations-components-registry.json` (all repo root, all shaped `{"components": {...}}` regardless of tier — the key name is kept literal across all files for structural parity, even though it reads oddly for a patterns/experiences/foundations file). `figma-foundations-components-registry.json` additionally carries a sibling top-level `illustrations` key (added 2026-08-28) shaped `{"page", "auditedDate", "status", "categories": {"<Category Name>": {"illustrations": [...]} } }` — illustrations are catalog-sized (173 entries across 10 categories) and category-grouped like Icons, so they get their own key rather than flattening into `components`. |
| **Library file keys** | Read from `figma-libraries-registry.json` under the matching tier. |
| **Audit log / Known traps** | `audit-log.md` / `known-traps.md` (this folder) — shared across all three tiers; audit entries are tagged with the tier + page they came from. |

## Steps

**STEP 0: Target resolution**
1. Determine the tier: if the user named it explicitly, use that. Otherwise infer it from the open file's name — `cd ~/figma-cli && node src/index.js eval 'JSON.stringify({name: figma.root.name})'` — and match that against `figma-libraries-registry.json`. **Match on the file *name*, never on `fileKey`: `figma.fileKey` is `undefined` through FigCli** (proved 2026-09-14), so a key-based match silently fails. If the name matches no tier, ask rather than guess.
2. Check if a component/pattern/experience name was given. If not, ask: "Which one would you like to document or update?"

**STEP 1: Registry pre-check (create vs. update)**
1. Look up the name in the resolved tier's registry file.
2. If present: UPDATE mode — preserve any manually-added notes on that entry. If absent: CREATE mode.

**STEP 2: Extract live Figma nodes**
1. Verify the plugin is attached, and treat this as two separate checks:
   - `cd ~/figma-cli && node src/index.js status` → the daemon only. `✓ Daemon running` says **nothing** about the plugin.
   - `node src/index.js eval 'JSON.stringify({name: figma.root.name})'` → the plugin, and which file it is on. Confirm it is the tier you resolved in STEP 0.
   - **`Error: fetch failed` means the plugin is not attached, not that the daemon is down.** The usual cause is Figma switching files, which stops the plugin. Ask Gabriel to run `Plugins → Development → FigCli`. You cannot do it.
2. Search the active file for the `COMPONENT_SET` (or a standalone `COMPONENT`, for a slot-style/no-variant case — see `Content Placeholder` in `figma-components-registry.json` for precedent) named [Name]. On Patterns/Experiences pages, a public pattern is often built from `.`-prefixed private helper sets on the same page — register the public one; private helpers stay internal, same convention already applied in Components (e.g. `.Select card AI test`).
   - **Flat asset family case** (first seen in Foundations' `Brand App Icons`): several standalone `COMPONENT`s (no shared `COMPONENT_SET`, no variant properties) that read as one family — e.g. per-platform/per-brand app icon exports. Register these as **one registry entry** for the family name, with an `assets: [{name, key, nodeId}]` array instead of `variantCount`/`componentPropertyDefinitions`. Don't split into one top-level entry per asset.
3. Extract by writing a script to the scratchpad and running `node src/index.js run <file>` — it executes in the plugin context, so `figma.loadAllPagesAsync()`, page and node lookup, `componentPropertyDefinitions` and `isExposedInstance` all behave as the Plugin API documents. Have it `return JSON.stringify(...)` and capture stdout. Extract:
   - Key and node ID.
   - Variant count (`children.length`) if a `COMPONENT_SET`; omit if a standalone `COMPONENT`.
   - All `componentPropertyDefinitions`, preserving exact string literals/typos.
   - Walk child instances up to 3-4 levels deep via `isExposedInstance` to classify Pattern 1 (self-contained) vs. Pattern 2 (composed, exposed sub-components) — patterns/experiences are more likely to land Pattern 2 since they're built by composing base components, but never assume; always verify live.
   - **For a Pattern 2 entry, also capture each exposed slot's own property definitions** — not just its name/key. A design agent instantiating the parent can't set a nested slot's variant/boolean via the parent's own `componentPropertyDefinitions`; Figma doesn't merge them. It has to find the exposed nested instance node by name and call `setProperties()` on that node directly, using the nested component's own definitions. Match by the nested instance's `mainComponent.key`, never by its (renamable) display name — see `known-traps.md`. Store this as a structured `exposedSubComponents: [{exposedAs, key, name, properties}]` array on the parent's registry entry, not prose — an agent needs to query it, not read it.

**STEP 3: Diff, cache guard & anomaly detection**
1. If UPDATE mode: compare live properties against the existing registry entry.
   - **Deletion guard**: before reporting a variant/option/property as removed, force `await figma.loadAllPagesAsync()`, re-query, and verify twice (see `known-traps.md`).
   - Update key, node ID, variant count, and property data to live values.
2. Identify structural anomalies (lowercase/typo'd names, unexposed slots, layer-tree inconsistencies, WIP/refactor markers like a page name prefixed `(WIP)` or containing "Refacto" — flag and defer rather than register as a finished entry).
3. If CREATE mode: build the full entry from scratch.

**STEP 4: Write the registry**
Merge the entry into the resolved tier's registry file — key, nodeId, pattern, variantCount, property definitions, auditedDate (`YYYY-MM-DD`), status.

**STEP 5: Log & self-enrich**
1. Append a 1-2 sentence entry to `audit-log.md`, tagged with the tier and page (e.g. `[Patterns / Burger menu]`).
2. If a library-wide issue surfaces, log it under its own heading in `audit-log.md`.
3. If a new reproducible API/plugin trap is discovered, append a row to `known-traps.md` — never edit an existing row's meaning, only add.

**STEP 6: Report**
Print a 2-sentence confirmation: tier, mode (CREATE/UPDATE), pattern classification, variant count, registry write confirmation, whether a new trap was logged.

## Known Traps & Resolutions

See `known-traps.md` in this folder.

---
name: figma-sync-icons
description: Extract the flat icon inventory (name, key, node ID, category, variant properties) from the GSL Foundations Figma library's "Icons" page into the local icons registry. Triggers on requests to update/sync/refresh Figma icons, or to look up/add/audit a specific icon.
metadata:
  author: Aviv
  version: "1.0.0"
  status: production
---

# Figma Icons Sync

Foundations' "Icons" page holds ~455 icons across 17 named category frames — each icon is a standalone `COMPONENT_SET` (not composed from other components, unlike Components/Patterns/Experiences). No Pattern 1/2 classification applies here: icons are leaf-level, so `figma-sync-component-sets` explicitly excludes this content and this skill owns it instead. `figma-icons-registry.json` (repo root) is the sole source of truth — Confluence is never read or written, matching the other Foundations-adjacent skills.

## Objective

Keep `figma-icons-registry.json` in sync with the live "Icons" page: one entry per icon, grouped by its category frame, capturing identity (key, node ID) and its own variant properties (not a composed Pattern 2 structure).

## Prerequisites & Mappings

| Item | Value / Configuration |
|---|---|
| **App & Plugin** | Figma Desktop with `0. GSL Foundations Library` open. Plugin: `Plugins → Development → **FigCli** → Run` (keep the plugin window open). **Only Gabriel can start it** — ask, then wait. |
| **How Figma is driven** | **Two channels, different jobs — use both.** **`figma-cli`**, at `~/figma-cli`, **not on PATH**: run as `cd ~/figma-cli && node src/index.js <cmd>`. `run <file>` executes a script in the plugin context, `eval <code>` handles one-liners. **This is the one for bulk extraction and for anything that writes** — far cheaper in tokens than the MCP, and quicker to draw with. **The Figma Dev Mode MCP**, at `127.0.0.1:3845/mcp`: official, **read-only**, and a genuinely *independent* channel — which is what makes it the right way to verify a write, rather than trusting the tool that made it. **Do not use the Desktop Bridge (`figma-console-mcp`)** — Gabriel retired it as unmaintained, and the `figma_execute` / `figma_get_status` / `figma_get_variables` tools these skills used to call no longer exist. |
| **Foundations Key** | Read from `figma-libraries-registry.json` under `foundations`. |
| **Registry** | `figma-icons-registry.json` (repo root), shaped `{"fileKey", "fileName", "page": "Icons", "categories": {"<Category Name>": {"icons": [{"name","key","nodeId","variantCount","properties"}]}}}`. |
| **Categories (17, live as of 2026-08-27)** | Action & Settings, Alert & Feedback, Brands, Navigation & Menu, Users & People, Map, Transportation, Device & Communication, Editor, Document & Content, Finance, Nature & Food, Lifestyle, Furnitures, Place & Property, Real Estate, Home. |
| **Excluded frame** | `Placeholders` — holds 2 generic template components (`placeholder`, `Figma component`), not real product icons. Never register. |
| **Audit log / Known traps** | `audit-log.md` / `known-traps.md` (this folder). |

## Steps

**STEP 0: Scope selection**
1. Check whether a specific icon or category was named. If not, and the request is a full sync, proceed against all 17 categories.
2. If an icon/category name was given, resolve to its category frame first.

**STEP 1: Registry pre-check (create vs. update)**
1. Look up the icon (by category + name) in `figma-icons-registry.json`.
2. If present: UPDATE mode — preserve any manually-added notes on that entry. If absent: CREATE mode.

**STEP 2: Extract live Figma nodes**
1. Verify the connection, in this order — the two failures look identical from the outside and have different fixes:
   - `cd ~/figma-cli && node src/index.js status` → the daemon. `✓ Daemon running (port 3456)` means the CLI is alive; it says **nothing** about the plugin.
   - `node src/index.js eval 'JSON.stringify({name: figma.root.name, pages: figma.root.children.map(p=>p.name)})'` → the plugin, and the file. It must return `0. GSL Foundations Library` with an `Icons` page.
   - **`Error: fetch failed` means the plugin is not attached, not that the daemon is down.** The most common cause is that Figma switched files — the plugin stops whenever the owner opens another document, so a sync that worked minutes ago can fail for that reason alone. Ask Gabriel to run `Plugins → Development → FigCli`. You cannot do it.
2. `await figma.loadAllPagesAsync()`, find the page named `Icons`, then the target category frame(s) by name, excluding `Placeholders`.
3. For each icon `COMPONENT_SET` in scope, extract by writing a script to the scratchpad and running `node src/index.js run <file>` (`eval <code>` works for one-liners). The script runs in the plugin context, so `figma.loadAllPagesAsync()`, page lookup and `componentPropertyDefinitions` all behave as the Plugin API documents. Have it `return JSON.stringify(...)` and capture stdout — all 455 icons come back in one call, about 140 KB. Extract:
   - `name`, `key`, node ID (`id`).
   - `variantCount` (`children.length`).
   - `properties`: the full `componentPropertyDefinitions` object, preserving exact string literals — including typos/casing inconsistencies (see `known-traps.md`, e.g. a lowercase `filled` prop on some icons vs the standard `Filled`).
4. Do not walk `isExposedInstance` or classify Pattern 1/2 — icons are leaf components, this skill doesn't track composition.

**STEP 3: Diff, cache guard & anomaly detection**
1. If UPDATE mode: compare live properties against the existing registry entry.
   - **Deletion guard**: before reporting an icon as removed, force `await figma.loadAllPagesAsync()`, re-query, and verify twice (same convention as `figma-sync-component-sets`).
2. **Check every name for `name !== name.trim()`.** A trailing space is invisible in Figma's layer list, in the registry JSON, and in any page generated from it, so an agent matching `assistance` against `assistance ` finds nothing while appearing to have searched correctly. **Report it; never silently trim** — the registry records what Figma actually holds until the library is fixed. Three were found this way on 2026-09-14.
3. **A rename looks like a deletion until you compare keys.** When an add and a remove appear together, check `key` and `nodeId` on both sides: same key and same node ID means the icon was renamed, and the deletion guard does not apply.
4. Flag, don't silently resolve:
   - A new icon name matching one already registered **in the same category** with a different key (duplicate name within a category — see `known-traps.md`'s `water-ladder` case).
   - A new/changed prop shape outside the common `{Name, Filled}` pattern (e.g. `Circle`/`Square`/`Half`/`Triangle` shape variants, a `Platform` prop) — these are legitimate, just note them; only escalate if the shape looks like a mistake.
3. If CREATE mode: build the full entry from scratch.

**STEP 4: Write the registry**
Merge the entry into `figma-icons-registry.json` under its category, preserving every other category and its manually-added notes untouched.

**STEP 5: Log & self-enrich**
1. Append a 1-2 sentence entry to `audit-log.md`.
2. If a new reproducible API/plugin trap is discovered, append a row to `known-traps.md` — never edit an existing row's meaning, only add.

**STEP 6: Report**
Print a 2-sentence confirmation: mode (CREATE/UPDATE), category, count of icons touched, registry write confirmation, whether a new trap was logged.

## Known Traps & Resolutions

See `known-traps.md` in this folder.

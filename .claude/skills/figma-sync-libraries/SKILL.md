---
name: figma-sync-libraries
description: Sync Figma library file keys (Foundations, Components, Patterns, Experiences tiers) from the active Figma Desktop file into the local registry. Triggers on requests to update/sync/refresh Figma library keys, or when a library file's key has changed and needs recording.
metadata:
  author: Aviv
  version: "2.0.0"
  status: production
---

# Figma Library Keys Sync

Local-only version of a skill formerly run against Confluence page `3423436876` ("Figma Libraries Keys", space `ADS`). Confluence is dropped entirely for this skill: the output is a machine-readable registry consumed by AI agents, not something humans read, so there was no reader-facing reason to keep publishing it there. `figma-libraries-registry.json` (repo root) is the sole source of truth.

## Objective

Keep `figma-libraries-registry.json` in sync with whichever GSL library file is currently open and focused in Figma Desktop.

## Prerequisites

| Item | Value / Configuration |
|---|---|
| **Figma Desktop** | Target library file open in Figma Desktop (the web browser app is not supported). |
| **Plugin** | `Plugins → Development → **FigCli** → Run` (keep the plugin window open). **Only Gabriel can start it** — ask, then wait. |
| **How Figma is driven** | **Two channels, different jobs — use both.** **`figma-cli`**, at `~/figma-cli`, **not on PATH**: run as `cd ~/figma-cli && node src/index.js <cmd>`. `run <file>` executes a script in the plugin context, `eval <code>` handles one-liners. **This is the one for bulk extraction and for anything that writes** — far cheaper in tokens than the MCP, and quicker to draw with. **The Figma Dev Mode MCP**, at `127.0.0.1:3845/mcp`: official, **read-only**, and a genuinely *independent* channel — which is what makes it the right way to verify a write, rather than trusting the tool that made it. **Do not use the Desktop Bridge (`figma-console-mcp`)** — Gabriel retired it as unmaintained, and the `figma_execute` / `figma_get_status` / `figma_get_variables` tools these skills used to call no longer exist. |
| **The file key must come from Gabriel** | **Proved 2026-09-14, on both channels.** `figma.fileKey` is `undefined` through FigCli; `node src/index.js files` returns `{"error":"fetch failed"}` because it needs CDP, which Safe Mode does not give; and the **Dev Mode MCP does not expose it either** — `get_metadata`, `get_design_context`, `get_code_connect_map` and `get_code_connect_suggestions` were each called and none returns a file key. The 40-character hex strings those tools do return are **component** keys; a Figma file key is 22 characters of base62. Neither channel has it. **Ask Gabriel for the file's URL** and take the key from it: `figma.com/design/<fileKey>/<name>`. This is a real capability the Desktop Bridge had and this path does not — say so rather than guessing a key. |
| **Registry** | `figma-libraries-registry.json` (repo root). Read and write this file directly — never Confluence. |
| **Core tiers** | `foundations`, `components`, `patterns`, `experiences` (extensible — a new tier can be added on request). |

## Steps

**STEP 1: Read the current registry**
Read `figma-libraries-registry.json` directly. This is the only source of prior state — there is no Confluence fallback to reconcile against.

**STEP 2: Inspect the active Figma file**
1. Verify the plugin is attached, and note that this is two checks, not one:
   - `cd ~/figma-cli && node src/index.js status` → the daemon only. `✓ Daemon running` says **nothing** about the plugin.
   - `node src/index.js eval 'JSON.stringify({name: figma.root.name})'` → the plugin, and which file it is on.
   - **`Error: fetch failed` means the plugin is not attached, not that the daemon is down.** The usual cause is Figma switching files, which stops the plugin. Ask Gabriel to run `Plugins → Development → FigCli`. You cannot do it.
2. Read the document `name` from that same `eval`. **The `fileKey` cannot be read this way** — see the Prerequisites row. Ask Gabriel to paste the file's URL and take the key from `figma.com/design/<fileKey>/<name>`. **Never invent a key, and never carry forward the key already in the registry as though you had confirmed it.**

**STEP 3: Identify tier & reconcile**
1. Match the active file's name against the existing tiers.
2. If the name is new or ambiguous, ask: "Which tier does '<Active File Name>' belong to, or should I create a new tier name?"
3. Update only the target tier's `name` and `key` — leave every other entry untouched.

**STEP 4: Write the registry**
Save the updated JSON to `figma-libraries-registry.json`. There is no other output location.

**STEP 5: Report status**
Print a Markdown table of all tracked tiers (Tier, File Name, Key, Status), then end with: "Updated [<Tier Name>]. Open another library file and reply 'Next' to continue, or 'Done' to finish."

## Known Traps & Resolutions

| Trap / Behavior | Root Cause & Resolution |
|---|---|
| **The plugin stops whenever Figma switches files** | Confirmed 2026-09-14. A command that worked minutes ago fails with `Error: fetch failed` for no reason other than the owner opening another document. The daemon stays up throughout, so `status` still reports healthy — check the plugin with an `eval`, not with `status`. Only Gabriel can restart it from `Plugins → Development → FigCli`. |
| **No channel on this machine exposes a file key** | Proved 2026-09-14 on `0. GSL Foundations Library`. Through FigCli an `eval` returning `figma.root.name` works while `figma.fileKey` comes back `undefined`; `node src/index.js files` would give it but needs CDP, which Safe Mode does not provide; and the Dev Mode MCP's four read tools return component keys but never a file key. **Component and component-set `key` values read normally — it is only the *file* key that is missing.** Get it from the URL Gabriel pastes: `figma.com/design/<fileKey>/<name>`. |

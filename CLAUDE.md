# CLAUDE.md

Project instructions for this repository.

How Gabriel wants Claude to communicate and handle git/PRs lives in his personal
`~/.claude/CLAUDE.md` and applies to every project. This file holds only what's
true about *this* repo.

Folder-specific detail lives in `.claude/rules/` and loads only when you touch
the matching folder. Don't duplicate it here.

## Objective

**Long-term**: document the full GSL Design System so an AI agent can consume it
with no human in the loop and generate interfaces that are compliant with the
design system and at the quality bar SeLoger holds its interfaces to.

**This repo is the knowledge base, not the agent.** It holds one
platform-neutral truth about GSL. Several agents consume it — design, web, iOS,
Android — each owning its own output surface and its own quality checks. The
roster will be refined once the tooling is tested. The `*-rules-ai.md` files are
the contract between this repo and any consuming agent; keep them
platform-neutral.

**A generating agent reads `*-rules-ai.md`, never the token pages.** The token
pages list everything that exists; the rulesets list what's allowed. Reading the
wrong one produces output built on tokens the audit rejected.

**Compliance means reuse before invention.** A consuming agent should use an
existing DS component or token wherever one fits, and create something new only
when nothing does — declaring it when it does. The failure mode to prevent is
reinventing what already exists, not designing something new.

**Judge any doc by one test**: could an agent build a compliant interface from
this alone, with nobody correcting it?

| When | What |
| --- | --- |
| **End Sept 2026** | An agent that designs fully compliant output in Figma. Compliance only — the quality bar is out of scope for this milestone; it currently exists only in Gabriel's head. |
| Later | The quality bar documented, so output can be judged on quality and not just compliance. |
| Later | Web, iOS and Android generation consuming this knowledge base. Dev teams, built separately. |
| Later | A full audit pipeline across Figma, web, Android and iOS components, so the differences between the four are known and recorded. Deliberately deferred. |

## What this repository is

**Not a source-code repository** — there is no build, lint, or test tooling here
(the one deliberate exception is `tokens/scripts/`). Treat file operations as
content and data work, not software engineering: reading Zeroheight exports,
matching images by hash, publishing to Confluence via the Atlassian MCP tools,
reading live Figma via the Desktop Bridge.

**Owner**: Gabriel Saint Martin, sole owner and maintainer of this repo and its
skills.

## Where to look

| Path | What's there |
| --- | --- |
| `tokens/README.md` | **Start here for tokens** — explains every token file and its role. `tokens/tokens.md` is the content index. |
| `components/<name>/<name>.md` | One doc plus a self-contained `images/` folder per component. |
| `figma/*.json` | Figma identity registries — sole source of truth for the `figma-sync-*` skills. |
| `.claude/skills/` | Six skills. Their descriptions auto-load at session start, so they aren't repeated here — read the `SKILL.md` before running one; it's the source of truth for its own workflow. |
| `.claude/rules/` | Path-scoped detail for `tokens/`, `figma/` and `components/`. Verified 2026-09-07: a rule loads on **Read/Edit/Write** of a matching path, **not** on `cat`, `sed`, `head` or `grep`. Open the first file you touch in one of those folders with Read, or you'll work without its rule. |
| `internal/` | Internal reference docs, e.g. `git-basics-tutorial.md`. |
| `design-language/` | Brand PDF exports. Legacy, superseded elsewhere, left as-is. |

All filenames are lowercase kebab-case. The one exception is image filenames,
left as their original hash-based names because those are Zeroheight asset
identifiers matched by exact filename/hash.

## Branch categories

`<category>/<kebab-case-description>`, e.g. `figma/sync-foundations-components`.

| Category | Use for |
| --- | --- |
| `figma` | Figma sync skills work |
| `zeroheight` | `zeroheight-confluence-transfer` work |
| `docs` | CLAUDE.md, rules, or skill doc edits |
| `audit` | `component-web-ai-docs` runs |

Extensible — add a category when a branch's work doesn't fit an existing one,
rather than forcing a bad fit.

## Pull requests

This repo has no automated test suite, so the PR body's evidence section is
**Verification** (what was checked — e.g. "verified live via Figma Desktop
Bridge", "confirmed registry JSON matches live Figma data") rather than a test
plan.

## Working conventions

- **Never invent** Confluence page IDs, Figma keys, or Atlassian cloud IDs. Read
  them from the registry JSON files, or resolve them live via the
  Atlassian/Figma MCP tools.
- **The Zeroheight MCP connector is never used** by any skill, even if it shows
  as connected in a session. Exports come from a Confluence-staged code block,
  or a human chat-paste as fallback.
- **The four `figma-sync-*` skills never read or write Confluence** — the
  `figma-*-registry.json` files are their sole source of truth.
- **Don't create a per-tier Figma skill.** `figma-sync-component-sets` handles
  Components, Patterns, Experiences and Foundations' real components — extend it
  instead. Foundations' Tokens (`figma-sync-tokens`) and Icons
  (`figma-sync-icons`) are different content shapes and stay outside its scope.

---
paths:
  - "components/**"
---

# Component docs

_Instructions for Claude when working anywhere in `components/`. This is not
design-system content — the component documentation itself starts at
[`components/components-index.md`](../../components/components-index.md)._

One folder per design-system component (`components/accordion/`,
`components/button/`, …), each holding its markdown doc plus a self-contained
`images/` folder — e.g. `components/button-group/button-group.md`.

## The four top-level files

Same `-rules-ai` / `-audit` split the token docs use, plus an `-eval`:

| File | Role |
| --- | --- |
| `components.md` | The index of components that have a usage doc. |
| `components-rules-ai.md` | **The ruleset — what a generating agent reads to choose a component.** Intent → component, tier order (Experiences before Patterns before Components), platform limits, never-select list, and the full inventory of all four Figma libraries. |
| `components-audit.md` | The evidence, the triage, rejected options, open questions. **Never read as rules.** |
| `components-eval.md` | The check on the ruleset — intents with expected answers, scoring bands, and the run log. **The test, not the rules.** |

The ruleset's inventory is generated from the four `figma/*-registry.json` files
and must stay complete: every registry name appears in it exactly once (twice for
`Image Ratio` and `Brand Logo`, which exist in two libraries with different keys).
Re-check after any `figma-sync-*` run.

- Folder and file names are lowercase kebab-case.
- **Image filenames are the exception**: left as their original hash-based
  names, because those are Zeroheight asset identifiers matched by exact
  filename/hash correlation. Never rename them, and never open an image to
  identify it — matching is by name/hash only.
- Images are self-contained per component. Don't reference another component's
  `images/` folder.

Content is produced by `zeroheight-confluence-transfer` (Zeroheight export →
Confluence, against a fixed template) and audited against real web code by
`component-web-ai-docs`. Read the relevant `SKILL.md` before editing docs by
hand, so the structure stays consistent with what those skills expect.

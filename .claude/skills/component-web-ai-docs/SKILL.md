---
name: component-web-ai-docs
description: Audit a GSL Design System web component's code against its Confluence usage documentation, then publish an audit report, a platform-agnostic decision tree, and an LLM-ready API spec as child pages under that component's Confluence page. Triggers on "analyse/analyze <Confluence component link>", one or several links at once, or an explicit request to audit/sync a component's docs against its code.
metadata:
  author: Aviv
  version: "1.0.0"
  status: production
---

# Component Web AI Docs

Given one or more Confluence links to GSL Design System component pages (space
`ADS`, e.g. `https://avivgroup.atlassian.net/wiki/x/GoDNq` or a full
`/wiki/spaces/ADS/pages/<id>/<Title>` URL), for each one: read the component's
real web implementation, compare it against the Confluence usage doc, and
produce three outputs — shared in chat first, then published as three new
Confluence pages nested under that same component page.

**Multiple links in one message → process them fully one at a time, in the
order given.** Finish everything for component 1 (chat outputs + all 3
published pages) before starting component 2. Give one short status line
between components (e.g. "Accordion done — moving to Badge (2/3)").

## 1. Resolve the link → page ID, title, space

1. If the URL already contains a numeric page id (`/pages/<digits>/`), use it directly.
2. Otherwise it's a short link (`/wiki/x/<code>`). Resolve it:
   - First try `getConfluencePage` directly with the short code as `pageId` —
     works for some page/tool combinations.
   - If that 400s, fetch the URL (WebFetch) and read the final redirected
     URL — Confluence resolves `/wiki/x/<code>` to the full
     `/wiki/spaces/<SPACE>/pages/<id>/<Title>` URL.
   - If neither works, use the Confluence `search` tool with a keyword guess
     and match the result whose page matches the link's context.
3. Call `getConfluencePage` (`contentFormat: markdown`) with the resolved ID
   to get the page's `title`, `space.key`, and full `body`. The **title is the
   component name** (e.g. "Button", "Accordion") — trim it, don't guess a
   different one. Keep `space.key` — every page you create later goes in this
   same space, not a hardcoded one.

If resolution fails outright for a link, say so for that link and continue
with the rest of the batch rather than aborting everything.

## 2. Locate the component's source

Search the repo for the matching component directory — do not assume a path:

```bash
find . -iname "*{ComponentName}*" -not -path "*/node_modules/*" -not -path "*/.git/*"
```

Expect something like `libraries/ui/src/{ComponentName}/{ComponentName}.tsx`.
If nothing matches (renamed, not yet built for web, or the title didn't map
cleanly to a directory), stop for that component and tell the user instead of
guessing at a near-match directory.

Once found, read everything needed to ground every claim in real code:
- The main `{ComponentName}.tsx`
- `types.ts` (and any nested `*/types.ts`, e.g. a sub-item's types)
- Any `use{ComponentName}*.ts(x)` hooks
- `i18n.ts` and `index.ts` (to know what's actually publicly exported)
- The matching token file(s): `libraries/tokens/src/shared/components/{name}.json`
  (lowercased/camelCase as it appears on disk) — tokens are the ground truth
  for which variant/state/suffix combinations are actually styled.

Prefer reading these directly; use the `Explore` agent only if the initial
`find` doesn't turn up an obvious match and broader searching is needed.

## 3. Generate the three outputs

Base every finding on a specific file/line, never speculation. Structure:

### OUTPUT 1 — Audit & Triage Report (human-readable)
Three categories:
1. **Outdated Documentation** — doc claims (defaults, behavior, visuals) that
   conflict with what the code/tokens actually do.
2. **Implementation Bugs / Silently Broken Prop Combinations** — type-valid
   or plausible-looking prop combinations that resolve to missing tokens,
   silently no-op, or silently drop part of what was passed (check especially:
   fallback branches in switch/mapping functions, prop combos gated by
   `!== undefined` vs truthiness, and any place a "controlled-sounding" prop
   is quietly downgraded to an uncontrolled one).
3. **Missing Edge-Case Documentation** — real, non-obvious behavior that's
   simply never written down: runtime string/array transformations feeding
   into accessibility labels, mutual-exclusivity rules enforced only by types,
   accessibility implementation that exists but isn't described, undocumented
   passthrough props (e.g. anything the component's prop type extends from a
   shared "external props" style-passthrough type), platform-specific
   constraints the web component doesn't itself enforce.

### OUTPUT 2 — Platform-agnostic decision tree (for `usage.md`)
A text-based decision tree for choosing variant/size/state/context. No code
syntax, no prop names — design intent and visual/UX rules only. Cover every
variant axis the component actually has (check the tokens file for the real
set, don't rely on the doc's list alone).

### OUTPUT 3 — Clean technical spec (for `api.web.md`)
Markdown spec for an LLM coding assistant, no Storybook references:
1. Import statement + polymorphic behavior notes (e.g. does the rendered tag
   change based on a prop like `href`; is there an old/new API split to warn
   about).
2. Strict props reference, including every mutual-exclusivity rule enforced
   by the types (discriminated unions, `never` fields, controlled-XOR-
   uncontrolled state pairs).
3. Invalid usage constraints — concrete "do not" list, one line per
   finding from Output 1's bug/edge-case categories that a code-writing
   assistant needs to know to avoid.
4. Three copy-pasteable JSX examples: a basic case, a stateful/async or
   otherwise "interesting" case, and a minimal/edge-case usage — pick the
   three that are most relevant to *this* component rather than forcing
   Button's loading/icon-only mold onto everything.

Share all three in the chat before doing anything in Confluence.

## 4. Publish to Confluence

Three new child pages under the **same page resolved in step 1**, same
`space.key`, titled exactly (substituting the real component name):

| Page title | Content | Format |
|---|---|---|
| `{ComponentName} API Web Audit` | Output 1 | Native Confluence HTML — `<h2>`/`<h3>` headings, `<table>` for each category. **Not** a code block. |
| `{ComponentName} Decision Tree` | Output 2 | Confluence code block, `language: text`. Preserves exact indentation/branch characters. **Also written into the repo — see 4b below.** |
| `{ComponentName} API Web` | Output 3 | Confluence code block, `language: markdown`, with a one-line intro noting it's intended as the content of `api.web.md`. |

**Before creating**, check the parent page's existing children
(`getConfluencePageDescendants`) for a title collision (a previous run of
this skill). If a page with the same title already exists, ask the user
whether to update it in place or skip — never silently create a duplicate.

**Escaping code-block content**: build the raw text/markdown first, then
HTML-escape it (`<`, `>`, `&`, quotes) before embedding in the `<pre><code>`
body — do this via a scratch file + `python3 -c "import html; ..."`, not by
hand, since the specs are full of generics (`Foo<Bar>`) and JSX tags that are
easy to mis-escape manually. Write the file(s) to the session scratchpad
directory, not the repo.

Report back the three created page URLs for that component, then move to the
next link in the batch (see intro).

## 4b. Write the decision tree into the repo (mandatory)

Publishing Output 2 to Confluence alone is not enough — it is the one output of
the three that is platform-neutral, and this repo is the platform-neutral source
of truth. Confluence-only publication is why every component doc here carried
`Variant Selection Flow: Not documented`.

1. Locate the component's doc: `components/<kebab-case-name>/<kebab-case-name>.md`.
   If there is no such folder, the component has no usage doc yet — say so and
   skip this step rather than creating one.
2. Replace the body of that doc's `### Variant Selection Flow` section with
   Output 2, wrapped in a fenced code block so the tree's indentation and branch
   characters survive. Replace only that section — never touch a neighbouring
   heading.
3. If the section already holds a tree from an earlier run, ask whether to
   overwrite it, exactly as step 4 asks before overwriting a Confluence page.
   Never silently replace human-written content.
4. Outputs 1 and 3 stay Confluence-only. They are code-level and web-specific;
   this repo is platform-neutral (see `components/components.md`).

Report the doc path alongside the three page URLs.

## Never do

- Never invent a component name or source path when the `find` search comes
  up empty — stop and say so for that one link.
- Never hardcode the Confluence space key or cloudId — derive space from the
  resolved parent page, and cloudId from `getAccessibleAtlassianResources` if
  not already known in-session.
- Never skip the collision check before creating a page.
- Never batch multiple links in parallel — always sequential, one fully
  finished component at a time.
- Never publish a claim in the audit that isn't traceable to a specific file
  (and ideally line range) you actually read this run.
- Never finish a component with Output 2 published to Confluence but not written
  into its repo doc (step 4b). That gap is what left every `Variant Selection
  Flow` section reading "Not documented".

---
paths:
  - "components/**"
---

# Component docs

One folder per design-system component (`components/accordion/`,
`components/button/`, …), each holding its markdown doc plus a self-contained
`images/` folder — e.g. `components/button-group/button-group.md`.

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

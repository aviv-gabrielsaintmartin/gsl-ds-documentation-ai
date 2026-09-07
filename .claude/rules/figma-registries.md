---
paths:
  - "figma/**"
---

# Figma registries

Seven registry JSON files — the **sole source of truth** for the `figma-sync-*`
skills. Confluence is neither read nor written by any of them (dropped
2026-08-26: the output was only ever consumed by AI agents, never read by
humans, so publishing it to Confluence was pure token cost with no audience).

| File | Contents |
| --- | --- |
| `figma-components-registry.json` | Components tier |
| `figma-patterns-registry.json` | Patterns tier |
| `figma-experiences-registry.json` | Experiences tier |
| `figma-foundations-components-registry.json` | Foundations tier |
| `figma-libraries-registry.json` | Maps the four GSL library tiers to their Figma library file keys (SoT for `figma-sync-libraries`) |
| `figma-tokens-registry.json` | Per-category design token inventory (SoT for `figma-sync-tokens`) |
| `figma-icons-registry.json` | Flat inventory of Foundations' "Icons" page (SoT for `figma-sync-icons`) |

All four tier registries are populated. As of 2026-09-07 the counts under the
`components` key are: Components 61, Patterns 21, Experiences 11. Treat the
files themselves as the count — not this line.

## Shared schema

The four tier registries share one entry shape:

```
key · nodeId · pattern (Pattern 1 | Pattern 2) · variantCount · auditedDate · status
```

A flat asset family like Brand App Icons carries an `assets` array in place of
the variant fields.

## Foundations tier scope

- Its real components: `Flag`, `Favicon`, `Image Ratio`, `Brand Logo`,
  `Brand App Icons`.
- Its 173 Illustrations (added 2026-08-28), under a sibling top-level
  `illustrations` key — category-grouped, since they're catalog-sized rather
  than a handful of named components.
- **Out of scope for this registry**: Tokens (`figma-tokens-registry.json`) and
  Icons (`figma-icons-registry.json`).

## Known drift with `components/`

The Figma registry and the component docs don't line up one-to-one. A rough
name-match on 2026-09-07 gave 61 Figma components against 53 doc folders, with
39 matching by name — so roughly 22 Figma components have no doc and 14 docs
have no Figma entry. Both figures are inflated by naming mismatches
(`feedback-message` ↔ `Feedback Messages`, `navigation-bar` ↔
`Navigation Bar (App)`), so real drift is smaller.

No reconciliation pass has been run. A component with no doc gives a generating
agent a node key but no usage rules, which invites guessing or needless
reinvention. Treat it as a documentation gap, not a fence.

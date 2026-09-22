_What is true of `Navigation bar` **in Figma** and nowhere else. Layer names, quirks, and
how to work with the component in the tool._

_**This is not the usage documentation.** [`navigation-bar.md`](navigation-bar.md) describes the
component; this page describes the tool. Identity — keys, node IDs, variant
counts, property definitions — lives in `figma/*-registry.json` and is never
restated here._

---

## Why there is only one variant

**The single variant is deliberate.** Gabriel, 21 September 2026. The one
property is unnamed — Figma's own `Property 1`, with the single option
`Default`.

**Breakpoints run on Figma variables, not on variants.** One component works at
every width, which is why no breakpoint axis exists. Building it as a variant
grid was the worse option under Figma's constraints.

## Do not read this structure as an architecture

**The development architecture does not mirror the Figma one.** Gabriel,
21 September 2026.

One Figma component that adapts is not a statement about how the bar is built,
or would be built, on web. It is a statement about Figma.

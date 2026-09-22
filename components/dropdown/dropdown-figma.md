_What is true of `Dropdown` **in Figma** and nowhere else. Layer names, quirks, and
how to work with the component in the tool._

_**This is not the usage documentation.** [`dropdown.md`](dropdown.md) describes the
component; this page describes the tool. Identity — keys, node IDs, variant
counts, property definitions — lives in `figma/*-registry.json` and is never
restated here._

---

## Not every position is drawn

**The component does not carry a variant for every position it supports.** They
were left out to keep the variant count down.

**Detach the component** when you need a position the variants do not offer. The
positions themselves are real and documented in
[`dropdown.md`](dropdown.md) — this is a limit of the Figma component, not of the
component.

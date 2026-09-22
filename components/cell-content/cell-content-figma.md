_What is true of `Cell content` **in Figma** and nowhere else. Layer names, quirks, and
how to work with the component in the tool._

_**This is not the usage documentation.** [`cell-content.md`](cell-content.md) describes the
component; this page describes the tool. Identity — keys, node IDs, variant
counts, property definitions — lives in `figma/*-registry.json` and is never
restated here._

---

## The leading placeholder setting is misspelled

The property that controls the leading placeholder is named
**`Placeholder left alignement`**. The misspelling is in the library, and it is
preserved here so a lookup by name still finds it.

Do not correct it in a document that an automated sync reads — the sync matches
the literal string.

## Zero padding is only on the non-clickable form

The clickable combinations were removed from the component set, so zero padding
is offered on the non-clickable form alone.

[`cell-content.md`](cell-content.md) carries the rule this produces: the web
build still accepts zero on a clickable cell content, and it must never be used
there.

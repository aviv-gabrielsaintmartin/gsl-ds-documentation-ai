_What is true of `Map template` **in Figma** and nowhere else. Layer names,
quirks, and how to work with the component in the tool._

_**This is not the usage documentation.** [`map-template.md`](map-template.md)
describes the component; this page describes the tool. Identity — keys, node IDs,
variant counts, property definitions — lives in `figma/*-registry.json` and is
never restated here._

---

## Two axis names are misspelled

| As written | Intended |
| --- | --- |
| **`Plateform`** | Platform |
| **`Very zommed / 3D`** | Very zoomed |

**Both are preserved verbatim** so a lookup by name still finds them. A sync
matching the literal string breaks if either is corrected, so anyone renaming
one should expect to update whatever reads it.

## The set's own description says to detach it

The component set carries a description that opens `===== DETACH ME ======` and
explains that templates are blueprints — set the map type, toggle the elements
off, detach, then build on top.

It is the source of the detach instruction in the usage page. **No other
component in the system carries an instruction like it.**

## Every variant is built on superseded components

**All 27 variants place components the library itself marks as outdated.**

| What | Instances | Marked in the library as |
| --- | --- | --- |
| Price pins | **81** — three per variant | `(❌ OUTDATED) mapPins` |
| Floating actions | **27** — one per variant | `❌ .base_floating_button_group (outdated)` |

**The current pin sets appear nowhere in the template.** `mapPinsV2_SL` and
`mapPinsV2_IWT` — 162 variants each, both registered — are used zero times
across all 27 variants.

_Proved by walking every variant, 22 September 2026._

**What follows for anyone placing it:** a detached copy inherits the superseded
pins and the superseded floating actions. Both have to be replaced by hand.

## The page holds the outdated pin set as well

`(❌ OUTDATED) mapPins` sits on the same page as a 112-variant set of its own.
It is deliberately excluded from the registry, and the exclusion is recorded in
the audit log — but excluding it from the registry did not stop the template
from using it.

## The map surface is its own set, mirroring the parent

`.map_background` carries the same three axes as the template and the same 27
variants. The template is a wrapper around it plus the controls, pins and card.

`.map_provider` is separate, with seven variants: Android and iOS in light and
dark, and three web forms — `Web desktop`, `Web mobile`, `Web mobile open` — in
light only.

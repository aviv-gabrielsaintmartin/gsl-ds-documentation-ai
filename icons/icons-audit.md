# Icons — the audit

_The evidence behind [icons-rules-ai.md](icons-rules-ai.md), the defective names,
and the questions only Gabriel can answer. **Never read as rules.** A generating
agent reads the ruleset and the index, never this page._

_Written 14 September 2026, from run-002's two icon findings._

---

## Why this pillar exists at all

**Proved.** Before 14 September 2026 there was **no icon documentation in this
repository**. 455 icons sat in `figma/figma-icons-registry.json` with their keys,
node IDs and variant properties, and nothing anywhere said which icon meant what,
which variant to use, or whether an icon could stand on its own.

Run-002 produced the first two findings that a rule would have caught:

| Finding | What happened | Ruled |
| --- | --- | --- |
| Nine | The right icon, the wrong variant. `info` was placed with every axis at its `Off` default, giving a bare glyph where the circled form was wanted | `ruleset gap`, 14 Sep |
| Ten | The icon stood alone as the trigger for an on-demand explanation, with no button around it | `ruleset gap`, 14 Sep |

Neither was an agent error. There was nothing to read.

---

## How the icons were measured

**Proved.** Every figure below was computed from
`figma/figma-icons-registry.json` on 14 September 2026, not estimated.

| | |
| --- | --- |
| Icons | **455 entries, 454 unique names** |
| Categories | 17 |
| The one repeat | `apple`, in **Brands** and in **Nature & Food** — the company and the fruit |
| Carry `Filled` | 442 |
| Carry `Circle` | 55 |
| Carry `Square` | 54 |
| Carry both `Circle` and `Square` | 48 |
| Rarer axes | `Triangle` on `exclamation` · `Half` on `star` · `Platform` on `location-arrow` |

**Proved.** Variant counts, which is what decides how much guidance is needed:

| Variants | Icons | What it means |
| --- | --- | --- |
| 1 | 133 | No choice at all |
| 2 | 276 | `Filled` on or off |
| 3–8 | 45 | A real decision, listed in the index |

**409 of 454 icons need no variant guidance.** That is why the variant question
is narrower than it first looked.

---

## The names are unique, and that is not the same as clean

**This corrects what was said on 14 September before the full pass was run.**
The first measurement checked uniqueness and near-collisions, found 454 unique
names and 21 near-identical pairs, and concluded the naming was in good shape
with about eight names needing a human. **Uniqueness held. Convention compliance
did not**, and a later pass found a second, larger problem.

**Proved. Fifteen names break the lowercase-kebab convention**, in three
distinct ways:

| Problem | Names |
| --- | --- |
| **Trailing whitespace** | `assistance ` · `virtual-staging ` · `two-three-dimensional-draw ` |
| **Spaces instead of hyphens** | `eye slash` · `smart fill` · `smart edit` · `smart search` · `image ai` |
| **Capital letters** | `Save` · `One` · `Two` · `Three` · `RDC` · `RER-paris` · `location-Xmark` |

**The trailing spaces are the dangerous ones.** A name ending in a space is
invisible in every rendering of it, and an agent matching `assistance` against
`assistance ` finds nothing while appearing to have looked correctly.

**Two further names are defective rather than merely non-conforming:**

| Name | Problem |
| --- | --- |
| `light-bulb` · `lightbulb` | **The same icon under two spellings.** An agent choosing by name has a coin flip, and the registry records both as real |
| `maginifying-glass-spark` | **A typo** — "maginifying". It is nonetheless the name the library holds, so it is the name that must be matched today |

**All seventeen need a Figma rename, then a `figma-sync-icons` run** so the
registry follows. Doing only the first half leaves the registry holding names
that no longer exist. On the task list as of 14 September.

---

## Near-identical pairs that are fine

**Proved.** A full pairwise comparison of all 454 names found 21 pairs above an
82% similarity threshold. **Most are legitimately distinct and need no action** —
`arrow-left` against `arrow-up-left`, `magnifying-glass-plus` against
`magnifying-glass-minus`, `double-chevron-left` against `double-chevron-right`.

Two resolve on category rather than on name, and the index says so:

| Pair | Resolved by |
| --- | --- |
| `apple` · `apple` | **Brands** is the company, **Nature & Food** is the fruit |
| `route` · `router` | **Map** against **Device & Communication** |

---

## Open questions — only Gabriel can answer these

| Question | Why it matters |
| --- | --- |
| What are `One`, `Two` and `Three`? | The only icons named as written-out numbers, and three of the fifteen that break the naming convention. Nothing suggests what they depict |
| Does `RDC` mean *rez-de-chaussée*? | **Guessing**, from the abbreviation alone. If it is the French ground floor, it belongs with `square-h` and the other property icons and needs an English-readable name |
| When is `comment` right and when is `comments`? | Both sit in **Device & Communication**, singular against plural, with nothing to choose between them |
| What is `magnifying-bars`? | Filed under **Real Estate**, away from the other magnifying glasses. The name does not describe a picture |
| What does the H in `square-h` stand for? | Hospital, helipad and something property-specific are all plausible. An agent must not pick |
| Is `power` in the right category? | A power symbol under **Furnitures**. A wrong category sends an agent to the wrong list, which is worse than a wrong name — nothing tells it to look elsewhere |
| Is `light-bulb` or `lightbulb` the current one? | Both exist. Whichever survives, the other should go |
| What are the variant axes for? | **The large one.** `Filled`, `Circle` and `Square` were added over several years for different cases and the reasoning was not recorded — Gabriel, 14 Sep. The ruleset currently tells an agent to match what is around it, which is guidance, not a rule |

---

## What was deliberately left out

| Decision | Why |
| --- | --- |
| **No Figma keys or node IDs on any icon page** | `figma/figma-icons-registry.json` is the sole source of truth for Figma identity. A copy in markdown drifts the first time `figma-sync-icons` runs. Gabriel, 14 Sep: "Keys are Figma specific" |
| **No rendered images** | 454 renders is real work, a generating agent never needs them, and a human has Figma open. The seven unresolved names are the only place a picture would help, and they are flagged in both the index and here |
| **No folder per icon** | A component folder holds prose and images. An icon has neither — a row in a table is the whole of it. 454 folders would be structure with nothing inside |
| **No theory about why the social icons carry `Square`** | Six brand icons — `instagram`, `linkedin`, `twitter`, `whatsapp`, `xing`, `youtube` — carry `Square` and not `Circle`. An earlier draft proposed this meant `Square` was a brand-tile shape. **Gabriel, 14 Sep: other icons carry `Square` too, he does not know why the social ones differ, and this is not to be theorised about.** Recorded as a fact, not explained |

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
| **Trailing whitespace** — fixed in Figma by Gabriel, 14 Sep | `assistance ` · `virtual-staging ` · `two-three-dimensional-draw ` |
| **Spaces instead of hyphens** | `eye slash` · `smart fill` · `smart edit` · `smart search` · `image ai` |
| **Capital letters** | `Save` · `One` · `Two` · `Three` · `RDC` · `RER-paris` · `location-Xmark` |

**The trailing spaces are the dangerous ones.** A name ending in a space is
invisible in every rendering of it, and an agent matching `assistance` against
`assistance ` finds nothing while appearing to have looked correctly.

**One further name is defective rather than merely non-conforming:**

| Name | Problem |
| --- | --- |
| `maginifying-glass-spark` | **A typo** — "maginifying". It is nonetheless the name the library holds, so it is the name that must be matched today |

**Thirteen still need a Figma rename, then a `figma-sync-icons` run** so the
registry follows. Doing only the first half leaves the registry holding names
that no longer exist. On the task list as of 14 September.

**Three of the fifteen were fixed the same day.** Gabriel renamed
`assistance `, `virtual-staging ` and `two-three-dimensional-draw ` by hand in
Figma on 14 September. **The registry has not been re-synced**, so it still holds
the old names and `icons/icons-index.md`, generated from it, still shows them.
A `figma-sync-icons` run is on the task list.

---

## The set appears to be Font Awesome 6, and that has not been proved

**Guessing, strongly.** On 14 September, 33 distinctive Font Awesome 6 names were
tested against the registry — `house-building`, `hot-tub-person`, `load-dock`,
`sprinkler-ceiling`, `clapperboard-play`, `magnet-diagonal`, `scale-balanced`,
`bell-concierge`, `square-h`, `circle-parking` and 23 more. **All 33 were
present. None was missing.**

A hit rate that high on names that specific is not coincidence. **It is still not
proof** — no diff against the full Font Awesome catalogue was run, and this
session had no network access to fetch one.

**What it would buy if confirmed.** Most of "which icon means what" is already
documented by Font Awesome, and only the custom real-estate additions —
`square-meter`, `three-six-zero-view`, `sold-property`, `magnifying-bars`,
`house-staging`, `RDC`, `One`/`Two`/`Three` — would need a human. That is a
handful rather than 454.

**It already answered three questions** that were otherwise going to Gabriel:
`square-h` is the hospital sign, on the same pattern as `circle-parking` being
the parking sign; `comment` and `comments` are one bubble against two; and
`lightbulb` is the Font Awesome spelling, which is what exposed `light-bulb` as a
separate icon rather than a duplicate.

**Deliberately kept out of the ruleset.** A generating agent does not need the
provenance, and an unverified one invites it to go and read Font Awesome's
documentation, importing assumptions this design system never made. The names in
the index are what an agent matches on. Verifying the hypothesis is on the task
list.

---

## Near-identical pairs that are fine

**Proved.** A full pairwise comparison of all 454 names found 21 pairs above an
82% similarity threshold. **Most are legitimately distinct and need no action** —
`arrow-left` against `arrow-up-left`, `magnifying-glass-plus` against
`magnifying-glass-minus`, `double-chevron-left` against `double-chevron-right`.

Three resolve on category rather than on name, and the index says so:

| Pair | Resolved by |
| --- | --- |
| `apple` · `apple` | **Brands** is the company, **Nature & Food** is the fruit |
| `route` · `router` | **Map** against **Device & Communication** |
| `light-bulb` · `lightbulb` | **Alert & Feedback** is an idea or a tip; **Furnitures** is a physical light |

**The lightbulb pair was recorded as a defect on 14 September and it was not
one.** The first pass called them "the same icon under two spellings" and filed a
rename. The categories disprove it: `light-bulb` sits with `info`, `exclamation`
and `question`, `lightbulb` sits with `dishwasher` and `refrigerator`. Two icons,
two jobs. **Corrected the same day, with Gabriel's go.** **What does hold:** they
are near-identical to look at, and Gabriel's view on 14 Sep is that one should go
in the long term. That is a consolidation question, not a rename.

**The lesson is about the check, not the icons.** A similarity score over names
cannot see meaning. Both times the naming was measured, the measure answered a
narrower question than the conclusion drawn from it — first *are these unique*,
then *do these look alike*.

---

## Questions asked and answered, 14 September 2026

*All of these were open when this page was written and were answered by Gabriel
the same day. The answers live in the index, where an agent reads them.*

| Question | Answer |
| --- | --- |
| Does `RDC` mean *rez-de-chaussée*? | **Yes.** The French ground floor |
| Should `file-cdd` and `file-cdi` be used outside France? | **No. France only** |
| What is `magnifying-bars`? | **A graph — a trend or data**, most likely for one classified listing on a listing page. Gabriel is unsure where it is used and offered this as his own reading, not a fact |
| Is `light-bulb` or `lightbulb` the current one? | **Both. They are different icons** — see the pairs section above |

---

## Open questions — only Gabriel can answer these

| Question | Why it matters |
| --- | --- |
| What are `One`, `Two` and `Three`? | **Asked and not answered — Gabriel does not know either, 14 Sep.** His hypothesis, stated as one: they may serve a designer-only Figma case, from a time when `Badge` offered no large enough size. The only icons named as written-out numbers, and they carry `Filled`, `Circle` and `Square`, which fits a numbered marker |
| Is the set Font Awesome 6? | **The large one, and the cheapest to settle.** If it is, ~440 of 454 names are already documented and only the custom additions need a human. 33 of 33 tested names matched. A proper diff against the catalogue would confirm or kill it |
| Is *Furnitures* the right name for that category? | It holds `dishwasher`, `microwave`, `refrigerator`, `vacuum`, `elevator` and `camera-cctv` — appliances and home equipment, not furniture. It is also not English. A wrong category name sends an agent to the wrong list, and nothing tells it to look elsewhere |
| Should `light-bulb` or `lightbulb` be retired? | Gabriel, 14 Sep: they are near-identical and one should go in the long term. Which one, and what the survivor is called, is his call |
| What are the variant axes for? | **The other large one.** `Filled`, `Circle` and `Square` were added over several years for different cases and the reasoning was not recorded — Gabriel, 14 Sep. The ruleset currently tells an agent to match what is around it, which is guidance, not a rule |

---

## What was deliberately left out

| Decision | Why |
| --- | --- |
| **No Figma keys or node IDs on any icon page** | `figma/figma-icons-registry.json` is the sole source of truth for Figma identity. A copy in markdown drifts the first time `figma-sync-icons` runs. Gabriel, 14 Sep: "Keys are Figma specific" |
| **No rendered images** | 454 renders is real work, a generating agent never needs them, and a human has Figma open. The names that do not explain themselves are the only place a picture would help, and they are answered in the index instead |
| **No folder per icon** | A component folder holds prose and images. An icon has neither — a row in a table is the whole of it. 454 folders would be structure with nothing inside |
| **No theory about why the social icons carry `Square`** | Six brand icons — `instagram`, `linkedin`, `twitter`, `whatsapp`, `xing`, `youtube` — carry `Square` and not `Circle`. An earlier draft proposed this meant `Square` was a brand-tile shape. **Gabriel, 14 Sep: other icons carry `Square` too, he does not know why the social ones differ, and this is not to be theorised about.** Recorded as a fact, not explained |

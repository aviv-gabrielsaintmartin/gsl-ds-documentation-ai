# Brief 02a — Tier parts list

| | |
| --- | --- |
| **Status** | Approved 2026-09-08, built |
| **Branch** | `docs/rule-0-parts-list` |
| **Written** | 2026-09-08 |
| **Depends on** | Nothing. No Figma access needed |
| **Blocks** | `C2 · Tier ceiling` — the check that catches the failure the ruleset itself calls the most common one |

---

## First: Block 2 should be three blocks

The plan describes Block 2 as one thing. Investigating it showed jobs with
nothing in common:

| | Job | Needs Figma? | Nature |
| --- | --- | --- | --- |
| **2a** | **Highest tier first** gains a machine-readable parts list | **No** | Hand-authored, ten rows, platform-neutral, and it needs decisions from Gabriel |
| **2b** | The registries gain structured variant properties | **Yes — live Desktop Bridge** | A schema change plus a data migration and a re-sync |

One task, one branch. **This brief covers 2a only.** 2b gets its own brief, and
can be done in either order — see the note at the end, because what I found
changes what 2b is.

---

## What this block is

`C2 · Tier ceiling` compares a locally-built element against the parts of each
**Highest tier first** row. **Highest tier first** states those parts in prose. The block turns that prose into
data — and, unavoidably, resolves what the prose actually means.

## Why it is not a transcription job

Every one of **Highest tier first**'s ten rows was checked against the four registries. **Four
rows work as written. Six do not.**

| # | **Highest tier first** row | Parts named in prose | Real inventory parts |
| --- | --- | --- | --- |
| 1 | `Listing Card` | Card · Image slider · Tag · **Price** | **3** — there is no `Price` component |
| 2 | `Listing summary` | *none named* | **0** |
| 3 | `Filter bar` | Chips · Buttons | **2** ✅ |
| 4 | `Wizard` | Tabs · Progress bar | **2** ✅ |
| 5 | `Map template` | **container** · **pins** | **0** — neither is a component |
| 6 | `Info State` | **Illustration** · **Text** · Button | **1** |
| 7 | `Estimation card` | *none named* | **0** |
| 8 | `Floor selection` | Counter field | **1** |
| 9 | `Phone Number Field` | Text field · Dropdown | **2** ✅ |
| 10 | `Table` | Cell content rows | **1** |

Two separate problems, and only the first is clerical.

**Clerical — case and plurals.** `Image slider` → `Image Slider`, `Progress bar`
→ `Progress Bar`, `Counter field` → `Counter Field`, `Text field` →
`Text Field`, `Cell content` → `Cell Content`, `Chips` → `Chip`, `Buttons` →
`Button`. A checker matching on exact inventory names fails on every one of
these today. Fixing them is unambiguous and I will just do it.

**Substantive — five named things are not components.**

| Named | What it actually is |
| --- | --- |
| `Price` | Nothing in any inventory. `Listing Card` has an internal `.listing_price_tag` slot, which is private and never selectable |
| `container` · `pins` | Descriptions, not names. The map pin sets exist as `mapPinsV2_SL` and `mapPinsV2_IWT`, but **Never select** marks both never-select |
| `Illustration` | Real, but not a component — Foundations holds 173 illustrations under a separate `illustrations` registry key |
| `Text` | Not a component. Text is a token-styled primitive, not something you instantiate |

**And three rows name exactly one part**, which contradicts **Highest tier first**'s own
operational test: *"**Highest tier first** fires when your build would need two or more of the
higher-tier component's own moving parts. One part alone is the lighter case, and
**Which component** wins."*

Read literally, `Floor selection`, `Table` and `Info State` can never trigger
**Highest tier first**. That is a real tension in the ruleset, and the component eval did not
catch it because no test intent probed those three.

## What changes

- **Highest tier first**'s table gains a **Parts** column, holding exact inventory names.
- Where a part is not a component, the row says so explicitly rather than naming
  something a checker will fail to find.
- Where a row has fewer than two identifiable parts, it is marked **not
  machine-checkable**, and `C2 · Tier ceiling` skips it rather than silently
  passing it.
- `components-audit.md` records the evidence and each decision.
- `compliance-scorecard.md`'s "dependency, not yet satisfied" note becomes a
  statement of which rows the check covers and which it cannot.
- `components-eval.md` gains intents for the three one-part rows, since the
  existing 27 never probed them.

## What deliberately does not change

- **No parts are invented.** `components-audit.md` already rejected exactly this:
  *"Guessing here would put inferred content into a ruleset that agents treat as
  authoritative."* A row whose parts nobody can name stays unchecked and says so.
- **Highest tier first's routing is untouched.** Every row keeps pointing at the same
  component. This block makes the rows checkable, not different.
- **The count-the-parts threshold stays at two.** Lowering it to one to rescue
  three rows would make `Chip group` a **Highest tier first** violation of `Filter bar`, which
  the ruleset explicitly says it is not.
- **No Figma access, no registry edits.** That is 2b.

## How we'll know it worked

| Test | Passes if |
| --- | --- |
| **Exact-match test** | Every name in the Parts column appears verbatim in a registry. Checked by script, not by eye |
| **Coverage test** | The scorecard states how many of the ten rows `C2 · Tier ceiling` covers, and names the ones it does not |
| **No-invention test** | Every part is traceable to prose that was already there, or to a decision Gabriel made in this block |
| **Eval test** | The three one-part rows get eval intents, and the ruleset answers them consistently — whatever the answer turns out to be |

## Decisions I need from you

Answered by Gabriel, 2026-09-08. His answers reframed the problem: the six
"broken" rows are not under-documented, they are **not parts-composed things**.

| # | Question | Decided |
| --- | --- | --- |
| 1 | Is `Price` a component, or the internal slot? | **The internal slot.** Dropped. `Card` · `Image Slider` · `Tag` clear the threshold anyway |
| 2 | What are `Map template`'s parts? | **None — it is all-or-nothing.** *"Full usage or nothing or almost. A designer could need a pin as illustration but will find other solutions."* No partial build exists to detect |
| 3 | Is an illustration a part of `Info State`? | **The question was wrong.** `Info State` is *"more a content component like a modal with specific content inside"* — a container, not an assembly. Reclassified rather than given parts |
| 4 | `Floor selection` and `Table` — really **Highest tier first** cases? | **`Table` yes, and it is Figma-only** — *"not even dev, only figma"*, confirmed by its own doc: Figma Ready, Web In progress. Classified as a container. **`Floor selection` unanswered** → left unresolved and recorded as open question 11 |
| 5 | `Listing summary` and `Estimation card` — mark unchecked? | **Agreed.** Both are `⚠︎ Undescribed` in **The inventory** |
| 6 | Can a never-select component count as a part? | **Yes.** **Never select** governs what an agent may *choose*; the Parts column describes what an imitation *contains* |

### A follow-up, and a correction

Gabriel then set the platform policy: *"Components existing on a platform should
be used on it. Figma first. When working on web or android, we will work on the
status and synchronisation."*

Acting on it exposed an error in this block's own first pass. The claim *"46 of
52 docs say Figma-ready, so six components are not"* was wrong: all six
non-Ready Figma cells are data-quality problems — three `Not documented`, two
holding a link instead of a status, one `To Do` — and **every one of those
components is in a registry, verified live in Figma.**

The conclusion inverts. **Figma generation has no availability constraint**, and
the doc's Figma cell is a drifted duplicate of the registries. **Platform limits** now states
the policy and names a source of truth per platform instead of tabulating
readiness.

## Risks

| Risk | Mitigation |
| --- | --- |
| **Inventing parts to make the check work.** The strongest temptation here, and the one the audit already ruled out | The no-invention test. A row with no nameable parts is marked unchecked, and the scorecard reports reduced coverage rather than false confidence |
| **`C2 · Tier ceiling` looks complete when it covers 4 rows of 10** | The scorecard must state coverage explicitly — which rows are checked and which are not |
| **Fixing the one-part rows by lowering the threshold** | Explicitly out of scope above. It would break the **Highest tier first** / **Which component** boundary the eval spent three runs getting right |

## Cost

Half a day, most of it waiting on the six decisions. The clerical fixes are
minutes.

## What this changed about Block 2b · Registry properties

The skill is not the problem. `figma-sync-component-sets` **already** says to
capture parent property definitions and to store exposed slots' properties
*"structured … not prose — an agent needs to query it, not read it"*.

The gap is that the **registry schema has no field for them**. The schema in
`.claude/rules/figma-registries.md` is `key · nodeId · pattern · variantCount ·
auditedDate · status`, so parent property definitions had nowhere to go and
ended up inside `status` as prose for 18 entries, and nowhere at all for the
Components tier.

So 2b is a **schema change plus a migration**, not a skill rewrite: add the
field, move the prose into it where it exists, then re-sync the Components tier
against live Figma. That is a materially different job from what the plan says,
and it needs its own brief.

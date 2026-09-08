# Brief 02d — Rule names

| | |
| --- | --- |
| **Status** | Approved 2026-09-08, built |
| **Branch** | `docs/rule-names` |
| **Written** | 2026-09-08, retroactively — the two design questions were settled before any file was touched |
| **Depends on** | Nothing |
| **Blocks** | Nothing, but cheaper now than after **Block 4 · Figma agent** references these rules from another repo |

---

## What this block is

The four rulesets numbered their rules. The numbers are gone; every rule now has
a name.

## Why

Gabriel: *"I want to change the name Rule 0. It's not understandable and has the
same issue as 2a, 2b. Maybe understandable for AI but not for human. I don't even
know how to explain."*

Two problems, and the second is worse than the one raised.

**The number carried no meaning.** Six numbers to memorise, in a repo that had
just banned bare identifiers for blocks and compliance checks. The rule against
it existed; the rules themselves were the one place it had not been applied.

**The same number meant four different things.** This is the part that made
sentences genuinely unresolvable rather than merely unmemorable:

| Ruleset | What its `Rule 5` said |
| --- | --- |
| components | When nothing fits |
| colour | Content covers text *and* icons |
| spacing | Start from what components actually use |
| typography | Do not use Display |

A sentence containing "Rule 5" could not be understood without knowing which
file it came from. Same for `Rule 0`, `Rule 2` and `Rule 3`.

**And the name already existed.** Every heading read `## Rule 0 — Reach for the
highest tier that fits`. The name was right there; references threw it away.

## The two design decisions

| Question | Decided |
| --- | --- |
| Names only, or number **and** name? | **Names only.** The number looked like it encoded precedence, but precedence is already stated explicitly in a five-step ladder — so the number carried nothing that was not written down elsewhere |
| Which rulesets? | **All four.** Renaming components alone would have left `Rule 5` still meaning four different things, so the ambiguity would have survived |

## What changed

- **Headings** become the short name, with the original descriptive sentence
  kept immediately beneath it in italics. Nothing was lost.
- **The components ruleset gains a precedence table** at the top — six rules,
  each with the question it decides. That table now carries the ordering the
  numbers used to imply.
- **All 287 references** across the repo were rewritten.
- **The three token rulesets' first rule turned out to be the same rule**, so it
  gets the same name — **Components first** — with a line in each noting that the
  other two open the same way. Numbering had hidden that they were identical.
- **`.claude/rules/project.md`** extends the bare-identifier rule to cover all
  three kinds of identifier, and records that rules deliberately have no numbers.

Two things fixed in passing:

- **`Block 2a` was named after the old rule.** It is now
  **Block 2a · Tier parts list**, and its brief file was renamed to match.
- **A pre-existing broken table cell in `alert.md`** — a stray `**` from the bulk
  doc enrichment two PRs ago, rendering `| **On web | **Modal bottom sheet…`.

## What deliberately does not change

- **No rule's content changes.** This is naming only. Every rule says exactly
  what it said before, decides exactly what it decided, and sits in the same
  precedence position.
- **No new rule, no merged rule.** The three token rulesets' shared first rule
  gets a shared *name*; it is not restructured into one rule referenced from
  three places. That was offered and not chosen.

## How we'll know it worked

| Test | Result |
| --- | --- |
| No `Rule <number>` anywhere in the repo | **0 occurrences** |
| Every part name in **Highest tier first** still resolves against a registry | **10 rows, 0 unresolved** |
| **The inventory** still complete | **98 rows, 0 invented** |
| Relative links | **453 checked, 0 broken** |
| No bare block references or check codes | **0**, excluding the rule's own counter-examples |
| **The explain test** | Gabriel can say what a rule decides from its name alone, without opening the file |

The last one is the only one that matters, and it is the reason the block exists.

## What went wrong while building it

Recorded because it is the kind of mistake worth not repeating.

The first pass applied the **component** rule names to *every* `Rule N` in the
mixed files — `compliance/`, `project/`, `.claude/rules/` — which silently
corrupted references to *token* rules. `compliance-audit.md` ended up claiming
typography's rule was **Never select**, and the scorecard claimed the Display
family was forbidden by **When nothing fits**.

Caught by grepping for every line that named a token ruleset and checking its
rule names were token names. The mixed files were reverted with
`git checkout HEAD --` and redone with an explicit list for token references
first, then component names for the remainder.

A second, smaller version of the same mistake: bulk-wrapping names in `**bold**`
produced nested bold wherever the original was already bold. Fixed by making the
substitution bold-aware — parse each paragraph's bold spans, and emit the name
plain when it already sits inside one.

**The lesson: a repo-wide identifier rename is not one substitution.** Any file
that references more than one ruleset needs a per-reference decision, and a
blind map will produce confident, wrong documentation.

## How the rename was verified

"Are you sure of the changes applied?" was the right question — the first round
of checks was structural and proved nothing about whether each name was the
*right* name. Three further checks were run, and each found something.

| Check | What it found |
| --- | --- |
| **Every rule kept its description, in order** — the old `## Rule N — <text>` sequence compared against the new `## Name` + descriptor sequence | Confirmed all 30 rules across four rulesets. Also caught that the "same rule" note had been inserted *above* each token ruleset's descriptor rather than below it |
| **Old-versus-new for every cross-file reference**, printed side by side | Caught the identifier rule's own example table, which had become self-contradictory: *"write **Highest tier first**, not **Highest tier first**"* |
| **Name against sentence context** — does a line mentioning typography carry a components rule name? | Caught nothing new, having already caught the corrupted token references by hand earlier |

A fourth round, run after Gabriel asked whether the changes were certain, found
the worst damage yet:

| Check | What it found |
| --- | --- |
| **Anchor links** — headings changed, so `#fragment` targets may be dead | **5 dead anchors**: two in the audit pointing at the old component-rule headings, three inside the colour ruleset pointing at its own old heading |
| **Precedence table against page order** | The new table lists **Platform limits** before **Which component** — correct for precedence, but the page presents them the other way round. A clause now says so explicitly |
| **Bold spans crossing a table cell boundary** — by marker parity, not regex | **3 corrupted rows.** The nested-bold collapse had merged `**not**` and `**never**` into the *following* table cell in eval intents 8 and 17, and dropped a closing `**` in the audit's kind table. Real content damage, invisible to every earlier check |

A fifth pass fixed readability rather than correctness: `**Never select**'s
never-select list`, `**Which Which component** problem`, `4 of Highest tier
first's 10 rows`, and seven bare compliance-check codes in prose that the naming
rule already forbade.

**The structural checks would all have passed on a wrong rename**, and did.
Zero occurrences of `Rule <number>` says the substitution happened, not that it
was correct — and says nothing at all about bold markers merging across a table
cell.

Three lessons, in order of how expensive they were:

1. **A rename is not verified by the absence of the old name.** Only an
   old-versus-new comparison establishes that each new name is the right one.
2. **Bulk formatting changes damage tables silently.** Markdown bold is a toggle,
   so a merged pair reads as valid syntax and renders as garbage. Check by marker
   parity per row, never by regex.
3. **Renaming a heading breaks every anchor pointing at it.** Nothing warns you.

## Cost

Half a day, most of it recovering from the bad first pass. The recurring cost is
zero — names do not drift the way numbers did.

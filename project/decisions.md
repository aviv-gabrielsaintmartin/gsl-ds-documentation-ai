# Decision log

_Why this project is shaped the way it is. Newest first._

**What belongs here:** a decision that would be expensive to reverse, or that
someone would otherwise ask "why is it like this?" about. Not a changelog — the
git history already does that.

**Format:** what was decided, why, and what it costs. The cost line matters. A
decision with no downside recorded is usually a decision that wasn't examined.

---

## 2026-09-08 · `README.md` and `project/` are human-first

**Decided.** Two places in this repo are written for people, not machines:
`README.md` and everything under `project/`. A rule file enforces it.

**Why.** Every other document here is deliberately optimised for unambiguous
machine parsing, because the primary reader is an agent. That works, and it also
makes the repo hard for its own owner to explain to someone else. When an AI
builds most of the content, the human needs one honest map that says what does
what and where — otherwise ownership quietly becomes unmaintainable.

**Cost.** A second surface to keep current, and it will drift if nothing forces
it. Mitigated by the block ritual: a block isn't done until its brief and its
decision entry exist.

---

## 2026-09-08 · Compliance is machine-scored; quality stays human

**Decided.** Design-system compliance will be scored automatically against a
fixed scorecard. Design quality stays Gabriel's judgment, undocumented, for the
End Sept 2026 milestone.

**Why.** They are different kinds of question. "Is every fill bound to an
authorised token?" is arithmetic. "Does this screen feel like SeLoger?" is not.
Mixing them produces a score nobody trusts. Separating them means the compliance
gate can run unattended today, while the quality bar gets written down later
from a corpus of real judgments rather than from scratch.

**Cost.** For now the loop can produce output that scores 100% compliant and
still looks wrong. That's accepted, and it's exactly why quality verdicts get
logged on every run — so there's evidence to write the quality bar from.

---

## 2026-09-08 · The generating agent lives outside this repo

**Decided.** The Figma design agent is a skill in the existing shared skills
repo. This repo stays the knowledge base and never contains a generating agent.

**Why.** Two reasons, and the second is the real one. It's the easiest thing to
set up, and the shared skills repo is where skills already live. More
importantly, physical separation keeps the contract honest: if the agent needs
something that isn't in a `*-rules-ai.md` file, it can't quietly read a token
page or an audit instead. It fails, and the failure is visible as a
knowledge-base defect.

**Cost.** Two repos to keep in step, and a change to the contract means a change
in two places.

---

## 2026-09-08 · `layout/` becomes a third pillar

**Decided.** Page composition gets its own top-level folder, `layout/`, as a
peer of `tokens/` and `components/` — not a token category.

**Why.** It spans grid, spacing and breakpoints, so it doesn't belong inside any
one of them. And it's the third of the three decisions an agent makes when it
turns a wireframe into a screen; the other two each have a home already.

The initial estimate — that this would be the largest piece of work in the plan
— was wrong. Most of a layout ruleset already exists, scattered: page-rhythm
spacing is verified in `spacing-rules-ai.md` Rule 3 with zero violations across
60 component files, containment is verified in Rule 4, and `Grid/Margin`,
`Grid/Gutter` and the derived column widths are all verified against
`grids.json` for all seven tiers. Six of nine pieces assemble from data that has
already been checked.

**Cost.** Two pieces genuinely have no evidence yet — *which* page-rhythm token
to use for a given gap, and column spans. Neither can come from the component
library, because page rhythm lives in product code. They need a small audit of
3–5 real product screens, which is a dependency on Gabriel naming them.

---

## 2026-09-08 · Components get the same rules / audit / eval split as tokens

**Decided.** `components-rules-ai.md`, `components-audit.md` and
`components-eval.md`, mirroring what `tokens/` already does. Merged as PR #17.

**Why.** `components.md` was an index, and an index can't be a contract. It
offered all 98 registry entries as equally valid choices, including `Status Bar`,
`Favicon` and `Programmatic Ads`, and it gave the Experiences tier no routing at
all — so an agent would compose a property card from `Card` + `Image Slider` +
`Tag` while `Listing Card` sat unused one tier up.

**The eval turned out to be the most valuable of the three.** A cold agent given
only the ruleset scored 22/22 on the first run — and that perfect score hid four
real defects, which surfaced only because the agent was also asked where it had
struggled. Twelve defects were found and fixed across three runs. The lesson,
written into the eval itself: **every miss is a defect in the ruleset, not in the
agent**, and a perfect score reached by forcing an answer is not a working
ruleset.

**Cost.** A fourth file per pillar to keep in step. Accepted, because the eval
is what makes the ruleset trustworthy rather than merely plausible.

---

## 2026-09-08 · The filename suffix is the contract vocabulary

**Decided.** Five suffixes — `-tokens`, `-rules-ai`, `-audit`, `-ledger`,
`-eval` — and every file's suffix says what it is and whether it may be read as
rules. Documented in `README.md`.

**Why.** It already existed as a convention and was documented only inside
`tokens/README.md`. Promoted to the root because it answers "what does what"
from the filename alone, for a human and an agent equally.

At the same time `component-selection-audit.md` and `component-selection-eval.md`
were renamed to `components-audit.md` and `components-eval.md`, so the grammar is
`<pillar>-<suffix>` with no exceptions. Done while both files were still
untracked, so it cost nothing.

**Cost.** Two known inconsistencies remain: token audits are `-usage-audit.md`
while the component audit is `-audit.md`, and ledgers have an uncommitted `.json`
twin. Both are documented rather than fixed — renaming seven token files would
churn history for cosmetics.

---

## 2026-09-07 · Instructions split into path-scoped layers

**Decided.** `CLAUDE.md` holds only what's true about the whole repo. Anything
folder-specific moved to `.claude/rules/`, which loads only when an agent opens
a file in the matching folder. Commit `8fe71b0`, PR #16.

**Why.** One instruction file for everything meant every session paid for
Figma-registry detail while editing a token page.

**Cost.** One real trap, verified: a rule loads on **Read / Edit / Write** of a
matching path, but **not** on `cat`, `sed`, `head` or `grep`. An agent that
opens its first file in a folder with a shell command works without that
folder's rule and won't know it.

---

## 2026-09-04 · Every token category audited against real component usage

**Decided.** No token page ships on its stated values alone; each is checked
against what the design-system code actually binds. Commit `884fcf3`, PR #14.

**Why.** A token existing is not evidence that it should be used. The audits
found orphans throughout — `Shadow/24` and `Shadow/32` with no consumer, only 3
of 11 opacity tokens in use, 6 dead sizing tokens, `Motion/500ms` unused — and
found that no component references the column grid at all.

**Cost.** The evidence goes stale as the code moves. Mitigated by
`tokens/scripts/`, four read-only Python scripts that regenerate the ledgers on
demand.

---

## 2026-08-26 · The Figma registries stopped publishing to Confluence

**Decided.** The four `figma-sync-*` skills neither read nor write Confluence.
The `figma/*-registry.json` files are their only source of truth.

**Why.** The published output was only ever consumed by AI agents. No human read
it, so publishing it was token cost with no audience.

**Cost.** Figma identity data is no longer browsable by anyone without repo
access. Accepted — that data is machine input, not documentation.

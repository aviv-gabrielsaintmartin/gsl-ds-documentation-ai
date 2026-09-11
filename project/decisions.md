# Decision log

_Why this project is shaped the way it is. Newest first._

**What belongs here:** a decision that would be expensive to reverse, or that
someone would otherwise ask "why is it like this?" about. Not a changelog — the
git history already does that.

**Format:** what was decided, why, and what it costs. The cost line matters. A
decision with no downside recorded is usually a decision that wasn't examined.

---

## 2026-09-11 · Graphify is retired, and the graph lives outside the repo

**Decided.** The knowledge graph is no longer refreshed as part of the task
loop. `graphify-out/` and `.graphifyignore` moved to
`~/Desktop/ai/gsl-ds-graphify-archive/`, with a README there explaining what it
is. `CLAUDE.md` gains a working convention saying not to rebuild it — the skill
is installed globally and will otherwise offer itself to a future session as if
nobody had got round to setting it up.

**Why.** Measured rather than assumed: 990,970 tokens spent to build and
maintain a graph over a corpus of 172,818 words. That is **4.2× what reading the
entire knowledge base costs**, for something queried exactly once — by the
session that built it. A targeted `grep` answers the same kind of question for
about 220 tokens. And the repo is already hand-indexed: the filename suffix says
what each file is, `tokens-index.md` and `components-index.md` route, and
`CLAUDE.md` carries a where-to-look table. That index beats a graph here because
Gabriel can read it too.

The deciding argument was this project's own test — that an agent should be able
to build a compliant interface from these documents alone. If an agent needs a
semantic graph to find its way around them, the documents have failed that test,
and the graph is hiding the failure rather than fixing it.

**Cost.** Cross-file inconsistencies that only surface when everything is read
at once are no longer caught automatically. This is not hypothetical: the one
graph run that was completed found that `color-rules-ai.md` still says the audit
claims 83 orphaned tokens, when the audit has since been corrected to 73. That
kind of drift now has to be caught by a targeted check or by noticing it.
Accepted, because a check that costs 10,000–30,000 tokens per task to catch a
defect a `grep` finds for 200 is the wrong trade.

**Not decided.** Graphify stays installed globally and stays in Gabriel's
personal `~/.claude/CLAUDE.md`. This decision is about a small, hand-indexed
corpus; a large unstructured codebase is exactly where the tool would pay.

## 2026-09-08 · **Highest tier first** has two kinds of row, and only one is countable

**Decided.** **Highest tier first**'s table gains a machine-readable **Parts** column and a
**Kind** column. `C2 · Tier ceiling` covers the composed kind — four rows of ten
— and reports the other six as skipped.

**Why the split exists at all.** Turning **Highest tier first**'s prose into data was supposed
to be transcription. It wasn't. Every part name failed an exact match against
the registries on case or plurals, five named things were not components at all
(`Price`, `container`, `pins`, `Illustration`, `Text`), and three rows named
exactly one part — which contradicts **Highest tier first**'s own test of *two or more moving
parts*. Read literally, those three could never fire the rule they belong to.

**Gabriel's answers reframed the problem better than the question did.** They
are not under-documented rows. They are **not parts-composed things**:

| Kind | Rows | Countable? |
| --- | --- | --- |
| Composed | `Listing Card` · `Filter bar` · `Wizard` · `Phone Number Field` | **yes** |
| Container — a shell you place content into | `Info State` · `Table` | no |
| All-or-nothing — *"full usage or nothing"* | `Map template` | no |
| Unresolved | `Floor selection` · `Listing summary` · `Estimation card` | no |

His words on the two that mattered: `Map template` is *"full usage or nothing or
almost — a designer could need a pin as illustration but will find other
solutions"*, and `Info State` is *"more a content component like a modal with
specific content inside"*. Neither is assembled, so neither can be caught by
counting what it was assembled from.

**Cost, stated plainly.** **Highest tier first** governs all ten rows; the checker enforces four.
And **detecting a rebuilt container is unsolved** — nothing catches an agent that
hand-builds an empty state instead of using `Info State`. That needs a
non-parts-based mechanism, and none is designed. Recorded rather than papered
over, because the alternative was inventing parts lists — which
`components-audit.md` had already rejected as *"inferred content in a ruleset
agents treat as authoritative"*.

---

## 2026-09-08 · The rulesets' rules have names, not numbers

**Decided.** Gabriel: *"I want to change the name Rule 0. It's not
understandable... Maybe understandable for AI but not for human. I don't even
know how to explain."*

All four rulesets lose their rule numbers. Every rule is now a name —
**Highest tier first**, **Never select**, **No raw colour**, **Page rhythm**.

**Why, beyond memorability.** The number was ambiguous, not just opaque. `Rule 5`
meant *when nothing fits* in components, *content covers text and icons* in
colour, *start from what components actually use* in spacing, and *do not use
Display* in typography. A sentence containing "Rule 5" could not be resolved
without knowing which file it came from.

And the name already existed: every heading read `## Rule 0 — Reach for the
highest tier that fits`. References simply threw it away.

**Why names only, with no number kept.** The number looked like it encoded
precedence. It did not — precedence is stated explicitly in a five-step ladder,
so the number carried nothing that was not already written down. The components
ruleset now opens with a table of the six rules and the question each decides,
which is what the numbering was gesturing at.

**A finding the rename surfaced.** All three token rulesets' first rule is the
*same rule* — "use a component, it carries its own colour / spacing / type". They
now share the name **Components first**. Numbering had hidden that they were
identical.

**Cost.** 287 references rewritten. And a real mistake along the way: the first
pass applied component rule names to *every* numbered reference in the files that
cite more than one ruleset, so `compliance-audit.md` briefly claimed typography's
rule was **Never select**. Caught by checking every line that names a token
ruleset, reverted, and redone with explicit per-reference mapping.

**The lesson, recorded because it will recur:** a repo-wide identifier rename is
not one substitution. Any file citing more than one ruleset needs a
per-reference decision, and a blind map produces confident, wrong documentation.

---

## 2026-09-08 · Use a component where it exists; the registry is authority for Figma

**Decided.** Gabriel: *"Components existing on a platform should be used on it.
Figma first. When working on web or android, we will work on the status and
synchronisation."*

**Platform limits** now states that policy and names a source of truth per platform, rather
than duplicating readiness data into the ruleset.

| Target | Source of truth | State |
| --- | --- | --- |
| **Figma** | `figma/*-registry.json`, verified live | **All 98 exist. No constraint** |
| Web · iOS · Android | the component's own doc | hand-maintained free text |

**A correction, made the same day.** The first reading of this was *"46 of 52
docs say Figma-ready, so six components are not"*. That was wrong. All six
non-Ready Figma cells are data-quality problems — three say `Not documented`,
two hold a link instead of a status, one says `To Do` — and **every one of those
components is in a registry, verified live in Figma.** Snackbar's doc even links
to its Figma node two lines under the cell that says it is undocumented.

So the doc's Figma cell is a hand-maintained duplicate that drifted, and the
conclusion inverts: the Figma agent has **no availability constraint at all**.

**Where availability data belongs**, since Gabriel asked whether it was a doc or
a skill concern:

- **Figma existence → the registries.** Machine-verifiable, verified live,
  complete, and it changes when Figma changes rather than when someone edits a
  doc.
- **Web and native existence → the component's own doc.** Nothing here can
  verify it, so a human record is the only option.
- **The rule → Platform limits.** It is a rule, not data. Duplicating 52 × 4 values into
  the ruleset would create a second source of truth — which is precisely how the
  Figma column drifted in the first place.

And the principle behind the question: **a skill reads docs and writes
registries. A skill is never a source of truth for knowledge.**

**Cost.** Web and native availability stays unruled. And its first job is not
reconciliation but a **controlled vocabulary**: the docs say `Ready`, `To Do`,
`To-do`, `WIP`, `In progress`, `Partially available`, `N/A`, `Non-gemini
component`, a bare link, or `Not documented` — 11 cells hold no status at all.
Nothing can be ruled on until those mean fixed things. **Block 2c · Platform
availability**.

---

## 2026-09-08 · The scorecard is platform-neutral; the checkers are not

**Decided.** `compliance/compliance-scorecard.md` defines *what* compliance is
and *what* to measure. It never defines *how* a tool measures it. Each platform
implements an **adapter** — in the consuming agent's repo, not here.

**Why.** The first draft got this wrong. Its measurement rows named Figma's
plugin API directly and its report format printed Figma node identifiers, which
made it a Figma checker specification sitting in a repo whose whole purpose is
one platform-neutral truth that several agents consume.

The fix is an **adapter contract**: the scorecard lists the *facts* a platform
must report — is this element a library component, is this property token-bound,
which token — and the checks operate on those facts. A data requirement is
platform-neutral; an API call is not.

It improved the design rather than just moving code. Neutral vocabulary turned
out to state the rules better than the mechanism did, and separating the layers
exposed that platforms answer *different questions*: Figma says "this is an
instance of a library component", web says "this is an import from the
design-system package". So facts are split into **required** and **optional**,
and a check whose facts a platform cannot supply reports `unavailable` — never
`0%`, which would blame the output for a gap in the adapter.

**Made concrete the same day**, after Gabriel asked how an adapter actually
works and whether it was documented. It was not — the contract listed the facts
and stopped. The scorecard now also carries what an adapter *is* (a translator
containing no rules), the five-step pipeline, a who-owns-what split, a JSON
example of the fact shape, and a worked example showing two elements going in and
each check's verdict coming out.

One subtlety that specification settled: **an omitted field means `unavailable`;
`false` means "no"**. Conflating them would let a gap in an adapter read as a
compliance failure.

**Cost.** The scorecard can no longer be executed by reading it. It needs an
adapter before it does anything at all. And the shape is specified without ever
having been built against, so the first adapter will probably revise it.

---

## 2026-09-08 · Identifiers are always written with their names

**Decided.** `C1 · Provenance`, never bare `C1`. In documents, reports, ledgers
and conversation.

**Why.** Gabriel's words: *"Not possible to remember all of them."* Six
two-character codes are not memorable, and a report using them can only be read
by its author. The first draft of the scorecard used bare codes throughout, and
so did the conversation that produced it.

**Cost.** A few characters per mention, and a habit to maintain. Recorded as a
rule in `.claude/rules/compliance.md` and `.claude/rules/project.md` rather than
left as a preference, because preferences decay.

---

## 2026-09-08 · Compliance gets its own pillar, and a sixth suffix

**Decided.** A `compliance/` folder, peer to `tokens/` and `components/`, holding
`compliance-scorecard.md`, `compliance-audit.md` and `compliance-flag-ledger.md`.
`-scorecard` joins the filename grammar as a sixth suffix.

**Why a new suffix rather than reusing `-eval`.** `-eval` means *the check on a
ruleset* — `components-eval.md` asks whether an agent reading the ruleset reaches
the right answer. The scorecard checks *generated output*, a different subject.
Reusing `-eval` would blur the one distinction the grammar exists to make.

**Four scoring decisions, all Gabriel's**, and two of them improved on the
recommendation:

| Question | Decided | Note |
| --- | --- | --- |
| Does a hard fail sink the run? | **Its own check only.** Extend later | A run-level gate on an unproven checker discards a whole run's data on one false positive. Mitigated by format: hard fails print above any percentage |
| Unauthorised tokens — fail or flag? | **Flag, and treat flags as findings** | The better reason. Flags now accumulate in a ledger; a subject seen three times is promoted to a ruleset defect |
| Is `C2 · Tier ceiling` machine-detectable? | **Yes, it must be** | Right, but not from the registries — `Listing Card`'s recorded sub-components are private internal slots, not the public parts an imitation would contain. Needs a parts column on **Highest tier first**'s ten rows |
| Thresholds now or later? | **Now** | Refined: derived from rules, never invented. `C3 = 100%` because "never write a pixel literal" says so. Where no rule states a number, the threshold is no-regression |

**Cost.** The scorecard can be enforced only as far as the rulesets are
verified. `C6 · Layout` ships defined and switched off, and `C2 · Tier ceiling`
cannot run until
**Block 2a · Tier parts list** makes **Highest tier first**'s parts machine-readable. Both are
stated in the scorecard
rather than quietly unmeasured.

---

## 2026-09-08 · Block 3 · Layout is verification, not authoring

**Decided.** `layout/` verifies page-composition rules that already exist, rather
than writing them from nothing.

**Why.** The earlier scoping was wrong. spacing's **Page rhythm** already
gives outer margin, section gap, card-grid gap and form-field gap for every
viewport tier, and **Container padding** gives it — but both carry an explicit
warning that they are **unverified**, because page composition lives outside the
component library and could not be checked against it.

So the work is confirming documented intent against real product screens, not
inventing rules. The two genuine gaps that remain are column spans and page
anatomy.

**Cost.** Same dependency as before — Gabriel naming 3–5 real product screens —
but a cheaper job and a stronger result, since the output will be verified rather
than newly asserted.

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

## 2026-09-08 · `layout/` becomes its own pillar

**Decided.** Page composition gets its own top-level folder, `layout/`, as a
peer of `tokens/` and `components/` — not a token category.

**Superseded in part** by the later entry above: this block turned out to be
verification of existing rules rather than authoring new ones.

**Why.** It spans grid, spacing and breakpoints, so it doesn't belong inside any
one of them. And it's the third of the three decisions an agent makes when it
turns a wireframe into a screen; the other two each have a home already.

The initial estimate — that this would be the largest piece of work in the plan
— was wrong. Most of a layout ruleset already exists, scattered: page-rhythm
page-rhythm spacing is verified by spacing's **Component spacing stops at 32**, zero violations across
60 component files, containment is verified in **Containment**, and `Grid/Margin`,
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

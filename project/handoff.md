# Handoff — 2026-09-09

_Written because the next stretch of work continues on a different Claude
account, in a fresh session with no conversation history. Everything a new
session needs that is **not already in the repo** is here._

**Read first:** [README.md](../README.md) for the map, then
[plan.md](plan.md) for where we are, then [decisions.md](decisions.md) for why.
This file only covers what those don't yet say.

---

## Where things stand

| | |
| --- | --- |
| `main` | `bc97f23` |
| Working branch | `audit/run-001`, off current `main` |
| Merged so far | PRs #17–#22 |
| Pillars | `tokens/` · `components/` · `compliance/` · `figma/` · `project/` |

An agent can now be told, from documentation alone: which component, which
variant of it, which tokens are authorised, where it may be used, and how its
output will be judged.

## Run 001 — the first real test, and it is not yet recorded

A separate session ran the Block 4 loop at zero cost, before any adapter or
checker exists. **Its findings are in this file and nowhere else** — the
scorecard's run log is still empty and the flag ledger has no rows. Recording it
is the first job.

### Method

Two mock images from a SeLoger classified detail page were turned into a
**content-only prompt** — objectives, real copy, dynamic-data placeholders, and
deliberately **no component names, no token names, no pixel or hex values**. The
point was to leave component selection genuinely open; a wireframe in
design-system vocabulary would have pre-answered it.

That prompt went to a **cold subagent** with no conversation history, restricted
to the four rulesets and the seven `figma/*.json` registries. It was forbidden
`compliance/` (it would have optimised to the test), `project/`, the token
*pages*, and one specific Figma node — a human-built version of the same block,
which would have turned selection into transcription.

Evidence is in [`compliance/runs/run-001/`](../compliance/runs/run-001/) —
the prompt and both output screenshots, rescued from a job scratch directory
that has since been deleted.

Output lives in Figma file `kik7hPMCvylSCY5qSah656`, page
`Run 001 - content prompt`, frames `59:4893` and `59:4894`.

### What worked

- **~33 library instances against 3 declared local components.** Every component
  key resolved from the registries. Nothing invented, nothing from the
  never-select list.
- **Token binding held**: 0 raw fills, 0 raw strokes, 0 unbound spacing or radius,
  0 text without a text style. Two literals, both declared.
- **`When nothing fits` was used exactly as designed.** It rejected `Badge` for a
  footnote marker by citing Badge's own anchoring test, and `Tag` by citing Tag's
  standalone test. The structural tests three eval rounds produced were used
  correctly by an agent that had never seen the reasoning.
- It reached for `Cell Content` + `Divider` for both list-shaped blocks, where
  hand-building rows was the predicted failure.

**Calibration:** the human-built version of the same block would not score 100%
either — three outdated instances and a legend hand-built from raw rectangles.

### What broke — five root causes

Ranked by consequence. Every claim marked **verified** was checked against the
files in this repo; the rest are the test session's live-Figma observations.

**① An agent cannot put text into a GSL component from the documentation alone.**
Not one component it used exposes a text property. `Cell Content`, `KPI`,
`Button`, `Text Field`, `Dropdown`, `Donut chart` are fillable only by overriding
nested text nodes whose names (`Title`, `Body`, `Suffix`,
`Total-container > Label|Value`) appear in no ruleset and no registry. Every
string in the output came from a live Figma read, not from the repo.
**Verified**: `figma-components-registry.json` records `variantCount` but property
definitions for only 1 of 61 entries.

**② Nine token categories have no contract.** **Verified**: only colour, spacing
and typography have a `-rules-ai.md`. Radius, shadow, border-width, sizing,
opacity, motion, z-index, grid and breakpoint have pages an agent is forbidden to
read, and no ruleset anywhere mentions `Radius/4`. The agent picked radius **by
taste** and applied **no shadow at all**, because nothing states whether a
set-apart card is elevated. `C3 · Token binding` is unenforceable in those
categories — there is no contract to check against.

**③ The colour ruleset routes DPE data to a family it forbids.** **Verified at
both lines**: `color-rules-ai.md:57` routes DPE / CO₂ domain data to `Scale/*`
while the same cell says "external team only, see Never use", and
`color-rules-ai.md:287` lists `Scale/*` as having no GSL consumer. No 7-step
scale component exists — `Energy tag` is a single-grade badge. The prompt
required a 7-step best-to-worst scale, so the most legally prominent element on a
French property listing is documented into a dead end, with no fallback stated.
The agent shipped a monochrome ladder: compliant, and semantically wrong.

**④ A mandatory element that physically cannot fit.** `Donut chart`'s ring is a
fixed 176 px and refuses `resize()`; ring + internal gap + legend =
**373 px in a 360 px frame**. `Legend` is mandatory per the ruleset. The agent
turned it off and **broke no rule** — `When nothing fits` covers a component
being *absent*, never one that exists, is correct, and does not fit.
`Platform limits` says "all 98 exist, no Figma constraint"; existence is not
usability at a target width.

**⑤ `C2 · Tier ceiling` could not be enforced at all.** **Verified**: the brief's
"price estimation block" routes via `Highest tier first` to `Estimation card`,
whose row reads `unresolved · ⚠︎ undescribed, see audit` — and
`components-audit.md` is flagged **never read as rules**. The
highest-precedence rule dead-ends into a file agents must not open. Three rows
have that shape. The agent ruled `Estimation card` out correctly but did so
entirely outside the ruleset, by reading `exposedSubComponents` in the registry.

Also **verified**: `Which component` has no row for "a block of controls that
computes a live result". A finance simulator is a recurring product pattern and
nothing routes it. The agent assembled one itself and noted it **cannot tell
whether it just hand-built something that should have been an Experience** —
precisely the failure `C2 · Tier ceiling` exists to catch.

### One correction to carry forward

The test's subagent reported `Legend` as present in the ruleset but absent from
the registry. **That is wrong.** **Verified**: `.Legend` exists as an exposed
sub-component of `Line chart`, key `c8b3a1d00cbd…`, with its own `Legend 3` and
`Interactive` properties.

The real defect is different and still live: it is dot-prefixed, i.e. private —
in practice a boolean sub-property of each chart. But
`components-rules-ai.md:253` gives it a full `Which component` row and calls it
**mandatory**, as though it were something you select and place. **The ruleset
models a sub-property as a selectable component**, and that row came from our own
eval round 3.

### What the agent had to guess

Every one is a documentation defect:

| Guess | Because |
| --- | --- |
| `Radius/4`, and `Card`'s `Radius=8` | no radius ruleset |
| No shadow anywhere | no shadow ruleset; effect styles are named `4/8/16/24/32` with no role mapping |
| An inverted surface for a called-out step on a non-interactive scale | `Never borrow a state token` forbids a `selected` leaf on something with no selected state. It followed the ruleset's instruction to raise a missing token |
| `body/12/regular` for footnote markers | `Size by context` forbids choosing by a hierarchy ladder and gives nine observed pairings — none covers footnote, caption or legal micro-copy. It picked on size alone, the one thing the rule forbids |
| `€` as a field suffix | nothing says whether currency is prefix, suffix or part of the value. The block now renders currency two ways |
| Six label/value pairs are a list, not a table | `Which component` routes "tabular and comparable" to `Table` and plain lists to `Cell content` rows, with **no discriminator between them**. Getting it wrong is a tier violation |

## The adapter contract — one assumption is broken

Tested directly against live Figma. This matters before any adapter is written.

| Fact | Reality |
| --- | --- |
| `mainComponent.key` | Yes, but **only** via `use_figma` JS against the plugin API. Not from `get_metadata` |
| Variant property names and values | Yes, same route |
| `isTokenBound` per property | **No.** `get_variable_defs` returns the variable *set* in a subtree, not a property→variable map. Needs `node.boundVariables` via JS |
| `isComponentInternal` | **Not answerable from the read tools.** Doable via JS by walking `mainComponent` and diffing overrides — the most expensive part of the adapter. Budget for it |

**The headline, and the reason `C4 · Authorisation` would silently pass
everything.** The same token returns two different names depending on where it is
bound:

| Source | Name returned |
| --- | --- |
| Inside a library `Cell Content` instance | `color.content.default.default` |
| Local hand-styling | `Color/Content/Default/Inverted/Default` |

Same file, same session. The adapter contract requires `property.tokenName` to be
"the name used on the token pages" — and the form coming out of library internals
is **not that form**. Any adapter that string-matches token names against the
token pages fails silently on every library component's internal styling. Cause
unknown — possibly a code-syntax name, a second collection, or a legacy binding.
**Pin this down before writing the adapter.**

One accidental heuristic fell out of it — internal styling came back
lowercase-dotted, local styling Title-Case-slashed. **Do not build on it.** It is
a symptom of whatever causes the discrepancy, not an API guarantee.

## Proposed plan changes, not yet applied

| Change | Why |
| --- | --- |
| **Block 2b · Registry properties → required, and next** | Finding ① . The earlier reasoning that it was "just a cache, properties can be read live" was wrong: live reads work for *variants*, but the text-node names are not variant properties at all |
| **New block: rulesets for radius, shadow, border-width** | Finding ② . Cheapest fix, values already exist, converts `C3 · Token binding` from unenforceable to enforceable in three categories |
| **Extend `When nothing fits`** to cover exists-but-doesn't-fit | Finding ④ . The `Donut chart` case broke no rule and produced a wrong screen |
| **Fix the `Legend` row** — it is a sub-property, not a selectable component | Our defect, from eval round 3 |
| **Fix the three `unresolved` rows** so they do not dead-end into the audit | Finding ⑤ . `C2 · Tier ceiling` is unenforceable until they do |
| **Add a `Which component` row** for controls that compute a live result | Finding ⑤ |
| **Widen the `audit` branch category** in `CLAUDE.md` | It currently reads "`component-web-ai-docs` runs". Compliance runs belong there too |

## Open decisions — these need Gabriel

Five were put to him by the test session and may already be answered in that
conversation; check before re-asking.

1. **Which gap to fix first.** The test session recommended the radius / shadow /
   border-width rulesets — cheapest, values already in the registry, converts two
   checks from unenforceable to enforceable.
2. **Promoting Block 2b · Registry properties** to required.
3. **`Scale/*` ownership** — who owns DPE / CO₂ colour, and what a GSL agent
   should do when a legally required element has no compliant component. This is
   a design-system question, not a documentation one.
4. **Extending `When nothing fits`** for the exists-but-doesn't-fit case.
5. **Recording run 001** in the scorecard's run log, on this branch.

## Working notes for the next session

- **The UI in the previous session showed the wrong folder and branch** —
  `gsl-core-web-design-system` / `chore/claude-design-export`, while the tools
  operated correctly in `gsl-ds-documentation-ai`. Trust `pwd`, not the
  indicator, and state the repo and branch before any commit or merge.
- **Several other sessions have been editing this repo today.** One merged PR #22
  mid-write; one left the working tree parked on a finished branch. Check
  `git status` and `git branch --show-current` before starting, and prefer one
  session per branch.
- **Subagents are authorised for cold test runs only** — eval runs and compliance
  scoring. The eval's central claim, "every miss is a defect in the ruleset, not
  in the agent", only holds if the reader is genuinely cold.
- **Verification is not a question to ask Gabriel.** Decide the depth, run it,
  report what it found.

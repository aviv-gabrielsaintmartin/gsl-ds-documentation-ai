# The plan

> **Superseded, 9 September 2026.** This file is kept as history and is no
> longer the current state of the project. Read [status.md](../../status.md) for
> where things are, and [backlog.md](../backlog.md) for every task, open question
> and finding. Do not work from this file.

_Human-first. Plain language. If this page needs a glossary, it's wrong._

> **Picking this up cold?** Read [handoff.md](handoff.md) after this page. It
> holds the run-001 findings and the open decisions, which are not yet
> reflected in the block table below.

## What we're actually trying to do

Document the GSL Design System well enough that an AI agent can design a
compliant SeLoger-quality interface with no human in the loop.

Two words carry all the weight:

- **Compliant** means it reuses what already exists — an existing component, an
  authorised token — and invents something new only when nothing fits, and says
  so when it does. The failure mode we're preventing is *reinventing what
  already exists*, not designing something new.
- **Quality** is a separate thing, and it is currently undocumented. It exists
  only in Gabriel's head. That's deliberate for now.

## Milestones

| When | What | Quality bar? |
| --- | --- | --- |
| **End Sept 2026** | An agent that designs fully compliant output in Figma | No — compliance only |
| Later | The quality bar written down, so output can be judged on more than compliance | Yes |
| Later | Web, iOS and Android generation consuming this knowledge base | — |
| Later | A full audit pipeline across Figma, web, Android and iOS. Deliberately deferred | — |

## How we're testing whether it works

One loop, end to end:

```
  build the docs  ──►  build the Figma agent  ──►  hand it a wireframe + brief
                                                            │
                                                            ▼
        you judge the quality  ◄──  score the compliance  ◄──  it makes the UI
        (human, for now)            (machine, automatic)
```

The point of the loop is not the UI. It is finding out **which layer of the
documentation fails**, because an agent turning a wireframe into a screen makes
three separate decisions:

| Layer | The decision | Where it's documented |
| --- | --- | --- |
| 1 | **Which component?** | `components/components-rules-ai.md` — done, and eval'd |
| 2 | **Which variant of it?** | The `Variant Selection Flow` in each component doc — done |
| 3 | **How does it sit on the page?** | Documented but **unverified** — spacing's **Container padding** and **Page rhythm**. **Block 3 · Layout** verifies them |

## The building blocks

One block at a time. One block = one branch = one PR.

| # | Name | What it is | Status | Brief |
| --- | --- | --- | --- | --- |
| — | **Component selection** | The ruleset, audit and eval | ✅ **Done** — PR #17, merged 2026-09-08 | — |
| 0 | **Doc layer** | README, plan, decisions, briefs | ✅ **Done** — PR #18, merged 2026-09-08 | [00-doc-layer](briefs/00-doc-layer.md) |
| 1 | **Compliance scorecard** | What compliance means, as six checks, platform-neutral | ✅ **Done** — PR #19, merged 2026-09-08 | [01-compliance](briefs/01-compliance.md) |
| 2a | **Tier parts list** | Ten rows become machine-readable so `C2 · Tier ceiling` can run | ✅ **Done** — PR #20, merged 2026-09-08 | [02a-tier-parts-list](briefs/02a-tier-parts-list.md) |
| 2b | **Registry properties** | The registry schema gains a field for parent property definitions, the 18 prose entries migrate into it, then the Components tier re-syncs. Needs live Figma | ⬜ Optional — see below | — |
| 2c | **Platform availability** | For web and native: first a controlled vocabulary for the 52 docs' readiness rows (10 different values today, 11 cells hold no status), then a rule. **Not needed for Figma** — all 98 registry entries exist | ⬜ Deferred until web or native is a target | — |
| **2d** | **Rule names** | The four rulesets' rules lose their numbers and gain names. The same number meant four different things across four files | 🔵 **In progress** | [02d-rule-names](briefs/02d-rule-names.md) |
| 3 | **Layout** | Verify page composition. Spacing's **Container padding** and **Page rhythm** already document it per tier, but mark themselves **unverified**. Verify them against real screens, then fill the two genuine gaps: column spans, and page anatomy | ⬜ Not started | — |
| 4 | **Figma agent** | The agent and the Figma adapter, both in the shared skills repo, not here. The adapter implements the scorecard's adapter contract. Plus wireframe #1 and a first scored run | ⬜ Not started | — |
| 5 | **Doc gaps** | Fill what remains, prioritised by what **Block 4 · Figma agent** actually broke on | ⬜ Not started | — |

**Always refer to a block by number *and* name** — `Block 2b · Registry
properties`, never just `2b`. Nobody holds a numbered list in their head.

**Block 2a · Tier parts list**, **Block 2b · Registry properties** and
**Block 2c · Platform availability** are independent and can run in any order.
**Block 4 · Figma agent** needs the parts list from **Block 2a**. **Block 2b · Registry
properties** is a cache rather than a blocker, since an agent can read property
definitions live from Figma. **Block 2c · Platform availability** only matters
once generation targets web or native.

## What each block is waiting on

| Block | Blocked by |
| --- | --- |
| **Block 3 · Layout** | **Gabriel naming 3–5 Figma product screens** as the evidence base. A SERP, a listing detail, one funnel step would do it. The rules exist; they cannot be *verified* without real screens |
| **Block 2b · Registry properties** · **Block 2d · Rule names** | Nothing. Registry properties needs Figma Desktop open |
| **Block 2c · Platform availability** | Deferred by decision — only matters once web or native is a generation target |
| **Block 4 · Figma agent** | **Block 2a · Tier parts list** for `C2 · Tier ceiling`'s parts column; **Block 2b · Registry properties** only if live property lookup proves too slow |

## The known holes, as of 2026-09-08

Recorded so they aren't rediscovered as surprises.

| Hole | Size |
| --- | --- |
| **Page composition is documented but unverified** | spacing's **Container padding** and **Page rhythm** say so themselves. `C6 · Layout` of the scorecard is defined and switched off until **Block 3 · Layout** verifies them |
| **Figma variant property names are missing** for the Components tier | 1 of 61 entries records them, while 57 of 61 have more than one variant. So a decision tree saying `Size → 40px` can't be checked against Figma |
| **Ten open questions** in `components/components-audit.md` | Each blocks a rule that can't be written until you answer it |
| **24 selectable components have no doc and no rule row** | They're named in the inventory, so an agent knows they exist, but nothing routes it there by intent |
| `Accessibility (a11y)` empty in 51 of 59 component docs | Inherited from the Zeroheight source |
| `Breakpoints & Platform Adaptations` empty in 36 of 54 | Same |
| **`C2 · Tier ceiling` reaches 4 of the 10 Highest tier first rows** | Six rows are not parts-composed things — two are containers, one is all-or-nothing, three are unresolved. **Highest tier first** still governs all ten; it just cannot be *enforced* by counting parts for six |
| **No way to detect a rebuilt container** | Nothing catches an agent that hand-builds an empty state instead of using `Info State`. Needs a non-parts-based mechanism; none designed |
| **Web and native availability is unruled** | 52 docs carry a readiness row in 10 different vocabularies, with 11 cells holding no status. Needs a controlled vocabulary before it can be a rule. **Figma is unaffected** — all 98 registry entries verified live. **Block 2c · Platform availability** |

## How we work through a block

Four steps, every time. Step 1 is the one that makes the project explainable.

| Step | What happens | Touches the repo? |
| --- | --- | --- |
| **1. Brief** | A one-page brief in `briefs/`: what this block is, why, what changes, what deliberately doesn't, and how we'll know it worked. Gabriel reads it, pushes back, approves | the brief only |
| **2. Build** | One block, one branch | yes |
| **3. Check** | Run that block's eval or verification. Record the result, pass or fail | yes |
| **4. Log** | One entry in [decisions.md](../decisions.md), then a PR with a Verification section | yes |

Why briefs rather than just PRs: a PR explains a diff. A brief explains an
intention. In three months the diffs will be unreadable and the intentions will
be the only thing worth having.

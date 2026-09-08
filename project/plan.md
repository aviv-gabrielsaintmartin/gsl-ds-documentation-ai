# The plan

_Human-first. Plain language. If this page needs a glossary, it's wrong._

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
| 3 | **How does it sit on the page?** | Documented but **unverified** — `spacing-rules-ai.md` Rules 6 and 7. Block 3 verifies them |

## The building blocks

One block at a time. One block = one branch = one PR.

| # | Block | Status | Brief |
| --- | --- | --- | --- |
| — | Component selection ruleset, audit and eval | ✅ **Done** — PR #17, merged 2026-09-08 | — |
| 0 | This doc layer — README, plan, decisions, briefs | ✅ **Done** — PR #18, merged 2026-09-08 | [00-doc-layer](briefs/00-doc-layer.md) |
| **1** | **Compliance scorecard** — what compliance means, as six checks, platform-neutral | 🔵 **In progress** | [01-compliance](briefs/01-compliance.md) |
| 2 | **Machine-readable component data** — variant property names in the registries, plus a parts column on Rule 0's ten rows so `C2` can run | ⬜ Next | — |
| 3 | **`layout/` — verify page composition.** Rules 6 and 7 of `spacing-rules-ai.md` already document container padding and page rhythm per tier, but mark themselves **unverified**. This block verifies them against real screens and fills the two genuine gaps: column spans, and page anatomy | ⬜ Not started | — |
| 4 | **The Figma agent and the Figma adapter** — both in the shared skills repo, not here. The adapter implements the scorecard's adapter contract; the scorecard itself stays platform-neutral. Plus wireframe #1 and a first scored run | ⬜ Not started | — |
| 5 | **Fill the remaining doc gaps**, prioritised by what block 4 actually broke on | ⬜ Not started | — |

Blocks 1 and 2 don't depend on each other and can run in either order. Block 4
needs both.

## What each block is waiting on

| Block | Blocked by |
| --- | --- |
| 3 | **Gabriel naming 3–5 Figma product screens** as the evidence base. A SERP, a listing detail, one funnel step would do it. The rules exist; they cannot be *verified* without real screens |
| 1 | Nothing |
| 2 | Nothing |
| 4 | Blocks 1 and 2. `C2` specifically needs block 2's parts column before it can run |

## The known holes, as of 2026-09-08

Recorded so they aren't rediscovered as surprises.

| Hole | Size |
| --- | --- |
| **Page composition is documented but unverified** | `spacing-rules-ai.md` Rules 6 and 7 say so themselves. `C6` of the scorecard is defined and switched off until block 3 verifies them |
| **Figma variant property names are missing** for the Components tier | 1 of 61 entries records them, while 57 of 61 have more than one variant. So a decision tree saying `Size → 40px` can't be checked against Figma |
| **Ten open questions** in `components/components-audit.md` | Each blocks a rule that can't be written until you answer it |
| **24 selectable components have no doc and no rule row** | They're named in the inventory, so an agent knows they exist, but nothing routes it there by intent |
| `Accessibility (a11y)` empty in 51 of 59 component docs | Inherited from the Zeroheight source |
| `Breakpoints & Platform Adaptations` empty in 36 of 54 | Same |
| **Rule 0 has no machine-readable parts list** | Its ten rows name the components each higher-tier component would be rebuilt from, but as prose. `C2` of the scorecard cannot run until they are data. Ten rows. Block 2 |

## How we work through a block

Four steps, every time. Step 1 is the one that makes the project explainable.

| Step | What happens | Touches the repo? |
| --- | --- | --- |
| **1. Brief** | A one-page brief in `briefs/`: what this block is, why, what changes, what deliberately doesn't, and how we'll know it worked. Gabriel reads it, pushes back, approves | the brief only |
| **2. Build** | One block, one branch | yes |
| **3. Check** | Run that block's eval or verification. Record the result, pass or fail | yes |
| **4. Log** | One entry in [decisions.md](decisions.md), then a PR with a Verification section | yes |

Why briefs rather than just PRs: a PR explains a diff. A brief explains an
intention. In three months the diffs will be unreadable and the intentions will
be the only thing worth having.

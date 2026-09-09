# Brief 00 — The project documentation layer

| | |
| --- | --- |
| **Status** | In progress |
| **Branch** | `docs/project-doc-layer` |
| **Written** | 2026-09-08 |
| **Depends on** | Nothing |

_This brief is written retroactively, because it describes the block that
invents briefs. Every block from 01 onward gets its brief **before** any work
starts._

---

## What this block is

Five files that make the repo explainable to a human:

| File | What it is |
| --- | --- |
| `README.md` | The map. What does what and where, plus the filename grammar |
| `project/plan.md` | The goal, the milestones, the six blocks and their status |
| `project/decisions.md` | Why the project is shaped this way. Newest first |
| `project/briefs/00-doc-layer.md` | This file — the ritual demonstrating itself |
| `.claude/rules/project.md` | The rule that keeps these files in plain language |

## Why

The problem in Gabriel's words: *"As the AI agent will build everything, how can
I as a human understand clearly what does what and where? I don't know if I'll
be able to explain what does what."*

That is a real risk, not a confidence problem. This repo is deliberately written
for machines — the global instructions say to *optimise for unambiguous machine
parsing over prose polish*. That's correct for the knowledge base and it has a
side effect: the owner can't easily explain his own project, and can't tell
whether a document is a page, a ruleset, an audit or a test without opening it.

Two specific gaps made it worse:

- **There was no root `README.md` at all.** Opening the repo gave you
  `CLAUDE.md`, which is instructions for an agent, not a map for a person.
- **The suffix grammar existed but was hidden.** `tokens/README.md` documents it
  beautifully — for `tokens/` only. Nothing said it applied repo-wide.

## What changes

- A human can open the repo and know within a minute what the folders are, which
  files are the contract, and which are evidence.
- Any filename explains itself, because the suffix table is at the root.
- There is one place that answers "why is it like this" — and it records the
  cost of each decision, not just the decision.
- There is one place that answers "where are we" — the block table in `plan.md`.
- "Am I about to lose work?" becomes a two-command check Gabriel can run
  himself, rather than a question he has to ask.

## What deliberately does not change

- **No knowledge-base content is touched.** Not a token page, not a component
  doc, not a ruleset, not a registry. This block adds a layer; it edits nothing
  underneath it.
- **`CLAUDE.md` keeps its job.** It stays the agent's instruction file. It is not
  rewritten for humans, and `README.md` does not duplicate it.
- **No new process for anyone but us.** The brief ritual is how this project
  runs, not something imposed on the design system's consumers.

## How we'll know it worked

There's no eval for prose, so the test is behavioural rather than scored:

| Test | Passes if |
| --- | --- |
| **The explain test** | Gabriel can describe what each folder is for, and what the five suffixes mean, without opening a file |
| **The stranger test** | Someone new to the repo can find the component ruleset, and understand why they must not read the audit as rules, from `README.md` alone |
| **The three-month test** | The reasoning behind a decision is recoverable from `decisions.md`, not only from a PR diff |
| **The safety test** | Gabriel answers "have I lost anything?" himself, in seconds |

The first and last are the ones that matter. If Gabriel still has to ask what a
file is for, this block failed and the README needs rewriting rather than
extending.

## Risks

| Risk | Mitigation |
| --- | --- |
| **It drifts.** A human-first layer that nobody updates is worse than none, because it lies with authority | A block is not done until its brief and its decision entry exist. `plan.md` stays one line per block so updating it is trivial |
| **It becomes a second knowledge base.** Explanation creeping into duplication of the rulesets | `.claude/rules/project.md` states these files describe and never specify. The rulesets remain the only contract |
| **An agent reads `project/` as instructions** and acts on a plan entry as if it were a rule | The rule file says `project/` is human-first and is never the source of truth for how to build anything |

## Cost

Roughly half a day, and a permanent small maintenance tax. The tax is the point:
it's what converts "the AI built it" into something Gabriel owns.

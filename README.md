# GSL Design System — the knowledge base

This repo is **one platform-neutral description of the GSL (Gemini) Design
System**, written so that an AI agent can read it and build a compliant
interface with nobody correcting it.

It is not a code repository. There is no build, no lint, no test suite — the one
deliberate exceptions are `tokens/scripts/` and `scripts/check-links.py`. Everything else here is content and data.

**It is also not the agent.** Several agents consume this knowledge base — a
design agent, and later web, iOS and Android. They live in their own repos. This
one only holds the truth they read.

Judge every page in here by one test:

> Could an agent build a compliant interface from this alone, with nobody
> correcting it?

---

## Start here

| If you want to… | Read |
| --- | --- |
| **Know where the project is, or pick it up cold** | **[status.md](status.md)** — one page, always current |
| See every task, open question and finding | [project/backlog.md](project/backlog.md) |
| **Generate an interface** | The rulesets, and only the rulesets — see the four of them below |
| Know what components exist | [components/components-index.md](components/components-index.md) |
| Know what tokens exist | [tokens/tokens-index.md](tokens/tokens-index.md) · then [tokens/README.md](tokens/README.md) for the folder |
| Know **why** a rule says what it says | The matching `-audit.md` |
| Know why the project is shaped like this | [project/decisions.md](project/decisions.md) |

**How work runs:** one task at a time. `/task-next` proposes a task and waits for
Gabriel's go; `/task-check` verifies it worked and names the next one. Every
finding is written into the backlog rather than left in conversation.
The old plan, briefs and handoff note are retired to
[project/archive/](project/archive/) — history, never worked from.

---

## Who reads what

The single most useful thing to know about this repo: **almost every file in it
is written for a machine, and two are written for you.**

| Who reads it | What it is | Where |
| --- | --- | --- |
| Agents working *inside* this repo | Instructions and workflows | `CLAUDE.md`, `.claude/rules/`, `.claude/skills/` |
| Agents *consuming* the knowledge base | **The contract** | the seven `*-rules-ai.md` files |
| Either — machine-first reference | The knowledge itself | `*-tokens.md`, `*-audit.md`, `*-ledger.md`, `components/<name>/<name>.md` |
| **You, and any human** | **Where the project is, and what's left** | **`status.md` and `project/backlog.md`** |
| You, and any human | The map and the story | `README.md` and the rest of `project/` |

Those last two rows are why this file exists. Everything else is optimised for
unambiguous machine parsing. `README.md`, `status.md` and `project/` are
deliberately not — they are plain language, and they are allowed to explain
rather than specify.

**If you only open one file, open [status.md](status.md).**

---

## The filename grammar

**A file's suffix tells you what it is and whether it may be trusted as rules.**
Learn these seven and any filename in the repo explains itself.

| Suffix | What it is | Written by | Read as rules? |
| --- | --- | --- | --- |
| `-index.md` | **The routing page.** Every page in the folder, what it covers, and which ruleset to read instead. Holds no values of its own | a human | no — it tells you where to go, not what to use |
| `-tokens.md`, or `<name>.md` | **The page.** What exists — every value, every variant, and when to use each | a human | no — it lists everything, including things the audit rejected |
| `-rules-ai.md` | **The ruleset.** What an agent is *allowed* to reach for | a human, from the audit | **yes. This is the contract** |
| `-audit.md` | **The evidence.** Why the ruleset says what it says, what was rejected, what is still open | a human, from the ledger | **never** |
| `-ledger.md` | **The raw evidence table** the audit was built from | **a script** | never — and never edit it, re-run the script |
| `-eval.md` | **The check on the ruleset** — test intents, expected answers, and the run log | a human | no — it is the test, not the rules |
| `-scorecard.md` | **The check on generated output** — how a produced screen is judged, and the format of the report it produces | a human | no — it is the test, not the rules |

The distinction that matters most:

> **A page says what exists. A ruleset says what you're allowed to use.**
> An agent that reads the page instead of the ruleset will build on tokens the
> audit already rejected.

And the distinction between the two kinds of check:

> **An `-eval` judges a ruleset. A `-scorecard` judges output.**
> The eval asks "would an agent reading this reach the right answer?" The
> scorecard asks "is this screen compliant?".

Two honest inconsistencies, so you aren't confused when you meet them:

- Token audits are named `-usage-audit.md`, the component audit is
  `-audit.md`. Same family, historical difference.
- A `-ledger.md` always has a `.json` twin holding the same data for scripts.
  The `.json` is not committed and is regenerated on demand.

### What exists today

| Rulesets — the contract | Audits — the evidence | Ledgers — script output | Evals — the check |
| --- | --- | --- | --- |
| `components/components-rules-ai.md` | `components/components-audit.md` | `tokens/color/color-usage-ledger.md` | `components/components-eval.md` |
| `tokens/color/color-rules-ai.md` | `tokens/color/color-usage-audit.md` | `tokens/spacing/spacing-usage-ledger.md` | |
| `tokens/typography/typography-rules-ai.md` | `tokens/typography/typography-usage-audit.md` | `tokens/typography/typography-usage-ledger.md` | |
| `tokens/spacing/spacing-rules-ai.md` | `tokens/spacing/spacing-usage-audit.md` | | |
| `tokens/radius/radius-rules-ai.md` | `tokens/radius/radius-usage-audit.md` | | |
| `tokens/shadow/shadow-rules-ai.md` | `tokens/shadow/shadow-usage-audit.md` | | |
| `tokens/border-width/border-width-rules-ai.md` | | | |
| | `tokens/color/surface-border-combination-audit.md` — draft, not yet a ruleset | | |
| | `compliance/compliance-audit.md` | `compliance/compliance-flag-ledger.md` | `compliance/compliance-scorecard.md` |
| | | `compliance/compliance-run-ledger.md` | |

Seven rulesets, eight audits, five ledgers, one eval, one scorecard.

The three token ledgers are written by a script. The two compliance ledgers are
written by the checking agent. Both are append-only and neither is ever edited
by hand.

---

## How a rule earns the right to exist

Nothing in a ruleset is allowed to be an opinion. This is the chain every rule
has to come through:

```
  a script reads the real design-system code
              │
              ▼
      ledger        every token, and every component that binds it
              │     ← raw, mechanical, never edited by hand
              ▼
      audit         a human reads the ledger and decides
              │     ← records what was rejected, and why
              ▼
    rules-ai        what an agent may reach for
              │     ← the contract. Nothing here without evidence above it
              ▼
       eval         a cold agent is given ONLY the ruleset and scored
                    ← every miss is a defect in the ruleset, not the agent
```

**The eval step is the one people skip, and it is the one that works.** The
component ruleset scored 22/22 on its first cold run — and that perfect score
still hid four real defects, which only surfaced because the agent was also
asked where it had struggled. Twelve defects were found and fixed across three
runs this way.

---

## The map

### The pillars — what an agent reads to build

| Folder | What's in it | Start at |
| --- | --- | --- |
| `tokens/` | 12 token categories — colour, typography, spacing, radius, shadow, and 7 more. Every one checked against real component usage | [tokens/tokens-index.md](tokens/tokens-index.md) |
| `components/` | 53 component docs, one folder each with a self-contained `images/`. Plus the ruleset, audit and eval | [components/components-index.md](components/components-index.md) |
| `figma/` | 7 registry JSON files — the identity of every Figma component, token and icon. Keys, node IDs, variant counts | `.claude/rules/figma-registries.md` |
| `compliance/` | How generated output is judged — six checks, what fails outright, and the report every run must produce. Read by a **checking** agent, not a generating one. `compliance/runs/` holds one folder per run: the brief, the screenshots, the facts and the report | [compliance/compliance-scorecard.md](compliance/compliance-scorecard.md) |

A further pillar, `layout/`, is planned but does not exist yet — see
[status.md](status.md). Page composition is currently the one decision an agent
has to make with no documentation behind it.

### Everything else

| Path | What's there |
| --- | --- |
| `CLAUDE.md` | Instructions for agents working in this repo. Not a human document |
| `.claude/rules/` | 5 path-scoped rule files — for `tokens/`, `figma/`, `components/`, `compliance/` and `project/`. Each loads automatically when an agent opens a file in that folder |
| `.claude/skills/` | 8 skills — the repeatable workflows. See below |
| `status.md` | **The one page.** Where the project is and what the next task is. Human-first |
| `project/` | `backlog.md` — every task, question and finding — plus `decisions.md`, the log of why the project is shaped this way. Retired files sit in `project/archive/`. **Human-first** |
| `tokens/scripts/` | 4 Python scripts. They only ever *read* the design-system code repo. Re-run them to refresh the evidence |
| `scripts/` | `check-links.py` — run it after renaming or deleting anything. It reports links whose target is gone, and rulesets that point an agent at evidence it may not read |
| `internal/` | Human reference notes, e.g. a git tutorial |

### The eight skills

Two run the work itself:

| Skill | What it does |
| --- | --- |
| `task-next` | Proposes one task — what, why, how long — waits for Gabriel's go, does it, reports in three lines |
| `task-check` | Verifies the task actually worked. Passed → logged, next task named. Failed → a sub-task to fix it becomes next |

Six do the content work:

| Skill | What it does |
| --- | --- |
| `zeroheight-confluence-transfer` | Zeroheight export → a Confluence component page, against a fixed template |
| `component-web-ai-docs` | Audits a component's web code against its docs; publishes an audit, a decision tree and an API spec |
| `figma-sync-component-sets` | Pulls component/pattern/experience identity from Figma into the tier registries |
| `figma-sync-tokens` | Pulls design tokens, text styles and effect styles into the token registry |
| `figma-sync-icons` | Pulls the icon inventory into the icon registry |
| `figma-sync-libraries` | Pulls the four library file keys into the library registry |

Read a skill's own `SKILL.md` before running it. That file, not this one, is the
source of truth for how it works.

---

## Am I about to lose work?

Two commands. Run them in any terminal, in this folder, any time.

```
git status --porcelain | wc -l      # 0     = everything is committed
git log --oneline @{u}..HEAD        # empty = everything is pushed
```

**Zero and empty means nothing can be lost.** Anything else is telling you
exactly what is exposed, and it is still all recoverable.

Two habits that prevent the problem instead of detecting it:

- **One Claude session on this project at a time.** Two sessions in the same
  folder can overwrite each other's edits, and one can commit the other's
  half-finished work under the wrong message.
- **A task isn't finished until `git status` is clean and everything is pushed.**
  That happens automatically when `/task-check` passes.

Git almost never throws work away. Committed, stashed, or even on a branch you
deleted, it stays retrievable. If something looks lost, ask before touching
anything — it is nearly always still there.

---

## Conventions

- All filenames are lowercase kebab-case. **One exception**: image filenames
  keep their original hash-based names, because those are Zeroheight asset
  identifiers matched by exact filename. Never rename them.
- Never invent a Confluence page ID, a Figma key, or an Atlassian cloud ID. Read
  them from the registry JSON, or resolve them live.
- The Zeroheight MCP connector is never used, even when a session shows it as
  connected.
- **One task = one commit, straight to `main`.** No branches, no pull requests —
  see the git section of `CLAUDE.md` for why, and for the short list of
  operations that always ask you first.

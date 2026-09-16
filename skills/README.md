# Skills for other tools

**This folder holds instructions written here and used somewhere else.** Today
that means Figma's design agent. `gsl-color-rules/SKILL.md` is the first one.

**Not to be confused with `.claude/skills/`.** Two folders, two jobs:

| Folder | Who runs it | What it does |
| --- | --- | --- |
| `.claude/skills/` | A Claude Code session **in this repo** | Maintains the repo — syncs Figma, transfers docs, runs the task loop |
| `skills/` | **Another tool**, elsewhere | Consumes this documentation to produce design work |

---

## What a Figma custom skill can be

**A single Markdown file following the [Agent Skills specification](https://agentskills.io/specification).** The same specification this repo's own skills use, which is why the source is portable.

| | |
| --- | --- |
| **Format** | One `.md` file. Frontmatter, then instructions |
| **`name`** | Becomes the slash command. **64 characters** |
| **`description`** | How the agent decides to use it. **1,024 characters**. Write it as *when to use this*, never as a summary |
| **No subdirectories** | Figma supports no `scripts/`, `references/` or `assets/`. Everything is inline or it does not exist |
| **One skill per prompt** | If several are named, only the first runs. You cannot compose two small skills |
| **Size** | **No published Figma limit.** The specification recommends under 500 lines, about 5,000 tokens |
| **Who** | Paid plans, full seats. Scope: personal, team, organisation or Community |

**The 500-line recommendation does not really apply in Figma.** It exists because
the specification assumes progressive disclosure — a small entry file, bulk in
`references/`, loaded on demand. Figma supports none of that. Anyone packaging a
real design system exceeds it.

For scale: this repo's eight rulesets are **1,916 lines and about 22,000 tokens**
together. The colour ruleset alone is 468 lines.

---

## The architecture, and why

Figma's own guidance is not to pack a design system into one skill. Guidance
belongs on the assets; the skill stays a thin decision layer.

```
   THIS REPO                    canonical. platform-neutral. versioned
        │
        ├─ generated ─────►     Figma variable and component descriptions
        │                       read at the moment someone picks
        │
        └─ generated ─────►     a compact skill
                                global rules, decision process, escalation
```

**What goes where:**

| Kind of guidance | Where it lives |
| --- | --- |
| What one token or component is for | Its description in Figma |
| Rules that cross many tokens — *never pick by appearance*, *never borrow a state token* | The skill |
| The inventory of what exists | The library itself. **Never copied into a skill** |
| Reasoning, evidence, contrast figures | Here, in the `-audit` files. Never shipped |

**One rule holds the whole thing together: what is pushed to Figma is generated,
never hand-edited.** Edit a description in Figma and this repo stops being true.

---

## What has been done

**Colour descriptions, 227 of them, written on 15 September 2026.**

- Generated from the seven colour token pages in `tokens/color/`, which already
  held **383 rows** of *When to use · Don't use for · Used by*.
- **53 had an exact row, 138 inherited a parent row, 36 are marked *Not for
  use*** — 22 `Symbol/*`, 9 `Native/*`, and 5 energy colours outside the French
  DPE ladder.
- Written to a branch of the Foundations library, verified, then published by
  Gabriel.

**Nothing was authored that did not already exist in the documentation.** The
only new text is *Not for use* and the state lines.

---

## The four traps

All four cost real time. All four will happen again to anyone writing to Figma
from here.

**One — variable names are not unique.** The Foundations file holds **1,010**
variables prefixed `Color/`, not the 227 in the Brand collection, and some names
exist twice in different collections. A script using `find(x => x.name === …)`
writes to whichever copy the API lists first. **Resolve the collection, capture
ids, then write by id.**

**Two — one variable write per call.** The FigCli plugin commits the first write
in an `eval` call and silently drops the rest. Batching forty pairs writes one.
**Use one HTTP call per write** to the daemon's `/exec` endpoint — 227 writes
take about a second.

**Three — the daemon needs its token.** `POST http://localhost:3456/exec` with
an `X-Daemon-Token` header. The token is at `~/.figma-ds-cli/.daemon-token`.

**Four — the plugin infers where to put the `return`.** It wraps submitted code
in an async function. **A script opening with a comment, or ending in an
`if/else` block, defeats that inference** — the code still runs, but the result
comes back empty. A loop then reports zero successes while having written
something, which is the worst possible failure mode.

Also: Figma now blocks the synchronous variables API. `getLocalVariables()`
throws. Everything must use `getLocalVariablesAsync`.

---

## What the first test showed

One run, 16 September 2026, using the same brief as compliance runs 001 to 003.
Gabriel's verdict: **mid.**

| What happened | What it suggests |
| --- | --- |
| Some colours right, some wrong. **The CO2 scale was replaced** | The rule did not reach the decision. CO2 is the hardest case: a plausible-looking alternative always exists |
| **Components chosen correctly even without descriptions** — the button among them | **Guessing:** the agent resolves components from the library structure, not from documentation. Component descriptions may buy less than expected |
| Components badly positioned | Expected. Placement guidance has never been checked against a real screen, and the scorecard has no question for it |

**What this test cannot tell us, and why.** The skill and the descriptions went
live together, so a correct choice cannot be attributed to either one. **Run it
twice next time** — once with descriptions only, once with the skill as well.

---

## What is not known

- Whether the agent reads variable descriptions at all. Nothing has isolated it.
- The real size ceiling for a skill in Figma. The colour skill is 389 lines and
  has never been pushed further.
- Whether component descriptions are worth writing, given the first test.
- Who keeps descriptions in step with this repo once several people edit Figma.

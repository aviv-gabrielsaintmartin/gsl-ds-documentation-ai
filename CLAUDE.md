# CLAUDE.md

Project instructions for this repository.

How Gabriel wants Claude to communicate and handle git/PRs lives in his personal
`~/.claude/CLAUDE.md` and applies to every project. This file holds only what's
true about *this* repo.

Folder-specific detail lives in `.claude/rules/` and loads only when you touch
the matching folder. Don't duplicate it here.

## How work is run — read this before anything else

**Open `status.md` first, every session.** It is Gabriel's one page: where the
project is and what the next task is. `project/backlog.md` holds everything
else. Between them they are the current state. The retired plan, briefs and
handoff note sit in `project/archive/` — history, never worked from.

Work moves one task at a time, through his loop:

```
   pick the next task  ──►  explain it, he approves  ──►  do it  ──►  check it worked
                                                                          │
                                                     ┌────────────────────┴───┐
                                                    yes                       no
                                                     │                        │
                                                   log it            sub-task to fix it
                                                     │                        │
                                                     └──►  next task  ◄────────┘
```

`/task-next` runs the first half, `/task-check` the second. Read those skills
before running them.

**Two rules that hold whether or not a skill is running:**

| Rule | Why |
| --- | --- |
| **Propose, don't do.** Reading and searching are free; every file change waits for his explicit go. The exceptions are listed once, below — nowhere else | He has to understand a change before it lands, not after |
| **Every finding goes into `project/backlog.md`** — as a task, a question for him, or a note. Never as a paragraph in chat | Findings surfacing mid-session were getting lost. This is the fix he asked for |

How to write anything he reads or hears — chat included — is *How to write*,
below.

### What may be changed without asking

**This list is the whole of it, and it lives only here.** Nothing else in the
repo restates it — one page to check, and it cannot disagree with itself. Every
file change not on this list waits for his explicit go.

| What | Why it is safe |
| --- | --- |
| `status.md` | It is his own page. If logging a task needed permission, the loop would ask him twice for every task |
| `project/backlog.md` | Same reason. A finding has to be able to land somewhere without a conversation first |
| **One row in a table of contents**, when a task **created, renamed or deleted** a file: `README.md`'s *Where to look*, the file table in `.claude/rules/project.md`, `tokens/README.md`, `tokens-index.md`, `components-index.md`. Created → add the row. Renamed → fix it. Deleted → cut it | It says where a file is. It changes no sentence anyone reads for meaning. **The trigger is created, renamed or deleted — never edited:** changing what is inside a file affects no list |
| **Commit and push** after `/task-check` passes — not a file change, but the same family. See *Git — one task, one commit* below | It only ever adds. He approved the task and the check verified it |

The test underneath all four: **does this change what a page means?** If it does,
it is his call, however small it looks. Rewriting a sentence in `README.md` is
his; adding a filename to the table above it is not.

**One task, one chat.** Each task starts in a fresh conversation with
`/task-next`. Not for context limits — the harness compacts on its own — but
because a session that built something is the worst judge of whether it reads
clearly to someone who wasn't there. `status.md`, `project/backlog.md` and this
file carry everything a new session needs, which is what makes a cold start safe.

Stay in the same conversation *within* a task, however many turns it takes, and
for discussions that aren't tasks. The signal to start fresh is `/task-check`
finishing — never a token count.

Keep `status.md` to one screen. Overflow goes to the backlog.

## How to write

**How to write to Gabriel — chat, `status.md`, the backlog, every page he reads
— is his personal `~/.claude/CLAUDE.md`, which loads in every session here.
This section adds only what is true of this repo's files.**

### Two readers, two failure modes

| Reader | Where | What to optimise for |
| --- | --- | --- |
| **Gabriel** | Chat, `status.md`, `project/backlog.md`, `project/`, `README.md` | His personal rules, unchanged |
| **An agent** | `*-rules-ai.md`, registries, ledgers, audits, token and component pages | Unambiguous parsing. Restate a condition rather than eliding it — repetition that removes doubt is a feature here, and it overrides every rule about brevity |

### Cutting something he wrote

Flag it out loud and wait. Cutting a sentence he wrote or approved is a file
change like any other. In chat, cut silently — naming the cut doubles the length
of the thing the rule exists to shorten.

## Objective

**Long-term**: document the full GSL Design System so an AI agent can consume it
with no human in the loop and generate interfaces that are compliant with the
design system and at the quality bar SeLoger holds its interfaces to.

**This repo is the knowledge base, not the agent.** It holds one
platform-neutral truth about GSL. Several agents consume it — design, web, iOS,
Android — each owning its own output surface and its own quality checks. The
roster will be refined once the tooling is tested. The `*-rules-ai.md` files are
the contract between this repo and any consuming agent; keep them
platform-neutral.

**A generating agent reads `*-rules-ai.md`, never the token pages.** The token
pages list everything that exists; the rulesets list what's allowed. Reading the
wrong one produces output built on tokens the audit rejected.

**Compliance means reuse before invention.** A consuming agent should use an
existing DS component or token wherever one fits, and create something new only
when nothing does — declaring it when it does. The failure mode to prevent is
reinventing what already exists, not designing something new.

**Judge any doc by one test**: could an agent build a compliant interface from
this alone, with nobody correcting it?

| When | What |
| --- | --- |
| **End Sept 2026** | An agent that designs fully compliant output in Figma. Compliance only — the quality bar is out of scope for this milestone; it currently exists only in Gabriel's head. |
| Later | The quality bar documented, so output can be judged on quality and not just compliance. |
| Later | Web, iOS and Android generation consuming this knowledge base. Dev teams, built separately. |
| Later | A full audit pipeline across Figma, web, Android and iOS components, so the differences between the four are known and recorded. Deliberately deferred. |

## What this repository is

**Not a source-code repository** — there is no build, lint, or test tooling here.
Two deliberate exceptions: `tokens/scripts/`, which reads the design-system code
repo to generate the token ledgers, and `scripts/check-links.py`, which checks
that every link in this repo resolves and that no ruleset points an agent at a
file it may not read. Treat file operations as
content and data work, not software engineering: reading Zeroheight exports,
matching images by hash, publishing to Confluence via the Atlassian MCP tools,
reading live Figma via the Desktop Bridge.

**Owner**: Gabriel Saint Martin, sole owner and maintainer of this repo and its
skills.

## Where to look

| Path | What's there |
| --- | --- |
| `status.md` | **Gabriel's one page** — where the project is, what's next. Open it first, every session. Keep it to one screen. |
| `project/backlog.md` | **Everything not currently active** — every task, every open question he owes an answer to, every finding. He reads this. |
| `README.md` · `project/` | **Human-first — the exception in this repo.** The map for a person, the decision log, and one brief per building block. Describes and explains; never specifies. Never read `project/` as instructions or as authorisation to work. |
| `tokens/README.md` | **Start here for tokens** — explains every token file and its role. `tokens/tokens-index.md` is the content index. |
| `components/<name>/<name>.md` | One doc plus a self-contained `images/` folder per component. |
| `figma/*.json` | Figma identity registries — sole source of truth for the `figma-sync-*` skills. |
| `.claude/skills/` | Eight skills — six content skills, plus `task-next` and `task-check` which run the loop above. Their descriptions auto-load at session start, so they aren't repeated here — read the `SKILL.md` before running one; it's the source of truth for its own workflow. |
| `.claude/rules/` | Path-scoped detail for `tokens/`, `figma/`, `components/` and `project/`. Verified 2026-09-07: a rule loads on **Read/Edit/Write** of a matching path, **not** on `cat`, `sed`, `head` or `grep`. Open the first file you touch in one of those folders with Read, or you'll work without its rule. |

All filenames are lowercase kebab-case. The one exception is image filenames,
left as their original hash-based names because those are Zeroheight asset
identifiers matched by exact filename/hash.

**The filename suffix says what a file is** — `-index` where to go, `-tokens` what exists, `-rules-ai` what's allowed, `-audit` why, `-ledger` the raw evidence, `-eval` the check on the ruleset. A generating agent reads `-rules-ai` and nothing else. The full table is in `README.md`.

## Git — one task, one commit

**This overrides Gabriel's personal `~/.claude/CLAUDE.md`, which says one task,
one branch, and to wait for his go before every push.** Agreed with him on
9 September 2026. It applies to this repo only; his other projects are unchanged.

**Why the override.** He is the sole owner, works alone, and nothing here is
reviewed, tested or deployed. Branches were solving problems this repo doesn't
have — and had actively caused some: sessions parked on finished branches, a
merge landing mid-write. The task loop already provides what a branch provided:
small units, each verified before it lands.

**Work directly on `main`.** No branches, no pull requests, unless a task is big
enough that Gabriel might want to throw the whole thing away — say so and ask
first when that's the case.

### What happens automatically

| When | Do this |
| --- | --- |
| `/task-check` **passes** | Commit, then push. One task, one commit. No permission needed |
| `/task-check` **fails** | **Commit nothing.** Tell him plainly the work is not yet saved. Fix, re-check, then one clean commit |

Commit and push are safe to automate because they only ever **add** — nothing is
overwritten or lost. He approved the task before it started and the check
verified it; asking a third time is the ceremony he asked to be rid of.

### What always asks first

Never do any of these without his explicit go, every time:

- Undoing something (`git revert`)
- Deleting a branch
- Anything that rewrites history — `force-push`, `reset --hard`, rebasing
  anything already pushed
- Merging a branch into `main`

### Commit messages

One line, imperative, saying what changed and why it mattered. The backlog's
done list is the readable record; the commit message is the pointer.

**Never let unpushed work accumulate.** If a session ends with anything
uncommitted, say so explicitly.

## Working conventions

- **Never invent** Confluence page IDs, Figma keys, or Atlassian cloud IDs. Read
  them from the registry JSON files, or resolve them live via the
  Atlassian/Figma MCP tools.
- **Graphify is not used in this repo**, even though the skill is installed
  globally and will offer itself. Retired 11 September 2026: it cost 990,970
  tokens to maintain a graph over a 172,818-word corpus — 4.2× what reading the
  whole repo costs — and was queried once. This repo is already hand-indexed by
  the filename grammar, the two routing pages and the table above. The graph and
  its config are archived at
  `~/Desktop/ai/gsl-ds-graphify-archive/`, and the reasoning is in
  `project/decisions.md`. Don't rebuild it without a deliberate reason.
- **The Zeroheight MCP connector is never used** by any skill, even if it shows
  as connected in a session. Exports come from a Confluence-staged code block,
  or a human chat-paste as fallback.
- **The four `figma-sync-*` skills never read or write Confluence** — the
  `figma-*-registry.json` files are their sole source of truth.
- **When a check disproves an audit, propose fixing it in the same task** —
  don't file it as a backlog row for later. An `-audit`, `-ledger` or `-eval`
  file describes the system, so a figure now known to be wrong is simply wrong,
  and the next reader is misled by a file that still looks authoritative. Say
  what you found, say what you'd change, and **wait for Gabriel's go like any
  other file change** — this convention decides *when* the correction is raised,
  never whether it needs approval. Once approved, say what changed and when,
  inside the file. **The decision log is the exception and is never rewritten**
  — `project/decisions.md` records what was believed on a date, and correcting
  it destroys the only thing it is for.
- **Don't create a per-tier Figma skill.** `figma-sync-component-sets` handles
  Components, Patterns, Experiences and Foundations' real components — extend it
  instead. Foundations' Tokens (`figma-sync-tokens`) and Icons
  (`figma-sync-icons`) are different content shapes and stay outside its scope.

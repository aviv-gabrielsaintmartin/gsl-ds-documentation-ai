---
name: generate-and-score
description: Run one compliance run end to end — open the run folder, save the brief before anything is built, have one agent build the screen in Figma, have a second cold agent score it against the scorecard, then append both ledger rows. Triggers on "/generate-and-score", on a pasted brief for a screen to build, or on a request to run, generate or score a design against the GSL Design System.
metadata:
  author: Aviv
  version: "1.0.0"
  status: draft — written 2026-09-14, never yet run
---

# Generate and score

Runs **one run**, end to end.

**This skill orchestrates. It never builds and it never scores.** Both halves are
done by subagents, and they must be two different ones.

```
  YOU paste a brief
        │
        ▼
  1. OPEN THE RUN     next run number · folder created · brief saved
        │             ← nothing is built before the brief is on disk
        ▼
  2. BUILD            subagent one · has Figma · reads the rulesets
        │             writes ## Declarations into the report
        ▼
  3. SCREENSHOTS      what the screen actually looked like
        │
        ▼
  4. SCORE            subagent two · fresh · has never seen subagent one
        │             writes the report FOR GABRIEL — verdict first —
        │             then appends both ledger rows itself
        ▼
  5. CHECK            the two ledger rows exist. You never write them
        │
        ▼
  6. REPORT BACK      three lines to Gabriel
```

## The rule this skill exists to enforce

**The agent that scores is never the agent that built.**

A building agent can read the scorecard, so it knows every question before it is
asked. Ask it to report on its own work and it reports truthfully and
selectively — it never has to state a falsehood to produce a flattering picture.
It only has to choose what to mention.

Two consequences, and neither is optional:

- **Subagent two is started fresh.** Never a fork, never handed this
  conversation, never allowed to ask subagent one anything.
- **Its prompt carries a pointer and nothing else.** The run folder path and the
  Figma frame to open. Never what was built, never what subagent one said,
  never a hint about what the answers should be.

If you find yourself explaining the screen to the scorer, stop. That is the
failure this whole arrangement exists to prevent.

**Subagents are authorised here.** Gabriel's personal rules say not to spawn one
unless he asked. He asked for exactly this shape on 14 September 2026 — one
orchestrating chat, one building agent, one scoring agent.

## Before you start

| Precondition | If it is missing |
| --- | --- |
| **The FigCli plugin is running, on the right file** | **Ask Gabriel to start it** — `Plugins → Development → FigCli` — then wait. Only he can. Do **not** stop and ask him to move to another session: this precondition used to read *the session can reach Figma Desktop Bridge, it is running off `~/.claude/` not `~/.claude-personal/`*, and that was wrong twice over. The Desktop Bridge is retired, and **`figma-cli` is machine-wide — it does not care which config root a session booted from.** Corrected 2026-09-14, after the old gate would have turned away a session that could do the work |
| **Both checks pass, and they are different checks** | `cd ~/figma-cli && node src/index.js status` tests the **daemon**; `node src/index.js eval 'JSON.stringify({name: figma.root.name})'` tests the **plugin** and names the open file. `✓ Daemon running` on its own proves nothing. **`Error: fetch failed` means the plugin is detached, not that the daemon is down** — and the usual cause is Figma switching files, which stops the plugin mid-run |
| **The building agent draws through `figma-cli`; the scoring agent reads through the Dev Mode MCP** | Two channels, and the split is deliberate. `figma-cli` (`~/figma-cli`, not on PATH) is far cheaper in tokens and quicker to draw with, so it builds. The **Dev Mode MCP** at `127.0.0.1:3845/mcp` is official, read-only and an **independent** channel — so a scorer using it is not trusting the tool that made the screen. Neither agent should verify its own writes through the channel that made them |
| A brief exists — pasted, or already a file | **Stop and ask for it.** Never write one yourself |
| Gabriel has said go | **Stop.** A run writes files. Ask once, here, then write the run's own artefacts without asking again |

## Step 1 — open the run

**Do this before anything is built. It is the step whose absence lost two runs.**

1. Read `compliance/runs/`. The next run number is the highest existing one plus
   one, three digits. **Never reuse, never renumber.**
2. Create `compliance/runs/run-NNN/`.
3. Save the brief **verbatim** as `prompt-run-NNN.md`. Never reword it, never
   tidy it, never fill a gap in it.
4. Tell Gabriel the run number before going further.

A brief saved after the screen exists is not a brief. It can be quietly reworded
to match whatever came out, and then the run proves nothing.

## Step 2 — build

Spawn **one** subagent. Give it:

- The path to `prompt-run-NNN.md`.
- **What to read:** `components/components-rules-ai.md` and the token rulesets
  under `tokens/*/`.
- **What not to read:** anything in `compliance/`. The scorecard is written for
  the agent that judges the output, and a builder that has read it is building
  against the marking scheme.
- **What to write:** the `## Declarations` section of
  `compliance/runs/run-NNN/report-run-NNN.md`, before it finishes — one block
  per element it built by hand. A run that invented nothing still writes the
  section, reading `_None._`.
- **What to report back:** the Figma file, page and frame it drew into, and the
  frame's node ID. That pointer is all subagent two will get.

**Paste the declaration format into the builder's prompt. Do not send it to the
scorecard to find it** — that file is the marking scheme, and a builder that
opens it for the template has read the questions.

```markdown
## Declarations (N)

### <short name for what was built>

| | |
| --- | --- |
| **What was built** | … |
| **Problem it belongs under** | … one of Which component's problems |
| **Ruled out** | `Component` — why · `Component` — why |
```

**All three fields are required.** A declaration missing one counts as absent,
and absent is a failure.

**Declarations are written before scoring, and never revised after.** A
declaration edited once the verdict is known is not a declaration.

## Step 3 — screenshots

The run needs images of what the screen actually looked like. A Figma file keeps
changing; a screenshot does not.

- Ask subagent one to export them into the run folder if it can.
- If it cannot, ask Gabriel to take them.
- **A run without screenshots is unfinished.** Do not proceed to scoring and
  call it done — say plainly that the run is incomplete.

Screenshots keep descriptive names — `block-1-energy-and-conditions.png` — not
run numbers. What you are looking at matters more than which run drew it.

## Step 4 — score, cold

Spawn a **second** subagent. Fresh. Give it exactly:

- The run folder path.
- The Figma frame pointer from step 2.
- The instruction to read `compliance/compliance-scorecard.md` and answer every
  question in it, including the steps that have none.
- The instruction to write the report into `report-run-NNN.md`, **in the order
  the scorecard's template gives** — verdict, decisions, answers, then the
  builder's declarations, then the evidence.
- The instruction to **append both ledger rows itself** when the report is done.
- **Never edit the `## Declarations` section.** It writes above and below that
  section. It reads it to answer *was anything hand-built without a complete
  declaration?* and changes nothing in it.

Give it nothing else. In particular, give it nothing about what was built.

## Step 5 — check the ledgers were appended

**The scoring agent writes both ledger rows, not you.** It holds the findings and
the counts; anything else re-derives them from the report, and a copy step
drifts. Both ledger files say the same — *written by the checking agent*.

Your job here is to **verify the two rows exist**:

- `compliance/compliance-run-ledger.md` — one row for the run.
- `compliance/compliance-flag-ledger.md` — one row per item the report lists
  under *Decisions you need to make*, failures included, not only flags.

**A run is unfinished until both rows exist.** If they are missing, send the
scoring agent back. Never write them yourself from the report — that is the copy
step the rule exists to prevent.

**This step exists because the first run lost it.** Step 4 said *"give it nothing
else"*, step 5 read as the orchestrator's job, and both ledger files said the
checking agent's. Three files, two answers, so nobody appended anything.

The **wireframe** label comes from the brief and is reused verbatim for every run
of that brief. Two runs are only comparable when it matches.

## Step 6 — report back, and save

Three lines to Gabriel: the run number, what the scorer found, where the report
is. Never paste the whole report into chat.

**The report is written for him**, so it opens with a verdict and the decisions
he has to rule on. If it opens with node IDs or a technical walk, the scoring
agent used the wrong order — send it back rather than summarising around it.

Then commit and push the run folder and both ledger rows. This only ever adds —
same reasoning as `/task-check`, written out in `CLAUDE.md`.

## What this skill never does

- **Never builds and never scores.** If you are tempted to answer one question
  yourself because it is obvious, you have become the scorer.
- **Never lets one agent do both halves**, however small the screen.
- **Never reuses or renumbers a run number.**
- **Never edits a declaration**, and never writes one on a builder's behalf.
- **Never records a run as finished** while the folder is missing the brief, the
  screenshots or the report.

## Known gaps

Stated so nobody reads this file as more finished than it is.

- **This skill has never been run.** Everything below the diagram is reasoning,
  not experience. Expect the first run to find defects in it, and fix them here
  rather than working around them.
- **The scoring agent is Figma-only.** A second platform needs a second scoring
  agent. The questions carry over unchanged; the agent answering them does not.
- **Nothing is stored but the report.** There is no facts file, by decision on
  14 September 2026. A question changed later cannot be re-run against an old
  screen.
- **Nothing checks that a report's answers match its ledger row.** Two files,
  kept in step by hand.

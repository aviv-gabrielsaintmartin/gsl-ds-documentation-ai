---
name: task-check
description: Check whether the task just done actually worked, then either log it and name the next task, or create a sub-task to fix it. Second half of Gabriel's do-check-next loop; updates status.md and project/backlog.md. Triggers on "/task-check", "did that work", "check the task", or a request to verify and close out the last piece of work.
metadata:
  author: Aviv
  version: "1.0.0"
  status: production
---

# Task — check

The second half of the loop. Answers one question: **did that actually work?**

```
   we check it worked
          │
     ┌────┴────┐
    yes        no
     │          │
     ▼          ▼
   log it    sub-task to fix it ──┐
     │                            │
     └────►  next task  ◄─────────┘
```

## Step 1 — verify it yourself first

**Verification is not a question to ask Gabriel.** Decide the depth, run it,
report what it found. Only bring him the result.

Check the actual thing, not the intention:

| Kind of task | How to check it |
| --- | --- |
| A rule was written for an agent | Read it back cold. Could an agent act on it with nothing else? |
| A file was moved or restructured | Every link that pointed at it still resolves |
| Something was deleted | Nothing left in the repo describes it as still present |
| A registry was synced | Spot-check entries against the live source |

If a claim can't be verified, say so plainly rather than reporting it as done.

## Step 2 — report the verdict

Three lines. What was checked, what was found, pass or fail. Include the
evidence — the count, the file and line, the command output. Never a bare
"done".

**Report failure as clearly as success.** A check that only ever passes is not a
check.

## Step 3a — if it worked

1. Log it. One line in `project/backlog.md`, moved to the done list with the date.
2. Update `status.md` — the current task becomes done, the next one moves up.
3. **Commit and push.** One task, one commit, straight to `main`. No permission
   needed — see the git section of `CLAUDE.md`. Commit and push only ever add,
   so nothing can be lost; he already approved the task and the check just
   verified it.
4. **Refresh the knowledge graph — only when the task changed a file other
   than `status.md` and `project/backlog.md`.** If it changed nothing else,
   skip this step and say nothing. Check with `git show --stat HEAD`.

   When it did, invoke the **graphify skill** with `--update`. Not the shell
   command.

   **Why not `graphify update .`, which this step used to say.** That command
   does a structural pass only — it prunes filenames that disappeared and picks
   up new ones as heading-level nodes. It never re-reads what a file *says*, so
   on a task that rewrites a rule without moving a file it reports "no
   code-graph topology changes" and leaves `graph.json` untouched. The tool says
   so in its own output: *"For doc/paper/image changes run `/graphify
   --update`."* That was a deliberate trade when this step was written on
   10 Sep 2026 — honest about what exists, uninformed about what changed.
   Gabriel upgraded it the same day: almost every task here rewrites content
   without moving a file, which is precisely the case the structural pass
   cannot see.

   Say one line if it reports anything; say nothing if it's quiet.

   **This costs real tokens, and that is why it is conditional.** Measured
   10 Sep 2026, not estimated: an update over **15 changed files cost 176,040
   tokens** — roughly 11,700 a file. That is about double what the files' own
   word count predicts, because the figure includes the extraction agent's
   reasoning and tool calls, not just the reading. Budget from the measured
   number, never from file size. An update re-reads each changed file **whole**;
   there is no diffing.

   That is why `status.md` and `project/backlog.md` are in `.graphifyignore`
   and why this step is skipped when they are all that changed. Nothing looks
   them up through the graph — every session opens them directly — so they cost
   on every task and return nothing. Even with both guards a task that edits one
   ruleset still costs on the order of **10,000–30,000 tokens**. Tasks that
   touch only the two ignored files cost nothing.

   **If it still feels expensive, take this step out of the loop and refresh
   the graph by hand before querying it.** A graph rebuilt deliberately is
   fine; one that taxes every task is not. Say so rather than quietly skipping.

   **Never delete `graphify-out/`.** The cache lives inside it, and deleting it
   turns the next run from a few thousand tokens into roughly 800,000 — that is
   what a full rebuild of this repo costs. If the graph ever looks wrong, say so
   and let Gabriel decide; do not rebuild it to be safe.

   **Skip this step, and say you skipped it, when the skill isn't loadable** —
   a session on a config root other than `~/.claude/` has no personal skills at
   all. Background sessions **do** load it; that was assumed otherwise until it
   was tried on 10 Sep 2026. Never a reason to stop; the graph is a working
   aid, not part of what this repo delivers.
5. Name the next task in one sentence. Do not start it. Take the top item from
   *I can start these today* in the backlog — that list is sorted by what goes
   wrong if we don't fix it, and the rule is written above it. If the task just
   done changed what's now most damaging, re-sort the list before naming one.
6. Tell him to start it **in a new conversation** with `/task-next`. One task,
   one chat — a session that built something is the worst judge of it.

## Step 3b — if it didn't

1. **Commit nothing.** Say plainly that the work is not yet saved.
2. Write the sub-task: what specifically failed, and what would fix it.
3. It becomes the **next** task, above everything else.
4. Do not attempt the fix in this turn. Propose, then wait.

If he wants to stop for the day with a check still failing, commit then — losing
a day's work is worse than an imperfect commit. Ask him first.

A failed check is normal and is information. Do not apologise for it, do not
re-litigate the original task, and do not quietly widen the fix.

## Step 4 — sweep the findings

### First, correct what this task falsified

**Re-read the backlog before adding anything to it.** A task that changes a file
usually changes what some other row claims about it — a count, a filename, a
"this is already answered", a blocker that is no longer blocking. Those rows are
what Gabriel reads to decide what happens next, so a stale one points the next
session at the wrong thing.

Only check rows about files this task touched. That keeps it a minute's work
rather than an audit, and it is where the staleness actually collects.

| What you find | What you do |
| --- | --- |
| A stale row in `status.md` or `project/backlog.md` | **Correct it.** Those two are the standing exception — always writable |
| A stale claim in any other file — a ruleset, an audit, a README repeating something this task disproved | **Report it and ask.** Finding it is the job; editing it is not, until he says so |

### Then add what's new

Ask: **did anything surface during this task that isn't recorded?** Each one goes
into `project/backlog.md` as exactly one of three:

| Kind | Where it goes | Example |
| --- | --- | --- |
| **I can fix it** | Task list, marked *proposed* | "Move the radius rules into the file agents read" |
| **Only Gabriel can decide** | Question list, with a recommendation | "Should this component be added to the Figma libraries, or composed?" |
| **Neither — just true** | Note list, closed | "The radius rules already existed and were verified" |

This is the step that stops findings from evaporating into chat. It is not
optional, and it is why Gabriel asked for this skill.

## The rules that make this readable

- **No codes, ever.** Describe things by what they do.
- **Plain language, short sentences, tables for comparisons.**
- **`status.md` never exceeds one screen.** Overflow goes to the backlog.
- **Never report something as done that wasn't verified.**

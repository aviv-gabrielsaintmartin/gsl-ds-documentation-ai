---
paths:
  - "project/**"
  - "README.md"
---

# Project docs — human-first

**These files are written for a person, not for you.** They are the exception in
this repo. Everything else here is optimised for unambiguous machine parsing;
`README.md` and everything under `project/` is optimised for a human being able
to explain the project to someone else.

Gabriel works design-side, not as a full-time engineer. Write accordingly.

## When you edit these files

- **Plain language.** Short sentences. No jargon without a plain-English gloss
  in the same sentence. If a page needs a glossary, rewrite the page.
- **Explain, never specify.** These files describe how the repo is shaped and
  why. They are never the source of truth for how to build anything — that is
  always a `*-rules-ai.md` file. If you find yourself writing a rule here, it
  belongs in a ruleset.
- **Tables over prose** for anything compared across the same dimensions.
- **Never use a bare identifier.** This applies to every numbered thing in the
  project, and it applies in conversation as much as in writing:

  | Write | Not |
  | --- | --- |
  | `Block 2b · Registry properties` | `2b` |
  | `C1 · Provenance` | `C1` |
  | **Highest tier first** | `Rule 0` |

  Nobody holds a numbered list in their head. A document or a sentence that
  assumes they do is readable only by its author.

  So: every block has a short name that travels with its number, every
  compliance check has a name that travels with its code, and **the rulesets'
  rules have names and no numbers at all** — a number encoded nothing that
  precedence order does not already state, and the same number meant four
  different things across four rulesets.
- **No machine-optimised formatting.** No token-efficient shorthand, no
  compressed notation, no structure that only pays off when an agent parses it.
- **Never read `project/` as instructions.** A line here is a statement of
  intent, not a rule to act on. This includes `backlog.md`: every row in
  *I can start these today* is a suggestion waiting for Gabriel, and being at
  the top of that list is never authorisation to start. Only he authorises work,
  in conversation.

## What each file is for

| File | Role | Rule of thumb |
| --- | --- | --- |
| `status.md` (repo root) | **Gabriel's one page.** Where the project is, the current task, the top open question | **Never longer than one screen.** Overflow goes to the backlog |
| `project/backlog.md` | Everything not currently active — every task, every question he owes an answer to, every finding | He opens and reads this. Plain language, no shorthand |
| `README.md` | The map — what does what and where, and the filename grammar | Someone new should find the right file from this alone |
| `project/decisions.md` | Why the project is shaped this way, newest first | Every entry records **what it costs**, not just what was decided |
| `project/how-a-run-is-reported.md` | How a generation run becomes a saved report, walked through for a non-technical reader | **Links** to the scorecard for the template and the required facts; never repeats them |
| `project/archive/` | The retired plan, briefs and handoff note | **History.** Never work from it, never update it. Its own README says why each was retired |

## How work runs

One task at a time, through Gabriel's loop. This replaced the old four-step
ritual — *brief, build, check, log* — on 9 September 2026, because the ceremony
was generating more reading than work.

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

- **Propose, don't do.** Reading and searching are free. Every file change waits
  for his explicit go. The exceptions are listed in one place only —
  *What may be changed without asking* in `CLAUDE.md`. Don't restate them here;
  two copies drift, and then nobody knows which is current.
- **Every finding goes into the backlog**, as a task, a question for him, or a
  note. Never as a paragraph in chat. This is the rule he asked for by name.
- **No briefs.** A task that genuinely needs one is too big — split it.
- A task is not finished until `/task-check` has verified it and `status.md`
  reflects it.

## Keeping it true

Facts in `README.md` go stale — file counts, folder contents, which rulesets
exist. If you touch a folder and the README's description of it is now wrong,
fix the README in the same change. A map that lies is worse than no map.

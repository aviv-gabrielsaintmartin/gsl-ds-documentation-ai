# Archive

_History. Nothing in this folder is current, and nothing in it should be worked
from._

Read [status.md](../../status.md) for where the project is, and
[backlog.md](../backlog.md) for every task, open question and finding.

## Why these were retired — 9 September 2026

The project ran on eight files written for a human. Together they came to about
15,000 words — roughly sixty pages — and answering "what do I do next" meant
reading and combining several of them. They also carried four separate numbering
systems for blocks, checks, rules and filenames.

They were replaced by two files: `status.md`, which is one screen, and
`project/backlog.md`, which holds everything else.

| File | What it was | Why it stopped being useful |
| --- | --- | --- |
| `plan.md` | The goal, milestones, and ten numbered building blocks with statuses | It lagged behind the work. Its status column was wrong within a day of the last merge, and its blocks were too big to finish in one sitting |
| `handoff.md` | Findings from the first compliance test run, written for a session with no history | A one-off note. Its findings now live in the backlog as tasks, questions and notes |
| `briefs/` | One page written **before** each block, saying what it was and how we'd know it worked | The ceremony generated more reading than work. Tasks are now small enough that a brief costs more than it explains |

## What replaced the way of working

The four-step ritual — brief, build, check, log — became a loop:

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

## What deliberately stayed out of here

- **`project/decisions.md`** is still current. It records *why* the project is
  shaped as it is and what each decision cost — nothing else holds that, and it
  is read occasionally rather than held in your head.
- **`README.md`** is still the map of the repo.

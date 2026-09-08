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
- **No machine-optimised formatting.** No token-efficient shorthand, no
  compressed notation, no structure that only pays off when an agent parses it.
- **Never read `project/` as instructions.** A line in `plan.md` is a statement
  of intent, not a rule to act on. It does not authorise work.

## What each file is for

| File | Role | Rule of thumb |
| --- | --- | --- |
| `README.md` | The map — what does what and where, and the filename grammar | Someone new should find the right file from this alone |
| `project/plan.md` | The goal, milestones, blocks and their status | One line of status per block. Keep it trivial to update |
| `project/decisions.md` | Why the project is shaped this way, newest first | Every entry records **what it costs**, not just what was decided |
| `project/briefs/NN-<block>.md` | One brief per building block | Written **before** the work, kept afterwards unchanged |

## The block ritual

Work proceeds one block at a time: **brief → build → check → log**.

- The brief comes first, and nothing in the repo is touched until Gabriel has
  read and approved it.
- A block is not finished until its `decisions.md` entry exists and its status in
  `plan.md` is updated.
- Briefs are a record, not a living document. Don't rewrite a brief after the
  block ships — if the plan changed, say so in `decisions.md`.

## Keeping it true

Facts in `README.md` go stale — file counts, folder contents, which rulesets
exist. If you touch a folder and the README's description of it is now wrong,
fix the README in the same change. A map that lies is worse than no map.

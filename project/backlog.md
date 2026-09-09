# Backlog

_Everything that isn't the current task. Written for Gabriel to read — open it
whenever you want the whole picture. `status.md` holds only what's active._

_Nothing here is started without approval. Updated 9 September 2026._

---

## Tasks — things I can do

Top of the list is next — the order **is** the priority, so there are no numbers
to remember. **Proposed** means waiting for your go.

| What | Why it matters | How long | Status |
| --- | --- | --- | --- |
| Move the corner-radius, shadow and border-thickness rules into the file agents are allowed to read | The agent guesses radii and uses no shadow. The rules exist and are verified — they're just in the wrong file | Half a day | **Approved — next** |
| Record the Figma text-field names for each component | The agent can place a component but cannot put words into it from the docs alone. Every string in the test came from reading Figma live | A day. **Needs Figma Desktop open** | Proposed |
| Archive the eight old human-facing files, `project/plan.md` among them | They're what made this project unreadable. Kept, moved out of the way, never deleted | An hour | Proposed |
| Fix the "Legend" entry — it's a setting on a chart, not a component you pick | The rules currently tell an agent to place something that can't be placed. Our own mistake, from the third round of testing | An hour | Proposed |
| Fix the three component entries that dead-end into a file agents are forbidden to open | The highest-priority rule in the whole system points nowhere for three cases | Half a day | Proposed |
| Add a routing entry for "a block of controls that computes a live result" | A mortgage simulator is a recurring product pattern and nothing routes an agent to it. In the test the agent hand-built one and said it couldn't tell whether it should have | Half a day | Proposed |
| Extend the "when nothing fits" rule to cover *exists, is correct, and doesn't fit* | The donut chart is 373px wide inside a 360px frame. The agent switched off a mandatory part and broke no rule | Half a day | Proposed |
| Widen the `audit` branch category to cover compliance runs | It currently names only one skill. Small, clerical | Ten minutes | Proposed |
| Write up the test run properly | Findings are safe in `project/handoff.md` for now | Half a day | **Parked** |
| Check the page-layout rules against real screens | Margins and rhythm are written but never verified | Unknown | **Blocked** — needs you to name 3–5 Figma screens |

---

## Questions — only you can answer these

Around two dozen, collected from the audit files where they'd been piling up
unseen. I'll bring them **one at a time**, with a recommendation. Listed here so
you can see the whole set.

### The heavy one

| Question | Why it matters |
| --- | --- |
| **Who owns the energy-rating (DPE) colours, and what should an agent do when a legally required element has no compliant component?** | French listings must show a seven-step energy scale. No GSL component does it, the colours belong to another team, and our own rules send agents to a colour family they also forbid. In the test the agent shipped a grey ladder |

### About components

| Question |
| --- |
| `Image Ratio` and `Brand Logo` exist in two libraries under different keys — which should an agent use? |
| Seven components can be selected but are described nowhere. What are they for? |
| Is `Badge` something you pick on its own, or only ever attached to a host? |
| Is `Filter button` pickable on its own, or only inside `Filter bar`? |
| `Tab Bar` is being rebuilt — confirm agents should not use it meanwhile |
| `Footer` is Figma-only and owned by another team — confirm it stays out of scope |
| Is `Flag` just an asset, or a real component for country and locale? |
| Four documented components are missing from the selection guide |
| Does anything follow "Identity and media" on the live Confluence page? |
| 24 components can be selected but have no documentation and no routing entry. Add entries for them? |
| `Floor selection` has one named part and needs two to qualify. What's the second? |
| How do we catch an agent that hand-builds an empty state instead of using the real one? |

### About colours

| Question |
| --- |
| Should borders gain a genuinely transparent token? |
| What exactly belongs to the `Decorative` colour family? Its boundary is too vague to apply |
| Two surface colours (`Accent/Light` and `Active`) resolve to the same value — deliberate? |
| The colour table still needs completing against Figma |

### About text, shadow, borders and grid

| Question |
| --- |
| No rule separates the two middle shadow levels. Both are used by similar floating components |
| The `Display` text style was never seen on any screen we sampled. Is it actually used? |
| Does the "emphasis plus container size" mechanism hold beyond the three screens checked? |
| A text style renders differently from its recorded value — worth telling whoever owns that Figma file |
| `Energy tag`'s border can't be confirmed; the Figma link we were given pointed at `Checkbox` |
| Is it still true that there's no live grid layout system? |

---

## Notes — recorded, no action needed

Things that turned out to be true and are worth not rediscovering.

| Date | Note |
| --- | --- |
| 9 Sep 2026 | **Only three files knew about the new way of working** — `CLAUDE.md`, `status.md` and this one. The rules file for `project/` still specified the old four-step ritual and loads automatically, so a future session would have been handed the old process. Became the next task |
| 9 Sep 2026 | **The corner-radius and shadow rules already existed and were already verified** — radius against nine components and three screens, shadow against eight components. The gap was only that they sit in files agents are told not to read as rules. Turned that task from research into moving text |
| 9 Sep 2026 | Twelve brand PDFs in `design-language/` were deleted by another session; Gabriel confirmed the removal. The folder is gone |
| 9 Sep 2026 | `status.md` is at 846 words against a one-screen budget of roughly 900. The next thing added to it should push something else out to this file |
| 9 Sep 2026 | The eight human-facing files totalled 15,400 words — about 60 pages. That, not the 120 machine files, is what made the project unreadable |

---

## Done

| Date | What |
| --- | --- |
| 9 Sep 2026 | **Git simplified: one task = one commit, straight to `main`.** No branches, no pull requests. A passing check now commits and pushes automatically; undoing, deleting and rewriting always ask first. Overrides Gabriel's personal one-task-one-branch rule, for this repo only. `audit/run-001` merged into `main` and deleted; `main` is now the only branch |
| 9 Sep 2026 | The repo now describes the new way of working — the rules file for `project/` carries the loop instead of the old ritual, `README.md` opens on `status.md`, and the plan, briefs and handoff note are marked superseded. Verified: 27 links resolve, no stale skill count, no surviving instruction to write briefs |
| 9 Sep 2026 | `status.md` created — one page replacing eight |
| 9 Sep 2026 | `design-language/` removed, and the two files that described it corrected |
| 8 Sep 2026 | The rules in all four rulesets lost their numbers and gained names |
| 8 Sep 2026 | The component parts list became machine-readable |
| 8 Sep 2026 | The compliance scoring sheet written |
| 8 Sep 2026 | Component selection written and tested cold, three rounds |

# Backlog

_Everything that isn't the current task. Written for Gabriel to read — open it
whenever you want the whole picture. `status.md` holds only what's active._

_Nothing here is started without approval. Updated 10 September 2026._

---

## Tasks — things I can do

### How these are sorted

The objective is an agent that designs a compliant screen with **nobody having
to correct it**. So a task's worth is how badly the thing it fixes breaks that.

| What goes wrong today | Why it ranks there |
| --- | --- |
| **It ships wrong, and breaks no rule doing it** | Worst. Non-compliant output leaves with confidence, and you only catch it by opening the screen and looking. Exactly the failure this project exists to prevent |
| **It stops, or asks** | Real, but it announces itself. Nothing wrong ships — you just had to step in, so "nobody corrects it" still failed |
| **The output doesn't change at all** | Only our own files are affected. Worth nothing on its own |

Then how often it comes up, then how long it takes. A silent failure on every
listing beats one on a rare screen.

**Fear the ones where the agent breaks no rule.** A stuck agent tells you it's
stuck. A confidently wrong one doesn't.

Nothing here is started without your go.

### I can start these today

| What | What goes wrong today | How often | How long |
| --- | --- | --- | --- |
| Extend the "when nothing fits" rule to cover *exists, is correct, and doesn't physically fit* | **Ships wrong, breaks no rule.** The donut chart is 373px wide inside a 360px frame. The agent switched off a mandatory part of it and broke no rule doing so | Any chart in a narrow column — so all of mobile | Half a day |
| Fix the "Legend" entry — it's a switch on a chart, not a component you pick | **Stops or asks.** All three charts expose the legend as an on/off property and the underlying piece is private in Figma. The rules tell an agent to go and place it. It cannot be placed | Any chart with two or more series | An hour |
| Add a routing entry for "a block of controls that computes a live result" | **Stops or asks.** In the test the agent hand-built a mortgage simulator, then said it couldn't tell whether it should have | A recurring product pattern | Half a day |
| Fix the three component entries that dead-end into a file agents are forbidden to open | **Stops or asks.** The reuse-before-invention rule — the first one an agent applies — points nowhere for three cases | Unknown until we look at which three | Half a day |
| Test the three new rulesets on a cold reader | Neither — it **finds** problems rather than fixing any. Same method found twelve defects in component selection. Run it *after* the fixes above, or we test rulesets we're about to rewrite | — | Half a day |

**The first and third may be one fix.** Both are "the thing I need isn't
available in the form I need it", and both land on the same fallback rule. Worth
checking before treating them as two half-days.

**Removing the leftover rule numbers in the spacing ruleset is not on this
list.** The file still says "Rules 6 and 7 are unverified" and "Rules 3–5" after
the renaming, which is untidy, but an agent's output doesn't change. It's a
rider on whatever next opens that file, not a task.

### Something is in the way

| What | What goes wrong today | What's in the way | How long once clear |
| --- | --- | --- | --- |
| Decide who owns the energy-rating (`Scale`) colours, and what an agent does with them | **Ships wrong, breaks no rule — the highest-impact item on this whole page.** In the test the agent produced a grey energy ladder: technically compliant, legally and visually wrong | **Your research.** The 19 colours exist in Figma and are fine. What's missing is a written decision. See the question below | Half a day |
| Record the Figma text-field names for each component | **Ships wrong, breaks no rule.** An agent can place a component but has no way to put words into it, so it ships with the default placeholder text still in place — which breaks nothing. Every string in the test came from reading Figma live, not from this repo | **A session with the Figma connector switched on.** Not just Figma Desktop being open — the bridge tools have to be live. Worth checking before starting, not after | A day |
| Check the page-layout rules against real screens | Unknown, and that's the problem — margins and rhythm are written but have never been checked against a real screen | **You naming 3–5 Figma screens** to check them against | Unknown |
| Write up the test run properly | The output doesn't change. Findings are already safe in `project/archive/handoff.md` and in this file's notes | Nothing — you parked it | Half a day |

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
| 9 Sep 2026 | **"Widen the `audit` branch category" was deleted from the task list, not done.** It only ever named one skill, and branches are gone from this repo entirely. Recorded here in case it ever needs bringing back |
| 9 Sep 2026 | **The Figma Desktop Bridge tools are not connected in this session** — no `figma_get_status` / `figma_execute` available at all. The text-field-names task needs more than Figma Desktop being open: it needs a session where that connector is on. Worth checking before starting it, not after |
| 9 Sep 2026 | Corner radius is applied in Figma as a plain number, never as a bound variable — confirmed across the component library and three real screens. A generating agent must set the value, and a checker must not flag it as an unbound token |
| 9 Sep 2026 | Border thickness has no separate evidence file; its rules come from the notes inside its own token page. Honest, but it is the one ruleset without a sibling audit |
| 9 Sep 2026 | The "Newest" sort control on the real results-list screen is a hand-built frame, not a real Button — spotted during the radius audit. Exactly the failure this project exists to prevent, in a shipped screen |
| 9 Sep 2026 | **Only three files knew about the new way of working** — `CLAUDE.md`, `status.md` and this one. The rules file for `project/` still specified the old four-step ritual and loads automatically, so a future session would have been handed the old process. Became the next task |
| 9 Sep 2026 | **The corner-radius and shadow rules already existed and were already verified** — radius against nine components and three screens, shadow against eight components. The gap was only that they sit in files agents are told not to read as rules. Turned that task from research into moving text |
| 9 Sep 2026 | Twelve brand PDFs in `design-language/` were deleted by another session; Gabriel confirmed the removal. The folder is gone |
| 10 Sep 2026 | `status.md` is back inside its one-screen budget at 897 words, after the three git commands were cut. The next thing added to it still has to push something else out |
| 10 Sep 2026 | **`internal/git-basics-tutorial.md` is about branches, which this repo stopped using on 9 Sep.** Starting a topic, worktrees, which branch a chat is on — none of it applies any more. It also only ever covered `git status`, not `git log` or `git revert`. Nothing depends on it, so nothing is broken, but it now describes a workflow that no longer exists |
| 9 Sep 2026 | The eight human-facing files totalled 15,400 words — about 60 pages. That, not the 120 machine files, is what made the project unreadable |

---

## Done

| Date | What |
| --- | --- |
| 9 Sep 2026 | **The retired files moved to `project/archive/`** — the old plan, the handoff note and all four briefs, with a README saying why each was retired. `decisions.md` and `README.md` deliberately stayed: one holds why the project is shaped this way, the other is the map |
| 9 Sep 2026 | **One task, one chat** — each task starts in a fresh conversation. Written into `CLAUDE.md`, `status.md` and the check skill. Not about context limits; a session that built something is the worst judge of whether it reads clearly to someone who wasn't there |
| 9 Sep 2026 | **Corner radius, shadow and border thickness now have rulesets** an agent is allowed to read — seven of twelve token kinds covered, up from three. Verified: every value matches its token page, 57 links resolve, and all three failures from the test run are now answered, including "a card is not elevated, give it a border" |
| 9 Sep 2026 | **Git simplified: one task = one commit, straight to `main`.** No branches, no pull requests. A passing check now commits and pushes automatically; undoing, deleting and rewriting always ask first. Overrides Gabriel's personal one-task-one-branch rule, for this repo only. `audit/run-001` merged into `main` and deleted; `main` is now the only branch |
| 9 Sep 2026 | The repo now describes the new way of working — the rules file for `project/` carries the loop instead of the old ritual, `README.md` opens on `status.md`, and the plan, briefs and handoff note are marked superseded. Verified: 27 links resolve, no stale skill count, no surviving instruction to write briefs |
| 9 Sep 2026 | `status.md` created — one page replacing eight |
| 9 Sep 2026 | `design-language/` removed, and the two files that described it corrected |
| 8 Sep 2026 | The rules in all four rulesets lost their numbers and gained names |
| 8 Sep 2026 | The component parts list became machine-readable |
| 8 Sep 2026 | The compliance scoring sheet written |
| 8 Sep 2026 | Component selection written and tested cold, three rounds |

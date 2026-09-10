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
| Assess the energy scale that exists in web code against the DPE question | **Ships wrong, breaks no rule.** `libraries/patterns/energyclassslider/src/` holds `EnergyScale.tsx` and `EnergyClassSlider.tsx`. The DPE question — the highest-impact open item on this page — is framed as *no GSL component does the seven-step energy scale*, and for web that framing looks wrong. Read the component, then re-put the question with what it actually does | Every French property listing | Half a day, and it may shrink the question behind it |
| Extend the "when nothing fits" rule to cover *exists, is correct, and doesn't physically fit* | **Ships wrong, breaks no rule.** The donut chart is 373px wide inside a 360px frame. The agent switched off a mandatory part of it and broke no rule doing so | Any chart in a narrow column — so all of mobile | Half a day |
| Generate the web availability list from the web code repo | **Ships wrong, breaks no rule — proven, not theorised.** The list built from the component docs was wrong for five of thirteen. `~/gsl-core-web-design-system` is ground truth: `libraries/ui/src/` and `libraries/patterns/`. The work is not the lookup but the name matching — Figma calls it `Bar graph`, the code calls it `barchart`; `Modal Bottom Sheet` maps to `Modal`; `Energy Tag` maps to neither `tag` nor `energyclassslider` cleanly. That matching is judgement, roughly 98 Figma names against 60 code directories | Every web screen | Half a day |
| Fix the "Legend" entry — it's a switch on a chart, not a component you pick | **Stops or asks.** All three charts expose the legend as an on/off property and the underlying piece is private in Figma. The rules tell an agent to go and place it. It cannot be placed | Any chart with two or more series | An hour |
| Add a routing entry for "a block of controls that computes a live result" | **Stops or asks.** In the test the agent hand-built a mortgage simulator, then said it couldn't tell whether it should have | A recurring product pattern | Half a day |
| Fix the eight remaining places where a ruleset sends an agent to evidence it may not read | **Stops or asks.** Was nine; the worst one is fixed — the rule that stopped mid-answer and said see the audit is gone. `scripts/check-links.py` names the rest exactly: six are header credit lines (their own row above), and two are mid-file — the colour restricted list (its own row above) and `shadow-rules-ai.md:113`, which does give the agent a fallback, so only the stray link needs removing | Every time an agent follows a ruleset to the end | An hour, once the two rows above are done |
| Bring the colour ruleset's restricted list into the file itself | **Stops or asks.** `color-rules-ai.md:298` names roughly ten restricted tokens, says "and 28 others", then points at the audit for the full list. Checked: the audit's own section is grouped by family too, so what's missing is per-token reasons and the exact membership of two families — smaller than it first looked, but the rule still ends by sending the agent somewhere it may not go | Any screen using an unusual colour token | Half an hour |
| Take the clickable audit links out of the six ruleset header lines | **Stops or asks, at worst.** Each ruleset opens with a line like *"Evidence and reasoning: color-usage-audit.md"* as a live link. An agent is told to read `-rules-ai` files and nothing else, so the top of the file offers a door it must not open — and labels it "reasoning", which is what an unsure agent goes looking for. No evidence any agent has followed one; the fix is to keep the sentence and drop the link | Every ruleset an agent opens | Half an hour |
| Add the missing platform-readiness rows to three component docs | **Stops or asks.** `date-picker`, `phone-number-field` and `tabs` have no `Figma \| Web \| iOS \| Android` row at all, so the component ruleset cannot say whether they are available anywhere. It names them as not recorded, which is honest but leaves an agent asking. **`Tabs` is the one that will bite** — this same ruleset tells an agent to use `Tabs` in place of the withheld `Tab Bar`, so the prescribed replacement is a component we cannot say is available. The other 52 docs all carry the row | Any screen using tabs — so most | An hour, once the real statuses are known |
| Fix two rules files that still name renamed files, and teach the link check to see bare filenames | **Stops or asks, and only ever a session working in this repo — never a shipped screen.** A defect we created ourselves: `.claude/rules/component-docs.md:22` tells a session the component index is `components.md`; it is `components-index.md`. `.claude/rules/token-docs.md:16` says the same about `tokens.md`. Both are live instructions naming files that no longer exist. `scripts/check-links.py` missed them because it only reads bracket-and-parenthesis links, not names in backticks — a rename check that only sees links is half a check. The same script also reports a broken link that isn't one: it reads link syntax written *inside* backticks as a real link, so this very row makes the checker fail. A checker that cries wolf gets ignored | Every session that opens either rules file | Half an hour |
| Scale the availability table to iOS and Android | **Stops or asks.** Web and Figma are now answered completely. The component docs record 22 components unavailable on iOS and 31 on Android, and none of that is in the ruleset — it says so plainly and tells the agent to ask. **Do not copy those rows in.** The web pass proved the docs' readiness rows are stale; there is no reason to think the iOS and Android columns are any better, and neither native code repo is on this machine to check against | Every iOS or Android screen | Unknown until a source is found |
| Test the three new rulesets on a cold reader | Neither — it **finds** problems rather than fixing any. Same method found twelve defects in component selection. Run it *after* the fixes above, or we test rulesets we're about to rewrite | — | Half a day |

**The chart-sizing task and the "Legend" task may be one fix.** Both are "the
component exists and is right, but I can't use it in the form I need", and both
land on the same fallback rule. The routing-entry task is worth holding against
the same rule too. Worth checking before treating them as separate days.

**Removing the leftover rule numbers in the spacing ruleset is not on this
list.** The file still says "Rules 6 and 7 are unverified" and "Rules 3–5" after
the renaming, which is untidy, but an agent's output doesn't change. It's a
rider on whatever next opens that file, not a task.

### Something is in the way

| What | What goes wrong today | What's in the way | How long once clear |
| --- | --- | --- | --- |
| Decide who owns the energy-rating (`Scale`) colours, and what an agent does with them | **Ships wrong, breaks no rule — the highest-impact item on this whole page.** In the test the agent produced a grey energy ladder: technically compliant, legally and visually wrong | **Your research.** The 19 colours exist in Figma and are fine. What's missing is a written decision. See the question below | Half a day |
| Record the Figma text-field names for each component | **Ships wrong, breaks no rule.** An agent can place a component but has no way to put words into it, so it ships with the default placeholder text still in place — which breaks nothing. Every string in the test came from reading Figma live, not from this repo | **A session running off `~/.claude/`, plus Figma Desktop open.** The Figma plugin is installed in that config only; a session on `~/.claude-personal/` has no Figma tools at all. Check the bridge responds before starting, not after | A day |
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
| 10 Sep 2026 | **The component docs' platform-readiness rows are stale, and building anything on them produces confident wrong answers.** Checked all 13 web statuses against the web code repo at `~/gsl-core-web-design-system`: five components the docs call `To Do`/`WIP`/`In progress` on web are shipping today — `Bar graph` (`libraries/patterns/barchart`), `Coachmark`, `Line chart` (`libraries/patterns/linechart`), `Segmented Control` and `Slider`. All three docs with no readiness row at all — `Tabs`, `Date Picker`, `Phone Number Field` — are also live on web. Gabriel spotted this from memory before any check was run |
| 10 Sep 2026 | **The web code repo is the real answer to "does this component exist on web", and it is already on this machine** — `~/gsl-core-web-design-system`, components at `libraries/ui/src/` and `libraries/patterns/`. `tokens/scripts/` already reads that repo to generate the token ledgers, so a generated availability list follows a pattern this repo has used before. A hand-copied list drifts; a generated one cannot |
| 10 Sep 2026 | **The web repo's per-component agent files are auto-generated, and not the finished contract they look like.** `ds-bundle/components/<area>/<Component>/<Component>.prompt.md` is one file per component with variants and a typed prop interface — but read in full, `Tabs.prompt.md` mixes 13 real props with 14 generic layout passthroughs (`marginTop`, `zIndex`, `order`) each carrying the same meaningless comment, and its **"Variants" list is padded with Storybook interaction tests** — *Should Handle Selection With Keyboard*, *Should Not Select Disabled Tabs* — presented exactly like real design variants. An agent would choose a test as a variant. Useful as evidence of what exists on web; unsafe as a contract. The earlier note here called it "what we're writing by hand", which overstated it |
| 10 Sep 2026 | **An energy scale exists in web code** — `libraries/patterns/energyclassslider/src/EnergyScale.tsx`, alongside `EnergyClassSlider.tsx`. The energy-rating (DPE) colour question is the highest-impact open item on this page and was framed as *no GSL component does this*. That framing may be wrong for web. Worth reading before answering the question |
| 10 Sep 2026 | **`Navigation Bar (App)` and `Navigation bar` are two different components — checked, and they do not contradict each other.** The ruleset's platform table says `Navigation Bar (App)` is mobile-only; `navigation-bar.md` says Ready on web. Those looked like the same component stated two opposite ways. They are not: the inventory carries both, the app one with no doc. Recorded because the near-identical names invite exactly this mistake, and it was made here once already |
| 9 Sep 2026 | **"Widen the `audit` branch category" was deleted from the task list, not done.** It only ever named one skill, and branches are gone from this repo entirely. Recorded here in case it ever needs bringing back |
| 10 Sep 2026 | **There are two Claude config folders on this machine, and they do not share their tools.** `~/.claude/` holds the four personal skills and the Figma plugin; `~/.claude-personal/` is a second, complete config with neither. Whichever a session runs off decides what it can do — one cause behind both today's missing pieces. Gabriel worked this out; the earlier note here blamed background sessions, which was wrong |
| 10 Sep 2026 | **The skills half is fixed:** `~/.claude-personal/skills` is now a link to `~/.claude/skills`, so both configs see the same four. Takes effect in new sessions, not ones already running. **Figma is not fixed** — plugins carry install state and an `enabledPlugins` setting the second config lacks, so the same trick is riskier and was left alone |
| 9 Sep 2026 | Corner radius is applied in Figma as a plain number, never as a bound variable — confirmed across the component library and three real screens. A generating agent must set the value, and a checker must not flag it as an unbound token |
| 9 Sep 2026 | Border thickness has no separate evidence file; its rules come from the notes inside its own token page. Honest, but it is the one ruleset without a sibling audit |
| 9 Sep 2026 | The "Newest" sort control on the real results-list screen is a hand-built frame, not a real Button — spotted during the radius audit. Exactly the failure this project exists to prevent, in a shipped screen |
| 9 Sep 2026 | **Only three files knew about the new way of working** — `CLAUDE.md`, `status.md` and this one. The rules file for `project/` still specified the old four-step ritual and loads automatically, so a future session would have been handed the old process. Became the next task |
| 9 Sep 2026 | **The corner-radius and shadow rules already existed and were already verified** — radius against nine components and three screens, shadow against eight components. The gap was only that they sit in files agents are told not to read as rules. Turned that task from research into moving text |
| 9 Sep 2026 | Twelve brand PDFs in `design-language/` were deleted by another session; Gabriel confirmed the removal. The folder is gone |
| 10 Sep 2026 | `status.md` is back inside its one-screen budget at 897 words, after the three git commands were cut. The next thing added to it still has to push something else out |
| 10 Sep 2026 | **The graph was rebuilt scoped and now passes the test the old one failed.** 583 things, 822 connections, 57 groups, from 143 files. Asked the same question — what does `-rules-ai` mean and who reads it — every source it returned is a live file: the decision log, `CLAUDE.md`, `README.md`, `tokens/README.md`. No archived briefs, no deleted PDF, and the retired four-step ritual is gone. The 9 Sep graph answered the same question citing all four |
| 10 Sep 2026 | **Scoping bought accuracy, not money.** The rebuild cost 814,930 tokens against the first run's 998,164 — 18% less, for 92% less text. Reading is not where the cost sits; the number of separate things to reason about is. Assume roughly this much again for any full rebuild, and use `--update` for anything smaller |
| 10 Sep 2026 | **49 of 936 connections point at something that isn't in the graph.** Six agents read the repo in parallel and split on what to do about links crossing between their batches — two emitted them, two deliberately did not. So whether a "Related components" link survives depends on which batch happened to hold that file. Never read a missing connection as "these two things are unrelated" |
| 10 Sep 2026 | **What graphify got right, and what it is actually for.** Its 81 groups do match this repo's real ideas — "Rules-AI Contract", "Filename Suffix Grammar", "Private Helper Sets" — so the concept extraction genuinely works. But `graphify query` returns a dump of matching nodes for an agent to read, not an answer a person can use, and it truncated 25 of 70 nodes at its token budget. It is a retrieval aid for Claude, never an answer surface for Gabriel |
| 10 Sep 2026 | **`.graphifyignore` now scopes graphify to the knowledge base** — 992 files and 2.8M words down to 143 files and 213k words. It excludes 842 images (`CLAUDE.md` says never to open one; they are matched by filename and hash) and `project/archive/`. It is committed, so the scoping holds for every future run including `--update`. Verified by re-running detection, which costs nothing |
| 10 Sep 2026 | **The scoped rebuild could not be run from a background session.** `graphify extract --backend claude` needs `ANTHROPIC_API_KEY`, which isn't set. The other route is `/graphify`, where Claude itself does the reading — but that skill only loads in a foreground session. Nothing was lost: the old graph was backed up and restored, and it is still the stale one from 9 Sep. Do not trust it until it is rebuilt |
| 10 Sep 2026 | **A dated entry in `project/decisions.md` still names `components.md`, and should stay that way.** It records what was true in August. Rewriting a decision log so it matches today makes it useless as a record — the point of the log is that it says what was believed when |
| 10 Sep 2026 | **Renaming a path-scoped rules file does not break it.** Verified live: after `.claude/rules/components.md` became `component-docs.md`, reading a file in `components/` still loaded it. The frontmatter `paths:` block does the work; the filename is free |
| 10 Sep 2026 | **`graphify update .` only does a structural pass.** It pruned the old filenames and picked up the new ones as heading-level nodes, but the richer concept extraction needs `/graphify --update` through the skill. The step in `/task-check` keeps the graph honest about what exists, not deeply informed about what changed |
| 10 Sep 2026 | **Only the bare filename `tokens.md` trips graphify's secrets filter — every other token page is fine.** Tested directly: `color-tokens.md`, `radius-tokens.md`, `tokens-index.md`, `design-tokens.md` all index normally. Two files are affected: `tokens/tokens.md` and `.claude/rules/tokens.md`. Any qualifier in the name fixes it |
| 10 Sep 2026 | **The graph never reaches the agent this project is for.** `graphify-out/` is git-ignored, so it does not ship with the repo, and the generating agent reads `*-rules-ai.md` and nothing else. The graph is a working aid for whoever is building the repo — never part of what it delivers, and never a reason to delete a file it duplicates |
| 10 Sep 2026 | **Never delete `graphify-out/`.** The extraction cache lives inside it. Deleting it is what turned this rebuild into 814,930 tokens; with the cache warm, `graphify update .` re-reads only what changed. `/task-check` now runs that after every passing task |
| 10 Sep 2026 | **If graphify is rebuilt, scope it to `components/`, `tokens/` and `figma/`.** The first run swept 992 files at ~1M input tokens, including `project/archive/` — the plan and briefs retired precisely so nobody works from them. The history is what poisoned the graph. Its own report said to run on a subfolder |
| 10 Sep 2026 | **Nothing in this repo checks that links resolve.** Deleting a file by hand can leave a ruleset pointing at something that no longer exists, and only reading catches it. `/task-next` now runs `git status` first and traces what referenced anything deleted — that covers a deletion you haven't committed yet, not one already committed |
| 10 Sep 2026 | **`internal/git-basics-tutorial.md` is about branches, which this repo stopped using on 9 Sep.** Starting a topic, worktrees, which branch a chat is on — none of it applies any more. It also only ever covered `git status`, not `git log` or `git revert`. Nothing depends on it, so nothing is broken, but it now describes a workflow that no longer exists |
| 9 Sep 2026 | The eight human-facing files totalled 15,400 words — about 60 pages. That, not the 120 machine files, is what made the project unreadable |

---

## Done

| Date | What |
| --- | --- |
| 10 Sep 2026 | **"Can I use this component here?" now has one answer for Figma, and an honest "ask" everywhere else.** Platform limits was three sources contradicting each other, seventeen spellings of readiness, and a rule that stopped mid-answer and pointed at a file agents may not read. Figma is now answered completely from the registries. The web list built from the component docs was **thrown away before it shipped** — checked against the web source code, it was wrong for five of thirteen, so web, iOS and Android now say plainly that nothing is established and the agent must ask. The dead end is gone, every component name matches the inventory, and the docs' readiness row is marked do-not-read on every platform |
| 10 Sep 2026 | **Two files called `tokens.md` and two called `components.md` — no longer.** The rules files became `token-docs.md` and `component-docs.md`, each now opening with a line saying it is an instruction for Claude, not design-system content. Nothing linked to them by name, so nothing broke. `figma-registries.md` already set the precedent that rules files are named for their subject |
| 10 Sep 2026 | **`-index` added to the filename grammar**, and the two routing pages renamed to `tokens-index.md` and `components-index.md`. They were the only two files in the repo whose names didn't follow the rule `CLAUDE.md` states. 13 links moved and the link check proves none broke. `tokens-index.md` also gained the title it never had |
| 10 Sep 2026 | **`scripts/check-links.py` written** — the repo's first repo-wide check. It answers two questions: is the file there, and is the agent allowed to read it. First run: 1,378 links, **zero broken**, nine dead ends now listed exactly instead of estimated at three |
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

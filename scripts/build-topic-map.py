#!/usr/bin/env python3
"""Generate `project/topic-map.md` — every design topic, and how far each one is.

The page is for a person: a designer being shown what this repo holds and what
it does not hold yet. **Every mark on it is read out of the repo's files**, so
the page cannot drift from them the way a hand-written count does.

What it reads:

| Topic | From |
| --- | --- |
| Components | `components/components-coverage-ledger.md`, itself written by `components/coverage.py` |
| Tokens | Which files each folder under `tokens/` holds |
| Icons | Which files `icons/` holds |
| Making a screen | Whether a ruleset exists under one of the names in MAKING_A_SCREEN |
| Writing it down | `specs/` |
| Building it | The name maps and the Figma registries |
| Checking it | `compliance/` |

**One thing is written by hand: KNOWN_LIMITS, below.** A file count cannot say
that a spec has no field for position, so those sentences are typed here, each
with the page it was taken from. Change them here and re-run.

    python3 scripts/build-topic-map.py

Re-run it after a ruleset, a token page, a name map or a spec is added, and
after `components/coverage.py` has been re-run.
"""

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "project" / "topic-map.md"
LEDGER = ROOT / "components" / "components-coverage-ledger.md"

WRITTEN, PARTIAL, EMPTY = "Written", "Partial", "Empty"
MARK = {WRITTEN: "●", PARTIAL: "◐", EMPTY: "○"}

# A token folder's name, where capitalising it is not enough.
TOKEN_NAMES = {"color": "Colour", "z-index": "Z-index"}

# Each topic of making a screen: the ruleset names that would make it written,
# the files that make it partial, and the component-page sections that touch it.
# The ruleset names for topics with no ruleset yet are a guess at the filename
# grammar; add the real name here when one is written.
MAKING_A_SCREEN = [
    ("Content and copy", ["content-rules-ai.md", "copy-rules-ai.md"], [],
     ["Writing", "Length Limits", "Capitalization", "Label Formula"]),
    ("Layout", ["layout-rules-ai.md", "grid-rules-ai.md"],
     ["tokens/grid/grid-tokens.md"], []),
    ("Responsive", ["responsive-rules-ai.md", "breakpoint-rules-ai.md"],
     ["tokens/breakpoint/breakpoint-tokens.md"], ["Breakpoints"]),
    ("Motion", ["motion-rules-ai.md"], ["tokens/motion/motion-tokens.md"], []),
    ("Edge cases", ["edge-cases-rules-ai.md", "states-rules-ai.md"], [], ["States"]),
]

# Each place a screen gets built, and the name maps it needs: components,
# tokens, icons. No Android or web map exists yet, so those names are a guess.
BUILDING = [
    ("Figma", ["figma/figma-components-registry.json",
               "figma/figma-tokens-registry.json",
               "figma/figma-icons-registry.json"]),
    ("iOS", ["components/components-ios-map.md", "tokens/tokens-ios-map.md",
             "icons/icons-ios-map.md"]),
    ("Android", ["components/components-android-map.md",
                 "tokens/tokens-android-map.md", "icons/icons-android-map.md"]),
    ("Web", ["components/components-web-map.md", "tokens/tokens-web-map.md",
             "icons/icons-web-map.md"]),
]

# Written by hand. Each sentence names the page it was taken from.
KNOWN_LIMITS_SOURCE = "`status.md` of 2 October 2026"
KNOWN_LIMITS = {
    "Components": "What each variant option means is still open",
    "Content and copy": "No rule says what a screen should say",
    "Layout": "Card and block-title rules are held back",
    "The spec format": "No field for where a block goes",
    "Figma": "`/design` builds. Illustration and card padding are still open",
    "iOS": "`/prototype` builds. It does not read a spec yet",
    "Android": "`/vibe` builds. It does not read a spec yet",
    "The scorecard": "Written for Figma. Nothing checks an app build",
}

# Named by Gabriel on 5 October 2026 as part of the design system. Not mapped yet.
ADDED_LATER = ["Research", "Problem definition", "Testing", "Prototyping guides"]

SKIP = {"node_modules", "archive", "skills", ".git"}


def exists(path: str) -> bool:
    return (ROOT / path).exists()


def find_ruleset(names: list[str]):
    """The repo-relative path of the first ruleset with one of these names."""
    for path in sorted(ROOT.rglob("*-rules-ai.md")):
        if SKIP & set(path.relative_to(ROOT).parts):
            continue
        if path.name in names:
            return str(path.relative_to(ROOT))
    return None


def link(path: str) -> str:
    """A link from `project/` to a repo-relative path."""
    return f"[`{Path(path).name}`](../{path})"


def plural(n: int, one: str, many: str) -> str:
    return f"{n} {one if n == 1 else many}"


def cell(status: str) -> str:
    return f"{MARK[status]} {status}"


def roll_up(statuses: list[str]) -> str:
    """One status for a topic, from the statuses of its sub-topics."""
    if all(s == WRITTEN for s in statuses):
        return WRITTEN
    if all(s == EMPTY for s in statuses):
        return EMPTY
    return PARTIAL


def read_ledger() -> tuple[int, int, int, dict[str, int]]:
    """Entries, entries with a page, selectable entries with none, fill per section."""
    text = LEDGER.read_text()

    def number(label: str) -> int:
        m = re.search(re.escape(label) + r"\s*\|\s*\*\*(\d+)\*\*", text)
        if not m:
            sys.exit(f"build-topic-map: cannot find '{label}' in {LEDGER.name}")
        return int(m.group(1))

    entries = number("Registry entries across the four Figma libraries")
    documented = number("— have a doc")
    gap = number("— no doc, and an agent may select them")

    block = re.search(r"^## Which sections are worst\s*$(.*?)^## ", text, re.M | re.S)
    if not block:
        sys.exit(f"build-topic-map: cannot find the section table in {LEDGER.name}")
    sections = {
        m.group(1).strip(): int(m.group(2))
        for m in re.finditer(r"^\|\s*([^|]+?)\s*\|(?:[^|]*\|){3}\s*(\d+)%\s*\|\s*$",
                             block.group(1), re.M)
    }
    if not sections:
        sys.exit(f"build-topic-map: the section table in {LEDGER.name} is empty")
    return entries, documented, gap, sections


def fill_status(percent: int) -> str:
    return WRITTEN if percent == 100 else EMPTY if percent == 0 else PARTIAL


def components(entries, documented, gap, sections):
    rows = [
        ("A page for each component",
         f"{documented} of {entries} library entries have a page. "
         f"{gap} that an agent may pick has none",
         WRITTEN if gap == 0 else PARTIAL),
    ]
    ruleset = "components/components-rules-ai.md"
    rows.append(("Which component to pick",
                 link(ruleset) if exists(ruleset) else "No rules page",
                 WRITTEN if exists(ruleset) else EMPTY))
    for name, percent in sorted(sections.items(), key=lambda s: s[1]):
        rows.append((f"Inside each page — {name}",
                     f"Filled on {percent}% of the pages", fill_status(percent)))
    return rows


def tokens():
    rows = []
    for folder in sorted((ROOT / "tokens").iterdir()):
        values = folder / f"{folder.name}-tokens.md"
        if not values.exists():
            continue
        rules = folder / f"{folder.name}-rules-ai.md"
        audits = sorted(folder.glob("*-audit.md"))
        name = TOKEN_NAMES.get(folder.name, folder.name.replace("-", " ").capitalize())
        rel = lambda p: str(p.relative_to(ROOT))
        rows.append((name, link(rel(values)),
                     link(rel(rules)) if rules.exists() else "None",
                     "Yes" if audits else "No",
                     WRITTEN if rules.exists() else PARTIAL))
    return rows


def icons():
    index, rules = "icons/icons-index.md", "icons/icons-rules-ai.md"
    return [
        ("The list of every icon", link(index) if exists(index) else "None",
         WRITTEN if exists(index) else EMPTY),
        ("Which icon to pick", link(rules) if exists(rules) else "None",
         WRITTEN if exists(rules) else EMPTY),
    ]


def making_a_screen(sections):
    rows = []
    for name, rulesets, material, in_pages in MAKING_A_SCREEN:
        ruleset = find_ruleset(rulesets)
        found = [m for m in material if exists(m)]
        status = WRITTEN if ruleset else PARTIAL if found else EMPTY
        rules = link(ruleset) if ruleset else "None"
        values = ", ".join(link(m) for m in found) or "None"
        pages = ", ".join(f"{s} {sections[s]}%" for s in in_pages if s in sections) or "—"
        rows.append((name, rules, values, pages, status))
    return rows


def writing_it_down():
    rules = "specs/spec-rules-ai.md"
    specs = len(list((ROOT / "specs").glob("spec-[0-9]*.md")))
    return [("The spec format",
             f"{link(rules)}. {plural(specs, 'spec', 'specs')} saved in `specs/`" if exists(rules)
             else "None",
             WRITTEN if exists(rules) else EMPTY)]


def building():
    rows = []
    for name, maps in BUILDING:
        found = sum(exists(m) for m in maps)
        status = WRITTEN if found == len(maps) else PARTIAL if found else EMPTY
        rows.append((name, f"{found} of {len(maps)} name maps", status))
    return rows


def checking():
    card = "compliance/compliance-scorecard.md"
    briefs = sorted((ROOT / "compliance" / "briefs").glob("brief-*"))
    runs = sum(len(list(b.glob("run-*"))) for b in briefs)
    return [("The scorecard",
             f"{link(card)}. {plural(len(briefs), 'brief', 'briefs')}, "
             f"{plural(runs, 'run', 'runs')} scored" if exists(card)
             else "None",
             WRITTEN if exists(card) else EMPTY)]


def count_skills() -> tuple[int, int]:
    inside = len(list((ROOT / ".claude" / "skills").glob("*/SKILL.md")))
    outside = len(list((ROOT / "skills").glob("*/SKILL.md")))
    return inside, outside


def limit(name: str) -> str:
    return KNOWN_LIMITS.get(name, "—")


def table(head: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(head) + " |", "|" + " --- |" * len(head)]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines) + "\n"


def tree(groups) -> str:
    """The whole map as one picture: each topic, its sub-topics, their marks."""
    lines = ["The design system"]
    for g, (group, topics) in enumerate(groups):
        last_group = g == len(groups) - 1
        status = roll_up([s for _, s in topics])
        lines.append(f"{'└' if last_group else '├'}── {group}  {MARK[status]}")
        for t, (topic, s) in enumerate(topics):
            stem = "    " if last_group else "│   "
            branch = "└" if t == len(topics) - 1 else "├"
            lines.append(f"{stem}{branch}── {topic}  {MARK[s]} {s.lower()}")
    return "```\n" + "\n".join(lines) + "\n```\n"


def main():
    entries, documented, gap, sections = read_ledger()
    comp, tok, ico = components(entries, documented, gap, sections), tokens(), icons()
    screen, spec, build, check = (making_a_screen(sections), writing_it_down(),
                                  building(), checking())
    inside, outside = count_skills()
    ruled = sum(r[-1] == WRITTEN for r in tok)

    groups = [
        ("The parts", [("Components", roll_up([r[-1] for r in comp])),
                       ("Tokens", roll_up([r[-1] for r in tok])),
                       ("Icons", roll_up([r[-1] for r in ico]))]),
        ("Making a screen", [(r[0], r[-1]) for r in screen]),
        ("Writing it down", [(r[0], r[-1]) for r in spec]),
        ("Building it", [(r[0], r[-1]) for r in build]),
        ("Checking it", [(r[0], r[-1]) for r in check]),
    ]
    summary = [
        [group, *(str(sum(s == status for _, s in topics))
                  for status in (WRITTEN, PARTIAL, EMPTY))]
        for group, topics in groups
    ]

    today = date.today()
    page = [
        "<!-- GENERATED FILE — do not edit by hand. "
        "Re-run: python3 scripts/build-topic-map.py -->\n",
        "# The design system — topic map\n",
        "_Every design topic, and how far each one is. **Written by a script** "
        f"on {today.day} {today:%B %Y}: every mark is read out of a file. "
        "Never edit this page; re-run `scripts/build-topic-map.py`._\n",
        "**This page shows what exists and what is missing.** "
        "It does not say the design system is finished.\n",
        "---\n",
        "## How to read it\n",
        table(["Mark", "Meaning"], [
            [cell(WRITTEN), "The rules for this topic are written down"],
            [cell(PARTIAL), "Some material exists, and the rules do not, or not all of them"],
            [cell(EMPTY), "Nothing is written"],
        ]),
        "**Written means the file exists.** It does not mean the rules are "
        "complete or correct.\n",
        "A topic takes its mark from its sub-topics. All written gives written. "
        "All empty gives empty. Anything else gives partial.\n",
        "---\n",
        "## The whole picture\n",
        tree(groups),
        table(["Topic", "Written", "Partial", "Empty"], summary),
        "---\n",
        "## The parts\n",
        "What a screen is made of.\n",
        "### Components\n",
        f"**Known limit:** {limit('Components').lower()}. "
        f"Written by hand, from {KNOWN_LIMITS_SOURCE}.\n",
        table(["Sub-topic", "What exists", "Status"],
              [[n, w, cell(s)] for n, w, s in comp]),
        "A section is written when every page fills it, and empty when none does.\n",
        "### Tokens\n",
        f"**{ruled} of {len(tok)} kinds have a rules page.** "
        "A kind with values and no rules is partial.\n",
        table(["Kind", "Values listed", "Rules page", "Checked against real use", "Status"],
              [[n, v, r, a, cell(s)] for n, v, r, a, s in tok]),
        "### Icons\n",
        table(["Sub-topic", "What exists", "Status"],
              [[n, w, cell(s)] for n, w, s in ico]),
        "---\n",
        "## Making a screen\n",
        "How the parts become a screen. A topic is written once it has a rules page.\n",
        table(["Topic", "Rules page", "Values listed", "Inside the component pages",
               "Status", "Known limit"],
              [[n, r, v, p, cell(s), limit(n)] for n, r, v, p, s in screen]),
        "**Inside the component pages** is how many pages fill the sections "
        "touching that topic. It never changes the status.\n",
        "---\n",
        "## Writing it down\n",
        "The spec is the written description of a screen, the same for every platform.\n",
        table(["Sub-topic", "What exists", "Status", "Known limit"],
              [[n, w, cell(s), limit(n)] for n, w, s in spec]),
        "---\n",
        "## Building it\n",
        "A name map gives each component, token and icon its name on a platform. "
        "A platform is written once it has all three.\n",
        table(["Platform", "What exists", "Status", "Known limit"],
              [[n, w, cell(s), limit(n)] for n, w, s in build]),
        f"**The skills that do the work:** {inside} run inside this repo, in "
        f"`.claude/skills/`. {outside} run outside it, in `skills/`.\n",
        "---\n",
        "## Checking it\n",
        table(["Sub-topic", "What exists", "Status", "Known limit"],
              [[n, w, cell(s), limit(n)] for n, w, s in check]),
        "---\n",
        "## Added later\n",
        "Part of the design system, and not on this map yet. Gabriel, "
        "5 October 2026: generating a screen comes first.\n",
        "\n".join(f"- {name}" for name in ADDED_LATER) + "\n",
        "---\n",
        "## What this page is built from\n",
        table(["Topic", "Read from"], [
            ["Components", f"{link('components/components-coverage-ledger.md')}. "
                           "Re-run `components/coverage.py` first"],
            ["Tokens", "The files in each folder under `tokens/`"],
            ["Icons", "The files in `icons/`"],
            ["Making a screen", "Whether a rules page exists for the topic"],
            ["Writing it down", "The files in `specs/`"],
            ["Building it", "The name maps, and the registries in `figma/`"],
            ["Checking it", "The files in `compliance/`"],
        ]),
        f"**Every *Known limit* is written by hand**, from {KNOWN_LIMITS_SOURCE}. "
        "A file count cannot see them. They live in the script and go stale "
        "unless someone updates them there.\n",
    ]
    OUT.write_text("\n".join(page))
    print(f"wrote {OUT.relative_to(ROOT)}")
    for group, topics in groups:
        print(f"  {group}: " + ", ".join(f"{t} {s.lower()}" for t, s in topics))


if __name__ == "__main__":
    main()

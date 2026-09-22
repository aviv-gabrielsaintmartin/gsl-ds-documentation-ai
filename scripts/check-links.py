#!/usr/bin/env python3
"""Check that every link in this repo goes somewhere an agent can actually use.

Three questions, because a pointer can fail in three different ways:

  1. Does the file exist?  A link to a file that was renamed or deleted sends
     an agent nowhere. Nothing else in this repo checks this.

  2. Is the agent allowed to read it?  A generating agent reads `-rules-ai`
     files and nothing else. When a ruleset links into an `-audit`, `-eval` or
     `-ledger` file, the agent has followed the rules to a door it must not
     open. That is a dead end, not a broken link, and it is worse: the link
     resolves, so nothing looks wrong.

  3. Does a filename written in backticks name a file that still exists?  Most
     of this repo names files without linking them — `components-index.md` in a
     sentence, a table of file roles, a path in a rules file. A rename check
     that only sees links is half a check: on 22 September 2026 two rules files
     had been telling every session for weeks that the indexes were
     `components.md` and `tokens.md`, months after both were renamed, and
     nothing here could see it.

Links inside fenced code blocks are skipped — they are illustrations, not
navigation. What the name check skips is listed beside each rule below.

Run it from the repo root:  python3 scripts/check-links.py
Exit code is 0 when clean, 1 when anything failed.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Folders that are history, generated, or not ours to police.
SKIP_DIRS = {".git", "graphify-out", "node_modules", "project/archive"}

# Files whose links are illustrations, not navigation. The component template
# is written in placeholders -- images/<hash>.png is the shape of a real
# reference, never a file that exists.
SKIP_FILES = {"components/component-template.md"}

# A generating agent is told to read these and nothing else.
RULESET = "-rules-ai.md"

# Evidence files. Real, useful, and off-limits to a generating agent.
EVIDENCE = ("-audit.md", "-eval.md", "-ledger.md")

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

# A run of three or more backticks opening or closing a fenced code block.
FENCE = re.compile(r"^(`{3,})(.*)$")

# --- The name check ------------------------------------------------------
#
# Anything in single backticks ending in an extension this repo actually uses.
# `.json` is deliberately left out: the design-system code repo's files are
# named in backticks here by the dozen (`scoreTag.json`, `shared/grids.json`)
# and none of them is ours to find.
BARE = re.compile(r"`([^`\n]{1,120}?\.(?:md|py|mjs))`")

# A name that stands for a shape rather than a file: `<name>-figma.md`,
# `*-rules-ai.md`, `report-run-NNN.md`, `python3 scripts/check-links.py`.
PLACEHOLDER = re.compile(r"[<>{}*\s]|NNN")

# Files that record what was true on a date. They name files that have since
# been renamed or deleted, on purpose — that is what a record is for, and
# `decisions.md` is never rewritten by rule.
#
# `status.md` is here for the same reason and was added the day the name check
# was: its done log said a rules file had named `components.md`, and the check
# failed on the very sentence reporting the fix. Every rename task after this
# one would have hit the same wall. The live pointers on that page are links,
# which the link check above still reads.
HISTORY = {"status.md", "project/backlog.md", "project/decisions.md"}

# Names of real files that are not in this repo, and so can never resolve here.
# Every entry needs a reason; a list that grows without one is how a check stops
# meaning anything.
ELSEWHERE = {
    # Confluence pages the component-web-ai-docs skill writes, named after the
    # files their content is destined for in a consuming repo.
    "usage.md": "a Confluence page written by component-web-ai-docs",
    "api.web.md": "a Confluence page written by component-web-ai-docs",
    # how-a-run-is-reported.md walks through a run folder file by file. run-001
    # predates the report convention and holds only screenshots, and brief-002
    # has not been written yet.
    "report-run-001.md": "a worked example in how-a-run-is-reported.md",
    "brief-002.md": "a worked example in how-a-run-is-reported.md",
}


def skipped(path: Path) -> bool:
    """True for anything under a skipped directory, at any depth.

    Matching whole path segments, not just the prefix -- `node_modules` only
    ever appears nested (scripts/node_modules/), and a prefix match misses it.
    """
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP_FILES:
        return True
    segments = rel.split("/")
    for d in SKIP_DIRS:
        parts = d.split("/")
        if rel == d or rel.startswith(d + "/"):
            return True
        if len(parts) == 1 and parts[0] in segments[:-1]:
            return True
    return False


def live_lines(text: str):
    """Yield (line_no, line) for every line outside a fenced code block.

    A link inside a fenced block is an illustration, not navigation. Checking
    it reports breaks that aren't there — and a checker that cries wolf gets
    ignored, which costs more than the links it catches.

    Fence length is tracked so a ```` block may contain ``` fences of its own,
    which is how a markdown template is shown inside a markdown file.
    """
    fence: str | None = None
    for line_no, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line.lstrip())
        if match:
            ticks, rest = match.groups()
            if fence is None:
                fence = ticks
                continue
            # Only a run at least as long as the opener, and nothing after it,
            # can close the block.
            if len(ticks) >= len(fence) and not rest.strip():
                fence = None
                continue
        if fence is None:
            yield line_no, line


def every_name() -> set[str]:
    """Every way a real file in this repo could honestly be named.

    A bare filename is a name, not a path — `surface.md` in a rules file means
    the one in `tokens/color/`, and the rules file lives nowhere near it. So
    each real file is indexed under every suffix of its path: `surface.md`,
    `color/surface.md`, `tokens/color/surface.md`.

    Built from every file on disk, including the ones whose *links* are skipped.
    `components/component-template.md` is skipped as a source because its links
    are placeholders; it is still a real file anyone may name.
    """
    names: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith((".git/", "scripts/node_modules/")):
            continue
        segments = rel.split("/")
        for i in range(len(segments)):
            names.add("/".join(segments[i:]))
    return names


def named_files(line: str):
    """Yield each backticked filename on a line that is worth resolving."""
    for raw in BARE.findall(line):
        name = raw.strip()
        if name.startswith("./"):
            name = name[2:]
        if PLACEHOLDER.search(name):
            continue
        # `-rules-ai.md`, `-audit.md` — the filename grammar, not a filename.
        if name.startswith("-"):
            continue
        # `~/.claude/CLAUDE.md`, `/etc/…` — outside the repo by construction.
        if name.startswith(("~", "/")):
            continue
        if name in ELSEWHERE:
            continue
        yield name


def main() -> int:
    broken: list[str] = []
    dead_ends: list[str] = []
    stale: list[str] = []
    checked = 0
    names_checked = 0
    real_names = every_name()

    for md in sorted(ROOT.rglob("*.md")):
        if skipped(md):
            continue
        rel_src = md.relative_to(ROOT).as_posix()
        for line_no, line in live_lines(md.read_text(encoding="utf-8")):
            for label, target in LINK.findall(line):
                # Leave external links and pure anchors alone.
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_part = target.split("#", 1)[0]
                if not path_part:
                    continue
                checked += 1
                resolved = (md.parent / path_part).resolve()

                if not resolved.exists():
                    broken.append(f"{rel_src}:{line_no}  [{label}] -> {target}")
                    continue

                if md.name.endswith(RULESET) and resolved.name.endswith(EVIDENCE):
                    dead_ends.append(
                        f"{rel_src}:{line_no}  [{label}] -> {target}"
                    )

            if rel_src in HISTORY:
                continue
            for name in named_files(line):
                names_checked += 1
                if name not in real_names:
                    stale.append(f"{rel_src}:{line_no}  `{name}`")

    print(
        f"Checked {checked} links and {names_checked} filenames "
        f"across the repo.\n"
    )

    if broken:
        print(f"BROKEN — the file is not there ({len(broken)}):")
        for b in broken:
            print(f"  {b}")
        print()

    if dead_ends:
        print(
            f"DEAD END — a ruleset sends the agent to a file it may not read "
            f"({len(dead_ends)}):"
        )
        for d in dead_ends:
            print(f"  {d}")
        print()

    if stale:
        print(
            f"STALE NAME — a filename in backticks matches no file here "
            f"({len(stale)}):"
        )
        for s in stale:
            print(f"  {s}")
        print()

    if not broken and not dead_ends and not stale:
        print(
            "Every link resolves, every filename exists, and no ruleset "
            "points at evidence. Clean."
        )
        return 0

    print(
        f"{len(broken)} broken, "
        f"{len(dead_ends)} dead end{'' if len(dead_ends) == 1 else 's'}, "
        f"{len(stale)} stale name{'' if len(stale) == 1 else 's'}."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())

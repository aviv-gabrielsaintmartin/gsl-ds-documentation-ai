#!/usr/bin/env python3
"""Check that every link in this repo goes somewhere an agent can actually use.

Two questions, because a link can fail in two different ways:

  1. Does the file exist?  A link to a file that was renamed or deleted sends
     an agent nowhere. Nothing else in this repo checks this.

  2. Is the agent allowed to read it?  A generating agent reads `-rules-ai`
     files and nothing else. When a ruleset links into an `-audit`, `-eval` or
     `-ledger` file, the agent has followed the rules to a door it must not
     open. That is a dead end, not a broken link, and it is worse: the link
     resolves, so nothing looks wrong.

Links inside fenced code blocks are skipped — they are illustrations, not
navigation. Links written inside single backticks are not yet skipped, and
neither are bare filenames outside link syntax.

Run it from the repo root:  python3 scripts/check-links.py
Exit code is 0 when clean, 1 when anything failed.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Folders that are history, generated, or not ours to police.
SKIP_DIRS = {".git", "graphify-out", "node_modules", "project/archive"}

# A generating agent is told to read these and nothing else.
RULESET = "-rules-ai.md"

# Evidence files. Real, useful, and off-limits to a generating agent.
EVIDENCE = ("-audit.md", "-eval.md", "-ledger.md")

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

# A run of three or more backticks opening or closing a fenced code block.
FENCE = re.compile(r"^(`{3,})(.*)$")


def skipped(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return any(rel == d or rel.startswith(d + "/") for d in SKIP_DIRS)


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


def main() -> int:
    broken: list[str] = []
    dead_ends: list[str] = []
    checked = 0

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

    print(f"Checked {checked} links across the repo.\n")

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

    if not broken and not dead_ends:
        print("Every link resolves, and no ruleset points at evidence. Clean.")
        return 0

    print(f"{len(broken)} broken, {len(dead_ends)} dead ends.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

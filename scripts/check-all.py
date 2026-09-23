#!/usr/bin/env python3
"""Run every standing check in this repo and print one verdict.

Five checks existed and each had to be remembered separately. Nothing said what
order to run them in, and nothing said what a clean run did and did not prove.
This is the one command.

    python3 scripts/check-all.py           # read-only, changes nothing
    python3 scripts/check-all.py --write   # also regenerates the two ledgers

**Nothing here is a new check.** It runs the five that already exist and reports
them together. Three read files and report. Two are generators, and this runs
them into a temporary file and compares -- so the question they answer here is
*is the committed page still current*, never *rewrite it*. Add `--write` when you
want the page itself brought up to date.

Exit code is 0 when every check passes, 1 when any fails.

**A failing check is not automatically a failing task.** Some defects are known
and recorded in `project/backlog.md`; `.claude/skills/task-check/SKILL.md` says
how to tell those from a fault the current task just introduced.

## What a clean run proves, and what it does not

It proves the docs are **well-formed**: every pointer resolves, every heading is
one the template defines, no page explains itself with a tool, and the two
generated pages match the files they are generated from.

**It proves nothing about whether a sentence is true.** Every check here reads
this repo against itself. None of them opens Figma, the web code, or the app.
A page can pass all five and be wrong in every paragraph -- `map-template.md`
fills 13 of its 16 sections and every word came off a component library, with
nobody who knows the product having read it.

Four things nothing in this repo checks, listed here because a runner that
prints a clean verdict is exactly where a reader stops looking:

  1. **Whether a readiness row is true.** The table is checked for existence and
     never read. `navigation-bar.md` claimed Ready on web while no web component
     exists, and a person caught it.
  2. **Whether a filled section is true.** Coverage answers shape only.
  3. **Whether the ruleset contradicts itself.** Only `components-rules-ai-eval.md`
     probes that, it is run by hand against a cold agent, and it is stale.
  4. **Whether a page is reachable at all.** A file nothing links to is
     invisible to the link check, which asks the opposite question.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- The three that read and report --------------------------------------
# Each prints a `Checked N ...` line first and exits non-zero on a finding.

SCRIPTS = [
    ("Links and filenames", "scripts/check-links.py"),
    ("Tool neutrality", "scripts/check-tool-neutral.py"),
    ("Docs against the ruleset", "scripts/check-rules-docs.py"),
]

# --- The two that generate a page ----------------------------------------
# Imported rather than run, so their OUTPUT can be pointed at a temp file.
# `template-drift.py` has a hyphen in its name and cannot be imported by name.

GENERATORS = [
    ("Coverage ledger", "components/coverage.py",
     "components/components-coverage-ledger.md"),
    ("Template drift page", "components/template-drift.py",
     "components/components-template-drift.md"),
]


def run_script(path: str) -> tuple[bool, str, str]:
    """Return (passed, one-line summary, full output)."""
    done = subprocess.run([sys.executable, str(ROOT / path)],
                          capture_output=True, text=True, cwd=ROOT)
    out = (done.stdout + done.stderr).strip()
    first = next((l for l in out.splitlines() if l.strip()), "no output")
    return done.returncode == 0, first, out


def load(path: str):
    spec = importlib.util.spec_from_file_location("gen_" + Path(path).stem, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_generator(path: str, page: str, write: bool) -> tuple[bool, str, str]:
    """Regenerate the page and say whether the committed one still matches."""
    module = load(path)
    committed = ROOT / page
    # Both generators report their own counts on stdout. Useful when run alone,
    # noise in a five-line verdict -- so their voice is swallowed here.
    quiet = contextlib.redirect_stdout(io.StringIO())

    if write:
        with quiet:
            module.main()
        return True, f"{page} regenerated", ""

    with tempfile.TemporaryDirectory() as tmp:
        module.OUTPUT = Path(tmp) / committed.name
        with quiet:
            module.main()
        fresh = module.OUTPUT.read_text()

    if not committed.exists():
        return False, f"{page} does not exist", ""
    if fresh == committed.read_text():
        return True, f"{page} is current", ""
    return False, f"{page} is STALE — re-run it", (
        f"The page on disk differs from what {path} produces today.\n"
        f"Re-run:  python3 {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--write", action="store_true",
                        help="regenerate the two ledgers instead of only checking them")
    args = parser.parse_args()

    results = []   # (passed, label, summary, detail)

    for label, path in SCRIPTS:
        passed, summary, out = run_script(path)
        results.append((passed, label, summary, "" if passed else out))

    for label, path, page in GENERATORS:
        passed, summary, detail = run_generator(path, page, args.write)
        results.append((passed, label, summary, "" if passed else detail))

    width = max(len(label) for _, label, _, _ in results)
    print()
    for passed, label, summary, _ in results:
        print(f"  {'PASS' if passed else 'FAIL'}  {label.ljust(width)}   {summary}")

    failed = [r for r in results if not r[0]]
    print()
    if failed:
        print(f"{len(failed)} of {len(results)} failed.\n")
        for _, label, _, detail in failed:
            if not detail:
                continue
            print(f"--- {label} " + "-" * max(0, 60 - len(label)))
            print(detail)
            print()
    else:
        print(f"All {len(results)} checks pass.")

    print("These five read this repo against itself. **None of them opens Figma,")
    print("the web code or the app, and none can tell you whether a sentence is")
    print("true.** The four questions nobody checks are listed in this script's")
    print("own docstring — read it before treating a clean run as a finished doc.")
    print()

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

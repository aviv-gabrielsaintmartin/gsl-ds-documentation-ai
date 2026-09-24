#!/usr/bin/env python3
"""
Map every GSL token name to the name that builds it on iOS.

Reads only. Writes `tokens/tokens-ios-map.md`.

Two sources are read:
  1. figma/figma-tokens-registry.json            -> every token name this repo uses
  2. the iOS design-system package, at a git ref  -> the iOS names, read with
     `git show`, never from the working copy. The local checkout was 21
     design-system commits behind the remote on 24 September 2026.

Nothing here decides whether a token may be used. The token rulesets decide
that. This only translates a name that was already chosen.

Confidence, per row:
  proved     colour: iOS fills the path from an asset named after this
             exact token, or a literal colour has the same light value.
             Numbers and shadows: the values are equal. Text: size and
             weight both exist
  guessing   the iOS name exists, and the match needed a stated rule —
             segments merged, a final `Default` dropped, a `default` level
             added, or a renamed segment
  not found  no iOS name matches

Usage:
    python3 extract_ios_token_map.py --ios-repo ~/gsl-ios
    python3 extract_ios_token_map.py --ios-repo ~/gsl-ios --check   # report drift, write nothing
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
REGISTRY = REPO / "figma" / "figma-tokens-registry.json"
OUT = REPO / "tokens" / "tokens-ios-map.md"
FOUNDATION = "Packages/aviv_design_system_ios/Sources/DesignSystem/Foundation"

# GSL segment -> iOS segment, where the two names differ. Each use makes a row
# `guessing`, and the rule is written into that row's note.
SEGMENT_RENAMES = {"scales": "scale", "symbols": "symbol"}


# --------------------------------------------------------------------------
# Reading the iOS package
# --------------------------------------------------------------------------

def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True).stdout


def ios_files(repo: Path, ref: str, folder: str) -> dict[str, str]:
    names = git(repo, "ls-tree", "-r", "--name-only", ref, f"{FOUNDATION}/{folder}").split()
    return {n: git(repo, "show", f"{ref}:{n}") for n in names if n.endswith(".swift")}


def parse_structs(sources: list[str]) -> dict[str, list[tuple[str, str]]]:
    """Return {'Content.Default': [(member, Type), ...]} for every struct.

    Nesting is tracked with a brace stack, so two structs both called
    `Default` inside different parents stay apart.
    """
    structs: dict[str, list[tuple[str, str]]] = {}
    for src in sources:
        stack: list[tuple[str | None, int]] = []  # (struct path or None, depth)
        depth = 0
        pending: str | None = None
        for line in src.splitlines():
            code = line.split("//")[0]
            m = re.search(r"\b(?:struct|extension)\s+([A-Za-z_][A-Za-z0-9_.]*)", code)
            if m:
                kind = "struct" if "struct" in code[:m.end()].split()[-2:] else "extension"
                name = m.group(1)
                parent = next((p for p, _ in reversed(stack) if p), None)
                if kind == "extension":
                    pending = name
                else:
                    pending = f"{parent}.{name}" if parent else name
                    structs.setdefault(pending, [])
            mm = re.search(r"\bpublic\s+(?:let|var)\s+`?([A-Za-z_][A-Za-z0-9_]*)`?\s*:\s*([A-Za-z_][A-Za-z0-9_.]*)", code)
            if mm and stack:
                owner = next((p for p, _ in reversed(stack) if p), None)
                if owner:
                    structs.setdefault(owner, []).append((mm.group(1), mm.group(2)))
            zero = re.search(r"\bpublic\s+var\s+zero\s*:\s*Double", code)
            if zero and stack:
                owner = next((p for p, _ in reversed(stack) if p), None)
                if owner:
                    structs.setdefault(owner, []).append(("zero", "Double"))
            for ch in code:
                if ch == "{":
                    depth += 1
                    stack.append((pending, depth))
                    pending = None
                elif ch == "}":
                    depth -= 1
                    if stack:
                        stack.pop()
    return structs


def resolve(structs: dict, scope: str, type_name: str) -> str | None:
    """Find a type named inside `scope`, looking outward like Swift does."""
    parts = scope.split(".")
    while parts:
        cand = ".".join(parts + [type_name])
        if cand in structs:
            return cand
        parts.pop()
    return type_name if type_name in structs else None


def leaves(structs: dict, root: str, leaf_types: set[str]) -> dict[tuple[str, ...], str]:
    """Every path from `root` down to a member whose type is a leaf type."""
    out: dict[tuple[str, ...], str] = {}

    def walk(t: str, path: tuple[str, ...]):
        for member, typ in structs.get(t, []):
            if typ in leaf_types:
                out[path + (member,)] = typ
                continue
            sub = resolve(structs, t, typ)
            if sub and sub != t:
                walk(sub, path + (member,))
    walk(root, ())
    return out


def parse_wiring(src: str) -> dict[tuple[str, ...], tuple[str, str]]:
    """Read ColorsDescription's init: which asset, or which hex, fills each path.

    Returns {('border', 'accent'): ('asset', 'borderAccentLightDefault'), ...}.
    The asset names are generated from the GSL token names, which is what lets a
    match on them count as proved.
    """
    body = src[src.index("self."):]
    tok = re.compile(r'self\.(\w+)\s*=|(\w+)\s*:(?!:)|assetColors\.(\w+)'
                     r'|Color\(hex:\s*"([0-9A-Fa-f]{6})"\)|(\()|(\))')
    stack: list[str | None] = []
    pending: str | None = None
    out: dict[tuple[str, ...], tuple[str, str]] = {}
    for m in tok.finditer(body):
        root, label, asset, hexv, opn, cls = m.groups()
        if root or label:
            pending = root or label
        elif asset or hexv:
            path = tuple(x for x in stack if x) + ((pending,) if pending else ())
            out[path] = ("asset", asset) if asset else ("hex", hexv.upper())
            pending = None
        elif opn:
            stack.append(pending)
            pending = None
        elif cls and stack:
            stack.pop()
    return out


# --------------------------------------------------------------------------
# Matching
# --------------------------------------------------------------------------

def norm(seg: str) -> str:
    return re.sub(r"[^a-z0-9]", "", seg.lower())


def match_colour(name: str, ios: dict[tuple[str, ...], str]):
    """Match on the joined name, so a segment iOS merged still matches.

    Proved only when the segments line up one for one. Every other match
    states its rule in the note and is `guessing`.
    """
    segs = [norm(s) for s in name.split("/")[1:]]  # drop the leading `Color`
    notes = []
    renamed = [SEGMENT_RENAMES.get(s, s) for s in segs]
    if renamed != segs:
        notes.append("segment renamed: " + ", ".join(
            f"`{a}` → `{b}`" for a, b in zip(segs, renamed) if a != b))
    joined: dict[str, list[tuple[str, ...]]] = {}
    for k in ios:
        joined.setdefault("".join(norm(p) for p in k), []).append(k)

    tries = [("".join(renamed), None)]
    if renamed and renamed[-1] == "default":
        tries.append(("".join(renamed[:-1]), "final `Default` dropped — iOS has a single colour at the parent"))
    if len(renamed) >= 2:
        tries.append(("".join(renamed[:-1] + ["default", renamed[-1]]),
                      "iOS adds a `default` level before the state"))
    for key, rule in tries:
        hits = joined.get(key, [])
        if len(hits) > 1:
            return None, "not found", notes + ["more than one iOS name matches: " + ", ".join(".".join(h) for h in hits)]
        if hits:
            path = hits[0]
            n = list(notes)
            if rule:
                n.append(rule)
            if [norm(p) for p in path] != renamed and not rule:
                n.append("segments merged on iOS")
            return path, ("guessing" if n else "proved"), n
    return None, "not found", notes


def ios_value(src: str, member: str) -> float | None:
    m = re.search(rf"\b{member}\s*:\s*([0-9.]+)", src)
    return float(m.group(1)) if m else None


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

def table(rows):
    lines = ["| Token | iOS name | Confidence | Note |", "| --- | --- | --- | --- |"]
    for tok, ios, conf, note in rows:
        lines.append(f"| `{tok}` | {f'`{ios}`' if ios else '—'} | {conf} | {note} |")
    return "\n".join(lines)


def build(ios_repo: Path, ref: str) -> str:
    reg = json.load(open(REGISTRY))["categories"]
    commit = git(ios_repo, "rev-parse", "--short=10", ref).strip()
    date = git(ios_repo, "log", "-1", "--format=%cs", ref).strip()

    colour_src = ios_files(ios_repo, ref, "Colors")
    structs = parse_structs(list(colour_src.values()))
    ios_colours = leaves(structs, "ColorsDescription", {"Color"})
    # InteractiveColor is a leaf group of three states.
    for path, typ in list(leaves(structs, "ColorsDescription", {"InteractiveColor"}).items()):
        for state in ("default", "hover", "pressed"):
            ios_colours[path + (state,)] = "Color"

    font_src = "\n".join(ios_files(ios_repo, ref, "Fonts").values())
    space_src = "\n".join(ios_files(ios_repo, ref, "Spacings").values())
    radius_src = "\n".join(ios_files(ios_repo, ref, "CornerRadius").values())
    shadow_src = "\n".join(ios_files(ios_repo, ref, "Shadows").values())

    sections = []
    counts = {"proved": 0, "guessing": 0, "not found": 0}

    def add(title, intro, rows):
        for r in rows:
            counts[r[2]] += 1
        sections.append(f"## {title}\n\n{intro}\n\n{table(rows)}")

    # Colour
    wiring_src = next(v for k, v in colour_src.items() if k.endswith("/ColorsDescription.swift"))
    wiring = parse_wiring(wiring_src)
    by_asset: dict[str, list[tuple[str, ...]]] = {}
    for path, (kind, val) in wiring.items():
        if kind == "asset":
            by_asset.setdefault(norm(val), []).append(path)
    scale_page = (REPO / "tokens" / "color" / "scale.md").read_text()
    scale_hex = {m.group(1): m.group(2).upper()
                 for m in re.finditer(r"^\| `Color/(Scales/[^`]+)` \| `#([0-9A-Fa-f]{6})`", scale_page, re.M)}
    rows = []
    for t in reg["Colors"]["tokens"]:
        name = t["name"]
        spec_name = name.removeprefix("Color/")
        own = norm("".join(spec_name.split("/")))
        hits = by_asset.get(own, [])
        if hits:
            path = min(hits, key=len)
            note = f"iOS fills this path from the asset `{wiring[path][1]}`, named after this token"
            if len(hits) > 1:
                note += "; the same asset also fills " + ", ".join(f"`{'.'.join(h)}`" for h in hits if h != path)
            rows.append((spec_name, "designSystem.colors." + ".".join(path), "proved", note))
            continue
        path, conf, notes = match_colour(name, ios_colours)
        if path and wiring.get(path, ("", ""))[0] == "hex" and spec_name in scale_hex:
            if wiring[path][1] == scale_hex[spec_name]:
                rows.append((spec_name, "designSystem.colors." + ".".join(path), "proved",
                             f"same light value, `#{scale_hex[spec_name]}`, on both sides"))
                continue
            notes.append(f"values differ: GSL `#{scale_hex[spec_name]}`, iOS `#{wiring[path][1]}`")
        ios = "designSystem.colors." + ".".join(path) if path else None
        rows.append((spec_name, ios, conf, "; ".join(notes)))
    add("Colour",
        "**The spec writes a colour without its `Color/` prefix**, as `spec-rules-ai.md` "
        "requires. The iOS name is a `Color`, used wherever SwiftUI takes one — "
        "`.foregroundStyle(…)`, `.background(…)`.",
        rows)

    # Typography
    rows = []
    weights = set(re.findall(r"case\s+(\w+)", font_src))
    for t in reg["Text Styles"]["tokens"]:
        kind, size, weight = t["name"].split("/")
        has_size = re.search(rf"struct\s+{kind.capitalize()}\b[\s\S]*?\bs{size}\s*:\s*DSFont", font_src)
        if has_size and weight in weights:
            rows.append((t["name"], f".dsFont(\\.{kind}.s{size}, weight: .{weight})", "proved", ""))
        else:
            why = [] if has_size else [f"no `s{size}` in `{kind}`"]
            if weight not in weights:
                why.append(f"no `{weight}` weight")
            rows.append((t["name"], None, "not found", "; ".join(why)))
    add("Text style",
        "Applied with the `.dsFont` view modifier. **The weight is part of the name** — "
        "`body/14/bold` is `.dsFont(\\.body.s14, weight: .bold)`.",
        rows)

    # Spacing
    rows = []
    for t in reg["Spacing"]["tokens"]:
        n = t["name"].split("/")[1]
        if n == "None":
            ok = "zero" in space_src
            rows.append((t["name"], "designSystem.spacings.main.zero" if ok else None,
                         "proved" if ok else "not found", "value 0"))
            continue
        v = ios_value(space_src, f"s{n}")
        if v is not None and v == float(n):
            rows.append((t["name"], f"designSystem.spacings.main.s{n}", "proved", f"value {n}, read from the iOS default"))
        else:
            rows.append((t["name"], None, "not found", ""))
    add("Spacing", "A `Double`, in points. Used for padding and stack spacing.", rows)

    # Radius
    rows = []
    for t in reg["Radius"]["tokens"]:
        n = t["name"].split("/")[1]
        if n == "None":
            ok = "zero" in radius_src
            rows.append((t["name"], "designSystem.cornerRadii.zero" if ok else None,
                         "proved" if ok else "not found", "value 0"))
            continue
        v = ios_value(radius_src, f"c{n}") if n.isdigit() else None
        if v is not None and v == float(n):
            rows.append((t["name"], f"designSystem.cornerRadii.c{n}", "proved", f"value {n}, read from the iOS default"))
        elif n == "Rounded":
            rows.append((t["name"], None, "not found",
                         "no fully rounded radius in the iOS foundation. **Not checked:** whether components use a capsule shape instead"))
        else:
            rows.append((t["name"], None, "not found", ""))
    add("Radius", "A `Double`, in points.", rows)

    # Shadow — matched by value: blur radius and vertical offset.
    rows = []
    shadow_page = (REPO / "tokens" / "shadow" / "shadow-tokens.md").read_text()
    gsl = {m.group(1): (float(m.group(2)), float(m.group(3)))
           for m in re.finditer(r"^\| `(\d+)` \| (\d+) \| (\d+) \|", shadow_page, re.M)}
    ios_sh = {}
    for m in re.finditer(r"(e\d+):\s*DSShadow\([\s\S]*?radius:\s*([0-9.]+)[\s\S]*?verticalOffset\(([0-9.]+)\)", shadow_src):
        ios_sh[(float(m.group(2)), float(m.group(3)))] = m.group(1)
    for t in reg["Effect Styles"]["tokens"]:
        n = t["name"]
        val = gsl.get(n)
        e = ios_sh.get(val) if val else None
        if e:
            rows.append((n, f"designSystem.shadows.elevation.{e}", "proved",
                         f"blur {val[0]:g}, y offset {val[1]:g} on both sides"))
        else:
            rows.append((n, None, "not found", ""))
    add("Shadow", "A `DSShadow`. **Matched by value**, because the two sides name shadows differently: GSL by blur radius, iOS by elevation step.", rows)

    # Border width
    rows = [(t["name"], None, "not found",
             "no border width in the iOS foundation. **Not checked:** whether components hold their own")
            for t in reg["Border Width"]["tokens"]]
    add("Border width", "", rows)

    total = sum(counts.values())
    head = f"""# Token names on iOS

_Joins each GSL token name to the name that builds it on iOS. **Generated by
[`scripts/extract_ios_token_map.py`](scripts/extract_ios_token_map.py) — never
edit by hand; re-run the script.**_

## What this file is for

A spec names tokens as `spec-rules-ai.md` requires — `Content/Light/Default`,
`body/14/bold`, `Spacing/16`. An iOS build agent reads this file to find the iOS
name for each one.

**This file never decides which token to use.** The token rulesets decide that.
This file lists every token in the GSL Foundations library, allowed or not, and
only translates a name that was already chosen.

**The spec keeps the GSL name.** An iOS name never appears in a spec, a ruleset
or a token page.

**Every iOS name below is read from the design-system environment**, which a
SwiftUI view gets with `@Environment(\\.designSystem) private var designSystem`.
Text styles are the exception: they are applied with the `.dsFont` modifier.

## Where the names come from

| Field | Value |
| --- | --- |
| GSL names | `figma/figma-tokens-registry.json` |
| iOS repository | `gsl-ios` |
| Ref and commit | `{ref}`, commit `{commit}`, dated {date} |
| Folder read | `{FOUNDATION}/` — `Colors`, `Fonts`, `Spacings`, `CornerRadius`, `Shadows`. The colour paths are read from `ColorsDescription`'s initialiser, which names the asset behind each one |
| GSL values compared | `tokens/color/scale.md` and `tokens/shadow/shadow-tokens.md` |
| How | `git show` at that commit, never the working copy |

## How to read the Confidence column

| Confidence | What it means |
| --- | --- |
| **proved** | For a colour: iOS fills the path from an asset named after this exact token, or, where iOS writes the colour as a literal, the light value is the same on both sides. For a text style: the size and the weight both exist. For a number: the value read from the iOS default is equal. For a shadow: blur and offset are equal |
| **guessing** | The iOS name exists, and the match needed a rule, written in the row's note: segments merged on iOS, a final `Default` dropped, a `default` level added, or a renamed segment. **No iOS engineer has confirmed it** |
| **not found** | No iOS name matched. **This does not prove the app lacks it** — only the foundation folder was read |

## Totals

| Confidence | Tokens |
| --- | --- |
| proved | {counts['proved']} |
| guessing | {counts['guessing']} |
| not found | {counts['not found']} |
| **total** | **{total}** |
"""
    return head + "\n" + "\n\n".join(sections) + "\n"


def without_commit_row(text: str) -> str:
    return "\n".join(l for l in text.splitlines() if not l.startswith("| Ref and commit |"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ios-repo", required=True, type=Path)
    ap.add_argument("--ref", default="origin/develop")
    ap.add_argument("--check", action="store_true", help="report drift, write nothing")
    ap.add_argument("--no-fetch", action="store_true")
    a = ap.parse_args()
    repo = a.ios_repo.expanduser()
    if not a.no_fetch:
        remote, _, branch = a.ref.partition("/")
        git(repo, "fetch", "-q", remote, branch)
    text = build(repo, a.ref)
    if a.check:
        current = OUT.read_text() if OUT.exists() else ""
        # The iOS repo gets commits that touch no token. Those change only the
        # commit row, and must not read as drift, or the check gets ignored.
        if without_commit_row(current) != without_commit_row(text):
            print(f"{OUT.relative_to(REPO)} is stale — a token mapping changed. Re-run without --check")
            sys.exit(1)
        if current != text:
            print(f"{OUT.relative_to(REPO)} is current — only the iOS commit moved, no mapping changed")
            return
        print(f"{OUT.relative_to(REPO)} is current")
        return
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()

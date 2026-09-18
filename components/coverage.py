#!/usr/bin/env python3
"""Generate components-coverage-ledger.md.

Reads every component doc under components/ and the four figma/*-registry.json
files, then writes one coverage table. Every value in the output is derived --
nothing here is a judgement made at generation time.

Run from anywhere:  python3 components/coverage.py
"""

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COMPONENTS = REPO / "components"
FIGMA = REPO / "figma"
OUTPUT = COMPONENTS / "components-coverage-ledger.md"

# --- The registries -------------------------------------------------------

REGISTRIES = [
    ("Components", "figma-components-registry.json"),
    ("Patterns", "figma-patterns-registry.json"),
    ("Experiences", "figma-experiences-registry.json"),
    ("Foundations", "figma-foundations-components-registry.json"),
]

# --- Registry name -> doc path, where slugifying the name does not reach it.
# Source: components-audit.md, "Five docs cover a registry entry under a
# different name".

ALIASES = {
    "Feedback Messages": "feedback-message/feedback-message.md",
    "Table": "tables/tables.md",
    "Bar graph": "charts/bar-chart.md",
    "Donut chart": "charts/donut-chart.md",
    "Line chart": "charts/line-chart.md",
    "Coachmark": "coach-mark/coach-mark.md",
}

# --- What every component is for, and which ones an agent may never select.
# Both are read out of the ruleset's inventory, never listed here. A row there
# reads `| `Name` | Purpose | Doc |`, and a purpose beginning with the never-
# select marker bars the component. That makes the ruleset the single place
# either fact is written -- the earlier version of this script kept its own
# copy, and it went stale within two days of the ruleset being extended.

RULESET = COMPONENTS / "components-rules-ai.md"

INVENTORY_HEADING = re.compile(r"^##\s+The inventory\s*$")
NEXT_H2 = re.compile(r"^##\s+(?!#)")
INVENTORY_ROW = re.compile(r"^\|\s*`([^`]+)`([^|]*)\|([^|]*)\|([^|]*)\|\s*$")
NEVER_SELECT = "🚫"


def load_inventory(path=None):
    """Return {name: (purpose, doc cell)} from the ruleset's inventory."""
    lines = (path or RULESET).read_text().splitlines()
    inside, out = False, {}
    for line in lines:
        if INVENTORY_HEADING.match(line):
            inside = True
            continue
        if inside and NEXT_H2.match(line):
            break
        if not inside:
            continue
        m = INVENTORY_ROW.match(line)
        if m:
            name, _, purpose, doc = m.groups()
            out[name.strip()] = (purpose.strip(), doc.strip())
    if not out:
        raise SystemExit(f"No inventory rows found in {path or RULESET}")
    return out


INVENTORY = load_inventory()


def purpose_of(name):
    """The ruleset's description, or None where it gives one."""
    row = INVENTORY.get(name)
    if not row or not row[0]:
        return None
    return row[0]


def is_never_select(name):
    return purpose_of(name) is not None and purpose_of(name).startswith(NEVER_SELECT)


def reason_not_to_select(name):
    """The never-select purpose with its marker and label stripped off."""
    text = purpose_of(name) or ""
    text = text.replace(NEVER_SELECT, "").strip()
    text = re.sub(r"^\*\*Never select\*\*\s*[—-]\s*", "", text)
    return text.strip()


# --- The template sections that become columns ----------------------------
# Read out of components/component-template.md, never listed here. A heading in
# that file becomes a column when the line directly under it carries a
# `<!-- column: X -->` marker. Document order there is column order here, so
# the template and this check cannot drift apart.

TEMPLATE = COMPONENTS / "component-template.md"

# Everything after this heading in the template is instructions, not a section.
TEMPLATE_INSTRUCTIONS = re.compile(r"^#\s+How to use this template\s*$")

COLUMN_MARKER = re.compile(r"^<!--\s*column:\s*(.+?)\s*-->$")

# A section can also require named bullets inside it, marked in the template as
# `<!-- required: A, B, C -->`. Each becomes a column of its own, so one writing
# rule can be compared across every component instead of only per page.
REQUIRED_MARKER = re.compile(r"^<!--\s*required:\s*(.+?)\s*-->$")


REQUIRED_BULLETS = []   # [(bullet label, the section it must appear in)]


def load_sections(path=None):
    """Return [(column, full section title, heading level, parent H2 or None)].

    Parsed from the template. A marked H2 has no parent; a marked H3 or deeper
    belongs to the nearest H2 above it.
    """
    lines = (path or TEMPLATE).read_text().splitlines()
    out, current_h2 = [], None
    for i, line in enumerate(lines):
        if TEMPLATE_INSTRUCTIONS.match(line):
            break
        m = re.match(r"^(#{2,6})\s+(.*?)\s*$", line)
        if not m:
            continue
        level, title = len(m.group(1)), m.group(2).strip()
        if level == 2:
            current_h2 = title
        column, required = None, []
        for ahead in lines[i + 1:i + 5]:
            marker = COLUMN_MARKER.match(ahead.strip())
            if marker:
                column = marker.group(1)
                continue
            needed = REQUIRED_MARKER.match(ahead.strip())
            if needed:
                required = [x.strip() for x in needed.group(1).split(",")]
                continue
            if ahead.strip():
                break
        if column:
            out.append((column, title, level, None if level == 2 else current_h2))
            for label in required:
                REQUIRED_BULLETS.append((label, title))
    if not out:
        raise SystemExit(f"No `<!-- column: -->` markers found in {TEMPLATE}")
    return out


SECTIONS = load_sections()

PRESENT, MISSING, ABSENT = "✅", "❌", "⬜"

# The platform-readiness table at the top of a doc. A different thing from the
# "### Platform" section, which is prose about platform restrictions.
READINESS_ROW = re.compile(r"^\|\s*Figma\s*\|\s*Web\s*\|\s*iOS\s*\|\s*Android\s*\|", re.M)

# Support pages under charts/ that are not registry components.
CHART_SUPPORT = [
    ("charts/charts.md", "Routing page — points at the chart types below"),
    ("charts/legend.md", "The chart legend, shared by every chart type"),
    ("charts/filters-and-actions.md", "Filters and actions attached to a chart"),
    ("charts/chart-colors.md", "Categorical, sequential, diverging and semantic palettes"),
    ("charts/chart-accessibility.md", "Colour-blind mode and the table fallback"),
]


def slug(name):
    s = name.lower().strip()
    s = re.sub(r"[()]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def load_registry_entries():
    """Return [(name, tier)] for every entry in the four registries."""
    entries = []
    for tier, filename in REGISTRIES:
        data = json.loads((FIGMA / filename).read_text())
        for name in data.get("components", {}):
            entries.append((name, tier))
    return entries


def find_doc(name):
    """Return the doc path relative to components/, or None."""
    if name in ALIASES:
        path = ALIASES[name]
        return path if (COMPONENTS / path).exists() else None
    s = slug(name)
    candidate = f"{s}/{s}.md"
    return candidate if (COMPONENTS / candidate).exists() else None


def clean(text):
    """Drop horizontal rules and surrounding whitespace."""
    return re.sub(r"^\s*-{3,}\s*$", "", text, flags=re.M).strip()


def parse_headings(text):
    """Return [(level, title, own_body, subtree)] in document order.

    own_body is the prose directly under the heading, before any sub-heading.
    subtree is all prose under the heading including its sub-sections, with
    the sub-heading lines themselves removed. A section counts as written if
    anything in its subtree was written -- `### Modifiers` often carries its
    content one level down, under `#### Icons`.
    """
    lines = text.splitlines()
    marks = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            marks.append((i, len(m.group(1)), m.group(2).strip()))

    out = []
    for idx, (i, level, title) in enumerate(marks):
        own_end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        sub_end = len(lines)
        for j, lvl, _ in marks[idx + 1:]:
            if lvl <= level:
                sub_end = j
                break
        heading_rows = {j for j, _, _ in marks if i < j < sub_end}
        subtree = "\n".join(l for j, l in enumerate(lines[i + 1:sub_end], i + 1)
                            if j not in heading_rows)
        out.append((level, title, clean("\n".join(lines[i + 1:own_end])), clean(subtree)))
    return out


def normalise(title):
    return re.sub(r"\s+", " ", title).strip().lower()


def is_not_documented(body):
    return normalise(body).startswith("not documented")


def bullet_answer(section_body, label):
    """What a doc says after `**<label>:**` inside a section, or None.

    Docs write these three as bolded bullets and have since before they were
    required, so this reads the shape already in use rather than demanding a
    heading. Matches with or without the bullet marker and with the colon
    inside or outside the bold.
    """
    pattern = re.compile(
        r"^\s*(?:[*-]\s+)?\*\*\s*" + re.escape(label) + r"\s*:?\s*\*\*\s*:?\s*(.*)$",
        re.M | re.I)
    m = pattern.search(section_body)
    return m.group(1).strip() if m else None


def has_readiness_table(doc_path):
    return bool(READINESS_ROW.search((COMPONENTS / doc_path).read_text()))


def coverage_for(doc_path):
    """Return {column: mark} for one doc."""
    headings = parse_headings((COMPONENTS / doc_path).read_text())
    by_title = {}
    for level, title, own, subtree in headings:
        by_title.setdefault((level, normalise(title)), (own, subtree))

    # Which H3s sit under which H2, so Variants can exclude its Modifiers child.
    children = {}
    current_h2 = None
    for level, title, _, _ in headings:
        if level == 2:
            current_h2 = normalise(title)
            children.setdefault(current_h2, [])
        elif level == 3 and current_h2:
            children[current_h2].append(normalise(title))

    marks = {}
    for column, title, level, parent in SECTIONS:
        key = (level, normalise(title))
        if key in by_title:
            own, subtree = by_title[key]
            if is_not_documented(own):
                marks[column] = MISSING
            elif subtree:
                marks[column] = PRESENT
            else:
                marks[column] = MISSING
            continue

        # Heading absent. If its H2 parent exists and says "Not documented",
        # the section was declared missing rather than never considered.
        if parent:
            parent_key = (2, normalise(parent))
            if parent_key in by_title and is_not_documented(by_title[parent_key][0]):
                marks[column] = MISSING
                continue
        marks[column] = ABSENT

    # The required bullets inside a section, each its own column. Present when
    # the doc answers it, missing when it says nothing or "Not documented",
    # absent when the section carrying it is not on the page at all.
    for label, section in REQUIRED_BULLETS:
        key = (2, normalise(section))
        if key not in by_title:
            marks[label] = ABSENT
            continue
        own, subtree = by_title[key]
        answer = bullet_answer(subtree, label)
        if answer is None or not answer or is_not_documented(answer) \
                or answer.startswith("["):
            marks[label] = MISSING
        else:
            marks[label] = PRESENT

    # "Variants" is the H2 minus its Modifiers child. An H2 whose only content
    # is the Modifiers sub-section documents no variants of its own.
    vm = normalise("Variants & Modifiers")
    if marks["Variants"] == PRESENT:
        own, _ = by_title.get((2, vm), ("", ""))
        others = [c for c in children.get(vm, []) if c != "modifiers"]
        if not own and not others:
            marks["Variants"] = MISSING

    return marks


def main():
    entries = load_registry_entries()

    documented = []      # (name, tier, doc, marks)
    undocumented = []    # (name, tier)
    for name, tier in entries:
        doc = find_doc(name)
        if doc:
            documented.append((name, tier, doc, coverage_for(doc)))
        else:
            undocumented.append((name, tier))

    gaps = [(n, t) for n, t in undocumented if not is_never_select(n)]
    skip = [(n, t) for n, t in undocumented if is_never_select(n)]
    skip_names = sorted({n for n, _ in skip})
    gap_names = sorted({n for n, _ in gaps})
    # Image Ratio and Brand Logo each occupy two registry entries -- they are
    # two distinct Figma components, so both entries are listed.
    dupes = sorted({n for n, _ in undocumented
                    if sum(1 for m, _ in undocumented if m == n) > 1})

    columns = [c for c, _, _, _ in SECTIONS] + [lbl for lbl, _ in REQUIRED_BULLETS]

    # --- Per-section totals across the documented set
    section_totals = {}
    for column in columns:
        counts = {PRESENT: 0, MISSING: 0, ABSENT: 0}
        for *_, marks in documented:
            counts[marks[column]] += 1
        section_totals[column] = counts

    # --- Per-component score
    scored = []
    for name, tier, doc, marks in documented:
        covered = sum(1 for c in columns if marks[c] == PRESENT)
        scored.append((covered, name, tier, doc, marks))

    # Does the inventory's Doc column still match the filesystem? It said
    # "no doc" for Button Bar two days after Button Bar got one, and nothing
    # noticed. Now it is checked on every run.
    drift = []
    seen = set()
    for name, _ in entries:
        if name in seen:
            continue
        seen.add(name)
        row = INVENTORY.get(name)
        if not row:
            continue
        claims_doc = "no doc" not in row[1]
        has_doc = find_doc(name) is not None
        if claims_doc != has_doc:
            drift.append((
                name,
                "has a doc" if claims_doc else "no doc",
                find_doc(name) if has_doc else "no doc",
            ))

    total_entries = len(entries)
    lines = []
    w = lines.append

    w("<!-- GENERATED FILE — do not edit by hand. Re-run: python3 components/coverage.py -->")
    w("")
    w("# Component documentation coverage")
    w("")
    w("_Which components have a doc, and which template sections that doc actually")
    w("fills. **Written by a script** — every mark below is read out of a file, not")
    w("judged. Never edit this page; re-run `components/coverage.py`._")
    w("")
    w("---")
    w("")
    w("## How to read it")
    w("")
    w("| Mark | Meaning |")
    w("| --- | --- |")
    w(f"| {PRESENT} | The section has content |")
    w(f"| {MISSING} | The section is there and says `Not documented` |")
    w(f"| {ABSENT} | The section heading is missing from the page entirely |")
    w("")
    w(f"{PRESENT} means somebody wrote something, not that it is complete or correct.")
    w("A few pages say *\"Not applicable\"* and explain why — that counts as written.")
    w("")
    w(f"{MISSING} and {ABSENT} differ in what they tell you. {MISSING} means someone")
    w(f"looked at the section and had nothing. {ABSENT} means the section was never")
    w("put on the page. Where an `##` parent says `Not documented` and its `###`")
    w(f"children are missing, the children are marked {MISSING} — the parent already")
    w("declared them.")
    w("")
    w("There is no *not relevant* mark. Deciding a section does not apply to a")
    w("component is a judgement, and no rule for it exists yet. Nothing here is")
    w("inferred.")
    w("")
    w("---")
    w("")
    w("## Where things stand")
    w("")
    w("| | Count |")
    w("| --- | --- |")
    w(f"| Registry entries across the four Figma libraries | **{total_entries}** |")
    w(f"| — have a doc | **{len(documented)}** |")
    w(f"| — no doc, and an agent may select them | **{len(gaps)}** entries, {len(gap_names)} names |")
    w(f"| — no doc, and an agent should never select them | **{len(skip)}** entries, {len(skip_names)} names |")
    w("")
    w("Entries outnumber names because " +
      " and ".join(f"`{n}`" for n in dupes) + " each exist in **two** Figma")
    w("libraries under the same name, with different keys. They are two distinct")
    w("components, so both entries are listed.")
    w("")
    filled = sum(section_totals[c][PRESENT] for c in columns)
    cells = len(documented) * len(columns)
    w(f"Across the {len(documented)} documented entries there are {cells} template")
    w(f"sections to fill. **{filled} are filled** — {round(100 * filled / cells)}%.")
    w("")
    w("---")
    w("")
    w("## Which sections are worst")
    w("")
    w("Ordered by how many documented components leave the section empty.")
    w("")
    w("| Section | ✅ | ❌ | ⬜ | Filled |")
    w("| --- | --- | --- | --- | --- |")
    ranked = sorted(columns, key=lambda c: section_totals[c][PRESENT])
    for column in ranked:
        t = section_totals[column]
        pct = round(100 * t[PRESENT] / len(documented))
        w(f"| {column} | {t[PRESENT]} | {t[MISSING]} | {t[ABSENT]} | {pct}% |")
    w("")
    w("**Read `Platform` differently from the rest.** It is prose saying a component")
    w("is restricted to some platforms — *\"pagination is only used on the web\"*. A")
    w(f"component with no restriction needs no such section, so its {ABSENT} is")
    w("probably correct rather than a gap. Every other row here is a real gap.")
    w(f"**Which of the {section_totals['Platform'][ABSENT]} are deliberate is unknown** — nobody has")
    w("checked, and until somebody does this row cannot be read as a score.")
    w("")
    w("**`a11y` and `Breakpoints` are the two worth acting on.** Between them they")
    w(f"account for {section_totals['a11y'][MISSING] + section_totals['Breakpoints'][MISSING]} pages that")
    w("looked at the section and wrote nothing.")
    w("")
    w("---")
    w("")
    w("## Which components are worst")
    w("")
    w(f"The ten documented components filling fewest of the {len(columns)} sections.")
    w("")
    w("| Component | Tier | Filled |")
    w("| --- | --- | --- |")
    for covered, name, tier, doc, _ in sorted(scored)[:10]:
        w(f"| [{name}]({doc}) | {tier} | {covered} / {len(columns)} |")
    w("")
    w("---")
    w("")
    w(f"## The matrix — {len(documented)} documented entries")
    w("")
    w("| Component | Tier | Readiness | " + " | ".join(columns) + " | Filled |")
    w("| --- | --- | --- |" + " --- |" * (len(columns) + 1))
    for name, tier, doc, marks in sorted(documented, key=lambda r: r[0].lower()):
        covered = sum(1 for c in columns if marks[c] == PRESENT)
        ready = PRESENT if has_readiness_table(doc) else ABSENT
        row = " | ".join(marks[c] for c in columns)
        w(f"| [{name}]({doc}) | {tier} | {ready} | {row} | {covered} |")
    w("")
    no_ready = sorted(n for n, _, d, _ in documented if not has_readiness_table(d))
    w("**Readiness** is the `Figma | Web | iOS | Android` table at the top of a page,")
    w("not a template section — so it is not counted in *Filled*. " +
      f"{len(documented) - len(no_ready)} of {len(documented)} pages")
    w("carry it. The " + str(len(no_ready)) + " without it: " +
      ", ".join(f"`{n}`" for n in no_ready) + ".")
    w("")
    w("### Chart pages that are not registry components")
    w("")
    w("`Bar graph`, `Donut chart` and `Line chart` are registry entries and appear")
    w("in the matrix above. These five pages support them and have no registry entry")
    w("of their own, so they are listed rather than scored.")
    w("")
    w("| Page | What it covers |")
    w("| --- | --- |")
    for path, what in CHART_SUPPORT:
        w(f"| [{path}]({path}) | {what} |")
    w("")
    w("---")
    w("")
    w(f"## The gap — {len(gap_names)} components an agent may select, with no doc at all")
    w("")
    w("These have no page anywhere in this repo. The *What it is* column is the one")
    w("sentence the ruleset's inventory gives — enough for an agent to pick the right")
    w("component, never enough to build one correctly.")
    w("")
    w("| Component | Tier | What it is |")
    w("| --- | --- | --- |")
    for name, tier in sorted(gaps, key=lambda r: (purpose_of(r[0]) is not None, r[0].lower())):
        w(f"| {name} | {tier} | {purpose_of(name) or '**Undescribed** — the ruleset has no sentence for it'} |")
    w("")
    blind = sorted({n for n, _ in gaps if purpose_of(n) is None})
    if blind:
        w(f"**{len(blind)} of those {len(gap_names)} are described nowhere** — no doc, and no")
        w("sentence in the ruleset either: " + ", ".join(f"`{n}`" for n in blind) + ".")
    else:
        w(f"**All {len(gap_names)} carry a sentence in the ruleset.** None is a doc, so an")
        w("agent can choose these components and cannot build them without inventing")
        w("the detail.")
    w("")
    w("---")
    w(f"## No doc, and none needed — {len(skip_names)} names")
    w("")
    w("An agent should never select these, so the missing doc is not a gap. The")
    w("reasons are the ruleset's own, read from the rows it marks " + NEVER_SELECT + ".")
    w("")
    w("| Component | Tier | Why no doc is needed |")
    w("| --- | --- | --- |")
    for name, tier in sorted(skip, key=lambda r: r[0].lower()):
        w(f"| {name} | {tier} | {reason_not_to_select(name)} |")
    w("")
    barred = sorted(n for n, _, _, _ in documented if is_never_select(n))
    if barred:
        w("**Careful with " + ", ".join(f"`{n}`" for n in barred) + ".** " +
          ("They are" if len(barred) > 1 else "It is") + " in the matrix above")
        w("with a doc, and still not selectable. A well-filled row in this page is not")
        w("permission to use the component. The ruleset decides that, not this page.")
        w("")
    w("---")
    w("")
    w("## What this page is built from")
    w("")
    w("| Input | Used for |")
    w("| --- | --- |")
    w("| `figma/figma-components-registry.json` | The Components tier — what exists |")
    w("| `figma/figma-patterns-registry.json` | The Patterns tier |")
    w("| `figma/figma-experiences-registry.json` | The Experiences tier |")
    w("| `figma/figma-foundations-components-registry.json` | The Foundations tier |")
    w("| `components/<name>/<name>.md` | Every mark in the matrix |")
    w("| [component-template.md](component-template.md) | Which sections are columns, and in what order |")
    w("| [components-rules-ai.md](components-rules-ai.md) | What each component is for, and which may never be selected |")
    w("| [components-audit.md](components-audit.md) | The five name aliases |")
    w("")
    w("### Does the ruleset's inventory still match the files?")
    w("")
    if drift:
        w("**No — " + str(len(drift)) +
          (" row disagrees.**" if len(drift) == 1 else " rows disagree.**") +
          " The inventory names a doc the")
        w("filesystem does not have, or misses one it does. Fix the inventory; this page")
        w("reads the files and the inventory does not.")
        w("")
        w("| Component | The inventory says | On disk |")
        w("| --- | --- | --- |")
        for name, claimed, actual in drift:
            w(f"| {name} | {claimed} | {actual} |")
    else:
        w(f"**Yes.** All {len(INVENTORY)} inventory rows agree with the files on disk about")
        w("whether a doc exists. Checked every time this page is generated, because the")
        w("inventory went stale unnoticed once already.")
    w("")

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUTPUT.relative_to(REPO)}")
    print(f"  {total_entries} registry entries: {len(documented)} documented, "
          f"{len(gaps)} selectable gaps, {len(skip)} not selectable")


if __name__ == "__main__":
    main()

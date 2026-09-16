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

# --- Why an undocumented entry needs no doc.
# Source: components-audit.md, "Not selectable, and why". This is the one
# classification in this file that a human made; it is copied, not re-derived.

NOT_SELECTABLE = {
    "Home Indicator": "Chrome — iOS system affordance",
    "Status Bar": "Chrome — OS-rendered",
    "Webview": "Chrome — embedded browser container, iOS/Android only",
    "Cell Content": "Composed-only — a slot inside Cards and lists",
    "Content Placeholder": "Composed-only — a slot, swapped for local content",
    "Filter dropdown container": "Composed-only — sibling pattern to Filter bar",
    "Map Polygon": "Composed-only — part of the Map experience",
    "Map Polygon backdrop": "Composed-only — part of the Map experience",
    "mapPinsV2_SL": "Composed-only — brand-specific pin set (SeLoger)",
    "mapPinsV2_IWT": "Composed-only — brand-specific pin set (Immowelt)",
    "Programmatic Ads": "Withheld — commercial ad slot, not a design choice",
    "Tab Bar": "Withheld — in-progress refactor. Use Tabs until it settles",
    "Footer": "Withheld — Figma only, not developed. Owned by Header/Footer team",
    "Favicon": "Asset — fixed, no properties of its own",
    "Brand App Icons": "Asset — per-platform, per-brand exports",
    "Brand Logo": "Asset — configured by brand, not chosen by design intent",
    "Flag": "Asset — country flag family",
}

# --- What an undocumented but selectable component is for, where the repo
# says so somewhere else. Source: components-audit.md, "Selectable but
# undocumented".

KNOWN_PURPOSE = {
    "Tooltip": ("Brief overlay clarifying one UI element", "coach-mark"),
    "State Messages": ("Inline form feedback — guide, correct, inform", "alert, text-area, text-field"),
    "Text Button": ("A distinct component from Button", "button, action-menu, autocomplete"),
    "Pop-up": ("The small-content alternative to Modal bottom sheet", "modal-bottom-sheet"),
    "Loading State": ("Signals data or content is being fetched", "autocomplete, dropdown, info-state"),
    "Image Slider": ("Horizontally sliding image sequence", "listing-card, carousel"),
    "Score Tag": ("A Tag specialised for seller lead scoring", "tag"),
    "Navigation Bar (App)": ("In-app navigation between destinations. Mobile only", "tabs, registry"),
    "Badge": ("Attention marker attached to a host element", "button, tabs, cell-content"),
    "Image Ratio": ("Enforces an image aspect ratio", "registry"),
    "Date Field": ("Date input, distinct from the Date Picker calendar", "date-picker, text-area"),
    "Filter button": ("The individual filter control inside Filter bar", "filter-bar, charts"),
    "Burger menu": ("Mobile menu opened from the navigation bar", "navigation-bar"),
    "Burger menu (profil)": ("A distinct component from Burger menu", "registry"),
    "Menus": ("Profile and language menus", "registry"),
    "Floor selection": ("Picking an apartment floor, including ground floor", "counter-field"),
    "Listing summary": ("The higher-flexibility alternative to Listing card", "listing-card"),
    "Map template": ("The map experience container", "registry"),
}

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

    gaps = [(n, t) for n, t in undocumented if n not in NOT_SELECTABLE]
    skip = [(n, t) for n, t in undocumented if n in NOT_SELECTABLE]
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
    w("probably correct rather than a gap. Every other row here is a real gap. Which")
    w("of the 29 are deliberate is unknown — nobody has checked.")
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
    w("These have no page anywhere in this repo. An agent asked to use one has")
    w("nothing to read. Where the *Known from* column is filled, the repo describes")
    w("the component inside **another component's** page — a sentence, not a doc.")
    w("")
    w("| Component | Tier | What it is | Known from |")
    w("| --- | --- | --- | --- |")
    for name, tier in sorted(gaps, key=lambda r: (r[0] not in KNOWN_PURPOSE, r[0].lower())):
        purpose, source = KNOWN_PURPOSE.get(name, ("**Unknown**", "—"))
        w(f"| {name} | {tier} | {purpose} | {source} |")
    w("")
    blind = sorted({n for n, _ in gaps if n not in KNOWN_PURPOSE})
    w(f"**{len(blind)} of those {len(gap_names)} have no evidence anywhere in the repo** —")
    w("no doc, and no other page mentions what they do: " +
      ", ".join(f"`{n}`" for n in blind) + ".")
    w("")
    w("---")
    w(f"## No doc, and none needed — {len(skip_names)} names")
    w("")
    w("An agent should never select these, so the missing doc is not a gap.")
    w("The reasons are copied from")
    w("[components-audit.md](components-audit.md#not-selectable-and-why) — that")
    w("classification is the one human judgement this page carries.")
    w("")
    w("| Component | Tier | Why no doc is needed |")
    w("| --- | --- | --- |")
    for name, tier in sorted(skip, key=lambda r: r[0].lower()):
        w(f"| {name} | {tier} | {NOT_SELECTABLE[name]} |")
    w("")
    documented_but_barred = sorted(n for n, _, _, _ in documented if n in NOT_SELECTABLE)
    if documented_but_barred:
        w("**Careful with " + ", ".join(f"`{n}`" for n in documented_but_barred) +
          ".** It is in the matrix above")
        w("with a full doc, and it is still not selectable — " +
          NOT_SELECTABLE[documented_but_barred[0]].lower() + ". A well-filled")
        w("row in this page is not permission to use the component. The ruleset decides")
        w("that, not this page.")
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
    w("| [components-audit.md](components-audit.md) | The five name aliases, and which components are not selectable |")
    w("")

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUTPUT.relative_to(REPO)}")
    print(f"  {total_entries} registry entries: {len(documented)} documented, "
          f"{len(gaps)} selectable gaps, {len(skip)} not selectable")


if __name__ == "__main__":
    main()

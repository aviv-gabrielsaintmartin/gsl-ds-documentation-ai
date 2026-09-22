#!/usr/bin/env python3
"""Generate components-template-drift.md.

Measures every component doc against components/component-template.md and
reports what would have to change for the doc to match it. Every figure below
is read out of a file. The one judgement here is which template section an
off-template heading belongs to, and it is written down in SYNONYM_OF, once.

Run from anywhere:  python3 components/template-drift.py
"""

import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COMPONENTS = REPO / "components"
TEMPLATE = COMPONENTS / "component-template.md"
OUTPUT = COMPONENTS / "components-template-drift.md"

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.M)
INSTRUCTIONS = re.compile(r"^#\s+How to use this template\s*$")
READINESS = re.compile(r"^\|\s*Figma\s*\|\s*Web\s*\|\s*iOS\s*\|\s*Android\s*\|", re.M)

# --- The one judgement on this page ---------------------------------------
# An off-template heading is one of two things. Either it names a template
# section under a different word -- then it is listed here, and merging it is a
# content decision a human makes. Or it names an axis of the component --
# `Size`, `Type`, `Alignment` -- which is not a section at all and belongs one
# level down, under the section above it. Anything not listed here is treated
# as an axis.
#
# `Anatomy` is deliberately NOT a section of its own. Gabriel's reasoning,
# 16 Sep 2026: a component's elements can be shown or hidden and often cannot
# all appear at once, so a diagram of every part is misleading. What those
# sections actually hold -- which sub-components exist and what each can be
# set to -- is Modifiers.

SYNONYM_OF = {
    "Anatomy": "Modifiers",
    "Variants": "Variants & Modifiers",
    "Interaction": "Interactive States & Loading",
    "Interactions": "Interactive States & Loading",
    "Animation": "Interactive States & Loading",
    "Scrolling": "Touch Target & Layout",
    "Scroll": "Touch Target & Layout",
    "Horizontal scroll": "Touch Target & Layout",
    "Position & Scrolling": "Touch Target & Layout",
    "Width": "Touch Target & Layout",
    "Scale": "Touch Target & Layout",
    "Clipped content": "Touch Target & Layout",
    "Overflow content": "Touch Target & Layout",
    "Overflow Content": "Touch Target & Layout",
    "Main elements": "Content & UX Writing",
    "Labels": "Content & UX Writing",
    "Label": "Content & UX Writing",
    "Helper text": "Content & UX Writing",
    "Digit": "Content & UX Writing",
    "Country": "Content & UX Writing",
    "Device": "Breakpoints & Platform Adaptations",
    "Color-blind friendly mode": "Accessibility (a11y)",
}

# Headings that are links to other pages, not sections of the doc.
LINK_SECTIONS = {"Resources", "Supporting documentation"}

# Absent by design: the template says to omit Platform when a component has no
# platform restriction, so its absence is not evidence of anything.
OMITTABLE = {"Platform"}

# Pages under charts/ the template does not describe. Checked page by page on
# 16 Sep: `charts.md` is a routing page, and the palettes and the accessibility
# fallback are organised by the thing itself rather than by component -- what
# Gabriel called a different architecture. Left as they are, deliberately.
#
# `legend.md` and `filters-and-actions.md` are NOT here. Both already carry the
# template's own sections and are measured like any component.
SUPPORT_PAGES = {
    "charts/charts.md", "charts/chart-colors.md", "charts/chart-accessibility.md",
}

# Pages measured for their sections but never for a readiness table. A legend
# is part of a chart, not something shipped per platform, so a Figma/Web/iOS/
# Android row would be four cells nobody can fill.
NO_READINESS_EXPECTED = {
    "charts/legend.md", "charts/filters-and-actions.md",
}


def template_sections():
    """[(level, title)] for every named H2/H3 in the template, in order."""
    return [(lv, t) for lv, t, free in _template_headings() if not free]


def free_name_slots():
    """H2 sections whose H3 children may be called anything.

    The template writes one as `### [Variant Category Name]` — a slot, not a
    title. A doc filling it with `### Shapes and sizes` is using the template
    correctly, and counting that as drift makes the report cry wolf: it was
    64 of 115 before this was handled.
    """
    out, current_h2 = set(), None
    for lv, title, free in _template_headings():
        if lv == 2:
            current_h2 = title
        elif lv == 3 and free and current_h2:
            out.add(current_h2)
    return out


def _template_headings():
    """[(level, title, is_a_free_slot)] for the template's H2s and H3s."""
    lines = TEMPLATE.read_text().splitlines()
    out = []
    for line in lines:
        if INSTRUCTIONS.match(line):
            break
        m = re.match(r"^(#{2,3})\s+(.*?)\s*$", line)
        if m:
            title = m.group(2).strip()
            out.append((len(m.group(1)), title, title.startswith("[")))
    return out


def headings_of(path):
    return [(len(h), t.strip()) for h, t in HEADING.findall(path.read_text())]


def fix_for(title, sections):
    if title in LINK_SECTIONS:
        return "link list — belongs under the title, not in a section"
    if title in SYNONYM_OF:
        return f"rename to **{SYNONYM_OF[title]}** and merge"
    return "one level down, under the section above it"


def main():
    sections = template_sections()
    titles = [t for _, t in sections]
    order = {t: n for n, t in enumerate(titles)}
    free_under = free_name_slots()

    # Only the usage doc is measured against the template. A sibling such as
    # `navigation-bar-figma.md` is a platform specification with its own shape,
    # so it is not drift for it to look nothing like this template.
    docs = sorted(p for p in COMPONENTS.glob("*/*.md")
                  if p.stem == p.parent.name or p.parent.name == "charts")
    rows, clean, support = [], [], []
    extra_names, missing_count = Counter(), Counter()

    for md in docs:
        heads = headings_of(md)
        h23 = [(lv, t) for lv, t in heads if lv in (2, 3)]
        present = [t for _, t in h23]

        # An H3 under a section that takes free names is the template working,
        # not drift. Track which H2 each H3 sits under to tell them apart.
        extra, current_h2 = [], None
        for lv, t in heads:
            if lv == 2:
                current_h2 = t
            if lv not in (2, 3) or t in titles:
                continue
            # A free slot takes ANY name. Checked doc by doc on 16 Sep: every
            # H3 there that collides with a section title -- `Width`, `Labels`,
            # `Device`, `Country`, `Horizontal scroll` -- is a real variant
            # category with its own comparison table. The collision is a
            # coincidence of wording, not a misfiling.
            if lv == 3 and current_h2 in free_under:
                continue
            extra.append(t)
        missing = [t for t in titles if t not in present]
        seq = [order[t] for t in present if t in order]
        out_of_order = sum(1 for a, b in zip(seq, seq[1:]) if b < a)
        wrong_level = [t for lv, t in h23 if t in order
                       and lv != dict((t2, lv2) for lv2, t2 in sections)[t]]
        name = md.relative_to(COMPONENTS).as_posix()
        readiness = bool(READINESS.search(md.read_text())) \
            or name in NO_READINESS_EXPECTED

        for t in extra:
            extra_names[t] += 1
        for t in missing:
            missing_count[t] += 1

        record = dict(name=md.relative_to(COMPONENTS).as_posix(), extra=extra,
                      missing=[t for t in missing if t not in OMITTABLE],
                      omitted=[t for t in missing if t in OMITTABLE],
                      out_of_order=out_of_order, wrong_level=wrong_level,
                      readiness=readiness)
        if record["name"] in SUPPORT_PAGES:
            support.append(record)
        elif not extra and not record["missing"] and not out_of_order \
                and not wrong_level and readiness:
            clean.append(record)
        else:
            rows.append(record)

    def weight(r):
        return (len(r["extra"]) * 2 + len(r["missing"]) + r["out_of_order"] * 3
                + len(r["wrong_level"]) * 2 + (0 if r["readiness"] else 2))

    rows.sort(key=lambda r: (-weight(r), r["name"]))

    kinds = Counter()
    for t, n in extra_names.items():
        if t in LINK_SECTIONS:
            kinds["link"] += n
        elif t in SYNONYM_OF:
            kinds["synonym"] += n
        else:
            kinds["axis"] += n

    w = []
    a = w.append
    a("<!-- GENERATED FILE — do not edit by hand. Re-run: python3 components/template-drift.py -->")
    a("")
    a("# Template drift")
    a("")
    a("_How far each component doc sits from")
    a("[component-template.md](component-template.md), and what would close the")
    a("gap. **Written by a script** — re-run it and the numbers move. Never edit")
    a("this page._")
    a("")
    a("---")
    a("")
    a("## Why this page exists and the coverage ledger does not cover it")
    a("")
    a("[components-coverage-ledger.md](components-coverage-ledger.md) measures what")
    a("is **filled in**. It looks for the template's own headings and reports which")
    a("carry content.")
    a("")
    a("It cannot see a heading the template never defined. A doc can put half its")
    a("content under sections that do not exist and still score well there. This")
    a("page is the other half of the question.")
    a("")
    a("---")
    a("")
    a("## Where things stand")
    a("")
    a("| | Count |")
    a("| --- | --- |")
    a(f"| Component docs measured | **{len(rows) + len(clean)}** |")
    a(f"| — already match the template | **{len(clean)}** |")
    a(f"| — need something changed | **{len(rows)}** |")
    a(f"| Chart support pages, listed apart | {len(support)} |")
    a(f"| Headings the template does not define | **{sum(extra_names.values())}**, "
      f"under {len(extra_names)} distinct names |")
    a(f"| Template sections absent from a page | **{sum(v for k, v in missing_count.items() if k not in OMITTABLE)}** |")
    a(f"| Sections at the wrong heading level | **{sum(len(r['wrong_level']) for r in rows)}** |")
    a(f"| Sections out of template order | **{sum(r['out_of_order'] for r in rows)}** |")
    a(f"| Pages with no readiness table | **{sum(1 for r in rows if not r['readiness'])}** |")
    a("")
    a("---")
    a("")
    a("## The three fixes, and how much of the drift each one clears")
    a("")
    a("Every off-template heading found so far falls into one of these. None has")
    a("ever needed a fourth. All three need a person, for the reason under each.")
    a("")
    a("**None of the three is a script.** Each was tried: a scripted pass was")
    a("built for the first and thrown away, because in all 11 cases the heading")
    a("has to move to a different parent rather than down a level where it is.")
    a("")
    a("| The fix | Headings | What it is |")
    a("| --- | --- | --- |")
    a(f"| **Move to the right section** | {kinds['axis']} | The heading names an "
      "axis of the component — `Opening menu`, `Rating results`, `Padding "
      "options` — sitting under a section it does not belong to. **Not "
      "mechanical:** demoting it in place would leave it under whatever "
      "happens to sit above, or under nothing at all. Somebody has to choose "
      "the destination |")
    a(f"| **Rename and merge** | {kinds['synonym']} | The heading is a template "
      "section under another word — `Interaction` for states, `Scrolling` for "
      "layout. **Not mechanical:** both headings can hold content, and merging "
      "them is a judgement |")
    a(f"| **Move out of the sections** | {kinds['link']} | The heading is a list "
      "of links to other pages. Links belong under the title, above the first "
      "`##` |")
    a("")
    a("**A free-name slot is not drift.** The template writes one H3 as")
    a("`### [Variant Category Name]` — a slot that takes any name. A doc filling")
    a("it with `### Shapes and sizes` is using the template correctly. Those are")
    a("not counted here. Before this was handled the page reported 64 of them as")
    a("drift, which was wrong and made the real work look three times bigger.")
    a("")
    a("**A free slot takes any name, including a section's.** `### Width` under")
    a("*Variants & Modifiers* looks like a misfiled layout section and is not:")
    a("it holds a Fixed / Full width comparison. All nine such collisions were")
    a("read on 16 Sep and every one was a real variant category.")
    a("")
    a("**`Anatomy` is not a section, and will not become one.** Decided 16 Sep 2026:")
    a("a component's elements can be shown or hidden, and often cannot all appear")
    a("at once, so a picture of every part at once misleads. What those sections")
    a("really hold — which sub-components exist, and what each can be set to — is")
    a("**Modifiers**.")
    a("")
    a("---")
    a("")
    a("## What each doc needs")
    a("")
    a("Ordered by how much. `—` means nothing to do in that column.")
    a("")
    a("| Doc | Extra headings | Missing sections | What to do |")
    a("| --- | --- | --- | --- |")
    for r in rows:
        extra = ", ".join(f"`{t}`" for t in r["extra"]) or "—"
        missing = ", ".join(r["missing"]) or "—"
        todo, grouped = [], {}
        for t in r["extra"]:
            grouped.setdefault(fix_for(t, sections), []).append(t)
        for fix, names in grouped.items():
            todo.append(", ".join(f"`{n}`" for n in names) + f" → {fix}")
        if r["wrong_level"]:
            todo.append("at the wrong heading level: " + ", ".join(r["wrong_level"]))
        if r["out_of_order"]:
            todo.append(f"{r['out_of_order']} section(s) out of template order")
        if not r["readiness"]:
            todo.append("**no readiness table**")
        a(f"| [{r['name']}]({r['name']}) | {extra} | {missing} | "
          + ("; ".join(todo) or "—") + " |")
    a("")
    if clean:
        a(f"**{len(clean)} docs need nothing**: "
          + ", ".join(f"`{r['name'].split('/')[0]}`" for r in clean) + ".")
        a("")
    a("---")
    a("")
    a("## The chart support pages")
    a("")
    a("These document a part of a chart — the legend, the palettes, the")
    a("accessibility fallback — not a component. Most template sections cannot")
    a("apply to them, so their missing sections are not counted above. What is")
    a("listed here is only the off-template headings.")
    a("")
    a("| Doc | Extra headings | What to do |")
    a("| --- | --- | --- |")
    for r in support:
        grouped = {}
        for t2 in r["extra"]:
            grouped.setdefault(fix_for(t2, sections), []).append(t2)
        todo = "; ".join(", ".join(f"`{n}`" for n in names) + f" → {fix}"
                         for fix, names in grouped.items()) or "—"
        a(f"| [{r['name']}]({r['name']}) | "
          + (", ".join(f"`{t2}`" for t2 in r["extra"]) or "—") + f" | {todo} |")
    a("")
    a("**Whether the template should apply to them at all is undecided.** Nobody")
    a("has asked the question; they are split out here so they do not drown the")
    a("component list above.")
    a("")
    a("---")
    a("")
    a("## Which sections go missing")
    a("")
    a("| Section | Absent from |")
    a("| --- | --- |")
    for _, t in sections:
        a(f"| {t} | {missing_count[t]} docs |")
    a("")
    a("**Read `Platform` differently from the rest.** The template says to omit it")
    a("when a component has no platform restriction, so its absence is expected on")
    a("most pages and is not counted as drift above. Which of those absences are")
    a("deliberate is unknown — nobody has checked.")
    a("")
    a("---")
    a("")
    a("## What this page is built from")
    a("")
    a("| Input | Used for |")
    a("| --- | --- |")
    a("| [component-template.md](component-template.md) | The sections every doc is measured against |")
    a("| `components/<name>/<name>.md` | Every heading counted here |")
    a("| `SYNONYM_OF` in `components/template-drift.py` | Which template section an off-template heading duplicates. **The one judgement on this page** |")

    OUTPUT.write_text("\n".join(w) + "\n")
    # `check-all.py` redirects OUTPUT to a temp file, to ask whether the
    # committed page is still current without touching it. The path is then
    # outside the repo, and `relative_to` raised after the file was already
    # written -- a crash reporting a success. Name it plainly instead.
    shown = OUTPUT.relative_to(REPO) if OUTPUT.is_relative_to(REPO) else OUTPUT
    print(f"Wrote {shown}")
    print(f"  {len(docs)} docs: {len(clean)} match the template, {len(rows)} need work")
    print(f"  {sum(extra_names.values())} extra headings — "
          f"{kinds['axis']} level, {kinds['synonym']} merge, {kinds['link']} links")


if __name__ == "__main__":
    main()

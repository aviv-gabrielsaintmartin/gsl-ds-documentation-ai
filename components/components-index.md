# Components

Component usage documentation for the GSL Design System.

## For AI generation

**Read the ruleset, not this list.** This page says what exists; the ruleset says
which component to reach for, and which ones must never be selected.

| File | What it is |
| --- | --- |
| [components-rules-ai.md](components-rules-ai.md) | **The ruleset** — intent → component, tier order, platform limits, the full 98-item inventory across all four Figma libraries |
| [components-rules-ai-audit.md](components-rules-ai-audit.md) | The evidence behind it, what was rejected, and the open questions. **Never read as rules** |
| [components-rules-ai-eval.md](components-rules-ai-eval.md) | The check on the ruleset — 64 intents with expected answers, scoring bands, and the run log |
| [components-coverage-ledger.md](components-coverage-ledger.md) | **Script-written.** Which of the 98 registry entries have a doc, and which template sections that doc fills. **Never read as rules** — it measures the docs, it does not say what may be used |
| [component-template.md](component-template.md) | **The one definition of a component doc.** Its headings are the contract `coverage.py` and `template-drift.py` both read |
| [components-template-drift.md](components-template-drift.md) | **Script-written.** How far each doc sits from the template, and what would close the gap. **Never read as rules** |
| [components-ios-map.md](components-ios-map.md) | Each component's SwiftUI name on iOS, with how sure the pairing is. **Translates a name already chosen — never read to choose one** |

The list below holds one row per component folder — **69** of them. The
ruleset's inventory covers all **98** registry entries: **71** reach a doc and
**27** do not. The two counts differ because `charts/` answers several registry
entries from a single row.

## Component list

| Component |
| --- |
| [Accordion](accordion/accordion.md) |
| [Action menu](action-menu/action-menu.md) |
| [Alert](alert/alert.md) |
| [Autocomplete](autocomplete/autocomplete.md) |
| [Avatar](avatar/avatar.md) |
| [Badge](badge/badge.md) |
| [Badge store](badge-store/badge-store.md) |
| [Breadcrumb](breadcrumb/breadcrumb.md) |
| [Button](button/button.md) |
| [Burger menu](burger-menu/burger-menu.md) |
| [Button bar](button-bar/button-bar.md) |
| [Button card](button-card/button-card.md) |
| [Button group](button-group/button-group.md) |
| [Card](card/card.md) |
| [Carousel](carousel/carousel.md) |
| [Cell content](cell-content/cell-content.md) |
| [Charts (Pattern)](charts/charts.md) |
| [Checkbox](checkbox/checkbox.md) |
| [Checkbox group](checkbox-group/checkbox-group.md) |
| [Chip](chip/chip.md) |
| [Chip group](chip-group/chip-group.md) |
| [Coach mark](coach-mark/coach-mark.md) |
| [Counter field](counter-field/counter-field.md) |
| [Date field](date-field/date-field.md) |
| [Date picker](date-picker/date-picker.md) |
| [Divider](divider/divider.md) |
| [Dropdown](dropdown/dropdown.md) |
| [Energy Tag](energy-tag/energy-tag.md) |
| [Estimation card](estimation-card/estimation-card.md) |
| [Feedback bar](feedback-bar/feedback-bar.md) |
| [Feedback message](feedback-message/feedback-message.md) |
| [Feedback thumb buttons](feedback-thumb-buttons/feedback-thumb-buttons.md) |
| [Filter bar](filter-bar/filter-bar.md) |
| [Floating button group](floating-button-group/floating-button-group.md) |
| [Floor selection](floor-selection/floor-selection.md) |
| [Image slider](image-slider/image-slider.md) |
| [Info state](info-state/info-state.md) |
| [KPI](kpi/kpi.md) |
| [Link](link/link.md) |
| [Listing card](listing-card/listing-card.md) |
| [Listing summary](listing-summary/listing-summary.md) |
| [Loading state](loading-state/loading-state.md) |
| [Map template](map-template/map-template.md) |
| [Media upload](media-upload/media-upload.md) |
| [Mega menus](mega-menus/mega-menus.md) |
| [Menus](menus/menus.md) |
| [Modal bottom sheet](modal-bottom-sheet/modal-bottom-sheet.md) |
| [Modal bottom sheet menu](modal-bottom-sheet-menu/modal-bottom-sheet-menu.md) |
| [Navigation bar](navigation-bar/navigation-bar.md) |
| [Navigation bar (app)](navigation-bar-app/navigation-bar-app.md) |
| [Pagination](pagination/pagination.md) |
| [Phone number field](phone-number-field/phone-number-field.md) |
| [Progress bar](progress-bar/progress-bar.md) |
| [Progress circle](progress-circle/progress-circle.md) |
| [Radio button group](radio-button-group/radio-button-group.md) |
| [Rating](rating/rating.md) |
| [Segmented control](segmented-control/segmented-control.md) |
| [Select card group](select-card-group/select-card-group.md) |
| [Slider](slider/slider.md) |
| [Score tag](score-tag/score-tag.md) |
| [Snackbar](snackbar/snackbar.md) |
| [State message](state-message/state-message.md) |
| [Tables](tables/tables.md) |
| [Tabs](tabs/tabs.md) |
| [Tag](tag/tag.md) |
| [Text area](text-area/text-area.md) |
| [Text button](text-button/text-button.md) |
| [Text field](text-field/text-field.md) |
| [Toggle](toggle/toggle.md) |
| [Toggle group](toggle-group/toggle-group.md) |
| [Tooltip](tooltip/tooltip.md) |
| [Top bar](top-bar/top-bar.md) |
| [Wizard](wizard/wizard.md) |

Charts (Pattern) has its own sub-pages under [charts/](charts/).

The `component-web-ai-docs` skill also produces code-level, web-specific API
output. That is not duplicated here — this export is platform-neutral. The
**Decision Tree** it produces is different: it is platform-neutral by design,
and it lives in this repo, written into each component's own
`### Variant Selection Flow` section.

## Tool specifications

**A usage doc never names a tool.** What is true of a component *in Figma* and
nowhere else lives beside it, in `<name>-figma.md`. **Ten exist; the other 59
components have nothing tool-specific to say.**

| Tool specification |
| --- |
| [Action menu](action-menu/action-menu-figma.md) |
| [Alert](alert/alert-figma.md) |
| [Autocomplete](autocomplete/autocomplete-figma.md) |
| [Carousel](carousel/carousel-figma.md) |
| [Cell content](cell-content/cell-content-figma.md) |
| [Dropdown](dropdown/dropdown-figma.md) |
| [Estimation card](estimation-card/estimation-card-figma.md) |
| [Info state](info-state/info-state-figma.md) |
| [Map template](map-template/map-template-figma.md) |
| [Media upload](media-upload/media-upload-figma.md) |
| [Navigation bar](navigation-bar/navigation-bar-figma.md) |
| [Wizard](wizard/wizard-figma.md) |

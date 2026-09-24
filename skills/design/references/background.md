<!-- Generated from `tokens/color/background.md` on 2026-09-24 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

_Which token to use inside this colour family. The value tables are left out: a spec never holds a raw value._

Page-level backgrounds. *`Background` is the page/screen canvas — for component fills (cards, buttons, inputs, sheets) use `Surface` instead.*

## Semantic usage

| Token | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Background/Default` | The base page/screen canvas behind all content. Applied once by the theme provider, not per-component. ⚠️ `#FFFFFF` in light — the same as nine other tokens; pick it by role, never because you need white. | Component fills (→ `Surface/Default`) | direct: `GeminiProvider` |
| `Background/Light` | **Not used.** No production consumer — it appears only in a Storybook story. | Section separation (→ `Background/Subdued`, which is used) | **not used** |
| `Background/Subdued` | A more recessed page-level background — e.g. behind a scrollable region or muted section. Also the `skeleton` shimmer gradient. | Disabled component states (→ `Surface/Disabled`) | `skeleton` · direct: `ImageSlider` |
| `Background/Backdrop/Default` | The scrim behind modals, bottom sheets, popups | Any in-flow (non-overlay) UI | `backdrop` |
| `Background/Constant/Black` | **Not used.** For an immersive media backdrop, `Surface/Constant/Black` has consumers (`imageSlider`, `tag`). | Anything that should respond to theme | **not used** |
| `Background/Constant/White` | **Not used.** | Anything that should respond to theme | **not used** |

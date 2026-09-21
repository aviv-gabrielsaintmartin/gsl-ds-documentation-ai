Tooltips give a brief clarification of one element, on hover or tap.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

A tooltip is a small panel that appears beside the thing it explains, points at
it with an arrow, and goes away when the user moves on. It explains **one**
element, once.

**It is always attached to something.** A tooltip has no place of its own on the
page — it wraps a trigger, and that trigger is what the user hovers, focuses or
taps.

### When to use

* A brief clarification of one UI element, shown on hover or tap.
* A single explanation, where nothing needs to be stepped through.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The guidance is persistent and inline, not tied to a control | **Feedback message** |
| A guided, multi-step tour is needed | **Coach mark** |

### Variant Selection Flow

```
Placement — which side of the trigger it sits on
├─ Default → bottom
├─ Top
├─ Left
└─ Right
   └─ No rule for choosing a side is documented
   └─ The placement is a request, not a guarantee: the component reads back
      where the panel actually landed and points the arrow there

Alignment — where it sits along that side
├─ Default → middle
├─ Start
└─ End
   └─ No rule for choosing is documented

Offset — how far it sits from the trigger
└─ Adjustable, and may be negative to compensate for an enlarged touch zone.
   No rule for when to adjust it is documented
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Trigger a tooltip from a component — a button, a chip, a field's label icon, a component's own icon slot. | **DON'T:** Trigger one from a bare icon. A bare icon has no states, no hit area and no accessible name, so there is nothing for the user to reach. |

_From the component ruleset, which is the authority on what may carry an
interaction. Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Tooltip** | — | A brief panel clarifying one element, on hover or tap. | — |
| [**Feedback message**](../feedback-message/feedback-message.md) | High | Persistent inline guidance or status within a section. | The guidance must stay visible without being hovered |
| [**Coach mark**](../coach-mark/coach-mark.md) | High | A guided, multi-step onboarding tour over several elements. | Introducing three new features in sequence |

## Variants & Modifiers

### Placement

#### Bottom, top, left and right

Four sides, `bottom` by default. The arrow follows the side, sitting against the
edge nearest the trigger.

**The requested side is not always the side used.** The component asks for a
position, then reads back where the panel was actually placed, and points the
arrow at wherever that turned out to be.

### Alignment

#### Start, middle and end

Three positions along the chosen side, `middle` by default. On the left and
right sides, `start` and `end` mean top and bottom.

### Modifiers

#### Offset

The gap between trigger and panel can be adjusted, and **may be negative**,
which is how an enlarged touch zone around a trigger is compensated for. No rule
for when to adjust it is documented.

## Behavior & Responsiveness

### Interactive States & Loading

* **Hover and keyboard focus:** the tooltip opens after a short delay of 300ms, and closes with no delay at all.
* **Tap:** a press toggles the tooltip open or closed **immediately**, with no delay in either direction.
* **Entering:** it fades in while sliding 4px towards its placement, over 150ms.
* **Leaving:** the same animation, reversed.
* **Loading:** Not documented — a tooltip has no loading state.

### Touch Target & Layout

* **Touch Target:** carried by the trigger, not by the tooltip. The tooltip itself is not a target.
* **Width:** capped at 256px.
* **Overflow:** content taller than the space available scrolls vertically inside the panel.
* **Arrow:** a rotated square, roughly 18px across its diagonal, centred against the trigger on the placement side.
* The panel sits above the page content rather than displacing it, so nothing on the page moves when it opens.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. **The real adaptation is by input, not by
width:** a pointer opens the tooltip on hover after a delay, a touch opens it on
tap with no delay, and a keyboard opens it on focus. All three are present at
once._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** No count is stated. The panel is capped at 256px wide and scrolls vertically beyond the space it has, so long content is possible and nothing prevents it.

## Accessibility (a11y)

* **Keyboard Navigation:** the tooltip opens when its trigger takes keyboard focus, and closes when focus leaves. It is not itself focusable — focus stays on the trigger throughout.
* **Screen Readers:** the trigger and the panel are associated, so the tooltip's content is announced together with the trigger it explains.
* **The trigger must be a real control.** A tooltip may be triggered by any component and never by a bare icon, which has no accessible name to attach the panel to.

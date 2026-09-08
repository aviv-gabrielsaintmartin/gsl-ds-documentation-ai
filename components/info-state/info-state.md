<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831253628/Info+state | Last modified: Aug 21, 2026 -->

# Info state

Info states are placeholders used to inform users about success, error and empty states.

![](images/46b091654d0343e2f7a1a8.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Info state on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7261)
* [Info state on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-infostate--docs)

---

## Usage

Info states are used to communicate system status, errors, or other relevant information to users. They typically include:

* **Empty states:** Shown when there is no content to display or resources are missing
* **Error states:** Indicates problems such as network outages
* **Success states:** Acknowledge successful actions, such as submitting a form
* **Loading states:** Notifies users that data or content is being processed or loaded

### When to use

**Info state** — full-area states — empty, error, success, loading.

**Pattern**-tier component. **Highest tier first**: do not compose an empty/error/loading screen from Illustration + Text + Button — this component already is it.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Inline section-level messages | **Feedback message** |
| A blocking decision is required | **Alert** |

### Variant Selection Flow

```
Device
├─ Phone → Phone variant
├─ Tablet → Tablet variant
└─ Desktop → Desktop variant

Content and actions
├─ The state needs a way forward → Show buttons
├─ A secondary way forward as well → Add the tertiary button
└─ Purely informational → No buttons

State being communicated
├─ Nothing to show yet → Empty
├─ Something failed → Error
├─ Something completed → Success
└─ Content is still arriving → Loading
```

### Usage Guidance

| DO |
| --- |
| ![](images/5458ffe59f844fedd88bcd.png) **DO:** Use the info state component for empty states, when there is no data to display. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Info state** | — | Info states are placeholders used to inform users about success, error and empty states. | — |
| [**Feedback message**](../feedback-message/feedback-message.md) | High | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. | Inline section-level messages |
| [**Alert**](../alert/alert.md) | High | Alerts are modals that provide users with critical information they need immediately. | A blocking decision is required |

---

## Variants & Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

The width of the info state and its buttons depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

| Layout | Breakpoint behavior |
| --- | --- |
| ![](images/f3aef2585646e61490db09.png) **Width: 100%** | - Web: XXS - XS (0 - 599 px) - Android: Compact (0 - 599 dp) - iOS: device 0 - 523 px |
| ![](images/2cb3baa27b299ffc1188db.png) **Reduced width** | - Web: SM - XXXL (> 599 px) → width: 50%, max-width: 570px - Android: Medium - Expanded (> 599 dp) → max-width: 429 dp - iOS: device > 524 px → max-width 524 px |

---

## Content & UX Writing

* **Title:** The mandatory title should be short and concise. It should contain a brief and clear statement or question.
* **Description:** Descriptions are mandatory and are used to give additional context and details. Use clear and simple language and don't overwhelm the user with too much information. Tell the user what happened and what they need to do to proceed. Don't blame the user. Stay positive and empathetic but don't say please and sorry. Don't use "Oops". Keep the description to 1-2 sentences.
* **Buttons:** Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button. Buttons should always lead with an action verb in the infinitive tense, using the {verb} + {noun} formula, except for common actions like "Done," "Close," "Cancel," or "OK." Use sentence case without punctuation. Keep it under 4 words and/or 30 characters maximum in English.

For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro) and [Info state guidelines](https://zeroheight.com/626199550/v/latest/p/85a997-info-state).

---

## Accessibility (a11y)

Not documented

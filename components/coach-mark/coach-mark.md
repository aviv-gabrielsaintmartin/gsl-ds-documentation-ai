<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831515736/Coach+mark | Last modified: Aug 17, 2026 -->

# Coach mark

Coach marks are temporary overlay messages that provide contextual information about user interface elements. They can be used successively to create a guided interface tour.

![](images/GwOjYxT8sMvbAII7lkLgcw.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | WIP 🚧 | To Do 🚧 | WIP 🚧 |

* [Coach mark on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=13151-2940)

---

## Usage

Coach marks are temporary messages that provide contextual information to educate users about new or unfamiliar features. It appears as small overlay containers on top of the content, with an arrow indicator. Coach marks can be linked together in a sequence to create a tour.

| Single step | Multi step |
| --- | --- |
| ![Single step](images/25643d6a8aadbe6492f147.png) | ![Multi step](images/21a6bee93866def418f9a9.png) |

### When to use

**Coach mark** — contextual onboarding overlays pointing at specific UI elements.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Persistent inline guidance not tied to onboarding | **Feedback message** |
| A single brief clarification rather than a guided tour | **Tooltip** |

### Variant Selection Flow

```
Elements
├─ Always present → Title and close icon
└─ Everything else is optional — hide what this step does not need

Tag position
├─ Title fits on one line → Tag aligned with the title
└─ Title runs to two lines → Tag placed above the title
```

### Usage Guidance

| DON'T |
| --- |
| **DON'T:** Limit the display of coach marks to one at a time to prevent distraction and cognitive overload for users. |
| **DON'T:** Avoid navigating between pages; clicking the next button should not lead to a transition between different pages within a flow. |
| **DON'T:** Use a coach mark to emphasize a specific user interface element rather than the entire page. Prefer a Modal for whole-page emphasis. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Coach mark** | — | Coach marks are temporary overlay messages that provide contextual information about user interface elements. | — |
| **Tooltip** | High | Temporary short overlay messages that clarify the purpose of UI elements or provide additional context about their function. | A single, brief clarification rather than a guided, multi-step tour |
| [**Feedback message**](../feedback-message/feedback-message.md) | High | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. | Persistent inline guidance not tied to onboarding |

---

## Variants & Modifiers

### Boolean

Only the title and the close icon are mandatory. All other elements can be hidden, offering a variety of layout.

| Full | Simple |
| --- | --- |
| ![Full](images/61b400115880f9fdfd12c9.png) | ![Simple](images/63bca522fa2e1b59beec7b.png) |

### Tag position

To ensure a perfect readability, the tag can be aligned with the title or placed on top when the title is on two lines. It's up to the consumer.

| Horizontally aligned | On-top |
| --- | --- |
| ![Horizontally aligned](images/4cf5e93d03522cb47ed843.png) | ![On-top](images/eebab352701bc568a324bc.png) |

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

The coach mark appears automatically after the page loaded (decided by the consumer). A coach mark is an advisory overlay, not a modal dialog — it provides optional information, and its interaction model should reflect its subordinate nature. By allowing it to be dismissed easily, we reinforce that the coach mark is a temporary guide, not a mandatory step. This distinguishes it from critical alerts or dialogs that require an explicit user action before proceeding.

| Multi step | Single step |
| --- | --- |
| ![Multi step](images/032d715feb3142d59e8056.png) | ![Single step](images/dbdb1e8369109afe25461c.png) |

#### Dismissal on scroll

The coach mark should be dismissed on scroll. A user's scroll action is a clear signal that their focus is shifting — they are navigating to a different part of the page.

* **Respecting Focus:** Keeping the coach mark visible would actively work against the user's intent, pulling their attention back to a part of the UI they have chosen to move away from.
* **Reducing Intrusion:** The coach mark's job is to be a helpful, temporary guide. Once the user navigates away, its job is done. Dismissing it respects the "temporary" nature of the component.

#### Animation

An animation is used when the coach mark appears and disappears. During a tour, the first coach mark fades out before the second one becomes visible. The coach mark doesn't move on screen.

### Touch Target & Layout

* **Width Adaptability:** Size should be defined by the user, between 296 and 400px.

#### Position

The coach mark appears near the triggering object. The auto-placement feature identifies the best position from all available placement options, promoting effective use of space.

| Bottom Start | Bottom Middle | Bottom End | Left End |
| --- | --- | --- | --- |
| ![Bottom Start](images/dce13f233b27b73ce00060.png) | ![Bottom Middle](images/b925e8adbe96e67624e9d6.png) | ![Bottom End](images/020b07fda8fb89b326f6ab.png) | ![Left End](images/e7dc7f7120e809398f10b9.png) |

| Left Middle | Left End | Left Start | Left Middle |
| --- | --- | --- | --- |
| ![Left Middle](images/cd5bcc919b075677189fac.png) | ![Left End](images/17961c3052982b2bda102e.png) | ![Left Start](images/9a40d56553395d22e7361a.png) | ![Left Middle](images/1eee35fec76d61bd9e9043.png) |

| Right End | Right Middle | Left Start | Right Start |
| --- | --- | --- | --- |
| ![Right End](images/a9679a46e69010dff8053d.png) | ![Right Middle](images/a771c4e2fb18a82f4aa0fe.png) | ![Left Start](images/5c6a75d8103d2efd2e7fcc.png) | ![Right Start](images/579c05da1e552681559aba.png) |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Label Formula:** Not documented.
* **Length Limits:** Title: a few words, ideally on one line. Body: at least a few words, no more than a few sentences.

**Keep body text succinct and informative:** Coach marks are quick overviews of functionality.

**Communicate the main benefit to the user:** For example, "Manage your issues" instead of "Issue types".

**Don't repeat content from the title:** Concise information is more effective, and placing the most important keywords at the beginning of each sentence enhances clarity.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

* **Keyboard Navigation:** When opened, the first focusable element within the content is focused, and focus is trapped and wrapped within it (Source: [Progress Design system kit](https://www.telerik.com/design-system/docs/components/popover/accessibility/)). Upon closing through the keyboard or by interacting with an element within the content, focus is returned to the anchor element. Focus order: Tag → Title → Subtitle → Close (positioned early to allow a quick close) → Steps → Button 1 → Button 2.
* **Screen Readers:** The illustrative picture is decorative and therefore ignored by screen readers.

#### Focus order

* **Tag**

* **Title**

* **Subtitle**

* Close (positioned here to allow an quick close)

* **Steps**

* **Button 1**

* **Button 2**

The picture is decorative and therefore ignored by the screen readers.

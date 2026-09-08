<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831712357/Feedback+message | Last modified: Aug 21, 2026 -->

# Feedback message

Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages.

![](images/wPVVnxmPv1fRlrS4GTAAeg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Feedback message on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7299)
* [Feedback message on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-feedback-feedbackmessage--docs)

---

## Usage

Feedback messages are used to provide guidance to the user about their current task or to provide general information about things like system processes. They persist until they are dismissed or the issue that caused the notification is resolved.

### When to use

**Feedback message** — persistent inline contextual guidance or status within a section.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Transient, action-triggered feedback | **Snackbar** |
| Full-area or page-level states | **Info state** |

### Variant Selection Flow

```
Type
├─ Neutral context → Info
├─ An action succeeded → Success
├─ Needs attention but is not blocking → Warning
└─ Something failed → Error

Placement
├─ Inline with the content → Non-floating
└─ Above the content → Floating

Corner radius, by breakpoint
├─ Desktop → Floating, with rounded corners
└─ Tablet and phone → Without corners, as a full-width banner

Text
├─ Description → Mandatory
└─ Title → Optional, recommended for clarity

Buttons
└─ None, one, or two

Close button
├─ Non-critical information the user may dismiss → With close button
└─ Feedback that requires ongoing action → No close button, so it stays visible
```

### Usage Guidance

| DO |
| --- |
| ![](images/48e5dcda1e852d62b619e3.png) **DO:** Use feedback messages to provide guidance related to the user's current task. |
| ![](images/4db1df333aebe4562b91ef.png) **DO:** Use feedback messages for general information related to the system or website/app. |
| **DO:** Use feedback messages to confirm actions. |
| ![](images/6e76938bd38c570ebc5d0c.png) **DO:** Use feedback messages for warnings or non-critical errors. |

| DON'T |
| --- |
| ![](images/c42e4b769a6d5ed3f052f4.png) **DON'T:** Don't use feedback messages for critical information that interrupts the user flow. Use alerts instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Feedback message** | Medium | Feedback messages are non-disruptive, inline notifications that provide users with important information or contextual messages. They inform users of system processes or provide additional information about a task. They can be used for critical alerts or as passive feedback. | Seeker receives warning that he has reached the limit of saved searches |
| [**Snackbar**](../snackbar/snackbar.md) | High | Snackbars are used to provide brief, non-critical, and non-intrusive feedback on actions that don't require user confirmation. | Seeker saves listing to favorites |
| **Banner (not a gemini component)** | Medium | Banners are used for important, persistent information. They remain until the user closes them or the problem that caused the banner is solved. | Seeker is shown static information about search results on map |
| **State message** | Medium | State messages are used for inline feedback in forms to guide users, correct errors, or provide additional information. | User enters incorrect password |
| [**Alert**](../alert/alert.md) | High | Alerts are used for critical information that requires immediate attention or confirmation before proceeding. They block user flow until an action is taken. | Agent deletes listings |
| [**Info State**](../info-state/info-state.md) | High | Info states are used to communicate system status, errors, or other relevant information that prevent users from progressing and require their full attention. They include empty, error, success and loading states. | User is not connected to the Internet |
| [**Tag**](../tag/tag.md) | Medium | Tags are used to label, categorize and highlight items to help users quickly identify content. | Tag redirects here when: Status needs supporting text |
| [**Coach mark**](../coach-mark/coach-mark.md) | Medium | Coach marks are temporary overlay messages that provide contextual information about user interface elements. | Coach mark redirects here when: Persistent inline guidance not tied to onboarding |

---

## Variants & Modifiers

### Type

Feedback messages come in the following types: info, success, warning, and error.

### Floating and corner radius

Feedback messages can be floating and non-floating. The floating version floats above the content, the non-floating one is used inline with the content.

Feedback messages are available with and without corner radius. The version without corner radius is manly used to create floating banner at the top of the page.

#### Breakpoints

We recommend displaying the floating feedback message with rounded corners on desktop and without corners (as a banner) on tablet and phones.

### Modifiers

#### Title and description

Titles are optional, but recommended for clarity. Descriptions are mandatory.

#### Buttons

Feedback messages are available with 1 - 2 buttons or without buttons.

#### Close button

Dismissible messages have a close button (x-icon), non-dismissible messages don't. Whether a message should be dismissible or not depends on the information you want to communicate. For example, critical global messages should stay displayed permanently, and errors should stay displayed until the problem that caused the error is fixed. A simple success confirmation, on the other hand, can be dismissible.

| DO | DON'T |
| --- | --- |
| ![](images/6e76938bd38c570ebc5d0c.png) **DO:** Use close buttons when the feedback message provides non-critical information that users can dismiss after reading. This helps reduce visual clutter and allows users to focus on other important tasks without being repeatedly reminded of the same message. | ![](images/4db1df333aebe4562b91ef.png) **DON'T:** Don't use close buttons for feedback that requires ongoing action. Keeping it visible ensures that the reminder stays in place until addressed. |

---

## Behavior & Responsiveness

### Interactive States & Loading

Feedback messages either appear in response to user actions, or they appear automatically to notify users of system processes. Dismissible feedback messages can be closed by clicking the x-button. Non-dismissible messages are either persistent or disappear when the issue that caused the message gets solved.

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

| Platform / Breakpoint | Layout & Width Behavior |
| --- | --- |
| **Web and Android** | On web and Android the alignment of the buttons depends on the breakpoint. To learn more, see the [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints). |
| **iOS** | On iOS the alignment is done manually. |

---

## Content & UX Writing

#### Title

The title should be short and concise. Titles are optional, but recommended to improve clarity.

#### Description

Descriptions are mandatory. Use clear and simple language and don't overwhelm the user with too much information. Provide clear instructions or next steps, especially when users need to take action. Keep descriptions to 1-2 sentences.

#### Buttons

Buttons should be clear and inciting. Users should be able to anticipate what will happen when they click a button. Buttons should always lead with an action verb that encourages action, in the infinitive tense. To provide enough context to our users, use the {verb} + {noun} content formula on buttons except in the case of common actions like "Done," "Close," "Cancel," or "OK." Use sentence case without punctuation. Try to keep it under 4 words and/or 30 characters maximum in English.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/v/latest/p/324518-intro) and [Feedback message guidelines](https://gemini.zeroheight.com/styleguide/s/92948/p/348cca-feedback-messages).

---

## Accessibility (a11y)

Not documented

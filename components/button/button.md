Buttons are used to trigger an immediate action. Button labels express what action will occur when the user interacts with it.

![](images/9x_Scmr1cd8CdgMGR1pZWA.png)  <!-- order-inferred, please verify -->
| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Button on Figma](https://www.figma.com/file/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?type=design&node-id=11%3A27&mode=design&t=dkkP9LV7KntXJ8DP-1)
* [Button on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-action-button--docs)

---

## Usage

Buttons are clickable elements that are used to trigger actions. They communicate calls to action to the user and allow users to interact with pages in a variety of ways. Button labels express what action will occur when the user interacts with it.

However, buttons are not intended to be navigational elements and should not be used to navigate to different areas of a website or app. Using buttons for navigation can confuse users, as buttons are generally associated with actions like submitting forms, triggering events, or performing specific tasks. For navigation, links should be used instead, as they are specifically designed to guide users to different pages or sections, ensuring a clear and intuitive user experience.

**Navigation button:** To guide users back to the previous page, use a tertiary button featuring a left-facing arrow and the label "Back." The recommended spacing between header and button depends on the content underneath: if there is a headline, 24px is recommended, but the spacing can be larger if there is an empty state below, for example.

**Read more button:** Use a "Read more" button to display additional content only when users choose to see it. By expanding or collapsing text, users control what they want to read, which makes interfaces cleaner and easier to navigate. The overlapping gradient indicates that the text is expandable. The read more button uses a text button, which is a different component than the normal button.

### Platform

On iOS and Android, an animated floating button is available. When the user starts scrolling, the button smoothly transitions to a smaller, circular icon button. The animation uses a duration of `500ms` and an easing `ease`.

### When to use

**Button** — the user triggers an immediate action — save, submit, share, open a modal.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Navigation | **Link** |
| Full button weight is visually too heavy | **Text button** |
| Prominent navigational entry point with icon or illustration | **Button card** |
| Choosing from a set of related options | **Button group** |

### Variant Selection Flow

```
Emphasis
├─ The main call to action → Primary — once per section only
├─ A supporting action beside a primary → Secondary
├─ A less prominent, independent, or sub-task action → Tertiary
└─ Destructive and irreversible → Danger — consider a confirmation step after it

Size — always match the size of an adjacent button or field
├─ Default → 40px
├─ Generous whitespace around it → 48px
└─ Dense layout → 32px

Context
├─ Overlapping an image or a map → Floating
└─ On a normal page surface → Standard

Icon
├─ The icon reinforces the label → Icon with label, icon on the left by default
└─ The action is unmistakable from the icon alone → Icon-only
   └─ Never place a bare interactive icon outside a button

Badge
└─ Dynamic attention-grabbing information — notifications, counts, active filters → Add a badge
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![DO](images/6508fd4a5b873b8436fa64.png) **DO:** Use buttons to trigger actions, such as sharing, saving or opening a modal with a contact form. | ![DON'T](images/e296b4e7cef1d2c8257112.png) **DON'T:** Don't use buttons as navigational elements. Instead, use links when the desired action is to take the user to a new page. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Button** | — | Buttons trigger actions. | — |
| [**Link**](../link/link.md) | High | Links are navigational elements that take users to different pages or sections. | Navigation |
| **Text button** | High | A distinct component from Button, for when full button weight is too heavy. | Full button weight is visually too heavy |
| [**Button card**](../button-card/button-card.md) | High | Button cards are prominent calls to action that can be used alone or in a group, with icons or pictograms. | Prominent navigational entry point with icon or illustration |
| [**Button group**](../button-group/button-group.md) | High | Button groups display multiple related choices in a horizontal row, allowing users to select one or more options. | Choosing from a set of related options |

---

## Variants & Modifiers

### Emphasis

These different types of buttons are based on the level of emphasis we want to give to various actions. The most important aspect is to establish a visual hierarchy among the buttons in your UI. Keep these best practices in mind.

![](images/1mRHRXrsfZVQJZhaFkWWEg.svg)
Proportion of emphasis used across AVIV products

| Emphasis | Purpose |
| --- | --- |
| Primary | For the main call to action on the page. Primary buttons should only appear once per section. |
| Secondary | For secondary actions on each page. Secondary buttons can be used in conjunction with a primary button. |
| Tertiary | For less prominent, and sometimes independent, actions. Tertiary buttons can be used in isolation or paired with a primary button when there are multiple calls to action. Tertiary buttons can also be used for sub-tasks on a page where a primary button for the main and final action is present. |
| Danger | Reserved for destructive actions. These actions normally delete user's data and cannot be reverted. Depending on the severity of the action a confirmation modal can follow a Danger button action. |

| DO | DON'T |
| --- | --- |
| ![DO](images/DpJQ8zZ_6ifdgFzLni-MJA.svg) **DO:** Use only one primary button per section. | ![DON'T](images/K-EoyUnI9ephHevzuDS99Q.svg) **DON'T:** Don't use more than one primary button per section. |

| DO |
| --- |
| ![DO](images/ZAbKJNmcHdL8CUQtc5yBFw.svg) **DO:** You can use secondary and tertiary buttons without the need to include a primary one. |
| ![DO](images/2j_UrTRY7PxpmhsPOD9Xew.png) **DO:** You can group multiple secondary and tertiary buttons. |

| CAUTION |
| --- |
| ![CAUTION](images/KyugH9BhMGSskvqeoxQkjg.svg) **CAUTION:** Be cautious using a standalone tertiary button as without context these buttons could be overlooked as actions. |

Data tracking in the [CDP](https://avivgroup.atlassian.net/wiki/spaces/ADS/database/1123451029) showed that the button change from secondary to tertiary initially caused a short-term drop in engagement but led to a sustained long-term increase. It is now performing the same / slightly better.

| Primary | Secondary | Tertiary | Danger |
| --- | --- | --- | --- |
| ![Primary](images/57bd78cc0bdca3e70fe2ba.png) | ![Secondary](images/0d313c16cab499f1533f1d.png) | ![Tertiary](images/8d62da00ee72d348499fa6.png) | ![Danger](images/7b6f16828b7a3afede3fdc.png) |

### Size

At AVIV we use our 40px height button as the default but there's no strict rule that prevents designers from using the 48px or 32px height one, however when using the different sizes be mindful of the white space around them: the more white space around a button or a group of buttons you'll have, the more chances to use a bigger button.

| DO | DON'T |
| --- | --- |
| ![](images/FFF0nICzSsOqcFS8l7wlxQ.svg) **DO:** Use the same size of the button or field aside. | **DON'T:** Do not use a different size between two buttons aside or the field next to the button. |

### Context

Buttons change appearance depending on their context and background to better adapt to the environment, maintaining the same level of accessibility and usability.

| DO |
| --- |
| ![](images/EHJnjd0Z48pYBzpRrSaBcA.png)  <!-- order-inferred, please verify --> **DO:** Use the floating variant for buttons that overlap images. |
| ![](images/k_8wf7IfkE-K3iZOEs9sLA.png) **DO:** Use the floating variant for buttons that overlap images. |

### Modifiers

#### Icons

Icons are used to emphasize the action stated in the label of the button. By default we use the left aligned button. Icon-only buttons should contain icons that easily depict the action intended.

| DO | DON'T |
| --- | --- |
| ![DO](images/xsQee_t-zxzmQ_plzaaW9A.svg) **DO:** Icons that serve an interactive function must be placed within an icon-only button. This ensures accessibility, and clear affordance for user interactions. | ![DON'T](images/aHbzr5JTbkd18UPzRxmMFA.svg) **DON'T:** Icons should not be added to layouts with the intent of being interactive. Icons themselves do not support different states or interactions and must be placed within appropriate interactive components, such as buttons, to ensure usability and accessibility. |

| Icon only | Icon left | Icon right |
| --- | --- | --- |
| ![Icon only](images/f4835cb9018e791783240a.png) | ![Icon left](images/1d9a4a0abc87b0e9c2ec8d.png) | ![Icon right](images/a2fcf4c2fb0404c5a039d7.png) |

#### Badge

Badges in buttons are used to display dynamic information that grabs the user's attention. They can be used for things like notifications, alerts, or filtering.

---

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
| ![](images/fa207426a269b0b12ef2fd.png) | ![](images/2c295086af06b6e6c8f16c.png) | ![](images/a7562a7cc88c3b569e77b4.png) |

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** Buttons have the states default, hover, pressed and disabled.
* **Disabled State Guidance:** We don't recommend using disabled buttons in most cases. They can be frustrating because they provide no feedback or information about why the button is disabled or what the user needs to do to enable it. This can lead to confusion and a negative user experience. This lack of guidance adds to the cognitive load and can make them inaccessible to neurodivergent people. In addition the low-contrast text is difficult to read for people with visual impairments. [User feedback from a Hotjar survey in the estimation funnel](https://docs.google.com/spreadsheets/d/1JzOYL405ef3BOIfBJ2nZwaXvxdSdubZNS04VhMvOJdo/edit?pli=1&gid=0#gid=0) showed that users didn't understand why the continue button was disabled and what they needed to do to enable it.

| DO | DON'T |
| --- | --- |
| ![](images/7152697f875f7018a1b7ee.png) **DO:** Keep the button active and mark mandatory fields as required. Show error messages when the user clicks the button but hasn't filled all mandatory fields. | ![](images/388cf31d0d63f96d28148d.png) **DON'T:** Avoid using disabled buttons. |

**Loading:** This state is typically triggered when the action initiated upon click involves an API call or server query. This provides the user with a visual indication that their action is being processed. When a button is in a Loading state, the user can still navigate the page. However, if they initiate a new action before the previous one is completed, a message or alert may appear.

| Default | Hover | Pressed | Disabled |
| --- | --- | --- | --- |
| ![Default](images/57bd78cc0bdca3e70fe2ba.png) | ![Hover](images/ffa4d2cd52b924d17ae8a7.png) | ![Pressed](images/24484746e5b5f9bd338898.png) | ![Disabled](images/383f1ca04ed9babda52cc6.png) |

#### Disabled button

| DO | DON'T |
| --- | --- |
| ![DO](images/7152697f875f7018a1b7ee.png)<br>**DO:** Keep the button active and mark mandatory fields as required. Show error messages when the user clicks the button but hasn’t filled all mandatory fields. | ![DON'T](images/388cf31d0d63f96d28148d.png)<br>**DON'T:** Avoid using disabled buttons. |

| Loading (Web) | Loading (Android) | Loading (iOS) |
| --- | --- | --- |
| ![Loading (Web)](images/63339ca9cc69a4aae06a6c.png) | ![Loading (Android)](images/6669853a8d45087f3386de.png) | ![Loading (iOS)](images/8e21437423d0fe30692057.png) |

#### Touch target

| 32px button | 40px button | 48px button |
| --- | --- | --- |
| ![32px button](images/97d84f26c98ff45e2964e9.png) | ![40px button](images/ed18a5834db875f71734f3.png) | ![48px button](images/cfb7b1b54899a68ecf8876.png) |

### Touch Target & Layout

* **Touch Target:** To ensure accessibility, the touch target of the 32px button has a height of 40px. For all other sizes, the touch target is the same height as the button.
* **Width Adaptability:** The width of the button adapts to the width of its content unless intentionally we span the width to the full of its container, specially in Mobile devices.

| DO |
| --- |
| ![](images/6BgGGjSs4ALrawTBowP1ag.svg) **DO:** Use full width buttons on mobile devices. |
| ![](images/-Yo3dabzd0hSc_wRSn8TSw.png) **DO:** Use full width buttons on smaller containers on desktop devices. |

| 32px height | 40px height | 48px height |
| --- | --- | --- |
| ![32px height](images/1c58d5d66bbe5a594e114c.png) | ![40px height](images/57bd78cc0bdca3e70fe2ba.png) | ![48px height](images/ab953ed9cbd769acd72b3d.png) |

| DO | DON'T |
| --- | --- |
| ![DO](images/FFF0nICzSsOqcFS8l7wlxQ.svg)<br>**DO:** Use the same size of the button or field aside | ![DON'T](images/OQMhDcnepc_TEc9LCuaqXQ.svg)<br>**DON'T:** Do not use a different size between two buttons aside or the field next to the button |

#### Context

| Default button | Inverted color button | Over primary color surface button | Over secondary color surface button | Floating button |
| --- | --- | --- | --- | --- |
| ![Default button](images/57bd78cc0bdca3e70fe2ba.png) | ![Inverted color button](images/753b2d323667a75189305d.png) | ![Over primary color surface button](images/c33968be10cedd1665aefd.png) | ![Over secondary color surface button](images/e268e782d5cc5bf0a8e47b.png) | ![Floating button](images/55d25f9397a62d8f3fdbdc.png) |

| DO |
| --- |
| ![DO](images/EHJnjd0Z48pYBzpRrSaBcA.png)<br>**DO:** Use the floating variant for buttons that overlap images |
| ![DO](images/k_8wf7IfkE-K3iZOEs9sLA.png)<br>**DO:** Use the floating variant for buttons that overlap images |

| DO |
| --- |
| ![DO](images/6BgGGjSs4ALrawTBowP1ag.svg)<br>**DO:** Use full width buttons on mobile devices |
| ![DO](images/-Yo3dabzd0hSc_wRSn8TSw.png)<br>**DO:** Use full width buttons on smaller containers on desktop devices |

#### Use cases

#### Navigation button

To guide users back to the previous page, please use a tertiary button featuring a left-facing arrow and the label "Back."

We recommend the following spacing between header and button:

| Breakpoint: XXS - SM (0 - 767px) | Breakpoint: MD - XXXL (> 767px) |
| --- | --- |
| ![Breakpoint: XXS - SM (0 - 767px)](images/89ea6efbc361bd1c34ffd4.png) | ![Breakpoint: MD - XXXL (> 767px)](images/62d5f057060f832af357ba.png) |

The space below the button depends on the content underneath.

#### Read more button

This makes interfaces cleaner and easier to navigate.

| Expanding | Collapsing |
| --- | --- |
| ![Expanding](images/7608aaf655410e51033de5.png) | ![Collapsing](images/228d458bf11fbec828e523.png) |

This example will be moved to the text button documentation when it's finished.

#### Animated floating button

| Default | Minimized |
| --- | --- |
| ![Default](images/0c6056281d80001ed084b1.png) | ![Minimized](images/f0b0122f54d006c8013cb0.png) |

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Buttons solicit an action from the user and trigger that action. Buttons should be clear and inciting. Our users should be able to anticipate what will happen when they click a button. Buttons should always lead with an action verb that encourages action, in the infinitive tense. For more information on content guidelines, please refer to UX Writing principles.

* **Capitalization:** Sentence case without punctuation.
* **Label Formula:** {Action Verb} + {Noun}, except in the case of common actions like "Done," "Close," "Cancel," or "OK."
* **Length Limits:** Under 4 words and/or 30 characters maximum in English.

| DO | DON'T |
| --- | --- |
| ![DO](images/awuqKfbT4aKJsszm5uVlHQ.svg) **DO:** Give actions a clear naming. | ![DON'T](images/Rolnjm71sEPmKJJzNO_gAg.svg) **DON'T:** Don't give actions a vague naming. |

---

## Accessibility (a11y)

Not documented

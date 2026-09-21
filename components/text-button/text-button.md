Text buttons act on the page without a full button's visual weight.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

A text button is a label, optionally with an icon, that the user can press. It
carries a button's behaviour and none of its container — no fill, no border, no
horizontal padding — so it reads as text until it is pressed.

**It exists because of an alignment constraint.** `Button` carries horizontal
padding, so a tertiary button placed below a block of text and aligned left does
not line up with the text above it. A text button has no horizontal padding, so
it does. That constraint is the reason the component was built, and `Button`
itself should be reworked one day.

Revealing more content in place — "Read more" under truncated text, "Show all 12
photos" under a gallery — is one common use, not the whole of what it is for.

### When to use

* An action needs less visual weight than a full button.
* The control must align with a block of text it sits beneath.
* Revealing more content in place, on the same page.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The control leaves the page | **Link** |
| The control belongs inside a sentence or in body copy — a text button is never inline | **Link** |
| The content collapses back into a persistent expandable list | **Accordion** |
| The control submits or resets a form | **Button** — primary emphasis for the submit, the form's main action |

_**Leaving the page settles it first.** A standalone control going to another
address meets the test for a text button too — it is not inline, and it stands on
its own. It is still a link, because **a link is underlined**, and the underline
is what makes a user read it as something that takes them somewhere._

### Variant Selection Flow

```
Colour variant
├─ The action erases or deletes → Danger
├─ The surface is dark → Inverted, which is a visual choice only
└─ Anything else → Default

Size
├─ Default → 16
└─ 14
   └─ No rule for choosing between the two is documented
   └─ An icon-only text button is available at 16 only

Icon
├─ None → label only
├─ Before the label → icon at the start
├─ After the label → icon at the end, for a chevron for example
└─ Icon only, no visible label
    └─ The label is still written, and becomes the spoken name

Does it go to another page or an external address?
└─ Yes → that is `Link`'s job, not a text button's. A link is underlined, and
   the underline is what makes it read as a link
   └─ If a text button is used that way even so, the external-link icon is
      mandatory, exactly as it is on `Link`
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Keep the label short enough to fit the width it has. | **DON'T:** Rely on a long label wrapping to a second line. It never wraps — it truncates with an ellipsis instead, and the cut-off words are simply gone. |
| **DO:** Put the external-link icon on any text button leading to an external address. | **DON'T:** Leave it off. The rule is the same one `Link` follows, and the component does not add the icon for you. |
| **DO:** Use **Button** to submit a form, at primary emphasis — submitting is the form's main action. | **DON'T:** Make a text button the control that submits or resets a form, even though it can be set to do so. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Text button** | — | A pressable label, lighter than a button, never inline. | — |
| [**Link**](../link/link.md) | High | Navigation — anything leaving the page, and most things inside a sentence or body content. **Underlined**, which is what makes it read as a link. | "Read our privacy policy" within a paragraph, or a standalone link to an external site |
| [**Accordion**](../accordion/accordion.md) | Medium | A persistent expandable list the content collapses back into. | Several sections, each opening and closing |
| [**Button**](../button/button.md) | Medium | An action needing full visual weight. **Submits a form, at primary emphasis** — the form's main action. | "Save", "Submit" |

## Variants & Modifiers

### Colour variant

#### Default, danger and inverted

Three variants, `default` by default. Each sets four label colours — resting,
hover, pressed and disabled.

| Variant | When to use it |
| --- | --- |
| **Default** | Every case the other two do not cover |
| **Danger** | The action erases or deletes |
| **Inverted** | On a dark surface. **A visual choice only** — it carries no meaning about the action |

### Size

#### 14 and 16

Two sizes, `14` and `16`, being the label's type size in pixels. Default `16`.
**The overall height does not change with size** — it is fixed at 40px in both.
No rule for choosing is documented.

### Modifiers

#### Icon

An icon may sit before the label, after the label, or replace it entirely. The
icon is 24px in every case, with a gap between it and the label.

**Icon-only has two constraints the other placements do not have:** it is
available at size 16 only, and the label must still be written, because it
becomes the control's spoken name.

#### Going to an address

A text button can behave as a button, or as a link to an address that may open
in a new tab.

**The capability exists; the selection rule does not send you to it.** A control
that leaves the page is `Link`'s job, because a link is underlined and the
underline is what tells the user it takes them somewhere.

**Where a text button is used as an external link even so, the external-link
icon is mandatory** — the same rule `Link` follows. **The component does not
supply it**: setting the address as external adds a spoken "opens in a new tab"
and nothing visible, so the icon is placed through the icon slot at the end.

#### Acting on a form

A text button can be set to submit or reset a form it belongs to.

**It should not be the control that does either.** Submitting is the form's main
action, so it takes `Button` at **primary** emphasis. A reset or a cancel beside
it takes a lower emphasis — see `Button`'s own emphasis table, which holds
primary to one per section.

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** the label colour changes on hover and again on press. The change is animated rather than instant.
* **Disabled:** the label takes the variant's disabled colour, and the cursor shows the action is unavailable.
* **Focus:** an outline appears on **keyboard** focus only, never when the control is pressed with a pointer.
* **Loading:** Not documented — a text button has no loading state.

### Touch Target & Layout

* **Touch Target:** height is fixed at 40px and carries the touch target. The vertical padding sits inside that height, so the target does not change with the type size.
* **Horizontal padding:** none. **This is the point of the component** — the control is flush with its text on both sides, so it aligns with a block of text above or beside it.
* **Width Adaptability:** content-hug, capped at the width of its container.
* **Overflow:** the label is a single line. Anything too long truncates with an ellipsis; it never wraps.
* **Never inline.** A text button stands on its own. It is not set inside a sentence.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint behaviour is defined. The control renders identically at every
width, and adapts to its container rather than to the viewport._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** No count is stated. **The label never wraps** — anything wider than its container truncates with an ellipsis, so the container sets the limit, not a word count.

## Accessibility (a11y)

* **Keyboard Navigation:** focusable and activated from the keyboard. The focus outline shows on keyboard focus only. A text button can be taken out of the tab order.
* **Screen Readers:** **an icon-only text button takes its spoken name from the label it does not display**, so the label must still be written. A separate accessible label can override it.
* **Leaving the page:** a text button set as a link opening in a new tab adds a hidden "opens in a new tab", in English, French, German and Dutch. That is separate from the visible external-link icon, which is required as well.

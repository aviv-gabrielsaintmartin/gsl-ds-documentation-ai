<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831155311/Rating | Last modified: Aug 21, 2026 -->

# Rating

The rating is used to display the result of user ratings.

![](images/ZB3p1QzprQonyzpmBN2UZA.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

* [Rating on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7313)
* [Rating on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-rating--docs)

---

## Usage

The rating is a non-interactive component used to display the results of user ratings and provide a quick overview of user satisfaction.

### When to use

**Rating** — displaying user rating results — non-interactive, from Opinion System.

### When NOT to use

**No alternative.** Nothing else in the system covers this — see [components-rules-ai.md](../components-rules-ai.md).

### Variant Selection Flow

```
Size
├─ Prominent placement → L
└─ Secondary placement → S

Display
├─ Space is limited → Condensed, a single star
└─ Space allows → Full, all stars
   └─ Never hide the rating amount in the condensed variant

Optional elements — hide only while the context stays understandable
├─ Number of ratings
├─ User rating
└─ Maximum rating, such as "/5"
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/d1670b2dfe3591c7cafb63.png) **DO:** Use the rating component to display results of user ratings. | ![](images/bb1b6d2794d3ca4b771aae.png) **DON'T:** Since it is not clickable, this component cannot be used to collect new ratings or feedback from users. This is done in an external tool called Opinion System. |

### Related Components

**No overlapping component.** Nothing else in the system covers displaying user rating results from Opinion System. Rating is chosen directly — see [components-rules-ai.md](../components-rules-ai.md) **Which component**, *Identity and media*.

---

## Variants & Modifiers

### Size

The rating is available in two different sizes. The choice of size depends on the layout and the desired prominence of the rating.

| L | S |
| --- | --- |
| ![](images/f875b861a590ce79f0f02b.png) | ![](images/fbee382d998532c0159605.png) |

### Condensed display

The rating can be condensed to a single star or shown in full with all the stars. Which version you use depends on how much space is available in the layout.

| Full | Condensed |
| --- | --- |
| ![](images/f875b861a590ce79f0f02b.png) | ![](images/851dda20c8c0cf4a25867e.png) |

| DO |
| --- |
| ![](images/a4d2bb3f5e381cba3cb032.png) **DO:** Use the condensed variant when space is limited. |
| ![](images/3ae3dd775510d0ea6d7dc1.png) **DO:** Use the full version when enough space is available. |

| DON'T |
| --- |
| ![](images/e21b45e8cf7be3e3a5e765.png) **DON'T:** Don't hide the rating amount when using the condensed variant. |

### Modifiers

The following elements are optional and can be hidden: Number of ratings, user rating and maximum rating (e.g., "/5"). When hiding elements, make sure the context is still understandable.

| All elements | Hidden maximum amount of rating | Hidden rating | Hidden reviews | Hidden rating and reviews |
| --- | --- | --- | --- | --- |
| ![](images/2c2a4bab596adfc43afd9b.png) | ![](images/2220a020069ee11ef1a1fc.png) | ![](images/edb8ef510e7ec0728778ee.png) | ![](images/af80284c12846d2bb8ff2b.png) | ![](images/05ed6f85f009e131ab7395.png) |

---

## Behavior & Responsiveness

### Interactive States & Loading

This component has no interactive states. It is a static, display-only element with no hover, focus, pressed, loading, or disabled behavior.

### Touch Target & Layout

Not applicable. This component does not respond to touch or pointer interaction and has no minimum touch target requirement.

### Breakpoints & Platform Adaptations

Not applicable. This component does not adapt its layout or behavior across breakpoints or platforms.

---

## Content & UX Writing

### Scale

The stars are mathematically rounded.

![](images/1e52578b681f7324437aa5.png)

### Rating results

The notation of the rating result depends on the language. For French, German, Spanish, and Dutch content, we write ratings using commas. In English, we write ratings with decimal points.

![](images/c5902d7ebcbef8781f991c.png)

### Reviews

We use the following abbreviations for numbers.

**English:**
* **K** for thousands
* **M** for millions

**French:**
* **k** for "mille" (thousand)
* **M** for "million" (million)

**Dutch:**
* **K** for "duizend" (thousand)
* **M** for "miljoen" (million)

**German:**
* **Tsd.** for "Tausend" (thousand)
* **Mio.** for "Million" (million)

![](images/2c90683eddbb3a8ec518b1.png)

For more information on content guidelines, please refer to the [number guidelines](https://zeroheight.com/626199550/p/60fe5b-numbers).

---

## Accessibility (a11y)

Not documented

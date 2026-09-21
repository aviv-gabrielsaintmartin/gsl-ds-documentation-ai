Image sliders step the user through a sequence of images inside one frame.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Not established 🚧 | Not established 🚧 |

---

## Usage

An image slider shows one image at a time from an ordered set, and lets the user
move through them by swiping or by pressing an arrow. A counter in the corner
says where they are in the set.

**It carries images only.** The whole slider can also lead somewhere — a listing
card's photos opening the listing, for example — in which case the entire frame
becomes one target, not each image separately.

### When to use

* A sequence of images the user swipes or steps through — images only.
* The whole set of images leads to a single destination.
* Up to two icon markers are needed over the images, such as "map available" or "3D view available".

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The slides carry mixed content, not only images | **Carousel** |

### Variant Selection Flow

```
Aspect ratio — required, and there is no default
├─ 3/2
├─ 4/3
├─ 16/9
└─ 21/9
   └─ No rule for choosing a ratio is documented

Corners
├─ Default → square
└─ Rounded
   └─ No rule for choosing is documented

Does the whole slider lead somewhere?
├─ Yes → set a destination or a press action, and a label describing it
│   └─ A destination may open in a new tab
└─ No → set neither

Looping
├─ Default → the sequence loops, and the arrows never disable
└─ Off → the previous arrow disables on the first image, the next arrow on the last

Arrows
├─ Default → shown on hover or on keyboard focus
└─ Always shown
   └─ No rule for choosing is documented

Swiping
├─ On → the user can swipe between images
└─ Off → arrows only

Disabled
└─ Shows only the first image. Sliding, the destination and the press action are
   all switched off, and the arrows and the counter are hidden
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Keep icon markers to two at most, and describe each one in the slider's accessibility label — "Map available", "3D view available". | **DON'T:** Leave an icon marker undescribed. It is hidden from assistive technology, so a user who cannot see it is told nothing. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Image slider** | — | An ordered set of images in one frame, stepped through by swipe or arrow. | — |
| [**Carousel**](../carousel/carousel.md) | High | A sequence whose slides carry mixed content, not only images. | Slides hold a heading and a body alongside the picture |

## Variants & Modifiers

### Aspect ratio

#### 3/2, 4/3, 16/9, 21/9

Four ratios. **The ratio is required and has no default.** It fixes the frame's
height against its width, so every image in the set is shown in the same shape.
No rule for choosing one is documented.

### Corners

#### Square and rounded

Two corner treatments, square by default. No rule for choosing is documented.

### Modifiers

#### Image loading

Three behaviours, controlling when the browser fetches each image:

| Setting | Behaviour |
| --- | --- |
| **Unset** | The current image loads immediately, along with the one before and the one after |
| **First** | The first image loads, then the one before and after it. From then on it behaves as unset |
| **All** | Every image loads only when it becomes visible |

Once an image has been shown, it stays loaded.

#### Counter offset

The counter sits at the bottom right. Its distance from the bottom edge is 16px
or 32px, 16px by default. No rule for choosing is documented.

#### Icon markers

Up to two icons may be placed beside the counter, each rendered as a tag. They
are hidden from assistive technology, so each one must be described in the
slider's accessibility label.

#### Vertical scrolling

By default a vertical drag scrolls the page rather than swiping the slider, and
pinch-to-zoom is off. It can be set to allow the browser's full default
behaviour instead.

## Behavior & Responsiveness

### Interactive States & Loading

* **Arrows:** hidden by default, appearing on hover or on keyboard focus. They can be set to show at all times. The change is animated.
* **Arrows, disabled:** only when looping is off — previous on the first image, next on the last.
* **Arrows and counter, hidden:** whenever there is one image only, or the slider is disabled.
* **Swiping:** a drag that turns into a page scroll does not change image, and does not follow the slider's destination.
* **Loading:** per the image-loading setting above.
* **Failed:** an image that will not load is replaced in place by a subdued panel carrying a banner illustration, an image icon and the words "No images available". The other images in the set are unaffected.

### Touch Target & Layout

* **Touch Target:** each arrow is 40px, inside an enlarged invisible hit area extending 16px to either side and 40px above and below.
* **Width Adaptability:** the slider fills the width of its container. Its height follows from the ratio.
* **Counter:** bottom right, 16px or 32px above the bottom edge, with the icon markers to its left.

### Breakpoints & Platform Adaptations

Not documented

_No breakpoint rules are defined — the slider fills its container at every
width, and only the ratio decides its height. **The one real adaptation is by
input, not by width:** arrows answer a pointer, swiping answers touch, and both
are present at the same time._

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented
* **Length Limits:** Not documented

_The slider carries no copy of its own beyond the counter, which is generated
and reads "n / total". Each image's alternative text, the slider's accessibility
label and the destination's label are all content, and none has a stated rule._

## Accessibility (a11y)

* **Keyboard Navigation:** the slider is focusable. Each arrow is a button carrying its own label — "go to previous slide" and "go to next slide" — supplied in English, French, German and Dutch.
* **Screen Readers:** an accessibility label on the slider is **required**. With more than one image it is announced as a carousel, and a change of image is announced politely rather than interrupting. The counter and the icon markers are hidden from assistive technology.
* **Leaving the page:** a destination that opens in a new tab adds a hidden "opens in a new tab", in the same four languages.
* **A failed image:** an image that will not load is replaced in place by a subdued panel — a banner illustration, an image icon, and the words "No images available" — supplied in the same four languages. The failure is also reported, naming which image it was.

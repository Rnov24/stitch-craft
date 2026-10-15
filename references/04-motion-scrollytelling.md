# Reference 04: Scrollytelling Patterns & Motion Engineering

## Why Scrollytelling Works
Scrollytelling converts passive reading into active exploration. As the user controls the scroll wheel, the interface responds synchronously.

However, poorly implemented motion causes severe user frustration:
- **Scroll-jacking** (trapping the user or overriding native scroll velocity).
- **Laggy layout recalculations** (animating `top`, `left`, `width`, or `height`).
- **Mobile jank** (complex pinning on small touch screens with dynamic URL bars).

---

## 4 Core Scrollytelling Patterns

### 1. The Pinned Narrative Stage (Desktop Split)
- **Concept:** As user scrolls, a graphic or 3D canvas remains pinned on one side while narrative text cards scroll past on the opposite side.
- **Trigger:** When Step $N$ enters the center of the viewport, the pinned graphic morphs or transitions to match.
- **Mobile Fallback:** Never pin full-height stages on mobile. Stack graphic and text inline.

```tsx
// Example with GSAP ScrollTrigger & matchMedia
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const mm = gsap.matchMedia();

// Desktop: Pinned layout
mm.add("(min-width: 1024px)", () => {
  ScrollTrigger.create({
    trigger: ".narrative-container",
    start: "top top",
    end: "bottom bottom",
    pin: ".pinned-stage",
    scrub: 1,
  });

  gsap.utils.toArray(".narrative-step").forEach((step: any, index) => {
    ScrollTrigger.create({
      trigger: step,
      start: "top center",
      end: "bottom center",
      onEnter: () => setActiveStageIndex(index),
      onEnterBack: () => setActiveStageIndex(index),
    });
  });
});

// Mobile: Simple stacked fade-ins
mm.add("(max-width: 1023px)", () => {
  gsap.utils.toArray(".narrative-step").forEach((step: any) => {
    gsap.from(step, {
      opacity: 0,
      y: 30,
      duration: 0.6,
      scrollTrigger: {
        trigger: step,
        start: "top 80%",
      }
    });
  });
});
```

### 2. Scrubbed Text Reveal (Word-by-Word Opacity)
- **Concept:** Hero or key manifestos start dimmed at `opacity: 0.15` and illuminate to `opacity: 1.0` word-by-word as the user scrolls through the section.
- **Formula:** Break sentence into `<span>` words, scrub each word with a stagger over a $150\text{vh}$ scroll distance.

### 3. Dynamic Card Stacking
- **Concept:** High-impact cards slide up from the bottom and stack on top of earlier cards like a deck of playing cards.
- **CSS Tip:** Set `position: sticky; top: calc(10vh + index * 20px);` or drive with ScrollTrigger for scale-down effects on cards below.

### 4. Continuous Ambient Micro-Motion
- Ambient subtle radial drift or particle field tied to scroll velocity.
- Micro-counter numbers that count up cleanly when scrolling into view (`font-mono tabular-nums`).

---

## Performance Rules & Hardware Acceleration
1. **GPU-Only Properties:** Only animate `transform` (`translate3d`, `scale`, `rotate`) and `opacity`. Never animate `margin`, `padding`, `width`, `height`, or `top`.
2. **Reduced Motion Mandatory:**
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  .pinned-stage {
    position: static !important;
  }
}
```
In GSAP:
```ts
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  // Render static finished state immediately
}
```

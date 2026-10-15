# Reference 05: The "Story Review" Skill (Awwwards Jury & Pacing Audit)

## The Philosophy of the Story Review
AI coding models have a severe bias toward visual hyperactivity:
- They add too many particles and floating stars that look like cheap confetti.
- They cram animations together without enough scroll distance (`vh`), firing everything in one blinding spasm.
- They write meaningless corporate AI buzzwords (*"Unleash the future of next-gen workflows"*).
- They cause text illegibility by sliding text directly over busy moving elements.

In Phase 6, you adopt the strict, discerning persona of an **Awwwards Site of the Day Judge** to cut through the noise and enforce genuine craft.

---

## The 4 Evaluation Pillars

### 1. Narrative Pacing & Breathing Room
- **The Scroll Distance Rule:** Each narrative chapter must have enough scroll runway to be absorbed. A chapter should span between $100\text{vh}$ and $200\text{vh}$ of scroll distance.
- **Easing Curves:** Ban linear and overly bouncy cartoonish transitions. Use intentional, editorial easing curves:
  - Standard ease: `cubic-bezier(0.22, 1, 0.36, 1)`
  - Exit ease: `cubic-bezier(0.4, 0, 1, 1)`
- **No Instant Trigger Pileups:** If multiple elements enter together, stagger them with $0.08\text{s}$ delay rather than firing simultaneously.

### 2. Visual Noise & Particle Discipline
- **The 50% Particle Cut Rule:** If using particle fields, glowing star streaks, or background canvas meshes, **reduce total particle count by 40% to 60%** and set maximum opacity to `0.25`–`0.35`. Background effects must be felt, not stared at.
- **Micro-Shake Dampening:** If using camera shake or impact animations, damp duration to under $300\text{ms}$ with maximum displacement under $4\text{px}$. Avoid motion sickness.

### 3. Readability & Contrast Under Motion
- **Backdrop Scrims:** Any text scrolling over images, canvas particles, or video MUST have an underlying subtle backdrop blur (`backdrop-blur-md bg-zinc-950/60`) or high-contrast scrim.
- **Contrast Check:** Verify foreground text maintains WCAG AAA (7:1) contrast against its immediate background at all points during the animation scrub.

### 4. Ruthless AI Copywriting Purge
Scan all headings, subtext, and button labels against the **Banned Cliché List**:

| Banned AI Cliché | Editorial Replacement |
|:---|:---|
| *"Unleash the power of..."* | State the direct utility or action plainly. |
| *"Elevate your workflow..."* | Name the specific outcome or speed increase. |
| *"Seamless integration..."* | *"Zero-config setup"* or name the exact tools. |
| *"Next-generation AI platform..."* | Focus on what the user creates or experiences. |
| *"Unlock possibilities..."* | *"Deploy in 60 seconds."* |

---

## Final Quality Sign-Off
Before presenting the final experience:
1. Re-run multi-viewport capture (`./scripts/discover_and_verify.sh capture`).
2. Verify smooth $60\text{fps}$ rendering on mobile and desktop without jank.
3. Confirm that reduced-motion preference produces a clean, elegant static layout.

#!/usr/bin/env python3
"""
brief_scaffold.py - Generates a standardized brief.md scaffolding for Stitch & Scrollytelling projects.
"""

import sys
from pathlib import Path

BRIEF_TEMPLATE = """# Project Brief: {title}

## 1. Core Narrative & High-Concept Goal
- **Elevator Pitch:** {pitch}
- **Primary Objective:** Convert visitors through immersive, scroll-driven storytelling.
- **Narrative Arc:** Hook (Attention) -> Core Problem/Insight -> High-Craft Solution (Desire) -> Proof & Metrics -> Decisive Call to Action.

## 2. Visual Tone & Aesthetic References
- **Atmosphere Direction:** {atmosphere}
- **Aesthetic References:** Linear-style dark minimalism, Awwwards Site of the Day, Swiss editorial typography.
- **Visual Restraint:** High density without clutter, expansive negative space (`py-32 md:py-48`), no decorative junk or fake status pills.

## 3. Color & Typography Blueprint
- **Neutral Surface Base:** Zinc-950 / Slate-950 (Strict ban on pure #000000).
- **Accented Brand Color:** Exactly one high-contrast accent (e.g. Electric Emerald `#10B981`, Amber `#F59E0B`, or International Klein Blue `#002FA7`).
- **Strict Color Bans:** BANNED generic AI purple/blue neon glows, BANNED multi-color rainbow gradients.
- **Typography Stack:**
  - Display / Headings: Modern geometric/grotesque (Satoshi, Cabinet Grotesk, Outfit, or Geist). BANNED Inter.
  - Body: Geist Sans or Satoshi with relaxed leading (max 65ch per line).
  - Editorial Accents (optional): Instrument Serif or Fraunces for select micro-moments.
  - Metrics / Numbers: Monospace tabular numerals (`font-mono tabular-nums`).

## 4. Chapters / Scroll Architecture
- **Chapter 1: The Cinematic Hero (Attention)**
  - Wide container (`max-w-6xl`), 2-line max headline, inline visual punctuation, dual high-contrast CTAs.
- **Chapter 2: The Core Shift / Bento Grid (Interest)**
  - Gapless bento grid with `grid-flow-dense` and interlocking spans (3-5 cards max).
- **Chapter 3: The Deep Dive / Scrollytelling Narrative (Desire)**
  - Sticky pinned visual track on desktop with progressive reveals / horizontal scrub.
- **Chapter 4: Performance & Social Proof**
  - High-density telemetry / partner ticker / interactive metrics counter.
- **Chapter 5: Decisive Finale & Action**
  - High-impact terminal CTA with clear visual hierarchy and dark-mode polished footer.

## 5. Motion & Physics Spec
- **Scroll Engine:** GSAP ScrollTrigger / CSS Scroll-Driven / IntersectionObserver.
- **Motion Restraint:** Dampened easing curves (`cubic-bezier(0.22, 1, 0.36, 1)`), max 40% particle opacity, zero jitter.
- **Accessibility:** Instant static fallback under `prefers-reduced-motion: reduce`.
"""

def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "Interactive Web Experience"
    pitch = sys.argv[2] if len(sys.argv) > 2 else "An Awwwards-caliber narrative journey that communicates product value through motion."
    atmosphere = sys.argv[3] if len(sys.argv) > 3 else "Dark-mode technical luxury with razor-sharp typography."
    output_path = Path("brief.md")

    content = BRIEF_TEMPLATE.format(title=title, pitch=pitch, atmosphere=atmosphere)
    output_path.write_text(content, encoding="utf-8")
    print(f"✓ Created brief.md scaffold at {output_path.resolve()}")

if __name__ == "__main__":
    main()

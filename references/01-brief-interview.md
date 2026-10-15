# Reference 01: Interactive Brief Discovery & `brief.md` Generation

## Why an Interview Before Prompting Stitch?
Google Stitch generates screens based on natural language prompts. When handed a generic one-liner (e.g. *"Build an AI analytics landing page"*), Stitch defaults to generic templates: crowded cards, cliché purple-blue gradients, Inter font, and repetitive 3-column layouts.

To produce Awwwards-caliber work, the agent must anchor all visual decisions to a structured **Project Constitution (`brief.md`)**.

---

## The 5-Point Discovery Interview
When initiating Phase 1, present these targeted questions to the user:

### 1. Core Narrative & High-Concept Goal
- What is the story of this page as someone scrolls from top to bottom?
- What single emotional response should the visitor feel within the first 3 seconds?
- What is the primary conversion event (e.g., Request Beta Access, Book Demo, Star on GitHub)?

### 2. Aesthetic Universe & Visual Tone
- Which design aesthetic best fits the brand?
  - *Option A:* Dark Technical Luxury (Linear / Vercel style: Zinc-950 surfaces, razor-sharp borders, monochromatic elegance, single electric accent).
  - *Option B:* High-Craft Swiss Editorial (Warm monochrome paper tones, massive display serif headings, grid lines, asymmetric margins).
  - *Option C:* Industrial Brutalist / Terminal (Rigid utilitarian grids, monospace telemetry, blueprint borders, amber/cyan CRT accents).
  - *Option D:* Fluid Organic Minimalist (Soft pastels, generous breathing room, glassmorphism pills, micro-motion).

### 3. Color & Typography Strict Boundary
- **Neutrals:** Zinc, Slate, Charcoal, or Warm Stone? *(Note: Pure `#000000` is banned).*
- **Accent Color:** Pick exactly ONE accent color (e.g., Electric Lime `#84CC16`, Hyper Amber `#F59E0B`, International Klein Blue `#002FA7`, or Sunset Coral `#F43F5E`).
- **Typography Direction:**
  - Display: Satoshi, Cabinet Grotesk, Outfit, or Geist Sans *(Inter is banned for display)*.
  - Accent / Editorial: Instrument Serif or Fraunces *(if editorial)*.
  - Numbers / Data: Monospace tabular numerals (`tabular-nums font-mono`).

### 4. Chapter Architecture (4–6 Narrative Beats)
Break the single-page experience into distinct chapters:
1. **Chapter 1: The Hook (Hero)** — Massive 2-line title, inline image visual punctuation, dual CTAs.
2. **Chapter 2: The Core Problem / Shift (Bento Grid)** — Gapless interactive bento showcasing key capabilities.
3. **Chapter 3: The Deep Dive (Scrollytelling)** — Pinned visual graphic on desktop with narrative steps scrolling past.
4. **Chapter 4: Proof / Telemetry** — Interactive metrics counter, client marquee, or live simulation.
5. **Chapter 5: Decisive Finale (CTA)** — High-contrast closing chapter and clean footer.

### 5. Motion Appetite & Constraints
- What level of motion is desired?
  - *Subtle:* Scroll-triggered fades, subtle hover states, smooth counter ticks.
  - *Cinematic Choreography:* GSAP ScrollTrigger pinning, scrubbed text reveals, parallax layers, particle field.
- Accessibility reminder: Reduced-motion mode is always supported.

---

## Compiling `brief.md`
Once answers are confirmed, generate `brief.md` using the project scaffold script:
```bash
python3 .agent/skills/stitch-craft/scripts/brief_scaffold.py "<Project Name>" "<Pitch>" "<Atmosphere>"
```
Or write it directly. Every downstream prompt to Stitch and every line of frontend motion code must reference the approved `brief.md`.

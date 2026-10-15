---
name: stitch-craft
description: >-
  Lead orchestrator for high-craft AI web design, motion engineering, and scrollytelling.
  Combines the Google Stitch CLI (@google/stitch), local machine design and taste skills
  (gpt-taste, stitch-design-taste, design-taste-frontend, brandkit), multi-viewport Stitch
  Review (Desktop, Tablet, Mobile), and Awwwards-caliber Story Review. Activate this skill
  whenever the user asks to design a website, build an animated or scrollytelling landing
  page, run the Stitch design pipeline, create award-winning UI/UX with motion, or mentions
  stitch-craft.
---

# StitchCraft: Awwwards-Caliber Web & Motion Design Orchestrator

You are the **Lead Creative Director, Design Systems Architect, and Motion Engineer**. Your mission is to execute the end-to-end Google Stitch CLI + Motion Design pipeline, producing Awwwards-caliber web experiences while dynamically combining all UI/UX and motion skills installed on this machine.

---

## Architecture & Progressive Disclosure

This master skill orchestrates a disciplined 7-phase pipeline. For deep reference material, inspect the bundled resources:
- Interview & Brief Constitution: [references/01-brief-interview.md](references/01-brief-interview.md)
- Stitch 4-Beat Prompt Recipes & Variants: [references/02-stitch-prompt-recipes.md](references/02-stitch-prompt-recipes.md)
- Responsive Viewport Audit & Linting: [references/03-responsive-review.md](references/03-responsive-review.md)
- Scrollytelling Patterns & GSAP Physics: [references/04-motion-scrollytelling.md](references/04-motion-scrollytelling.md)
- Story & Awwwards Jury Pacing Audit: [references/05-story-awwwards-review.md](references/05-story-awwwards-review.md)
- Local Machine Skills Integration Matrix: [references/06-machine-skills-matrix.md](references/06-machine-skills-matrix.md)

Executable utilities are bundled in `scripts/`:
- `scripts/discover_and_verify.sh`: Discovers local machine skills (`discover`) and captures multi-viewport snapshots (`capture`).
- `scripts/verify_responsive.py`: Automated linter for viewport breakages, font issues, and AI clichés.
- `scripts/brief_scaffold.py`: Generates the standardized `brief.md` project constitution.

---

## Phase 0: Machine Skill Amalgamation (Run First)

Before prompting Stitch or writing code:
1. **Discover Installed Design Skills:**
   Execute the discovery script:
   ```bash
   ./scripts/discover_and_verify.sh discover
   ```
2. **Synthesize Capabilities:**
   Inspect detected skills (such as `stitch`, `scrollytelling`, `gpt-taste`, `stitch-design-taste`, `design-taste-frontend`, `brandkit`, `playwright-cli`). Merge their core directives into your active context:
   - From `gpt-taste`: Enforce ultra-wide H1 containers (max 2 lines), gapless bento grids (`grid-flow-dense`), and GSAP ScrollTrigger physics.
   - From `stitch-design-taste`: Enforce calibrated monochrome bases with a single accent color; ban neon purple/blue AI gradients.
   - From `scrollytelling`: Enforce story-driven scroll choreography with strict mobile fallbacks and reduced-motion support.
3. **Verify CLI Environment:**
   Confirm Stitch authentication with `stitch status`. If unauthenticated, prompt the user to run `stitch login` or export `STITCH_API_KEY`.

---

## Phase 1: Interactive Discovery & `brief.md` Generation

Never prompt Google Stitch from an unvetted one-liner. Every screen and animation decision must anchor back to a project constitution.

1. **Conduct the 5-Point Discovery Interview:**
   Ask the user targeted questions covering:
   - **Core Narrative:** What journey does the visitor experience from top to bottom?
   - **Aesthetic Tone:** Dark Technical Luxury, Swiss Editorial, Industrial Brutalist, or Fluid Minimalist?
   - **Color & Typography Strict Bounds:** Neutral base (Zinc/Slate), exactly ONE accent color, modern font pairings (e.g., Satoshi, Cabinet Grotesk, or Geist; Inter is banned for display).
   - **Chapter Progression:** 4 to 6 distinct narrative chapters (Hero -> Bento Feature Grid -> Sticky Scrollytelling Stage -> Telemetry/Proof -> Conversion Action).
   - **Motion Appetite:** Subtle vs. Cinematic GSAP Choreography.
2. **Freeze `brief.md`:**
   Generate and save `brief.md` in the project root:
   ```bash
   python3 ./scripts/brief_scaffold.py "<Project Name>" "<Pitch>" "<Atmosphere>"
   ```
   Confirm the finalized brief with the user before proceeding.

---

## Phase 2: Iterative Design in Google Stitch CLI (Up to 8 Passes)

Use the Stitch CLI to generate, critique, and refine screens against `brief.md`.

1. **Initialize Project:**
   ```bash
   stitch create project --title "<Project Name>"
   stitch config set project <project-id>
   ```
2. **Generate Screen Using the 4-Beat Recipe:**
   Structure the prompt using `[Canvas]`, `[Principles]`, `[Artwork & Assets]`, and `[Content & Chapters]` (see [references/02-stitch-prompt-recipes.md](references/02-stitch-prompt-recipes.md)):
   ```bash
   stitch generate screen --title "Main Experience" --device DESKTOP --prompt "<Detailed 4-Beat Prompt>"
   ```
3. **Inspect & Iterate:**
   Retrieve the generated HTML and preview:
   ```bash
   mkdir -p .stitch/review
   stitch get screen <screen-id> --code --output .stitch/review/draft.html
   ```
   If visual hierarchy or typography feels generic:
   - Explore variants: `stitch generate variants --screen <screen-id> --count 3 --creative-range EXPLORE --aspects LAYOUT,COLOR_SCHEME`
   - Apply surgical corrections: `stitch edit screen <screen-id> --prompt "<Specific fix>"`
4. **Extract & Freeze `DESIGN.md`:**
   Validate tokens using the official linter:
   ```bash
   design.md lint DESIGN.md
   design.md export css-tailwind DESIGN.md > src/styles/tokens.css
   ```

---

## Phase 3: Production Code Translation

1. Pull the approved Stitch screen code into `.stitch/reference/index.html`.
2. Translate static HTML into production framework components (React + Vite, Next.js, or Semantic HTML/Tailwind) while respecting `DESIGN.md` tokens.
3. Ensure semantic HTML structure (`<header>`, `<main>`, `<section data-chapter="...">`, `<footer>`) prepared for scroll triggers.

---

## Phase 4: The Stitch Responsive Review (Multi-Viewport Parity)

Because Stitch defaults to desktop screens ($1440\text{px}$), designs frequently break on mobile and tablet.

1. **Capture 3 Viewports:**
   Launch the dev server and run:
   ```bash
   ./scripts/discover_and_verify.sh capture http://localhost:3000 .stitch/review
   ```
   This generates `.stitch/review/desktop-1440.png`, `.stitch/review/tablet-768.png`, and `.stitch/review/mobile-375.png`.
2. **Desktop Parity Audit:**
   Verify fidelity against Stitch reference: exact typography line-heights, single accent color, and chapter vertical padding (`py-28 md:py-40`).
3. **Tablet ($768\text{px}$) & Mobile ($375\text{px}$) Remediation:**
   - Fix horizontal overflow: Apply `overflow-x-clip` on main containers.
   - Collapse grids: Bento grids must stack cleanly on mobile (`col-span-1`) with `grid-flow-dense` preventing gaps.
   - Fluid typography: Apply `clamp()` to headings so they never wrap past 3 lines on mobile.
   - Run automated linter:
     ```bash
     python3 ./scripts/verify_responsive.py src/
     ```

---

## Phase 5: Scrollytelling & Motion Engineering

Transform the responsive static page into a narrative journey (see [references/04-motion-scrollytelling.md](references/04-motion-scrollytelling.md)):

1. **Select Narrative Scroll Pattern:**
   - *Desktop:* Pinned graphic stage on one side with narrative steps scrolling past, or scrubbed text reveal.
   - *Mobile:* Graceful stacked view without scroll-jacking.
2. **Implementation Standards:**
   - Animate GPU-accelerated properties only (`transform: translate3d(...)`, `opacity`).
   - Use GSAP `matchMedia()` to disable pinning on viewports $< 1024\text{px}$.
   - Support `prefers-reduced-motion: reduce` with instant static fallbacks.

---

## Phase 6: The "Story Review" (Awwwards Jury & Pacing Audit)

Act as a strict **Awwwards Site of the Day Judge** to eliminate visual fatigue and AI clichés (see [references/05-story-awwwards-review.md](references/05-story-awwwards-review.md)):

1. **Narrative Pacing:**
   Ensure each chapter has adequate scroll runway ($100\text{vh}$ to $200\text{vh}$). Use intentional easing (`cubic-bezier(0.22, 1, 0.36, 1)`).
2. **Visual Noise Reduction:**
   Apply the **50% Particle Cut Rule**: reduce particle counts and glowing streaks by 40%–60%, lowering background opacity to $\le 0.30$.
3. **Contrast & Readability in Motion:**
   Add subtle backdrop blur scrims (`backdrop-blur-md bg-zinc-950/60`) under all text crossing moving backgrounds.
4. **Ruthless Copywriting Purge:**
   Replace robotic AI clichés ("Unleash the power", "Elevate your workflow") with concise, authentic product copy.
5. **Final Sign-Off:**
   Confirm stable $60\text{fps}$ performance across Desktop, Tablet, and Mobile.

# Reference 06: Local Machine Skills Integration Matrix

`stitch-craft` acts as the conductor for all existing design, UI, UX, and motion skills on your machine. When running Phase 0, the agent inspects discovered skills and blends their specialized capabilities into the pipeline.

---

## Skills Integration Map

| Installed Skill | Primary Role in the Master Pipeline | How to Combine |
|:---|:---|:---|
| **`stitch`** | Canvas generation, project state, DOM capture | Runs `stitch generate screen`, `stitch edit`, and `stitch capture`. |
| **`scrollytelling`** | Narrative scroll architecture & mobile fallbacks | Supplies Scrollama / IntersectionObserver patterns and reduced-motion logic. |
| **`gpt-taste`** | GSAP ScrollTrigger engineering & layout variance | Enforces the 2-line H1 limit, gapless bento grids (`grid-flow-dense`), and GSAP pinning. |
| **`stitch-design-taste`** | Semantic `DESIGN.md` token generation | Generates normative design tokens, bans purple neon clichés, establishes typographic scales. |
| **`design-taste-frontend`** | Anti-slop frontend engineering | Audits code structure, removes template boilerplate, refines micro-interactions. |
| **`brandkit`** | High-end visual identity & asset direction | Crafts logo systems, typography palettes, and mood boards for the brief. |
| **`high-end-visual-design`** | Agency-level craft & subtle surface depth | Guides border contrasts, multi-layered dark shadows, and typographic tracking. |
| **`industrial-brutalist-ui`** | Alternative aesthetic engine (Option C in Brief) | Used when user requests terminal, monospace, or military blueprint aesthetics. |
| **`minimalist-ui`** | Alternative aesthetic engine (Option B in Brief) | Used for warm monochrome, editorial paper textures, and airy layouts. |
| **`playwright-cli`** | Headless multi-viewport verification | Resizes browser to $1440\text{px}$, $768\text{px}$, and $375\text{px}$ to capture responsive review screenshots. |
| **`shadcn-ui`** | Accessible React component primitives | Supplies unstyled Radix-based accessible components (dialogs, tooltips, accordions). |
| **`react-vite-dashboard`** | Fast modern project scaffolding | Scaffolds Vite + React + Tailwind + TanStack Query if starting from a fresh workspace. |
| **`ponytail`** | Senior dev efficiency | Ensures the shortest working diff, deletes bloated abstractions, and verifies code with zero friction. |

---

## The Synthesis Workflow
During Phase 0, the agent executes `discover_and_verify.sh discover`. If any of the above skills are present in `.agents/skills/`, `~/.agents/skills/`, or plugins, the agent dynamically incorporates their specialized rules:
1. When generating `brief.md` and `DESIGN.md`, draw color, typography, and bento rules from `stitch-design-taste` and `gpt-taste`.
2. When coding motion, draw GSAP ScrollTrigger recipes from `scrollytelling` and `gpt-taste`.
3. When capturing viewports for review, leverage `playwright-cli` and `stitch capture`.
4. When auditing aesthetics, run the `Story Review` checks informed by `high-end-visual-design` and `design-taste-frontend`.

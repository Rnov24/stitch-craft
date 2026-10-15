# 🎨 StitchCraft

> **Awwwards-Caliber Web & Motion Design Pipeline for AI Coding Agents**  
> Clones and enhances the Google Stitch CLI (`@google/stitch`) + Motion Design pipeline for **Google Antigravity**, **Claude Code**, **Cursor**, and **Gemini CLI**.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Stitch CLI](https://img.shields.io/badge/Google%20Stitch%20CLI-%3E%3D0.11.0-4285F4)](https://www.npmjs.com/package/@google/stitch)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D20.0.0-green.svg)](https://nodejs.org/)

---

## 🌟 What is StitchCraft?

Google Stitch CLI is a breakthrough AI tool that generates full web screens. However, raw AI-generated designs often suffer from three major shortcomings:
1. **Desktop-Only Bias:** Designs break on mobile ($375\text{px}$) and tablet ($768\text{px}$) viewports.
2. **Visual Clichés:** Repetitive purple/blue neon gradients, cramped bento grids, and generic typography.
3. **Motion Fatigue:** Jittery animations, excessive particle density, and lack of narrative scroll pacing.

**StitchCraft** solves this by engineering a unified 7-phase design pipeline that:
- **Interviews you before prompting Stitch** to create an immutable `brief.md`.
- **Amalgamates existing machine design skills** (`gpt-taste`, `stitch-design-taste`, `scrollytelling`, `brandkit`).
- **Conducts a strict 3-Viewport Responsive Review** ($1440\text{px}$, $768\text{px}$, and $375\text{px}$) via Playwright & Stitch capture.
- **Engineers production GSAP Scrollytelling** with hardware-accelerated transforms and reduced-motion compliance.
- **Applies the Awwwards Jury Story Review** to damp visual noise and cut particle density by 50%.

---

## 🚀 Quick Install

### Option 1: Automatic 1-Line Installer (Recommended)

Run in your terminal (Linux, macOS, Termux, Git Bash):

```bash
curl -fsSL https://raw.githubusercontent.com/Rnov24/stitch-craft/main/install.sh | bash
```

### Option 2: Clone Directly into Your Agent Directory

#### For Google Antigravity & Global Agents:
```bash
git clone https://github.com/Rnov24/stitch-craft.git ~/.agents/skills/stitch-craft
```

#### For Claude Code:
```bash
git clone https://github.com/Rnov24/stitch-craft.git ~/.claude/skills/stitch-craft
```

#### For Cursor:
```bash
git clone https://github.com/Rnov24/stitch-craft.git ~/.cursor/skills/stitch-craft
```

#### For Project-Specific Workspaces:
```bash
mkdir -p .agent/skills
git clone https://github.com/Rnov24/stitch-craft.git .agent/skills/stitch-craft
```

---

## ⚙️ Prerequisites

StitchCraft requires **Node.js $\ge 20$** and the official Google Stitch CLI:

```bash
# 1. Install Google Stitch CLI & DESIGN.md linter globally
npm install -g @google/stitch @google/design.md

# 2. Authenticate with Google Stitch
stitch login

# Or set your API key globally:
stitch config set apiKey "YOUR_STITCH_API_KEY" --global

# 3. Verify status
stitch status
```

---

## 📐 The 7-Phase Master Workflow

```
[Phase 0: Skill Amalgamation] ──> Auto-scans machine for local UI/UX skills
              │
[Phase 1: Discovery & Brief] ───> 5-point interview -> Freezes brief.md
              │
[Phase 2: Stitch CLI Loop]  ────> 4-beat prompts -> Screen variant iteration -> DESIGN.md
              │
[Phase 3: Code Translation] ────> React / Vite / Tailwind semantic implementation
              │
[Phase 4: Responsive Review] ───> Multi-viewport audit (1440px / 768px / 375px)
              │
[Phase 5: Scrollytelling]   ────> GSAP ScrollTrigger pinning & scrubbed reveals
              │
[Phase 6: Awwwards Review]   ───> 50% particle cut rule & narrative pacing polish
```

| Phase | Action | Key Deliverable |
|:---|:---|:---|
| **Phase 0** | **Machine Skill Amalgamation** | Scans `~/.agents/skills/` and local plugins to synthesize all design skills. |
| **Phase 1** | **Interactive Brief Discovery** | 5-point interview establishing narrative, aesthetic universe, and strict constraints into `brief.md`. |
| **Phase 2** | **Stitch CLI Generative Iteration** | 4-Beat Prompting (`[Canvas]`, `[Principles]`, `[Artwork]`, `[Content]`) + Variant Loop + `DESIGN.md`. |
| **Phase 3** | **Production Code Translation** | Converts approved Stitch screen HTML into modular React/Vite/Tailwind components. |
| **Phase 4** | **Stitch Responsive Review** | Headless browser capture at $1440\text{px}$, $768\text{px}$, and $375\text{px}$ to fix overflow-x and broken grids. |
| **Phase 5** | **Scrollytelling & Motion** | Narrative pinned stages, scrubbed word reveals, and strict `prefers-reduced-motion` compliance. |
| **Phase 6** | **Awwwards Story Review** | Eliminates visual hyperactivity: cuts particle counts by 50%, adds backdrop scrims, and purges AI copywriting clichés. |

---

## 💬 How to Trigger in Your AI Agent

Once installed, simply prompt your AI assistant (Antigravity, Claude Code, Cursor):

> *"Use `stitch-craft` to build an interactive scrollytelling website for [your project idea]. First scan my machine for all available design skills, then interview me to create `brief.md`."*

### Example Invocations:
- *"Run the stitch-craft responsive review on http://localhost:3000 to catch mobile breakages."*
- *"Audit our scroll motion pacing using the stitch-craft Awwwards review pass."*
- *"Generate a 4-beat Stitch CLI prompt for an ultra-wide editorial hero section."*

---

## 🛠️ Bundled Helper Scripts

StitchCraft bundles deterministic CLI utilities in `scripts/`:

- **`scripts/discover_and_verify.sh discover`**: Scans the machine for all installed design, UI, and animation skills.
- **`scripts/discover_and_verify.sh capture <url>`**: Captures $1440\text{px}$, $768\text{px}$, and $375\text{px}$ full-page screenshots using Playwright.
- **`scripts/verify_responsive.py <path>`**: Automated linter detecting missing viewport tags, fixed-width overflow risks, unconstrained grids, and AI clichés.
- **`scripts/brief_scaffold.py <title> <pitch> <atmosphere>`**: Generates a standardized `brief.md` template.

---

## 📄 License

MIT © [Rnov24](https://github.com/Rnov24)

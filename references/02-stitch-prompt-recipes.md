# Reference 02: Stitch Prompt Recipes & Generation Iteration

## The 4-Beat Prompt Formula for Google Stitch CLI
Never send generic requests to Stitch. Always structure prompts using the **4-Beat Recipe**:

```markdown
[Canvas]
Target device: Desktop 1440x900 (designed for responsive scaling down to tablet 768px and mobile 375px).
Surface background: Zinc-950 (#09090b) with subtle top-radial luminance. High contrast text (#fafafa).

[Principles]
- Visual Hierarchy: Dramatic size contrast between ultra-wide 2-line H1 and relaxed body copy.
- Typography: Display in Satoshi or Cabinet Grotesk (track-tight, uppercase kicker). Numbers in monospace.
- Restraint: Zero decorative clutter, zero floating badges, zero multi-color purple-to-blue neon gradients.
- Grids: Mathematical gapless bento grid with dense interlocking cells.

[Artwork & Visual Assets]
- Hero: Cinematic center or asymmetric offset with an inline photographic pill embedded inside the heading.
- Media: High-craft product viewport mockups with subtle 1px zinc-800 borders and dark wash backdrops.

[Content & Chapters]
- Chapter 1 (Hero): "[Kicker] [Massive Headline with inline visual punctuation] [2 CTAs]".
- Chapter 2 (Bento): "3-4 dense feature cards showcasing core capabilities".
- Chapter 3 (Scrollytelling Anchor): "Sticky visual stage on left/right with narrative steps".
- Chapter 4 (Social Proof / Metrics): "High-density telemetry ticker with tabular numbers".
- Chapter 5 (Action): "High-contrast conversion finale".
```

---

## Stitch CLI Command Playbook

### 1. Initialize & Pin Project
```bash
# Create project
stitch create project --title "My Scrollytelling App"

# Pin as active project context
stitch config set project <project-id>
```

### 2. Generate Initial Screen
```bash
stitch generate screen \
  --title "Main Experience" \
  --device DESKTOP \
  --prompt "$(cat <<'EOF'
[Canvas]
Desktop 1440px wide landing experience on Zinc-950 background with single Emerald-500 (#10B981) accent.
[Principles]
Ultra-wide H1 (max 2 lines), Satoshi typography, gapless bento grid, linear dark aesthetic.
[Content]
Cinematic hero, 4-card bento grid, sticky narrative showcase, and conversion footer.
EOF
)"
```

### 3. Inspect Screen Code & Artifacts
```bash
# Retrieve code & draft HTML
mkdir -p .stitch/review
stitch get screen <screen-id> --code --output .stitch/review/draft.html

# Open canonical Stitch Canvas URL in browser
stitch url screen <screen-id>
```

### 4. The Variant Loop (Explore & Refine)
When a screen needs exploration across layouts or color schemes:
```bash
stitch generate variants \
  --screen <screen-id> \
  --count 3 \
  --creative-range EXPLORE \
  --aspects LAYOUT,COLOR_SCHEME \
  --prompt "Explore wider H1 containers, increase whitespace to py-36 between chapters, and tighten typography contrast."
```

For targeted surgical fixes:
```bash
stitch edit screen <screen-id> \
  --prompt "Remove floating badge pills from the hero and ensure bento grid has zero empty cells."
```

### 5. Extract & Validate `DESIGN.md`
Once a screen design is approved:
```bash
# Extract DESIGN.md tokens
stitch capture .stitch/review/draft.html -o .stitch/captured-dom.html

# Lint and validate DESIGN.md specification
design.md lint DESIGN.md

# Export CSS variables or Tailwind tokens
design.md export css-tailwind DESIGN.md > src/styles/tokens.css
```

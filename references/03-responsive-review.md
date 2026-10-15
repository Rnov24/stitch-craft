# Reference 03: The Stitch Responsive Review (Multi-Viewport Audit)

## Why the Responsive Review Is Mandatory
Google Stitch defaults to generating desktop screen layouts ($1440\text{px}$). When converted to real code without responsive discipline, Stitch designs frequently break on mobile and tablet devices:
1. Fixed-width containers force horizontal scrolling (`overflow-x` drift).
2. Desktop bento grids collapse into awkward, single-column towers or leave blank holes.
3. Giant desktop display titles wrap onto 6+ lines on small screens.
4. Absolute-positioned decorative elements collide with text.

The **Stitch Responsive Review** is a hard quality gate before any motion or animation is introduced.

---

## The 3-Viewport Capture Protocol
Run the helper script against your running local server (e.g. `http://localhost:3000` or `http://localhost:5173`):

```bash
./scripts/discover_and_verify.sh capture http://localhost:3000 .stitch/review
```

This captures:
- `.stitch/review/desktop-1440.png` ($1440 \times 900$ reference)
- `.stitch/review/tablet-768.png` ($768 \times 1024$ tablet portrait)
- `.stitch/review/mobile-375.png` ($375 \times 812$ iPhone standard)
- `.stitch/review/captured-dom.html` (self-contained DOM snapshot)

---

## The Two-Part Audit Checklist

### Part 1: Desktop Parity Audit against Stitch & `DESIGN.md`
Compare `.stitch/review/desktop-1440.png` side-by-side with Stitch reference:
1. **Surface & Neutral Calibration:** Are backgrounds using true `DESIGN.md` tokens (e.g., `zinc-950`) rather than arbitrary hex codes? Are borders `1px` subtle `zinc-800`?
2. **Singular Accent Restraint:** Is there only ONE accent color on the screen? Remove accidental secondary accent colors.
3. **Typography Scaling:** Does H1 span an ultra-wide container (`max-w-6xl`) and stay strictly at 2 (maximum 3) lines?
4. **Spacing Integrity:** Do section boundaries use massive spacing (`py-28 md:py-40`) to feel like cinematic chapters rather than crammed web forms?

### Part 2: Tablet ($768\text{px}$) & Mobile ($375\text{px}$) Verification
Inspect `.stitch/review/tablet-768.png` and `.stitch/review/mobile-375.png`:

| Viewport | Common Breakage | Fix Pattern |
|:---|:---|:---|
| **All** | Horizontal scroll drift (`overflow-x`) | Add `overflow-x-clip` or `overflow-x-hidden` on parent container. |
| **Mobile 375px** | H1 wrapping into 5-6 lines | Use fluid type: `font-size: clamp(2.25rem, 6vw, 4.5rem);` |
| **Mobile 375px** | Bento grid dead zones | Apply `grid-flow-dense` and reset `col-span` to full-width (`col-span-1`) on mobile. |
| **Mobile 375px** | Buttons cramped together | Stack CTAs vertically on mobile: `flex flex-col sm:flex-row gap-4`. |
| **Tablet 768px** | Side-by-side columns colliding | Switch to 2-column stacked grid at `md` breakpoint. |
| **Mobile 375px** | Touch targets too small | Ensure all links/buttons have at least $44 \times 44\text{px}$ hit area. |

---

## Automated Responsive Linting
Run the automated responsive checker:
```bash
python3 ./scripts/verify_responsive.py src/
```
Ensure all critical warnings are resolved before proceeding to Phase 5 (Motion Design).

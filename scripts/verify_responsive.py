#!/usr/bin/env python3
"""
verify_responsive.py - Automated responsive & anti-slop parity linter for Stitch-generated code.
Audits HTML/CSS/JSX files for common viewport breakages, font issues, and banned AI patterns.
"""

import sys
import re
import os
from pathlib import Path

def audit_file(filepath: Path) -> list:
    issues = []
    content = filepath.read_text(encoding="utf-8", errors="ignore")

    # 1. Viewport Meta Tag Check (for HTML files)
    if filepath.suffix in [".html", ".htm"]:
        if not re.search(r'<meta[^>]+name=["\']viewport["\'][^>]*>', content, re.I):
            issues.append(("CRITICAL", "Missing <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">. Mobile layout will scale incorrectly."))

    # 2. Fixed width breakages without responsive wrappers
    fixed_widths = re.findall(r'(?:width|w-):\s*([0-9]{3,4}px)|w-\[(\d{3,4})px\]', content)
    for match in fixed_widths:
        val = int(match[0] or match[1])
        if val > 500:
            issues.append(("WARNING", f"Fixed width constraint of {val}px found without responsive clamp or max-width. May cause horizontal scrolling on mobile (375px) / tablet (768px)."))

    # 3. Horizontal Overflow Guards
    if "overflow-x" not in content and "overflow-hidden" not in content:
        issues.append(("INFO", "No explicit overflow-x guard detected on body/main container. Add 'overflow-x: hidden' or 'overflow-x-clip' to prevent horizontal drift."))

    # 4. Banned Font Cliché: Unintentional Inter Default
    if re.search(r'font-sans|font-[\'"]?Inter[\'"]?', content) and "Geist" not in content and "Satoshi" not in content:
        issues.append(("DESIGN_TASTE", "Default generic sans or 'Inter' detected. For high-craft/Awwwards aesthetic, upgrade to Satoshi, Cabinet Grotesk, Outfit, or Geist."))

    # 5. Neon AI Gradients Check
    neon_patterns = [r'#8[Bb]5[Cc][Ff]6', r'#3[Bb]82[Ff]6', r'from-purple-500\s+to-blue-500', r'from-indigo-500\s+to-pink-500']
    for pat in neon_patterns:
        if re.search(pat, content):
            issues.append(("DESIGN_TASTE", "Generic AI purple/blue neon gradient detected. Prefer calibrated monochrome surfaces with a single controlled accent."))

    # 6. Bento Grid Missing Dense Flow
    if "grid-cols-" in content or re.search(r"display:\s*grid", content):
        if "grid-flow-dense" not in content and not re.search(r"grid-auto-flow:\s*dense", content):
            issues.append(("LAYOUT", "CSS grid detected without 'grid-flow-dense'. May leave empty gaps/voids across responsive breakpoints."))

    # 7. Reduced Motion Fallback
    if re.search(r'gsap|ScrollTrigger|motion\.|framer-motion', content, re.I):
        if "prefers-reduced-motion" not in content and "useReducedMotion" not in content:
            issues.append(("ACCESSIBILITY", "Scroll/motion engine detected without 'prefers-reduced-motion' query or reduced-motion fallback."))

    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify_responsive.py <file-or-dir>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    if not target_path.exists():
        print(f"Error: Target '{target_path}' does not exist.")
        sys.exit(1)

    files_to_check = []
    if target_path.is_file():
        files_to_check = [target_path]
    else:
        for ext in [".html", ".jsx", ".tsx", ".vue", ".css"]:
            files_to_check.extend(target_path.rglob(f"*{ext}"))

    total_issues = 0
    print(f"=== [RESPONSIVE & DESIGN TASTE AUDIT: {target_path}] ===")
    
    for f in files_to_check:
        # Ignore node_modules, .git, dist, build
        if any(part in f.parts for part in ["node_modules", ".git", "dist", "build"]):
            continue
        issues = audit_file(f)
        if issues:
            print(f"\nFile: {f}")
            for severity, msg in issues:
                total_issues += 1
                symbol = "🔴" if severity == "CRITICAL" else "🟡" if severity == "WARNING" else "🎨" if severity == "DESIGN_TASTE" else "♿"
                print(f"  {symbol} [{severity}] {msg}")

    print("\n" + "=" * 55)
    if total_issues == 0:
        print("✓ All responsive, accessibility, and anti-slop checks passed cleanly!")
    else:
        print(f"Found {total_issues} audit item(s) to inspect/address.")

if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# File: scripts/discover_and_verify.sh
# Purpose: Auto-discover machine design skills & capture multi-viewport snapshots for Stitch Review

set -euo pipefail

ACTION="${1:-discover}"
TARGET_URL="${2:-http://localhost:3000}"
OUTPUT_DIR="${3:-.stitch/review}"

case "$ACTION" in
  discover)
    echo "=== [ANTIGRAVITY DESIGN SKILL DISCOVERY] ==="
    echo "Scanning local workspace and global skill directories for design, UI, UX, and motion skills..."
    
    SEARCH_PATHS=(
      ".agents/skills"
      ".agent/skills"
      "$HOME/.agents/skills"
      "$HOME/.gemini/config/plugins"
      "$HOME/.gemini/antigravity/skills"
      "$HOME/.claude/skills"
      "$HOME/.cursor/skills"
    )

    FOUND_COUNT=0

    for base_dir in "${SEARCH_PATHS[@]}"; do
      if [ -d "$base_dir" ]; then
        while IFS= read -r skill_file; do
          if grep -qiE "design|ui|ux|css|tailwind|motion|scroll|animation|stitch|frontend|react|gsap|brutalist|brand" "$skill_file" 2>/dev/null; then
            echo ""
            echo "-> FOUND DESIGN SKILL: $skill_file"
            grep -E "^(name|description):" "$skill_file" | head -n 3 | sed 's/^/   /' || true
            FOUND_COUNT=$((FOUND_COUNT + 1))
          fi
        done < <(find "$base_dir" -maxdepth 4 -name "SKILL.md" 2>/dev/null || true)
      fi
    done

    echo ""
    echo "Total design skills discovered: $FOUND_COUNT"
    echo "=== [END DISCOVERY] ==="
    ;;

  capture)
    echo "=== [STITCH & MULTI-VIEWPORT CAPTURE] ==="
    echo "Target URL: $TARGET_URL"
    echo "Destination: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"

    # 1. Native Stitch DOM capture if stitch CLI is installed
    if command -v stitch &>/dev/null; then
      echo "[1/4] Capturing DOM with Stitch CLI..."
      if stitch capture "$TARGET_URL" -o "$OUTPUT_DIR/captured-dom.html" 2>/dev/null; then
        echo "  ✓ Saved DOM snapshot to $OUTPUT_DIR/captured-dom.html"
      else
        echo "  ! Note: stitch capture exited with code $?. Falling back to curl for DOM..."
        curl -sL "$TARGET_URL" -o "$OUTPUT_DIR/captured-dom.html" || true
      fi
    else
      echo "[1/4] stitch CLI not found in PATH. Saving raw HTML..."
      curl -sL "$TARGET_URL" -o "$OUTPUT_DIR/captured-dom.html" || true
    fi

    # 2. Multi-viewport Screenshots (Desktop 1440x900, Tablet 768x1024, Mobile 375x812)
    echo "[2/4] Capturing Desktop Viewport (1440x900)..."
    if command -v playwright-cli &>/dev/null; then
      playwright-cli open "$TARGET_URL" 2>/dev/null || true
      playwright-cli resize 1440 900 2>/dev/null || true
      playwright-cli screenshot "$OUTPUT_DIR/desktop-1440.png" 2>/dev/null || true
      
      echo "[3/4] Capturing Tablet Viewport (768x1024)..."
      playwright-cli resize 768 1024 2>/dev/null || true
      playwright-cli screenshot "$OUTPUT_DIR/tablet-768.png" 2>/dev/null || true

      echo "[4/4] Capturing Mobile Viewport (375x812)..."
      playwright-cli resize 375 812 2>/dev/null || true
      playwright-cli screenshot "$OUTPUT_DIR/mobile-375.png" 2>/dev/null || true
      playwright-cli close 2>/dev/null || true
    elif command -v npx &>/dev/null; then
      npx -y playwright screenshot --viewport-size="1440,900" --full-page "$TARGET_URL" "$OUTPUT_DIR/desktop-1440.png" 2>/dev/null || true
      echo "[3/4] Capturing Tablet Viewport (768x1024)..."
      npx -y playwright screenshot --viewport-size="768,1024" --full-page "$TARGET_URL" "$OUTPUT_DIR/tablet-768.png" 2>/dev/null || true
      echo "[4/4] Capturing Mobile Viewport (375x812)..."
      npx -y playwright screenshot --viewport-size="375,812" --full-page "$TARGET_URL" "$OUTPUT_DIR/mobile-375.png" 2>/dev/null || true
    else
      echo "Warning: Neither playwright-cli nor npx playwright found. Viewport screenshots skipped."
    fi

    echo "=== [CAPTURE COMPLETE] ==="
    echo "Screenshots and DOM stored in $OUTPUT_DIR:"
    ls -lh "$OUTPUT_DIR" || true
    ;;

  *)
    echo "Usage: $0 [discover|capture] [target_url] [output_dir]"
    exit 1
    ;;
esac

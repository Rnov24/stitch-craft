#!/usr/bin/env bash
# StitchCraft Automated Installer
# Installs StitchCraft skill into your active AI coding agent directory
# Usage: curl -fsSL https://raw.githubusercontent.com/Rnov24/stitch-craft/main/install.sh | bash

set -euo pipefail

REPO_URL="https://github.com/Rnov24/stitch-craft.git"
TARGET_DIR=""

echo "🎨 StitchCraft: Awwwards-Caliber Web & Motion Design Skill Installer"
echo "------------------------------------------------------------------"

# Determine target directory
if [ -d ".agent/skills" ]; then
  TARGET_DIR=".agent/skills/stitch-craft"
elif [ -d ".agents/skills" ]; then
  TARGET_DIR=".agents/skills/stitch-craft"
elif [ -d "$HOME/.agents/skills" ]; then
  TARGET_DIR="$HOME/.agents/skills/stitch-craft"
elif [ -d "$HOME/.claude/skills" ]; then
  TARGET_DIR="$HOME/.claude/skills/stitch-craft"
elif [ -d "$HOME/.cursor/skills" ]; then
  TARGET_DIR="$HOME/.cursor/skills/stitch-craft"
else
  # Default to global agents skills directory
  TARGET_DIR="$HOME/.agents/skills/stitch-craft"
  mkdir -p "$HOME/.agents/skills"
fi

echo "Installing StitchCraft into: $TARGET_DIR"

if [ -d "$TARGET_DIR" ]; then
  echo "Updating existing installation..."
  cd "$TARGET_DIR"
  if [ -d ".git" ]; then
    git pull --quiet
  else
    cd - >/dev/null
    rm -rf "$TARGET_DIR"
    git clone --depth 1 "$REPO_URL" "$TARGET_DIR"
  fi
else
  git clone --depth 1 "$REPO_URL" "$TARGET_DIR"
fi

# Ensure helper scripts are executable
chmod +x "$TARGET_DIR/scripts"/* 2>/dev/null || true

echo ""
echo "✓ StitchCraft successfully installed!"
echo ""
echo "Next Steps:"
echo "1. Ensure Google Stitch CLI is installed:"
echo "   npm install -g @google/stitch @google/design.md"
echo ""
echo "2. Authenticate Stitch:"
echo "   stitch login"
echo ""
echo "3. Trigger StitchCraft inside your AI assistant (Antigravity, Claude Code, Cursor):"
echo "   'Use stitch-craft to build an interactive scrollytelling website for [my project]'"

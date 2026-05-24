#!/usr/bin/env bash
# Git post-commit hook — mines each commit for project knowledge.
#
# INSTALL (Unix/macOS/Git Bash on Windows):
#   cp .claude/plugins/project-builder/scripts/post-commit.sh .git/hooks/post-commit
#   chmod +x .git/hooks/post-commit
#
# Windows (PowerShell, no Git Bash): use post-commit.bat instead.

set -euo pipefail

COMMIT_HASH=$(git rev-parse HEAD)
COMMIT_MSG=$(git log -1 --pretty=%B)
COMMIT_AUTHOR=$(git log -1 --pretty=%an)
COMMIT_DATE=$(date +%Y-%m-%d)
STAT=$(git diff HEAD~1 HEAD --stat 2>/dev/null || echo "")
DIFF=$(git diff HEAD~1 HEAD -- '*.ts' '*.js' '*.py' '*.go' '*.rs' 2>/dev/null | head -200 || echo "")

SCRIPT_DIR="$(git rev-parse --show-toplevel)/.claude/plugins/project-builder/scripts"

python "$SCRIPT_DIR/mine-commit.py" \
  --hash "$COMMIT_HASH" \
  --author "$COMMIT_AUTHOR" \
  --message "$COMMIT_MSG" \
  --stat "$STAT" \
  --diff "$DIFF" \
  --date "$COMMIT_DATE" &

# Run in background — don't slow down the commit

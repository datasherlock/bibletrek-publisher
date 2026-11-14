#!/usr/bin/env bash
# Commits and pushes any updates in the Bible Trek Publisher plugin/skill repo to GitHub.
# Usage: bash sync_to_github.sh "Commit message describing the skill update"
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
MSG="${1:-chore(skill): sync bibletrek-publisher updates}"

cd "${REPO_ROOT}"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "[bibletrek-sync] Working tree clean — pulling latest from origin/main..."
  git pull --ff-only origin main || true
  exit 0
fi

git add -A
git commit -m "${MSG}"
git pull --rebase origin main || true
git push -u origin main
echo "[bibletrek-sync] Synced cleanly to $(git remote get-url origin)"

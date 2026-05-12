#!/usr/bin/env bash
# serve.sh — Launch a local preview server for Dingrui Scholars study guides
# Usage: ./serve.sh [port]  (default: 8000)
#
# Walks the repo for <Subject>/{Study Guides,Practice Questions}/ directories
# and prints clickable URLs grouped by subject. Replaces the previous version
# which was hard-coded to AP Physics' Unit_*.html files.

set -euo pipefail

PORT="${1:-8000}"
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Pick a python interpreter — `python3` on Linux/Mac/Git-Bash, `python` on
# native Windows.
PY="python3"
command -v "$PY" >/dev/null 2>&1 || PY="python"

echo "Serving Dingrui Scholars products at:"
echo ""
echo "  http://localhost:$PORT/         (home / index.html)"

# Discover subjects (any top-level dir containing a Study Guides/ subfolder)
for d in */; do
  d="${d%/}"
  if [[ -d "$d/Study Guides" ]] || [[ -d "$d/Practice Questions" ]]; then
    enc="${d// /%20}"
    sg_count=$(ls -1 "$d/Study Guides"/*.html 2>/dev/null | wc -l | tr -d ' ')
    pq_count=$(ls -1 "$d/Practice Questions"/*.html 2>/dev/null | wc -l | tr -d ' ')
    echo ""
    echo "  $d ($sg_count study guide, $pq_count practice)"
    [[ "$sg_count" -gt 0 ]] && echo "    Study Guides:      http://localhost:$PORT/$enc/Study%20Guides/"
    [[ "$pq_count" -gt 0 ]] && echo "    Practice Questions: http://localhost:$PORT/$enc/Practice%20Questions/"
  fi
done

echo ""
echo "Press Ctrl+C to stop."
echo ""

exec "$PY" -m http.server "$PORT"

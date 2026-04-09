#!/usr/bin/env bash
# serve.sh — Launch a local preview server for Dingrui Scholars study guides
# Usage: ./serve.sh [port]  (default: 8000)

PORT="${1:-8000}"
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Serving Dingrui Scholars study guides at:"
echo ""
for f in "$DIR"/AP\ Physics/Unit_*.html; do
  name=$(basename "$f")
  echo "  http://localhost:$PORT/AP%20Physics/$name"
done
echo ""
echo "Press Ctrl+C to stop."
echo ""

cd "$DIR" && python3 -m http.server "$PORT"

#!/usr/bin/env bash
# Take a screenshot of an HTML product for visual comparison
# Usage: bash scripts/screenshot.sh <file.html> [output.png]
#
# Requires: either `puppeteer` (npx) or `wkhtmltoimage`
# TODO: Add actual screenshot implementation based on available tooling

set -euo pipefail

FILE="${1:?Usage: screenshot.sh <file.html> [output.png]}"
OUTPUT="${2:-/tmp/$(basename "$FILE" .html)_$(date +%s).png}"

if ! [[ -f "$FILE" ]]; then
  echo "Error: File not found: $FILE" >&2; exit 1
fi

# Placeholder: detect available screenshot tool and capture
# Option 1: npx puppeteer-based capture
# Option 2: wkhtmltoimage
# Option 3: playwright screenshot
echo "[screenshot] Tool not yet configured."
echo "[screenshot] Target: $FILE"
echo "[screenshot] Output would be: $OUTPUT"
echo ""
echo "To enable, install one of:"
echo "  npm i -g puppeteer   # then update this script"
echo "  apt install wkhtmltopdf"
echo "  npx playwright install chromium"
exit 0

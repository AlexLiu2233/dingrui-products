#!/usr/bin/env bash
# Take screenshot(s) of an HTML product for visual comparison.
# Uses Playwright (globally installed) with Chromium.
#
# Usage:
#   bash scripts/screenshot.sh <file.html> [output.png]
#   bash scripts/screenshot.sh <file.html> [output.png] --dark
#   bash scripts/screenshot.sh <file.html> [output.png] --full
#   bash scripts/screenshot.sh <file.html> [output.png] --both
#
# Flags:
#   --dark   Capture in dark mode only
#   --full   Full-page screenshot (default: viewport 1280x900)
#   --both   Capture light AND dark (appends _light / _dark to filename)
#   --mobile Capture at 375px mobile width

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

FILE="${1:?Usage: screenshot.sh <file.html> [output.png] [--dark|--full|--both|--mobile]}"
OUTPUT="${2:-/tmp/$(basename "$FILE" .html)_$(date +%s).png}"
shift 2 2>/dev/null || shift 1 2>/dev/null || true

DARK=false
FULL=false
BOTH=false
MOBILE=false
for arg in "$@"; do
  case "$arg" in
    --dark)   DARK=true ;;
    --full)   FULL=true ;;
    --both)   BOTH=true ;;
    --mobile) MOBILE=true ;;
  esac
done

if [[ ! -f "$FILE" ]]; then
  echo "Error: File not found: $FILE" >&2; exit 1
fi

ABS_FILE="$(cd "$(dirname "$FILE")" && pwd)/$(basename "$FILE")"

# Ensure globally-installed Node modules are discoverable
export NODE_PATH="${NODE_PATH:-$(npm root -g)}"

# Node script that does the actual capture
capture() {
  local OUT="$1"
  local SET_DARK="$2"
  local WIDTH="${3:-1280}"

  node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: ${WIDTH}, height: 900 } });
  await page.goto('file://${ABS_FILE}', { waitUntil: 'networkidle', timeout: 30000 }).catch(() =>
    page.goto('file://${ABS_FILE}', { waitUntil: 'load', timeout: 15000 })
  );
  // Let KaTeX + fonts render
  await page.waitForTimeout(2000);
  if (${SET_DARK}) {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(500);
  }
  await page.screenshot({ path: '${OUT}', fullPage: ${FULL}, type: 'png' });
  await browser.close();
  console.log('${OUT}');
})();
" 2>&1
}

WIDTH=1280
if $MOBILE; then WIDTH=375; fi

if $BOTH; then
  BASE="${OUTPUT%.png}"
  echo "[screenshot] Capturing light + dark..."
  LIGHT_OUT="${BASE}_light.png"
  DARK_OUT="${BASE}_dark.png"
  capture "$LIGHT_OUT" "false" "$WIDTH"
  capture "$DARK_OUT" "true" "$WIDTH"
  echo "[screenshot] Light: $LIGHT_OUT"
  echo "[screenshot] Dark:  $DARK_OUT"
else
  echo "[screenshot] Capturing $(if $DARK; then echo 'dark'; else echo 'light'; fi) mode..."
  capture "$OUTPUT" "$DARK" "$WIDTH"
  echo "[screenshot] Saved: $OUTPUT"
fi

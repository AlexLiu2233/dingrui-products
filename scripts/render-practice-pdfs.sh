#!/usr/bin/env bash
# Render distribution PDFs for a subject's Practice Questions HTML files.
# Output: dist/practice-pdfs/<slug>/<source>.pdf  (gitignored)
#
# Usage:
#   bash scripts/render-practice-pdfs.sh                  # defaults to "AP Physics"
#   bash scripts/render-practice-pdfs.sh "IB Math HL"
#
# Requires Chrome or Edge on PATH, or at a standard Windows install location.

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

SUBJECT="${1:-AP Physics}"
SRC_DIR="$SUBJECT/Practice Questions"
SLUG="${SUBJECT// /-}"
OUT_DIR="dist/practice-pdfs/$SLUG"

if [[ ! -d "$SRC_DIR" ]]; then
  echo "Error: $SRC_DIR not found." >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

# Resolve a Chrome-family binary
CHROME=""
for candidate in \
  google-chrome chromium chrome msedge \
  "/c/Program Files/Google/Chrome/Application/chrome.exe" \
  "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
  "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
  "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"; do
  if command -v "$candidate" >/dev/null 2>&1 || [[ -x "$candidate" ]]; then
    CHROME="$candidate"; break
  fi
done

if [[ -z "$CHROME" ]]; then
  echo "Error: Chrome/Edge not found. Install one or edit this script." >&2
  exit 1
fi

# Convert a repo-relative HTML path to a file:// URI (cross-platform via python)
to_file_uri() {
  python -c "import pathlib,urllib.parse,sys; print(pathlib.Path(sys.argv[1]).resolve().as_uri())" "$1"
}

shopt -s nullglob
files=("$SRC_DIR"/*.html)
shopt -u nullglob

if [[ ${#files[@]} -eq 0 ]]; then
  echo "No HTML files in $SRC_DIR" >&2; exit 1
fi

echo "Rendering ${#files[@]} file(s) from '$SUBJECT' using: $CHROME"
echo "Output: $OUT_DIR/"
echo ""

for html in "${files[@]}"; do
  base="$(basename "$html" .html)"
  out="$OUT_DIR/$base.pdf"
  uri="$(to_file_uri "$html")"
  echo "  -> $base.pdf"
  "$CHROME" \
    --headless=new \
    --disable-gpu \
    --no-pdf-header-footer \
    --print-to-pdf="$out" \
    "$uri" 2>/dev/null
done

echo ""
echo "Done. ${#files[@]} PDF(s) in $OUT_DIR/"

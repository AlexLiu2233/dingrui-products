#!/usr/bin/env bash
# Validate Dingrui Scholars HTML products
# Usage: bash scripts/validate.sh [file.html]  (omit file to validate all)

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
ERRORS=0

validate_file() {
  local f="$1"
  echo -e "\n${YELLOW}Validating:${NC} $f"

  # Check file exists and is non-empty
  if [[ ! -s "$f" ]]; then
    echo -e "  ${RED}FAIL${NC}: File is empty or missing"; ((ERRORS++)); return
  fi

  # Required structure checks
  for pattern in '<!DOCTYPE html>' '<meta charset' 'katex' 'data-theme' 'DM Serif Display'; do
    if ! grep -qi "$pattern" "$f"; then
      echo -e "  ${RED}FAIL${NC}: Missing '$pattern'"
      ((ERRORS++))
    fi
  done

  # Check for unclosed KaTeX delimiters (basic check)
  local single_dollars
  single_dollars=$(grep -o '\$' "$f" | wc -l)
  if (( single_dollars % 2 != 0 )); then
    echo -e "  ${YELLOW}WARN${NC}: Odd number of \$ delimiters ($single_dollars) — possible unclosed math"
  fi

  # Check dark mode CSS exists
  if ! grep -q '\[data-theme="dark"\]' "$f"; then
    echo -e "  ${RED}FAIL${NC}: Missing dark mode styles"
    ((ERRORS++))
  fi

  # File size sanity check
  local size
  size=$(wc -c < "$f")
  if (( size < 5000 )); then
    echo -e "  ${YELLOW}WARN${NC}: File seems small (${size} bytes)"
  fi

  echo -e "  ${GREEN}OK${NC}"
}

if [[ $# -gt 0 ]]; then
  for f in "$@"; do validate_file "$f"; done
else
  while IFS= read -r -d '' f; do
    validate_file "$f"
  done < <(find . -name '*.html' -print0)
fi

if (( ERRORS > 0 )); then
  echo -e "\n${RED}${ERRORS} error(s) found.${NC}"
  exit 1
else
  echo -e "\n${GREEN}All checks passed.${NC}"
fi

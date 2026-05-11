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

  # Universal structure checks (apply to every product)
  for pattern in '<!DOCTYPE html>' '<meta charset' 'DM Serif Display'; do
    if ! grep -qi "$pattern" "$f"; then
      echo -e "  ${RED}FAIL${NC}: Missing '$pattern'"
      ((ERRORS++))
    fi
  done

  # Theme support is required except for print-targeted Practice Questions
  if [[ "$f" != *"Practice Questions"* ]] && ! grep -qi 'data-theme' "$f"; then
    echo -e "  ${RED}FAIL${NC}: Missing 'data-theme'"
    ((ERRORS++))
  fi

  # KaTeX is conditional: required only when the file actually uses math syntax
  # (AP CSA, for example, is Java-only and has no math content).
  local needs_katex=false
  if grep -qE '\\\(|\\\[' "$f" \
     || grep -qE '\$[^$[:space:]][^$]{0,200}\$' "$f"; then
    needs_katex=true
  fi
  if $needs_katex && ! grep -qi 'katex' "$f"; then
    echo -e "  ${RED}FAIL${NC}: Uses math delimiters but missing KaTeX"
    ((ERRORS++))
  fi

  # Unclosed-math heuristic only meaningful when the file uses math
  if $needs_katex; then
    local single_dollars
    single_dollars=$(grep -o '\$' "$f" | wc -l)
    if (( single_dollars % 2 != 0 )); then
      echo -e "  ${YELLOW}WARN${NC}: Odd number of \$ delimiters ($single_dollars) — possible unclosed math"
    fi
  fi

  # Check dark mode CSS exists (skipped for print-targeted Practice Questions products)
  if [[ "$f" != *"Practice Questions"* ]] && ! grep -q '\[data-theme="dark"\]' "$f"; then
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

#!/usr/bin/env bash
# Scaffold a new unit HTML file from template.
#
# Usage:
#   bash scripts/new-unit.sh "<subject-dir>" "<Prefix: Topic>"
#
# Examples:
#   bash scripts/new-unit.sh "AP Physics" "Unit 8: Magnetic Fields"
#   bash scripts/new-unit.sh "IB Chemistry HL" "Structure 3: Classification of Matter"
#   bash scripts/new-unit.sh "IB Math HL" "Unit A2: Exponents and Logarithms"
#
# The TITLE argument MUST be in 'Prefix: Topic' form (colon between the
# prefix and the topic) so that build-index.py parses the resulting <title>
# tag correctly. Output goes to '<subject-dir>/Study Guides/'.

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

if [[ $# -lt 2 ]]; then
  cat <<USAGE >&2
Usage: bash scripts/new-unit.sh "<subject-dir>" "<Prefix: Topic>"

  subject-dir   one of: 'AP Calculus', 'AP Physics', 'AP CSA',
                'IB Chemistry HL', 'IB Math HL'
  Prefix: Topic e.g. 'Unit 8: Magnetic Fields'
                e.g. 'Structure 3: Classification of Matter'
                e.g. 'Unit A2: Exponents and Logarithms'
USAGE
  exit 2
fi

SUBJECT_DIR="$1"
TITLE="$2"

# Validate TITLE has 'Prefix: Topic' form
if [[ "$TITLE" != *": "* ]]; then
  echo "Error: TITLE must be 'Prefix: Topic' (got: '$TITLE')" >&2
  exit 2
fi

# Map directory -> long subject name used in the <title> tag.
# Keep this in sync with scripts/build-index.py SUBJECTS.
case "$SUBJECT_DIR" in
  "AP Calculus")     SUBJECT_LONG="AP Calculus AB/BC" ;;
  "AP Physics")      SUBJECT_LONG="AP Physics C: Mechanics" ;;
  "AP CSA")          SUBJECT_LONG="AP CSA" ;;
  "IB Chemistry HL") SUBJECT_LONG="IB Chemistry" ;;
  "IB Math HL")      SUBJECT_LONG="IB Math AA HL" ;;
  *)
    echo "Error: unknown subject '$SUBJECT_DIR'." >&2
    echo "Valid: AP Calculus | AP Physics | AP CSA | IB Chemistry HL | IB Math HL" >&2
    exit 2
    ;;
esac

# Build filename from TITLE: replace ': ' with '_', then spaces with '_'.
# 'Unit 8: Magnetic Fields' -> 'Unit_8_Magnetic_Fields'
FILENAME=$(echo "$TITLE" | sed 's/: /_/; s/ /_/g')
DEST_DIR="$SUBJECT_DIR/Study Guides"
DEST="$DEST_DIR/${FILENAME}.html"

mkdir -p "$DEST_DIR"

if [[ -f "$DEST" ]]; then
  echo "Error: $DEST already exists" >&2
  exit 1
fi

if [[ ! -f rag/template.html ]]; then
  echo "Error: rag/template.html not found." >&2
  exit 1
fi

# Substitute SUBJECT (long form) and UNIT_TITLE ('Prefix: Topic') in template.
# Use a sentinel character ('|') in sed to avoid clashes with '/' in titles.
sed "s|{{SUBJECT}}|$SUBJECT_LONG|g; s|{{UNIT_TITLE}}|$TITLE|g" rag/template.html > "$DEST"

echo "Created: $DEST"
echo ""
echo "Next steps:"
echo "  1. Fill in {{SUBJECT_SHORT}}, {{UNIT_DESCRIPTION}}, {{TOC_LINKS}}, {{CONTENT_SECTIONS}}"
echo "     and any remaining placeholders inside $DEST."
echo "  2. bash scripts/validate.sh \"$DEST\""
echo "  3. python scripts/build-index.py   # regenerates index.html cards"

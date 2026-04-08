#!/usr/bin/env bash
# Scaffold a new unit HTML file from template
# Usage: bash scripts/new-unit.sh "AP Subject" "Unit N Topic Name"

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

SUBJECT="${1:?Usage: new-unit.sh \"AP Subject\" \"Unit N Topic Name\"}"
TITLE="${2:?Usage: new-unit.sh \"AP Subject\" \"Unit N Topic Name\"}"

# Convert title to filename
FILENAME=$(echo "$TITLE" | sed 's/ /_/g')
DEST="$SUBJECT/${FILENAME}.html"

if [[ -f "$DEST" ]]; then
  echo "Error: $DEST already exists" >&2; exit 1
fi

mkdir -p "$SUBJECT"

if [[ -f rag/template.html ]]; then
  sed "s/{{TITLE}}/$TITLE/g; s/{{SUBJECT}}/$SUBJECT/g" rag/template.html > "$DEST"
  echo "Created: $DEST (from template)"
else
  echo "Warning: rag/template.html not found. Creating minimal placeholder."
  cat > "$DEST" <<TMPL
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>$SUBJECT — $TITLE | Dingrui Scholars</title>
<!-- TODO: Full implementation — use prompts/create-unit.md with Claude -->
</head>
<body>
<h1>$TITLE</h1>
<p>Placeholder — generate with Claude using prompts/create-unit.md</p>
</body>
</html>
TMPL
  echo "Created: $DEST (minimal placeholder)"
fi

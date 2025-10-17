#!/bin/bash
set -e

# Get the current UTC time
DEPLOY_TIME=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Find all HTML files and replace the placeholder
find . -name "*.html" -print0 | while IFS= read -r -d $'\0' file; do
    # Use a temporary file for sed to avoid issues with in-place editing
    tmp_file=$(mktemp)
    sed "s|__DEPLOY_TIME__|${DEPLOY_TIME}|g" "$file" > "$tmp_file"
    mv "$tmp_file" "$file"
done

echo "Successfully updated deployment time to ${DEPLOY_TIME}"

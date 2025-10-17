#!/bin/bash

# Script to fix the order of readingreference in all card files
CARD_DIR="/Users/rifaterdemsahin/projects/ai-security-course/3_UI/Cards"

# Process all .md files except template and readme
for file in "$CARD_DIR"/*.md; do
    filename=$(basename "$file")
    
    # Skip template and readme files
    if [[ "$filename" == "_"* ]]; then
        continue
    fi
    
    echo "Processing $filename..."
    
    # Create a temporary file
    temp_file="/tmp/temp_card.md"
    
    # Extract each line and reorder
    question_line=$(grep "^- question :" "$file")
    hint_line=$(grep "^- hint :" "$file")
    answer_line=$(grep "^- answer :" "$file")
    youtube_line=$(grep "^- youtubereference :" "$file")
    images_line=$(grep "^- googleimages :" "$file")
    reading_line=$(grep "^- readingreference :" "$file")
    
    # Write to temp file in correct order
    {
        echo "$question_line"
        echo "$hint_line"
        echo "$answer_line"
        echo "$youtube_line"
        echo "$images_line"
        echo "$reading_line"
    } > "$temp_file"
    
    # Replace original file
    cp "$temp_file" "$file"
    
    echo "Fixed order in $filename"
done

# Clean up
rm -f /tmp/temp_card.md

echo "All cards have been reordered!"
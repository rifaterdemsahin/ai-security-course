#!/bin/bash

# Script to add readingreference to all card files
CARD_DIR="/Users/rifaterdemsahin/projects/ai-security-course/3_UI/Cards"

# List of cards that need updating (excluding template, readme, and already updated ones)
cards=(
    "adversarial_patch.md"
    "adversarial_robustness.md"
    "adversarial_training.md"
    "ai_security_lifecycle.md"
    "art_toolbox.md"
    "backdoor_attack.md"
    "black_box_attack.md"
    "data_poisoning.md"
    "defense_in_depth.md"
    "differential_privacy.md"
    "evasion_attack.md"
    "input_sanitization.md"
    "llm.md"
    "model_extraction.md"
    "model_hardening.md"
    "model_stealing.md"
    "perturbation_budget.md"
    "pgd.md"
    "red_teaming.md"
)

for card in "${cards[@]}"; do
    file_path="$CARD_DIR/$card"
    if [ -f "$file_path" ]; then
        echo "Updating $card..."
        
        # Extract the card topic from filename for search query
        topic=$(echo "$card" | sed 's/.md$//' | sed 's/_/ /g')
        
        # Add readingreference line before the last line
        sed -i '' '$i\
- readingreference : <a href="https://www.google.com/search?q='"$topic"'+AI+security+research+papers" target="_blank">'"$(echo "$topic" | sed 's/\b\w/\U&/g')"' Research Papers and Articles</a>
' "$file_path"
        
        echo "Updated $card"
    else
        echo "File $card not found"
    fi
done

echo "All cards updated with readingreference!"
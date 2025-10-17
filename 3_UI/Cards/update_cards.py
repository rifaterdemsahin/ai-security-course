import os
import re

def update_card_file(filepath):
    """Update a single markdown card file to new template format"""
    if filepath.endswith(('_template.md', '_readme.md')):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already updated (has youtubereference)
        if 'youtubereference :' in content:
            return False
            
        # Replace "reference :" with "youtubereference :"
        updated_content = content.replace('- reference :', '- youtubereference :')
        
        # Extract question for Google Images search
        question_match = re.search(r'- question : ([🎯⚡🏋️🛡️🔒🎪🕳️📊🧠🔧🎨🔍💊🚫📝🤖🎭🔐🎲📈🔴⬛🔖🚪🧪🔄]*)\s*(.+)', updated_content)
        if question_match:
            question_text = question_match.group(2).strip()
            # Create search term for Google Images
            search_term = question_text.lower().replace(' ', '+').replace('-', '+')
            google_search = f'- googleimages : <a href="https://www.google.com/search?q={search_term}+AI+security+machine+learning&tbm=isch" target="_blank">{question_text.title()} Examples and Visualizations</a>'
            
            # Add googleimages line after youtubereference
            lines = updated_content.strip().split('\n')
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if line.startswith('- youtubereference :'):
                    new_lines.append(google_search)
            
            updated_content = '\n'.join(new_lines) + '\n'
        
        # Write updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

# Process all markdown files in current directory
updated_count = 0
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        if update_card_file(filename):
            print(f"✅ Updated: {filename}")
            updated_count += 1
        else:
            print(f"⏭️  Skipped: {filename}")

print(f"\n🎉 Total files updated: {updated_count}")

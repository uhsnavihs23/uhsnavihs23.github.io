import os
import re

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Structural border radius
    content = content.replace('rounded-xl', 'rounded-xl')
    content = content.replace('rounded-lg', 'rounded-lg')
    
    # Remove crazy background glows that ruin the Vercel aesthetic
    content = re.sub(r'<div class="absolute[^>]*blur-3xl[^>]*></div>', '', content)
    content = re.sub(r'<div class="absolute[^>]*blur-2xl[^>]*></div>', '', content)

    with open(filepath, 'w') as f:
        f.write(content)

print("Vercel structural borders applied!")

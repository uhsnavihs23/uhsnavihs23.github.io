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

    # Vercel Blue for light mode
    content = re.sub(r'--accent-color: #[0-9a-fA-F]+;', '--accent-color: #0070f3;', content, count=1)
    
    # Vercel Blue (lighter) for dark mode
    # Find the second occurrence (inside html.dark)
    parts = content.split('--accent-color:')
    if len(parts) >= 3:
        # parts[0] + '--accent-color:' + parts[1] is light mode
        # parts[2] starts with ' #...;'
        parts[2] = re.sub(r'^\s*#[0-9a-fA-F]+;', ' #3291ff;', parts[2])
        content = '--accent-color:'.join(parts)

    with open(filepath, 'w') as f:
        f.write(content)

print("Vercel Blue accent color applied!")

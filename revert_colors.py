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

original_light = """        :root {
            --bg-color: #f9fafb;
            --card-bg: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --border-color: #e5e7eb;
            --accent-color: #3b82f6;
            --nav-bg: rgba(255, 255, 255, 0.8);
        }"""

original_dark = """        html.dark {
            --bg-color: #18181b;
            --card-bg: #27272a;
            --text-primary: #f4f4f5;
            --text-secondary: #d4d4d8;
            --border-color: #3f3f46;
            --accent-color: #2dd4bf;
            --nav-bg: rgba(24, 24, 27, 0.8);
        }"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace Light Theme
    content = re.sub(r':root\s*\{[^}]+\}', original_light, content, count=1)
    
    # Replace Dark Theme
    content = re.sub(r'html\.dark\s*\{[^}]+\}', original_dark, content, count=1)
    
    # Revert Vercel blue if it exists
    # Vercel blue was #0070f3 and #3291ff, but since we just replaced the whole block, 
    # we don't need to do anything else because --accent-color is in the block!

    with open(filepath, 'w') as f:
        f.write(content)

print("Original color variables restored!")

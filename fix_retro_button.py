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

missing_count = 0
for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # If it has themeToggle but NO retroToggle
    if 'id="themeToggle"' in content and 'id="retroToggle"' not in content:
        # Find themeToggle and inject right before it
        retro_btn = '<button id="retroToggle" title="Go Retro" class="ml-2 p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-secondary" style="font-family: \'Segoe UI\', Tahoma, sans-serif; font-size: 0.75rem; font-weight: bold; border: 1px solid currentColor;">Retro</button>\n'
        content = re.sub(r'(<button[^>]*id="themeToggle")', retro_btn + r'\1', content)
        with open(filepath, 'w') as f:
            f.write(content)
        missing_count += 1
        print(f"Injected button into {filepath}")
        
print(f"Fixed {missing_count} files missing retro button.")

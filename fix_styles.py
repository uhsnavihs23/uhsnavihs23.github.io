import os
import re

css_vars = """
        :root {
            --bg-color: #f9fafb;
            --card-bg: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --border-color: #e5e7eb;
            --accent-color: #3b82f6;
            --nav-bg: rgba(255, 255, 255, 0.8);
        }
        html.dark {
            --bg-color: #18181b;
            --card-bg: #27272a;
            --text-primary: #f4f4f5;
            --text-secondary: #d4d4d8;
            --border-color: #3f3f46;
            --accent-color: #2dd4bf;
            --nav-bg: rgba(24, 24, 27, 0.8);
        }
"""

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if ':root {' not in content:
        content = content.replace('</style>', css_vars + '</style>')
    
    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_file(os.path.join(root, file))

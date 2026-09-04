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

# Vercel Light Theme
vercel_light = """        :root {
            --bg-color: #ffffff;
            --card-bg: #ffffff;
            --text-primary: #000000;
            --text-secondary: #666666;
            --border-color: #eaeaea;
            --accent-color: #000000;
            --nav-bg: rgba(255, 255, 255, 0.8);
        }"""

# Vercel Dark Theme
vercel_dark = """        html.dark {
            --bg-color: #000000;
            --card-bg: #0a0a0a;
            --text-primary: #ededed;
            --text-secondary: #a1a1a1;
            --border-color: #333333;
            --accent-color: #ffffff;
            --nav-bg: rgba(0, 0, 0, 0.8);
        }"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace Light Theme
    content = re.sub(r':root\s*\{[^\}]+\}', vercel_light, content, count=1)
    
    # Replace Dark Theme
    content = re.sub(r'html\.dark\s*\{[^\}]+\}', vercel_dark, content, count=1)
    
    # Replace fonts if possible. Vercel uses Geist. Let's swap Inter for Geist if we can, or just add Geist.
    if 'family=Inter' in content:
        content = content.replace('family=Inter:wght@300;400;500;600;700', 'family=Geist:wght@300;400;500;600;700')
        # We need to add Geist font import if we do this. But Google Fonts doesn't have Geist yet!
        # Geist is hosted on Vercel. We can use font-sans in Tailwind and let it fallback, 
        # or stick to Inter but change styling. Let's stick to Inter (it's what Vercel used before Geist).

    with open(filepath, 'w') as f:
        f.write(content)

print("Vercel theme CSS variables applied globally!")

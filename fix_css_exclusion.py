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

dark_css_replacement = """
    /* DARK THEME RETRO MODE CONSISTENCY (High Contrast Black style) */
    html.dark.retro body {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Apply black background to everything EXCEPT the fake IE chrome */
    html.dark.retro main, html.dark.retro footer, html.dark.retro section, 
    html.dark.retro main div, html.dark.retro footer div, html.dark.retro section div {
        background-color: #000000 !important;
        color: #ffffff !important;
        border-color: #ffffff !important;
    }
    
    html.dark.retro a { color: #ffff00 !important; }
    html.dark.retro a:hover { color: #ff0000 !important; }
    html.dark.retro h1, html.dark.retro h2, html.dark.retro h3, html.dark.retro h4 { color: #00ff00 !important; }
    
    html.dark.retro .bg-cardBg, html.dark.retro .bg-white, html.dark.retro [style*="background"] {
        background-color: #000000 !important;
    }
    
    /* We MUST protect the IE chrome from these dark mode overrides */
    html.dark.retro #ie-chrome-top [style*="background"], html.dark.retro #ie-chrome-bottom [style*="background"] {
        /* let inline styles win */
    }
"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace the old bad dark retro css block with the precise one
    content = re.sub(r'/\* DARK THEME RETRO MODE CONSISTENCY.*?html\.dark\.retro #ie-chrome-top input \{.*?\n\s*\}', dark_css_replacement, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

print("CSS exclusion fixed!")

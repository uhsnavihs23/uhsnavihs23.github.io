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

dark_aero_css = """
    /* DARK AERO (Zune Theme) FOR DARK MODE + RETRO */
    html.dark.retro body { background-color: #111111 !important; color: #e0e0e0 !important; }
    html.dark.retro header { background: linear-gradient(to bottom, #444444 0%, #222222 49%, #111111 50%, #1a1a1a 100%) !important; border-bottom: 1px solid #000000 !important; }
    html.dark.retro header a, html.dark.retro header span { color: #ffffff !important; text-shadow: 0 1px 2px rgba(0,0,0,0.8) !important; }
    html.dark.retro header nav a:hover { background: linear-gradient(to bottom, #555 0%, #333 100%) !important; border: 1px solid #777 !important; }
    html.dark.retro main { background-color: #1e1e1e !important; border: 1px solid #333333 !important; box-shadow: 0 0 8px rgba(0,0,0,0.5) !important; }
    html.dark.retro h1, html.dark.retro h2, html.dark.retro h3, html.dark.retro h4 { color: #6699ff !important; border-bottom: 1px solid #333333 !important; }
    html.dark.retro a { color: #6699ff !important; }
    html.dark.retro .bg-cardBg, html.dark.retro .bg-white, html.dark.retro [style*="background-color: var(--card-bg)"] { background: linear-gradient(to bottom, #2a2a2a 0%, #222222 100%) !important; border: 1px solid #111111 !important; }
    html.dark.retro button { background: linear-gradient(to bottom, #555555 0%, #333333 49%, #222222 50%, #333333 100%) !important; border: 1px solid #000 !important; color: #ffffff !important; box-shadow: inset 0 1px 0 rgba(255,255,255,0.2) !important; }
    html.dark.retro button:active { background: linear-gradient(to bottom, #222 0%, #111 100%) !important; box-shadow: inset 0 1px 3px rgba(0,0,0,0.5) !important; }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    if 'DARK AERO' not in content:
        content = content.replace('</style>', dark_aero_css + '\n</style>', 1)
        
        # Also let's fix the font on the retroToggle button to match the new aero aesthetic (remove comic sans)
        content = content.replace("font-family: 'Comic Sans MS', cursive;", "font-family: 'Segoe UI', Tahoma, sans-serif;")

        with open(filepath, 'w') as f:
            f.write(content)

print("Dark Aero injected!")

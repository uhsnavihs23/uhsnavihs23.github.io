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

dark_overrides = """
    /* FIX EXPLICIT WHITE/LIGHT BACKGROUNDS IN DARK MODE */
    html.dark .bg-white { background-color: var(--card-bg) !important; color: var(--text-primary) !important; border-color: var(--border-color) !important; }
    html.dark .bg-gray-50, html.dark .bg-slate-50 { background-color: var(--bg-color) !important; color: var(--text-primary) !important; }
    html.dark .text-gray-900, html.dark .text-gray-800, html.dark .text-slate-900, html.dark .text-slate-800, html.dark .text-black { color: var(--text-primary) !important; }
    html.dark .text-gray-700, html.dark .text-gray-600, html.dark .text-gray-500, html.dark .text-slate-700, html.dark .text-slate-600, html.dark .text-slate-500 { color: var(--text-secondary) !important; }
    html.dark .border-gray-200, html.dark .border-gray-300, html.dark .border-slate-200, html.dark .border-slate-300 { border-color: var(--border-color) !important; }
    html.dark table, html.dark th, html.dark td { border-color: var(--border-color) !important; }
    html.dark input, html.dark select, html.dark textarea { background-color: var(--card-bg) !important; color: var(--text-primary) !important; border-color: var(--border-color) !important; }
"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # If it's already there, don't add it again
    if "/* FIX EXPLICIT WHITE/LIGHT BACKGROUNDS IN DARK MODE */" not in content:
        # Inject right after /* DYNAMIC LIGHT-BOX COLOR OVERRIDES FOR DARK THEME */ or just after html.dark { ... }
        if "/* DYNAMIC LIGHT-BOX COLOR OVERRIDES FOR DARK THEME */" in content:
            content = content.replace("/* DYNAMIC LIGHT-BOX COLOR OVERRIDES FOR DARK THEME */", dark_overrides + "\n    /* DYNAMIC LIGHT-BOX COLOR OVERRIDES FOR DARK THEME */")
        else:
            # Fallback
            content = content.replace("</style>", dark_overrides + "\n</style>")

    with open(filepath, 'w') as f:
        f.write(content)

print("White backgrounds and text colors fixed in Dark Mode!")

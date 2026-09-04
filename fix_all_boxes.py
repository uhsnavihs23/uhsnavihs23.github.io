import os
import re

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"

# 1. FIX BUDGET VISUALIZER DEFAULTS
budget_file = os.path.join(base_path, 'projects', 'budget-visualizer', 'index.html')
with open(budget_file, 'r') as f:
    budget_content = f.read()

# Replace incomes and expenses arrays
budget_content = re.sub(r'let incomes\s*=\s*\[.*?\];', 'let incomes = [];', budget_content, flags=re.DOTALL)
budget_content = re.sub(r'let expenses\s*=\s*\[.*?\];', 'let expenses = [];', budget_content, flags=re.DOTALL)

with open(budget_file, 'w') as f:
    f.write(budget_content)


# 2. ADD COMPREHENSIVE TAILWIND COLOR BOX FIXES TO ALL HTML FILES
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

color_box_css = """
    /* DYNAMIC LIGHT-BOX COLOR OVERRIDES FOR DARK THEME */
    html.dark .bg-amber-100, html.dark .bg-amber-50 { background-color: rgba(245, 158, 11, 0.15) !important; color: #fcd34d !important; }
    html.dark .bg-blue-100, html.dark .bg-blue-50 { background-color: rgba(59, 130, 246, 0.15) !important; color: #93c5fd !important; border-color: rgba(59, 130, 246, 0.3) !important; }
    html.dark .bg-emerald-100, html.dark .bg-emerald-50 { background-color: rgba(16, 185, 129, 0.15) !important; color: #6ee7b7 !important; border-color: rgba(16, 185, 129, 0.3) !important; }
    html.dark .bg-gray-100, html.dark .bg-gray-50, html.dark .bg-slate-100, html.dark .bg-slate-50 { background-color: var(--card-bg) !important; color: var(--text-primary) !important; border: 1px solid var(--border-color) !important; }
    html.dark .bg-indigo-100, html.dark .bg-indigo-50 { background-color: rgba(99, 102, 241, 0.15) !important; color: #a5b4fc !important; border-color: rgba(99, 102, 241, 0.3) !important; }
    html.dark .bg-red-100, html.dark .bg-red-50 { background-color: rgba(239, 68, 68, 0.15) !important; color: #fca5a5 !important; border-color: rgba(239, 68, 68, 0.3) !important; }
    html.dark .bg-yellow-100, html.dark .bg-yellow-50 { background-color: rgba(234, 179, 8, 0.15) !important; color: #fde047 !important; border-color: rgba(234, 179, 8, 0.3) !important; }
    html.dark .bg-orange-100, html.dark .bg-orange-50 { background-color: rgba(249, 115, 22, 0.15) !important; color: #fdba74 !important; border-color: rgba(249, 115, 22, 0.3) !important; }
    html.dark .bg-purple-100, html.dark .bg-purple-50 { background-color: rgba(168, 85, 247, 0.15) !important; color: #d8b4fe !important; border-color: rgba(168, 85, 247, 0.3) !important; }
    html.dark .bg-teal-100, html.dark .bg-teal-50 { background-color: rgba(20, 184, 166, 0.15) !important; color: #5eead4 !important; border-color: rgba(20, 184, 166, 0.3) !important; }
    html.dark .bg-green-100, html.dark .bg-green-50 { background-color: rgba(34, 197, 94, 0.15) !important; color: #86efac !important; border-color: rgba(34, 197, 94, 0.3) !important; }
    
    /* OVERRIDE TEXT COLORS INSIDE DYNAMIC BOXES TO PREVENT CLASHING */
    html.dark .bg-amber-100 *, html.dark .bg-amber-50 * { color: inherit !important; }
    html.dark .bg-blue-100 *, html.dark .bg-blue-50 * { color: inherit !important; }
    html.dark .bg-emerald-100 *, html.dark .bg-emerald-50 * { color: inherit !important; }
    html.dark .bg-indigo-100 *, html.dark .bg-indigo-50 * { color: inherit !important; }
    html.dark .bg-red-100 *, html.dark .bg-red-50 * { color: inherit !important; }
    html.dark .bg-yellow-100 *, html.dark .bg-yellow-50 * { color: inherit !important; }
    html.dark .bg-orange-100 *, html.dark .bg-orange-50 * { color: inherit !important; }
    html.dark .bg-purple-100 *, html.dark .bg-purple-50 * { color: inherit !important; }
    html.dark .bg-teal-100 *, html.dark .bg-teal-50 * { color: inherit !important; }
    html.dark .bg-green-100 *, html.dark .bg-green-50 * { color: inherit !important; }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Append to existing universal css block if not already there
    if 'DYNAMIC LIGHT-BOX COLOR OVERRIDES FOR DARK THEME' not in content:
        content = content.replace('</style>', color_box_css + '\n</style>', 1)
        
        with open(filepath, 'w') as f:
            f.write(content)

print("Comprehensive box color fixes applied!")

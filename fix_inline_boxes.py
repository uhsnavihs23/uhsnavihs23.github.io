import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

inline_box_css = """
    /* DYNAMIC INLINE HEX-COLOR OVERRIDES FOR DARK THEME (e.g. Campus Electricity) */
    html.dark [style*="#dbeafe" i] { background-color: rgba(59, 130, 246, 0.15) !important; border-color: rgba(59, 130, 246, 0.3) !important; color: #93c5fd !important; }
    html.dark [style*="#f0fdf4" i] { background-color: rgba(16, 185, 129, 0.15) !important; border-color: rgba(16, 185, 129, 0.3) !important; color: #6ee7b7 !important; }
    html.dark [style*="#fefce8" i] { background-color: rgba(234, 179, 8, 0.15) !important; border-color: rgba(234, 179, 8, 0.3) !important; color: #fde047 !important; }
    html.dark [style*="#f3f4f6" i], html.dark [style*="#f9fafb" i] { background-color: var(--card-bg) !important; border-color: var(--border-color) !important; color: var(--text-primary) !important; }
    
    html.dark [style*="#dbeafe" i] *, html.dark [style*="#f0fdf4" i] *, html.dark [style*="#fefce8" i] *, html.dark [style*="#f3f4f6" i] *, html.dark [style*="#f9fafb" i] * { color: inherit !important; }
    
    /* FIX HOVER STATES FOR THE TABLE/ROWS IN DARK MODE */
    html.dark tr:hover { background-color: rgba(255,255,255,0.05) !important; }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    if 'DYNAMIC INLINE HEX-COLOR OVERRIDES' not in content:
        content = content.replace('</style>', inline_box_css + '\n</style>', 1)
        
        with open(filepath, 'w') as f:
            f.write(content)

print("Inline hex color fixes applied!")

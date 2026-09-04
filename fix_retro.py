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

retro_btn = """
<button id="retroToggle" title="Go Retro" class="ml-2 p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-secondary" style="font-family: 'Comic Sans MS', cursive; font-size: 0.75rem; font-weight: bold; border: 1px solid currentColor;">IE</button>
"""

retro_css = """
    /* GO RETRO BETA FEATURE */
    html.retro body {
        font-family: "Comic Sans MS", "Chalkboard SE", "Comic Neue", "Times New Roman", serif !important;
        background-color: #c0c0c0 !important;
        color: #000000 !important;
    }
    html.retro header {
        background-color: #000080 !important;
        border-bottom: 2px outset #ffffff !important;
    }
    html.retro header a, html.retro header span {
        color: #ffffff !important;
    }
    html.retro header nav a {
        background-color: #c0c0c0 !important;
        color: #000000 !important;
        border: 2px outset #ffffff !important;
        padding: 2px 8px !important;
        margin-right: 4px !important;
        text-decoration: none !important;
        font-family: "MS Sans Serif", "Tahoma", sans-serif !important;
        border-radius: 0 !important;
    }
    html.retro header nav a:active {
        border-style: inset !important;
    }
    html.retro main {
        border: 2px inset #ffffff !important;
        background-color: #ffffff !important;
        margin-top: 10px !important;
        padding: 15px !important;
    }
    html.retro h1, html.retro h2, html.retro h3, html.retro h4 {
        font-family: "Times New Roman", Times, serif !important;
        color: #000080 !important;
        border-bottom: 1px dashed #808080 !important;
        margin-bottom: 10px !important;
    }
    html.retro a {
        color: #0000EE !important;
        text-decoration: underline !important;
    }
    html.retro .bg-cardBg, html.retro .bg-white, html.retro [style*="background-color: var(--card-bg)"] {
        background-color: #ffffff !important;
        border: 2px inset #808080 !important;
        box-shadow: none !important;
        border-radius: 0 !important;
    }
    html.retro button {
        background-color: #c0c0c0 !important;
        border: 2px outset #ffffff !important;
        border-radius: 0 !important;
        color: #000000 !important;
        font-family: "MS Sans Serif", sans-serif !important;
    }
    html.retro button:active {
        border: 2px inset #ffffff !important;
    }
    html.retro img {
        border: 2px outset #c0c0c0 !important;
    }
    html.retro #retroToggle {
        border: 2px inset #ffffff !important;
        background-color: #808080 !important;
        color: #ffffff !important;
    }
"""

retro_js = """
        const retroToggle = document.getElementById('retroToggle');
        function setRetro(isRetro) {
            if (isRetro) {
                html.classList.add('retro');
                localStorage.setItem('retro', 'true');
            } else {
                html.classList.remove('retro');
                localStorage.setItem('retro', 'false');
            }
        }
        if (localStorage.getItem('retro') === 'true') { setRetro(true); } else { setRetro(false); }
        if (retroToggle) { retroToggle.addEventListener('click', () => { setRetro(!html.classList.contains('retro')); }); }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Inject button next to themeToggle
    if 'id="retroToggle"' not in content:
        # We find <button id="themeToggle" ...> ... </button>
        # Or just append after </button> if we capture the themeToggle block
        # Safest way: find id="themeToggle" and insert right before it
        content = re.sub(r'(<button\s+id="themeToggle")', retro_btn + r'\n\1', content)

    # 2. Inject CSS into <style> block
    if 'GO RETRO BETA FEATURE' not in content:
        content = content.replace('</style>', retro_css + '\n</style>', 1)

    # 3. Inject JS into theme script block
    if 'retroToggle' not in content and 'localStorage.getItem(\'retro\')' not in content:
        # Find where theme script ends, or just put it after themeToggle event listener
        content = re.sub(r"(if\s*\(themeToggle\)\s*\{\s*themeToggle\.addEventListener\('click',.*?\);\s*\})", r"\1\n" + retro_js, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

print("Go Retro feature injected!")

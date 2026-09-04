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

goatcounter_script = '<script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Inject GoatCounter if missing (into <head>)
    if "goatcounter.com/count" not in content:
        if '</head>' in content:
            content = content.replace('</head>', goatcounter_script + '\n</head>')

    with open(filepath, 'w') as f:
        f.write(content)

# 2. Fix urban-governance.html
urban_path = os.path.join(base_path, "projects/urban-governance.html")
if os.path.exists(urban_path):
    with open(urban_path, 'r') as f:
        content = f.read()
    
    # If it is missing themeToggle, let's inject a basic header right after <body>
    if 'id="themeToggle"' not in content:
        header_html = """
    <!-- Global Header -->
    <header class="bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-gray-200 dark:border-slate-800 sticky top-0 z-50 transition-colors duration-300">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="../index.html" class="text-xl font-bold text-gray-900 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Shivanshu Sharma</a>
            <nav class="flex items-center gap-6">
                <a href="../index.html" class="text-sm font-medium text-gray-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Home</a>
                <a href="index.html" class="text-sm font-medium text-gray-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Projects</a>
                <a href="../about.html" class="text-sm font-medium text-gray-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">About</a>
                <button id="themeToggle" aria-label="Toggle dark mode" class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-slate-800 transition-colors text-gray-600 dark:text-slate-300">
                    <svg id="themeIconDark" class="w-5 h-5 hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    <svg id="themeIconLight" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                </button>
                <button id="retroToggle" title="Go Retro" class="ml-2 p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-secondary" style="font-family: 'Segoe UI', Tahoma, sans-serif; font-size: 0.75rem; font-weight: bold; border: 1px solid currentColor;">Retro</button>
            </nav>
        </div>
    </header>
"""
        # Inject right after <body>
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + header_html, content)
        with open(urban_path, 'w') as f:
            f.write(content)

print("Final QA issues addressed!")

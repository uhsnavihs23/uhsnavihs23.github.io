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

universal_dark_mode_css = """
<style>
    /* UNIVERSAL THEME VARIABLES */
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
    
    /* GLOBAL OVERRIDES FOR TAILWIND HARDCODED CLASSES */
    html.dark body { background-color: var(--bg-color) !important; color: var(--text-primary) !important; }
    html.dark .bg-white { background-color: var(--card-bg) !important; }
    html.dark .bg-gray-50, html.dark .bg-slate-50 { background-color: var(--bg-color) !important; }
    html.dark .text-gray-900, html.dark .text-gray-800, html.dark .text-slate-900, html.dark .text-slate-800, html.dark .text-black { color: var(--text-primary) !important; }
    html.dark .text-gray-700, html.dark .text-gray-600, html.dark .text-gray-500, html.dark .text-slate-700, html.dark .text-slate-600, html.dark .text-slate-500 { color: var(--text-secondary) !important; }
    html.dark .border-gray-200, html.dark .border-gray-300, html.dark .border-slate-200, html.dark .border-slate-300 { border-color: var(--border-color) !important; }
    
    /* COMPATIBILITY OVERRIDES FOR INLINE STYLES AND CUSTOM CSS (Campus Electricity) */
    html.dark .header, html.dark .intro-card, html.dark .kpi-card, html.dark .chart-card, html.dark .impact-card, html.dark .recommendation-card, html.dark .warning-card { 
        background-color: var(--card-bg) !important; 
        border-color: var(--border-color) !important;
    }
    html.dark .header { background: var(--card-bg) !important; }
    html.dark .header h1, html.dark .header-badge, html.dark h2, html.dark h3, html.dark h4, html.dark .kpi-value, html.dark .rec-title { color: var(--text-primary) !important; }
    html.dark .header p, html.dark p, html.dark .kpi-label, html.dark .rec-description, html.dark .rec-detail-label { color: var(--text-secondary) !important; }
    
    /* OVERRIDES FOR TAILWIND PROSE */
    html.dark .prose h1, html.dark .prose h2, html.dark .prose h3, html.dark .prose h4 { color: var(--text-primary) !important; }
    html.dark .prose p, html.dark .prose li, html.dark .prose span { color: var(--text-secondary) !important; }
    
    /* OVERRIDES FOR HEADER SPECIFICALLY */
    html.dark header.bg-white\/80 { background-color: var(--nav-bg) !important; }
    
    /* ANY ELEMENT WITH WHITE BG IN DARK MODE */
    html.dark [style*="background: white"], html.dark [style*="background-color: white"], html.dark [style*="background-color: #ffffff"] { background-color: var(--card-bg) !important; }
    html.dark [style*="color: #111827"], html.dark [style*="color: #0f172a"] { color: var(--text-primary) !important; }
    html.dark [style*="color: #4b5563"], html.dark [style*="color: #6b7280"] { color: var(--text-secondary) !important; }
</style>
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Inject the universal CSS into <head>
    if '/* UNIVERSAL THEME VARIABLES */' not in content:
        content = re.sub(r'(</head>)', universal_dark_mode_css + r'\n\1', content, flags=re.IGNORECASE)

    # 2. Re-wire Tailwind config if it exists so that custom colors use var()
    # It will override the colors dict.
    if 'tailwind.config =' in content:
        # Find the tailwind.config script and replace it with a standard dynamic one
        replacement_config = """tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] },
                    colors: { 
                        primary: 'var(--text-primary)', 
                        secondary: 'var(--text-secondary)', 
                        accent: 'var(--accent-color)',
                        bgColor: 'var(--bg-color)',
                        cardBg: 'var(--card-bg)',
                        borderColor: 'var(--border-color)',
                        navBg: 'var(--nav-bg)'
                    }
                }
            }
        }"""
        # Using a non-greedy match to replace the whole config object
        content = re.sub(r'tailwind\.config\s*=\s*\{.*?\}(?=\s*</script>)', replacement_config, content, flags=re.DOTALL)
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Theme support injected universally!")

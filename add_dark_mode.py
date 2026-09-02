import os

import glob
import re

css_vars = """    <style>
        body { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
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
    </style>"""

tailwind_cfg = """    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'sans-serif'] },
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
        }
    </script>"""

toggle_html = """
                <button id="themeToggle" class="ml-4 p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-secondary">
                    <svg id="themeIconLight" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
                    <svg id="themeIconDark" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
                </button>
"""

script_html = """
    <!-- Theme Script -->
    <script>
        const html = document.documentElement;
        const themeToggle = document.getElementById('themeToggle');
        const themeIconLight = document.getElementById('themeIconLight');
        const themeIconDark = document.getElementById('themeIconDark');
        
        function setTheme(isDark) {
            if (isDark) {
                html.classList.add('dark');
                themeIconLight.classList.remove('hidden');
                themeIconDark.classList.add('hidden');
                localStorage.setItem('theme', 'dark');
            } else {
                html.classList.remove('dark');
                themeIconLight.classList.add('hidden');
                themeIconDark.classList.remove('hidden');
                localStorage.setItem('theme', 'light');
            }
        }
        
        // Initialize theme (default to non-dark unless local storage says otherwise)
        if (localStorage.getItem('theme') === 'dark') {
            setTheme(true);
        } else {
            setTheme(false); // default non-dark
        }
        
        if (themeToggle) {
            themeToggle.addEventListener('click', () => {
                setTheme(!html.classList.contains('dark'));
            });
        }
    </script>
"""

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update tailwind config
    content = re.sub(r'<script>\s*tailwind\.config = \{.*?\s*\}\s*</script>', tailwind_cfg, content, flags=re.DOTALL)
    
    # 2. Update styles (if it exists, replace, else append to head)
    if '<style>' in content and 'var(--bg-color)' not in content:
        content = re.sub(r'<style>.*?</style>', css_vars, content, flags=re.DOTALL)
    elif 'var(--bg-color)' not in content:
        content = content.replace('</head>', css_vars + '\n</head>')

    # 3. Inject Toggle Button into Navbar
    if 'id="themeToggle"' not in content:
        # find the end of the <nav> block and inject button right after it inside the flex container
        content = content.replace('</nav>', '</nav>' + toggle_html)
    
    # 4. Inject Theme Script before </body>
    if 'setTheme(isDark)' not in content:
        content = content.replace('</body>', script_html + '\n</body>')

    # 5. Class Replacements
    content = content.replace('bg-gray-50', 'bg-bgColor')
    content = content.replace('bg-white', 'bg-cardBg')
    content = content.replace('border-gray-200', 'border-borderColor')
    content = content.replace('border-gray-100', 'border-borderColor')
    content = content.replace('bg-white/80', 'bg-navBg')
    content = content.replace('bg-white/90', 'bg-navBg')
    
    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_file(os.path.join(root, file))

print("Dark mode injected globally!")

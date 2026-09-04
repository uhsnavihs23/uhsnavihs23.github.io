import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/news-app/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Add standard header right after <body>
header_html = """
    <!-- Global Header -->
    <header style="position: sticky; top: 0; z-index: 50; width: 100%; backdrop-filter: blur(12px); background-color: rgba(255, 255, 255, 0.8); border-bottom: 1px solid #e5e7eb;">
        <div style="max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; height: 4rem; display: flex; align-items: center; justify-content: space-between;">
            <a href="../../index.html" style="font-size: 1.25rem; font-weight: 700; color: #0f172a; text-decoration: none;">Shivanshu Sharma</a>
            <nav style="display: flex; gap: 1.5rem; align-items: center;">
                <a href="../../index.html" style="font-size: 0.875rem; font-weight: 500; color: #475569; text-decoration: none;">Home</a>
                <a href="../index.html" style="font-size: 0.875rem; font-weight: 500; color: #3b82f6; text-decoration: none;">Projects</a>
                <a href="../../about.html" style="font-size: 0.875rem; font-weight: 500; color: #475569; text-decoration: none;">About</a>
                <button id="themeToggle" style="margin-left: 1rem; padding: 0.5rem; border-radius: 9999px; cursor: pointer; border: none; background: transparent; color: #64748b;" onmouseover="this.style.backgroundColor='#f1f5f9'" onmouseout="this.style.backgroundColor='transparent'">
                    <svg id="themeIconLight" style="width: 1.25rem; height: 1.25rem; display: none;" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
                    <svg id="themeIconDark" style="width: 1.25rem; height: 1.25rem; display: block;" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
                </button>
            </nav>
        </div>
    </header>
"""

content = re.sub(r'(<body[^>]*>\s*)', r'\1' + header_html, content)

theme_script = """
    <script>
        const html = document.documentElement;
        const themeToggle = document.getElementById('themeToggle');
        const themeIconLight = document.getElementById('themeIconLight');
        const themeIconDark = document.getElementById('themeIconDark');
        
        function setTheme(isDark) {
            if (isDark) {
                html.classList.add('dark');
                if(themeIconLight) themeIconLight.style.display = 'block';
                if(themeIconDark) themeIconDark.style.display = 'none';
                localStorage.setItem('theme', 'dark');
            } else {
                html.classList.remove('dark');
                if(themeIconLight) themeIconLight.style.display = 'none';
                if(themeIconDark) themeIconDark.style.display = 'block';
                localStorage.setItem('theme', 'light');
            }
        }
        if (localStorage.getItem('theme') === 'dark') { setTheme(true); } else { setTheme(false); }
        if (themeToggle) { themeToggle.addEventListener('click', () => { setTheme(!html.classList.contains('dark')); }); }
    </script>
"""

if 'function setTheme(' not in content:
    content = re.sub(r'</body>', theme_script + '\n</body>', content)

with open(filepath, 'w') as f:
    f.write(content)

print("news-app updated")

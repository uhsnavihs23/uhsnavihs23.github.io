import re
import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/data-analyst-projects"
files = [
    'campus-electricity/index.html',
    'customer-shopping-trends/index.html',
    'food-delivery-analytics/index.html',
    'cohort-retention/index.html'
]

theme_btn = """
                <button id="themeToggle" style="margin-left: 1rem; padding: 0.5rem; border-radius: 9999px; cursor: pointer; border: none; background: transparent; color: #64748b;" onmouseover="this.style.backgroundColor='#f1f5f9'" onmouseout="this.style.backgroundColor='transparent'">
                    <svg id="themeIconLight" style="width: 1.25rem; height: 1.25rem; display: none;" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
                    <svg id="themeIconDark" style="width: 1.25rem; height: 1.25rem; display: block;" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
                </button>
"""

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
</body>
"""

for file in files:
    filepath = os.path.join(base_path, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Insert the button before the closing </nav> in the header
    if 'id="themeToggle"' not in content:
        content = re.sub(r'(<a href="[^"]*about\.html"[^>]*>About</a>\s*)(</nav>)', r'\1' + theme_btn + r'\n            \2', content)
    
    # 2. Insert the script before </body>
    if 'function setTheme(' not in content:
        content = re.sub(r'</body>', theme_script, content, flags=re.IGNORECASE)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Theme buttons added successfully.")

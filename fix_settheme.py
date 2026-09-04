import re

files = [
    '/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/book-recommender/index.html',
    '/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/image-filter-app/index.html'
]

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

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    if 'function setTheme(' not in content:
        content = re.sub(r'(</body>)', theme_script + r'\n\1', content, flags=re.IGNORECASE)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("setTheme script injected.")

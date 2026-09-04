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

    if "localStorage.getItem('retro')" not in content:
        # Find where theme script is and inject
        content = re.sub(r"(if\s*\(themeToggle\)\s*\{\s*themeToggle\.addEventListener\('click',.*?\);\s*\})", r"\1\n" + retro_js, content, flags=re.DOTALL)
        
        # some files might not match this exact regex if formatting is different. Let's try appending before </script> in the same block as setTheme
        if "localStorage.getItem('retro')" not in content:
             content = re.sub(r"(function setTheme\(isDark\) \{.*?</script>)", r"\1", content, flags=re.DOTALL) 
             # actually a simpler replace
             content = content.replace("localStorage.setItem('theme', 'light');\n        }", "localStorage.setItem('theme', 'light');\n        }\n" + retro_js, 1)

    with open(filepath, 'w') as f:
        f.write(content)

print("Retro JS injected!")

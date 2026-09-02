with open('projects/breathing-room/index.html', 'r') as f:
    content = f.read()

# Restore tailwind config
tailwind_config = """<script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'sans-serif'] },
                    colors: { primary: '#0f172a', secondary: '#475569', accent: '#3b82f6' }
                }
            }
        }
    </script>"""

import re
# Replace the broken script tag in head with tailwind config
content = re.sub(r'<head>.*?</head>', lambda m: m.group(0).replace(re.search(r'<script>\s*const wrapper.*?</script>', m.group(0), re.DOTALL).group(0), tailwind_config), content, flags=re.DOTALL)

# Delete the old broken script at the bottom
content = re.sub(r'<script>\s*const wrapper = document\.getElementById\(\'breatheWrapper\'\);\s*const btn = document\.getElementById\(\'toggleBtn\'\);.*?</script>', '', content, flags=re.DOTALL)

with open('projects/breathing-room/index.html', 'w') as f:
    f.write(content)

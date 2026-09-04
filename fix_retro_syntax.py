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

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # The broken syntax was:
    #             setTheme(!html.classList.contains('dark'));
    #         }
    #
    #         const retroToggle = document.getElementById('retroToggle');
    # ...
    #         if (retroToggle) { retroToggle.addEventListener('click', () => { setRetro(!html.classList.contains('retro')); }); }
    # );
    #         }
    
    # We can just extract the retro JS, remove it from the bad place, and put it at the correct place.
    # OR we can just replace the entire script block with a known good one.
    
    # Let's fix the specific syntax error.
    content = content.replace("            }\n\n        const retroToggle", "            });\n        }\n\n        const retroToggle")
    content = content.replace("retroToggle.addEventListener('click', () => { setRetro(!html.classList.contains('retro')); }); }\n);\n        }", "retroToggle.addEventListener('click', () => { setRetro(!html.classList.contains('retro')); }); }\n")
    
    # Rename button "IE" to "Retro"
    content = content.replace('>IE</button>', '>Retro</button>')

    with open(filepath, 'w') as f:
        f.write(content)

print("Retro syntax and button text fixed!")

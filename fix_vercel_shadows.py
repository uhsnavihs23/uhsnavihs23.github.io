import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Flatten shadows for Vercel aesthetic
    content = content.replace('shadow-2xl', 'shadow-md')
    content = content.replace('shadow-xl', 'shadow-md')
    content = content.replace('shadow-lg', 'shadow-sm')

    with open(filepath, 'w') as f:
        f.write(content)

print("Vercel flattened shadows applied!")

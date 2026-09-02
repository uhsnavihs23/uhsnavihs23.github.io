import os

def fix_footer_id(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace the footer span ID
    if '<span id="year">' in content:
        content = content.replace('<span id="year">', '<span id="footerYear">')
        content = content.replace("document.getElementById('year').textContent = new Date().getFullYear();", "document.getElementById('footerYear').textContent = new Date().getFullYear();")
        
        with open(filepath, 'w') as f:
            f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            fix_footer_id(os.path.join(root, file))


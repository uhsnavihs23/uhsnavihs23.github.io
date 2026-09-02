import os
import re

def fix_scripts(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Define the block we want to deduplicate
    # Let's just find and remove ALL instances of these two lines anywhere in the document
    
    # 1. Remove all script year tags
    content = re.sub(r'<script>document.getElementById\((?:.year.|.footerYear.)\).textContent = new Date\(\).getFullYear\(\);</script>\s*', '', content)
    
    # 2. Remove all goatcounter scripts
    content = re.sub(r'<script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>\s*', '', content)
    
    # Now, if the file HAS a footer, we want to inject exactly ONE copy of these scripts right before the footer
    # Because they need to exist!
    
    clean_scripts = """    <script>document.getElementById('footerYear').textContent = new Date().getFullYear();</script>
    <script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>\n"""

    if '<footer' in content:
        content = content.replace('<footer', clean_scripts + '    <footer')

    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            fix_scripts(os.path.join(root, file))


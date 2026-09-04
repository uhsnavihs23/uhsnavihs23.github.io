import os
import re

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Clean up the trailing mess. 
            # Find the LAST </body> and everything after it, replace with just </body>\n</html>
            content = re.sub(r'</body>.*', '</body>\n</html>', content, flags=re.DOTALL)
            
            with open(filepath, 'w') as f:
                f.write(content)


import glob
import re

for filepath in glob.glob('./projects/**/*.html', recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Strip liquid tags in link hrefs
    content = re.sub(r'href="\{\{[^}]*\}\}"', 'href=""', content)
    content = re.sub(r'src="\{\{[^}]*\}\}"', 'src=""', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
        

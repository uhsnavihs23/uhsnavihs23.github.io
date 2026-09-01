import glob
import re

for filepath in glob.glob('./projects/**/*.html', recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Strip Jekyll frontmatter
    if content.startswith('---'):
        content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
        with open(filepath, 'w') as f:
            f.write(content.strip())
            print(f"Stripped frontmatter from {filepath}")

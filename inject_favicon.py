import glob
import re

for filepath in glob.glob('./**/*.html', recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()

    # Calculate depth to prefix the favicon path correctly
    depth = len(filepath.split('/')) - 2
    prefix = '../' * depth if depth > 0 else './'

    favicon_tag = f'<link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">'

    # If it already has a favicon, replace it, else inject after <title>
    if 'favicon' not in content:
        content = re.sub(r'(<title>.*?</title>)', r'\1\n    ' + favicon_tag, content, flags=re.IGNORECASE)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Favicon globally injected.")

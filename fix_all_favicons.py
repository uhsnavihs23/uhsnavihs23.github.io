import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    parts = filepath.split('/')
    depth = len(parts) - 2
    prefix = '../' * depth if depth > 0 else './'
    favicon_tag = f'<link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">'

    # First, remove existing favicon tags (be careful not to match too much)
    content = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>\s*', '', content, flags=re.IGNORECASE)

    # Insert into <head> precisely
    if re.search(r'<head\b[^>]*>', content, re.IGNORECASE):
        content = re.sub(r'(<head\b[^>]*>)', r'\1\n    ' + favicon_tag, content, count=1, flags=re.IGNORECASE)
    else:
        # If no <head>, see if we can wrap the whole thing or prepend
        if re.search(r'<html\b[^>]*>', content, re.IGNORECASE):
            content = re.sub(r'(<html\b[^>]*>)', r'\1\n<head>\n    ' + favicon_tag + '\n</head>', content, count=1, flags=re.IGNORECASE)
        else:
            # prepend doctype, html, head, body
            title = parts[-2].replace('-', ' ').title() if depth > 0 else 'Portfolio'
            content = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>{title}</title>\n    {favicon_tag}\n</head>\n<body>\n" + content + "\n</body>\n</html>"
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Favicons fixed across all HTML files.")

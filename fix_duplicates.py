import os
import re

def fix_duplicates(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all headers
    headers = list(re.finditer(r'<header.*?</header>', content, flags=re.DOTALL))
    if len(headers) > 1:
        # Keep the first one, remove the others
        first_header_end = headers[0].end()
        # To remove others, we can just replace them with empty string in the remaining text
        rest_of_text = content[first_header_end:]
        rest_of_text = re.sub(r'<header.*?</header>', '', rest_of_text, flags=re.DOTALL)
        content = content[:first_header_end] + rest_of_text

    # Find all footers
    footers = list(re.finditer(r'<footer.*?</footer>', content, flags=re.DOTALL))
    if len(footers) > 1:
        # Keep the first one, remove the others
        first_footer_end = footers[0].end()
        rest_of_text = content[first_footer_end:]
        rest_of_text = re.sub(r'<footer.*?</footer>', '', rest_of_text, flags=re.DOTALL)
        content = content[:first_footer_end] + rest_of_text

    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            fix_duplicates(os.path.join(root, file))


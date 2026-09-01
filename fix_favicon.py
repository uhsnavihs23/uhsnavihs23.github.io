import re

with open('tailwind_redesign.py', 'r') as f:
    content = f.read()

# Add favicon link to get_tailwind_head
replacement = r"""    <title>{title} | Shivanshu Sharma</title>
    <link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">
    <script src="https://cdn.tailwindcss.com"></script>"""

content = re.sub(r'    <title>\{title\} \| Shivanshu Sharma</title>\n    <script src="https://cdn.tailwindcss.com"></script>', replacement, content)

with open('tailwind_redesign.py', 'w') as f:
    f.write(content)

print("Updated tailwind_redesign.py with favicon")

import re
import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
files = []
for root, dirs, fnames in os.walk(base_path):
    for f in fnames:
        if f.endswith('.html'):
            files.append(os.path.join(root, f))

# The broken image tag
broken_img_pattern = r'<img\s+src="https://23022000\.goatcounter\.com/count\?.*?"\s+width="auto"\s+height="26"\s+alt="Views">'

# A nice small SVG chart icon to replace the broken image
chart_icon = '<svg class="w-5 h-5 text-secondary hover:text-accent transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>'

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    if re.search(broken_img_pattern, content):
        content = re.sub(broken_img_pattern, chart_icon, content)
        with open(filepath, 'w') as f:
            f.write(content)

print("GoatCounter images replaced with SVGs.")

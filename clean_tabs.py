import re

with open('projects/data-analyst-projects/campus-electricity/index.html', 'r') as f:
    content = f.read()

# Using regex to remove the entire tabs block
content = re.sub(r'<div class="tab" data-tab="analysis">.*?</div>\n        </div>', '', content, flags=re.DOTALL)

with open('projects/data-analyst-projects/campus-electricity/index.html', 'w') as f:
    f.write(content)

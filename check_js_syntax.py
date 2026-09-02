import re
with open('projects/policy-brief-generator/index.html', 'r') as f:
    content = f.read()

scripts = re.findall(r'<script>(.*?)</script>', content, flags=re.DOTALL)
# The last script should be the App Logic
with open('test_logic.js', 'w') as f:
    f.write(scripts[-1])

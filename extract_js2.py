import re
with open('projects/policy-brief-generator/index.html', 'r') as f:
    content = f.read()

scripts = re.findall(r'<script>(.*?)</script>', content, flags=re.DOTALL)
with open('test_logic.js', 'w') as f:
    f.write(scripts[-1])

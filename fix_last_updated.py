import re

with open('projects/political-intel/index.html', 'r') as f:
    content = f.read()

target = "document.getElementById('lastUpdated').textContent = date.toLocaleString();"
replacement = """const options = { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' };
                    document.getElementById('lastUpdated').textContent = date.toLocaleString('en-GB', options);"""

content = content.replace(target, replacement)

with open('projects/political-intel/index.html', 'w') as f:
    f.write(content)

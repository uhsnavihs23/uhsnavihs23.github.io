with open('projects/policy-brief-generator/index.html', 'r') as f:
    content = f.read()

# Replace the broken string
old_str = """document.getElementById('briefContext').innerText = contextText + "
These developments underscore a critical need for targeted regulatory intervention.";"""

new_str = """document.getElementById('briefContext').innerText = contextText + "\\nThese developments underscore a critical need for targeted regulatory intervention.";"""

content = content.replace(old_str, new_str)

with open('projects/policy-brief-generator/index.html', 'w') as f:
    f.write(content)

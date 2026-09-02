with open('projects/policy-brief-generator/index.html', 'r') as f:
    content = f.read()

# I will just replace the exact broken string
content = content.replace("document.getElementById(\\'briefContext\\').innerText", "document.getElementById('briefContext').innerText")

with open('projects/policy-brief-generator/index.html', 'w') as f:
    f.write(content)

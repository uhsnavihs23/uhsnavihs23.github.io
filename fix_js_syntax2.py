with open('projects/policy-brief-generator/index.html', 'r') as f:
    content = f.read()

# We need to find the exact broken line and replace it
import re
content = re.sub(r'document.getElementById\(\'briefContext\'\)\.innerText = contextText \+ "\\n\nThese developments underscore a critical need for targeted regulatory intervention\.";', 
                 r'document.getElementById(\'briefContext\').innerText = contextText + "\\nThese developments underscore a critical need for targeted regulatory intervention.";', 
                 content)

with open('projects/policy-brief-generator/index.html', 'w') as f:
    f.write(content)

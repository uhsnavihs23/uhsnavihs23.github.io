with open('about.html', 'r') as f:
    content = f.read()

import re

# find all blocks of <!-- Certifications Modal -->...
# actually just split
parts = content.split('<!-- Certifications Modal -->')
if len(parts) > 2:
    # meaning there's more than one
    # The last part has the Modal HTML + JS + Theme Script + </body>
    # The middle part has the first Modal HTML + JS.
    # We want to remove the middle part!
    # So we join parts[0] + '<!-- Certifications Modal -->' + parts[-1]
    
    new_content = parts[0] + '<!-- Certifications Modal -->' + parts[-1]
    
    with open('about.html', 'w') as f:
        f.write(new_content)
        

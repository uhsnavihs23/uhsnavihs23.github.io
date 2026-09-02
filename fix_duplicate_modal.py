import re

with open('about.html', 'r') as f:
    content = f.read()

# Replace all occurrences of the modal block with a single one
# The block starts with "<!-- Certifications Modal -->" and ends with "<!-- Theme Script -->"

modal_block_regex = r'(\s*<!-- Certifications Modal -->.*?)</script>\s*<!-- Theme Script -->'
matches = list(re.finditer(modal_block_regex, content, flags=re.DOTALL))

if len(matches) > 1:
    # Just grab the last one and replace the whole chunk covering from the first match to the last match
    first_match_start = matches[0].start()
    last_match_end = matches[-1].end()
    
    single_block = matches[0].group(0)
    
    content = content[:first_match_start] + single_block + content[last_match_end:]
    
    with open('about.html', 'w') as f:
        f.write(content)

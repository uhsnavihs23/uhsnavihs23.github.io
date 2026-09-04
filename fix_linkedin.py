import os
import re

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

linkedin_block = """
                <a href="https://linkedin.com/in/sharma-shivanshu-2302" target="_blank" class="text-secondary hover:text-accent transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # If linkedin is missing
    if "linkedin.com" not in content:
        # Find the github block and append linkedin after it
        # The github block ends with </a>
        github_pattern = r'(<a href="https://github\.com/sharma-shivanshu" target="_blank" class="text-secondary hover:text-accent transition-colors">.*?</a>)'
        
        # We can use re.sub to append it
        content = re.sub(github_pattern, r'\1' + linkedin_block, content, flags=re.DOTALL)
        
        with open(filepath, 'w') as f:
            f.write(content)
            
print("LinkedIn icons restored across all files!")

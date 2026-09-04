import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
py_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.py') and file != os.path.basename(__file__):
            py_files.append(os.path.join(root, file))

for filepath in py_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Apply Vercel structural fixes to the generator strings
    content = content.replace('rounded-3xl', 'rounded-xl')
    content = content.replace('rounded-2xl', 'rounded-lg')
    content = content.replace('shadow-2xl', 'shadow-md')
    content = content.replace('shadow-xl', 'shadow-md')
    
    # We shouldn't replace bg-white universally in python scripts because it might be logic, 
    # but the global CSS in index.html will catch it anyway when the HTML is generated.
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Python generator scripts updated to align with AWESOME_DESIGN.md!")

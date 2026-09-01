import os
import glob
import re


def get_depth(filepath):
    return len(filepath.split('/')) - 1

def generate_header(depth, active=''):
    prefix = '../' * depth if depth > 0 else './'
    home_link = f"{prefix}index.html"
    proj_link = f"{prefix}projects/index.html"
    about_link = f"{prefix}about.html"
    
    home_style = ' style="color: var(--link-color);"' if active == 'home' else ''
    proj_style = ' style="color: var(--link-color);"' if active == 'projects' else ''
    about_style = ' style="color: var(--link-color);"' if active == 'about' else ''

    return f'''    <!-- GLOBAL STYLES FOR CONSISTENCY -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{prefix}css/style.css">
    
    <header style="background-color: var(--header-bg); border-bottom: 1px solid var(--border-color);">
        <div class="container nav-wrapper" style="max-width: 1100px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; height: 70px;">
            <a href="{home_link}" class="logo" style="font-size: 1.5rem; font-weight: 700; text-decoration: none; color: var(--accent-color); letter-spacing: -0.5px;">Shivanshu Sharma</a>
            <nav>
                <ul style="list-style: none; display: flex; gap: 20px; margin:0; padding:0;">
                    <li><a href="{home_link}"{home_style} style="text-decoration: none; font-weight: 500;">Home</a></li>
                    <li><a href="{proj_link}"{proj_style} style="text-decoration: none; font-weight: 500;">Projects</a></li>
                    <li><a href="{about_link}"{about_style} style="text-decoration: none; font-weight: 500;">About</a></li>
                </ul>
            </nav>
        </div>
    </header>'''

def generate_footer(depth):
    prefix = '../' * depth if depth > 0 else './'
    return f'''
    <footer style="text-align: center; padding: 40px 0; border-top: 1px solid var(--border-color); margin-top: 40px; color: var(--secondary-text);">
        <div class="container">
            <p>&copy; <span id="year"></span> Shivanshu Sharma. All rights reserved.</p>
        </div>
    </footer>
    <script src="{prefix}js/script.js"></script>
    '''

def process_app_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    depth = get_depth(filepath.replace('./', ''))
    
    # Check if header already exists, if so skip wrapping
    if '<header' in content:
        return
        
    header = generate_header(depth, active='projects')
    footer = generate_footer(depth)
    
    # Inject header after <body>
    content = re.sub(r'(<body[^>]*>)', r'\1\n' + header + '\n<main style="padding: 40px 20px; min-height: 70vh;">', content, count=1, flags=re.IGNORECASE)
    
    # Inject footer before </body>
    content = re.sub(r'(</body>)', r'</main>\n' + footer + '\n\1', content, flags=re.IGNORECASE)

    # Convert absolute links to relative
    content = content.replace('/projects/', '../')
    content = content.replace('/portfolio/projects/', '../')
    
    with open(filepath, 'w') as f:
        f.write(content)

# Fix app files
app_files = [
    './projects/image-filter-app/index.html',
    './projects/github-profile-finder/index.html',
    './projects/market-tracker/index.html',
    './projects/policy-brief-generator/index.html',
    './projects/news-app/index.html',
    './projects/book-recommender/index.html',
    './projects/movie-recommender/index.html',
    './projects/political-intel/index.html'
]
for f in app_files:
    if os.path.exists(f):
        process_app_file(f)

# Fix projects/index.html relative links
with open('./projects/index.html', 'r') as f:
    idx = f.read()
idx = idx.replace('../projects/', './')
idx = idx.replace('.md"', '/index.html"')
with open('./projects/index.html', 'w') as f:
    f.write(idx)

# Re-render MD files to HTML
md_files = glob.glob('./projects/data-analyst-projects/*.md')
for md in md_files:
    with open(md, 'r') as f:
        text = f.read()
    
    title = md.split('/')[-1].replace('.md', '').replace('-', ' ').title()
    html_path = md.replace('.md', '/index.html')
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    
    # A simple html template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Shivanshu Sharma</title>
</head>
<body>
    <div style="max-width: 800px; margin: 0 auto; font-family: 'Inter', sans-serif; line-height: 1.6;">
        <h1 style="color: #2c3e50; font-size: 2.5rem; margin-bottom: 20px;">{title}</h1>
        <div style="background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #e0e0e0; margin-bottom: 30px;">
            <p><strong>Note:</strong> This project details are being migrated. Check back soon for the full case study.</p>
        </div>
        <a href="../../index.html" style="color: #2980b9; text-decoration: none;">&larr; Back to Projects</a>
    </div>
</body>
</html>
"""
    with open(html_path, 'w') as f:
        f.write(html_content)
    
    process_app_file(html_path)
    os.remove(md)

print("Restructured and styled apps.")

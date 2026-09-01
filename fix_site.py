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

    return f'''    <header>
        <div class="container nav-wrapper">
            <a href="{home_link}" class="logo">Shivanshu Sharma</a>
            <nav>
                <ul>
                    <li><a href="{home_link}"{home_style}>Home</a></li>
                    <li><a href="{proj_link}"{proj_style}>Projects</a></li>
                    <li><a href="{about_link}"{about_style}>About</a></li>
                </ul>
            </nav>
        </div>
    </header>'''

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    depth = get_depth(filepath.replace('./', ''))
    prefix = '../' * depth if depth > 0 else './'
    
    # 1. Fix CSS/JS links in existing header
    content = re.sub(r'href=".*?(?:/portfolio)?/css/style\.css"', f'href="{prefix}css/style.css"', content)
    content = re.sub(r'src=".*?(?:/portfolio)?/js/script\.js"', f'src="{prefix}js/script.js"', content)

    # 2. Replace the whole header block if it exists (for index, about, projects/index, urban-governance)
    if '<header>' in content:
        active = 'projects'
        if filepath == './index.html': active = 'home'
        elif filepath == './about.html': active = 'about'
        
        new_header = generate_header(depth, active)
        content = re.sub(r'<header>.*?</header>', new_header, content, flags=re.DOTALL)

    # 3. Fix project links in index.html and projects/index.html
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/market-tracker\.html"', f'href="{prefix}projects/market-tracker/index.html"', content)
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/market-tracker(?:/index\.html)?"', f'href="{prefix}projects/market-tracker/index.html"', content)
    
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/urban-governance\.html"', f'href="{prefix}projects/urban-governance.html"', content)
    
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/image-filter-app/index\.html"', f'href="{prefix}projects/image-filter-app/index.html"', content)
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/image-filter-app(?:/index\.html)?"', f'href="{prefix}projects/image-filter-app/index.html"', content)

    content = re.sub(r'href=".*?(?:/portfolio)?/projects/movie-recommender\.html"', f'href="{prefix}projects/movie-recommender/index.html"', content)
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/github-profile-finder/index\.html"', f'href="{prefix}projects/github-profile-finder/index.html"', content)
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/policy-brief-generator/index\.html"', f'href="{prefix}projects/policy-brief-generator/index.html"', content)
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/news"', f'href="{prefix}projects/news"', content)
    
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/data-analyst-projects/food-delivery-analytics/index\.html"', f'href="{prefix}projects/data-analyst-projects/food-delivery-analytics.md"', content)
    content = re.sub(r'href=".*?(?:/portfolio)?/projects/data-analyst-projects/project-1-customer-shopping-trends-analysis/index\.html"', f'href="{prefix}projects/data-analyst-projects/project-1-customer-shopping-trends-analysis.md"', content)

    with open(filepath, 'w') as f:
        f.write(content)

for filepath in glob.glob('./**/*.html', recursive=True):
    process_file(filepath)

print("HTML files processed successfully.")

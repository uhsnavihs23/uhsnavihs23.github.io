import os
import glob
import re

from tailwind_redesign import get_header, get_footer, get_tailwind_head

def process_app_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    depth = get_depth(filepath.replace('./', ''))
    
    # Let's remove the old injected header and footer
    content = re.sub(r'<!-- GLOBAL STYLES FOR CONSISTENCY -->.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer.*?</footer>\s*<script src="[^"]*js/script.js"></script>', '', content, flags=re.DOTALL)
    
    # Also remove <main style="..."> if it was injected
    content = re.sub(r'<main style="padding: 40px 20px; min-height: 70vh;">', '<main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">', content)
    
    # Add Tailwind CDN if not present
    if 'cdn.tailwindcss.com' not in content:
        content = content.replace('</head>', '    <script src="https://cdn.tailwindcss.com"></script>\n</head>')

    header = get_header(depth, active='projects')
    footer = get_footer(depth)
    
    # Inject new header after <body>
    content = re.sub(r'(<body[^>]*>)', r'\1\n' + header, content, count=1, flags=re.IGNORECASE)
    
    # Inject new footer before </body>
    content = re.sub(r'(</body>)', footer + '\n\1', content, flags=re.IGNORECASE)

    with open(filepath, 'w') as f:
        f.write(content)

def get_depth(filepath):
    return len(filepath.split('/')) - 1

app_files = [
    './projects/image-filter-app/index.html',
    './projects/github-profile-finder/index.html',
    './projects/market-tracker/index.html',
    './projects/policy-brief-generator/index.html',
    './projects/news-app/index.html',
    './projects/book-recommender/index.html',
    './projects/movie-recommender/index.html',
    './projects/political-intel/index.html',
    './projects/data-analyst-projects/food-delivery-analytics/index.html',
    './projects/data-analyst-projects/project-1-customer-shopping-trends-analysis/index.html'
]

for f in app_files:
    if os.path.exists(f):
        process_app_file(f)

print("Updated apps with Tailwind Header/Footer.")

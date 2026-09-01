import os
import re

# 1. Fix Image Filter App layout
def fix_app_layout(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # The body might have flex classes that mess up the injected header
    if 'body class="' in content:
        # replace old body class with global tailwind class
        content = re.sub(r'<body class="[^"]*">', '<body class="bg-gray-50 text-primary flex flex-col min-h-screen">', content)
    
    # We need to wrap the app content in a flex container so it's centered, but below the header.
    # The header was already injected. Let's find </header>
    if '</header>' in content:
        # Check if we already have a <main> wrapper. My previous script didn't inject <main> properly into image-filter-app
        # It just injected <header> and <footer>
        
        # Let's completely remove the header and footer, then rebuild it safely.
        content = re.sub(r'<!-- Navbar -->.*?</header>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Footer -->.*?</footer>\s*<script[^>]*></script>', '', content, flags=re.DOTALL)
        content = re.sub(r'^\s*$', '', content, flags=re.MULTILINE)

        # Now we have the raw app body. Let's ensure the body tag is clean
        content = re.sub(r'<body[^>]*>', '<body class="bg-gray-50 text-primary flex flex-col min-h-screen">', content)

        from tailwind_redesign import get_header, get_footer
        header = get_header(2, 'projects')
        footer = get_footer(2)

        # Inject header and start main
        content = content.replace('<body class="bg-gray-50 text-primary flex flex-col min-h-screen">', 
                                  '<body class="bg-gray-50 text-primary flex flex-col min-h-screen">\n' + header + '\n<main class="flex-grow flex justify-center items-center py-12 px-4">')
        
        # End main and inject footer
        content = content.replace('</body>', '</main>\n' + footer + '\n</body>')
        
        with open(filepath, 'w') as f:
            f.write(content)

fix_app_layout('./projects/image-filter-app/index.html')
fix_app_layout('./projects/github-profile-finder/index.html')
fix_app_layout('./projects/news-app/index.html')

print("Fixed flex layouts for apps.")
fix_app_layout('./projects/market-tracker/index.html')
fix_app_layout('./projects/movie-recommender/index.html')
fix_app_layout('./projects/book-recommender/index.html')
fix_app_layout('./projects/policy-brief-generator/index.html')
fix_app_layout('./projects/political-intel/index.html')

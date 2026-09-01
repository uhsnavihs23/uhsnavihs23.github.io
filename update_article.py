import re

with open('./projects/urban-governance.html', 'r') as f:
    content = f.read()

# Extract the actual article content
match = re.search(r'<div class="article-content">(.*?)</div>\s*<div style="text-align', content, re.DOTALL)
if match:
    article_body = match.group(1)
else:
    print("Could not find article body.")
    exit(1)

article_body = article_body.replace('<h2>', '<h2 class="text-2xl font-bold text-primary mt-12 mb-4">')
article_body = article_body.replace('<p>', '<p class="text-lg text-secondary leading-relaxed mb-6">')
article_body = article_body.replace('<ul>', '<ul class="list-disc pl-6 text-lg text-secondary leading-relaxed mb-6 space-y-2">')
article_body = article_body.replace('<div class="article-quote">', '<div class="border-l-4 border-accent bg-blue-50 p-6 my-8 rounded-r-lg italic text-lg text-secondary shadow-sm">')
article_body = article_body.replace('<div class="article-quote" style="background-color: #f8f9fa; border-left-color: #28a745;">', '<div class="border-l-4 border-emerald-500 bg-emerald-50 p-6 my-8 rounded-r-lg text-secondary shadow-sm">')

from tailwind_redesign import get_tailwind_head, get_header, get_footer

new_html = get_tailwind_head("Urban Governance", 1) + get_header(1, 'projects') + f'''
    <main class="flex-grow max-w-3xl mx-auto px-4 sm:px-6 py-20">
        <a href="./index.html" class="inline-flex items-center text-sm font-medium text-secondary hover:text-accent mb-8 transition-colors">
            <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
        
        <article>
            <header class="mb-12 text-center sm:text-left">
                <div class="inline-block px-3 py-1 bg-amber-100 text-amber-800 text-xs font-bold rounded-full uppercase tracking-wide mb-4">Policy & Governance</div>
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight text-primary mb-4 leading-tight">Fixing Urban Governance in India: Simple Steps for Better Cities</h1>
                <p class="text-secondary text-sm font-medium">June 2, 2025</p>
            </header>
            
            <div class="prose prose-lg prose-blue max-w-none">
                {article_body}
            </div>
        </article>
    </main>
''' + get_footer(1)

with open('./projects/urban-governance.html', 'w') as f:
    f.write(new_html)

print("Updated urban governance article.")

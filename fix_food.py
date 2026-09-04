import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/data-analyst-projects/food-delivery-analytics/index.html"
with open(filepath, 'r') as f:
    content = f.read()

header_html = """
    <!-- Global Header -->
    <header class="sticky top-0 z-50 w-full backdrop-blur-md bg-white/80 border-b border-gray-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="../../../index.html" class="text-xl font-bold tracking-tight text-gray-900 hover:text-blue-600 transition-colors">Shivanshu Sharma</a>
            <nav class="flex gap-6 items-center">
                <a href="../../../index.html" class="text-sm font-medium transition-colors hover:text-blue-600 text-gray-600">Home</a>
                <a href="../../index.html" class="text-sm font-medium transition-colors hover:text-blue-600 text-blue-600">Projects</a>
                <a href="../../../about.html" class="text-sm font-medium transition-colors hover:text-blue-600 text-gray-600">About</a>
            </nav>
        </div>
    </header>
"""

content = re.sub(r'<header.*?</header>', header_html, content, flags=re.DOTALL)

back_btn = """
        <a href="../../index.html" class="inline-flex items-center text-sm font-medium text-gray-500 hover:text-blue-600 mb-8 transition-colors">
            <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
"""

content = re.sub(r'(<main[^>]*>\s*)', r'\1' + back_btn, content)

with open(filepath, 'w') as f:
    f.write(content)

print("food-delivery-analytics updated")

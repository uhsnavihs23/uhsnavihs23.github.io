import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/data-analyst-projects/cohort-retention/index.html"
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

# Insert right after <body ...>
content = re.sub(r'(<body[^>]*>\s*)', r'\1' + header_html, content)

with open(filepath, 'w') as f:
    f.write(content)

print("cohort-retention updated")

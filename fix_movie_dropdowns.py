import os

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Fix dropdowns
content = content.replace('class="w-full sm:w-1/3 p-2 border rounded"', 'class="w-full sm:w-1/3 p-2 border border-borderColor rounded bg-cardBg text-primary"')

# Let's also check for pagination buttons or search inputs
content = content.replace('class="p-2 border rounded w-full sm:w-2/3"', 'class="p-2 border border-borderColor rounded w-full sm:w-2/3 bg-cardBg text-primary"')
content = content.replace('class="px-4 py-2 bg-blue-500 text-white rounded"', 'class="px-4 py-2 bg-accent text-white rounded"')

with open(filepath, 'w') as f:
    f.write(content)

print("Movie Recommender dropdowns and inputs fixed!")

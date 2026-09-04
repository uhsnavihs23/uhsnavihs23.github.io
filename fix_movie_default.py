import re

html_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/index.html"
with open(html_path, 'r') as f:
    content = f.read()

# Change the classes on the buttons
# Remove blue from Recent
content = content.replace('data-sort="primary_release_date.desc" class="sort-btn px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700 font-medium"', 'data-sort="primary_release_date.desc" class="sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600"')
# Add blue to Popular
content = content.replace('data-sort="popularity.desc" class="sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600"', 'data-sort="popularity.desc" class="sort-btn px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700 font-medium"')

with open(html_path, 'w') as f:
    f.write(content)

js_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/app.js"
with open(js_path, 'r') as f:
    appjs = f.read()

appjs = appjs.replace("let currentSortBy = 'primary_release_date.desc';", "let currentSortBy = 'popularity.desc';")

with open(js_path, 'w') as f:
    f.write(appjs)

print("Movie recommender default fixed")

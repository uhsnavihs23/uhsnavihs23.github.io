import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Remove the sortBy select that I added previously
content = re.sub(r'<select id="sortBy".*?</select>', '', content, flags=re.DOTALL)

# 2. Add the row of sort buttons directly below the filters row
# The filters row is <div class="flex flex-col sm:flex-row flex-wrap gap-4 mb-8"> ... </div>
# We need to insert the buttons after that div.
sort_buttons_html = """
        <div class="mb-8">
            <h3 class="text-sm font-semibold mb-3 text-secondary uppercase tracking-wider">Sort Movies By:</h3>
            <div class="flex flex-wrap gap-3" id="sortButtons">
                <button data-sort="primary_release_date.desc" class="sort-btn px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700 font-medium">Recent (Newest)</button>
                <button data-sort="popularity.desc" class="sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600">Most Popular</button>
                <button data-sort="vote_average.desc" class="sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600">Highest Rated</button>
                <button data-sort="revenue.desc" class="sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600">Highest Grossing</button>
                <button data-sort="primary_release_date.asc" class="sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600">Oldest</button>
            </div>
        </div>
"""

# Insert after the closing div of the filters.
# Let's find: `</select>\n        </div>\n        <div id="movies"`
content = re.sub(r'(</select>\s*</div>)(\s*<div id="movies")', r'\1\n' + sort_buttons_html + r'\2', content)

with open(filepath, 'w') as f:
    f.write(content)

appjs_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/app.js"
with open(appjs_path, 'r') as f:
    appjs = f.read()

# Remove the sortBySelect const and event listener
appjs = re.sub(r'const sortBySelect = document.getElementById\(\'sortBy\'\);\n', '', appjs)
appjs = re.sub(r'sortBySelect\.addEventListener.*?\}\);\n', '', appjs, flags=re.DOTALL)

# Change default to recent
appjs = appjs.replace("let currentSortBy = 'popularity.desc';", "let currentSortBy = 'primary_release_date.desc';")

# Add event listener for sortButtons
sort_logic = """
const sortButtons = document.querySelectorAll('.sort-btn');
sortButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Reset styles
        sortButtons.forEach(b => {
            b.className = "sort-btn px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 font-medium dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600";
        });
        // Set active style
        e.target.className = "sort-btn px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700 font-medium";
        
        currentSortBy = e.target.getAttribute('data-sort');
        currentPage = 1;
        fetchMovies(currentGenre, currentLanguage, currentYear, currentSortBy);
    });
});
"""

appjs = appjs + "\n" + sort_logic

with open(appjs_path, 'w') as f:
    f.write(appjs)

print("Movie recommender updated!")

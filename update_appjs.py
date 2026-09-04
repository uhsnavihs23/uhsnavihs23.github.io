import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/app.js"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Add const
content = content.replace("const yearSelect = document.getElementById('year');", "const yearSelect = document.getElementById('year');\nconst sortBySelect = document.getElementById('sortBy');")

# 2. Add state let
content = content.replace("let currentYear = '';", "let currentYear = '';\nlet currentSortBy = 'popularity.desc';")

# 3. Update fetchMovies definition
content = content.replace("async function fetchMovies(genreId, language, year, page = 1)", "async function fetchMovies(genreId, language, year, sortBy, page = 1)")
content = content.replace("if (year) url += `&primary_release_year=${year}`;", "if (year) url += `&primary_release_year=${year}`;\n    if (sortBy) url += `&sort_by=${sortBy}`;\n    else url += `&sort_by=popularity.desc`;")

# 4. Update calls to fetchMovies
# Initial call
content = content.replace("fetchMovies(currentGenre, currentLanguage, currentYear);", "fetchMovies(currentGenre, currentLanguage, currentYear, currentSortBy);")

# Prev / Next button calls
content = content.replace("fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);", "fetchMovies(currentGenre, currentLanguage, currentYear, currentSortBy, currentPage);")

# 5. Add event listener for sortBySelect
event_listeners = """
sortBySelect.addEventListener('change', (e) => {
    currentSortBy = e.target.value;
    currentPage = 1;
    fetchMovies(currentGenre, currentLanguage, currentYear, currentSortBy);
});
"""
content = content.replace("yearSelect.addEventListener('change', (e) => {", event_listeners + "\nyearSelect.addEventListener('change', (e) => {")

with open(filepath, 'w') as f:
    f.write(content)

print("app.js updated")

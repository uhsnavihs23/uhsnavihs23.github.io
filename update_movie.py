import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/movie-recommender/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Make the filters div wrap and add the sort dropdown
old_filters = '<div class="flex flex-col sm:flex-row gap-4 mb-8">'
new_filters = '<div class="flex flex-col sm:flex-row flex-wrap gap-4 mb-8">'

content = content.replace(old_filters, new_filters)

# Add the select option
sort_select = """
            <select id="sortBy" class="w-full sm:flex-1 p-2 border rounded bg-cardBg text-primary" aria-label="Sort movies by">
                <option value="popularity.desc">Most Popular</option>
                <option value="primary_release_date.desc">Release Date (Newest)</option>
                <option value="primary_release_date.asc">Release Date (Oldest)</option>
                <option value="vote_average.desc">Highest Rated</option>
                <option value="revenue.desc">Highest Grossing</option>
            </select>
"""

# Insert sort_select right after year select
content = re.sub(r'(<select id="year".*?</select>\s*)', r'\1' + sort_select, content, flags=re.DOTALL)

with open(filepath, 'w') as f:
    f.write(content)

print("movie html updated")

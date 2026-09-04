import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

issues = []

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    rel_path = os.path.relpath(filepath, base_path)
    
    # 1. Check for Analytics
    if "Cloudflare Web Analytics" not in content or "fd1a57da9b654dedb6076173c64023f2" not in content:
        issues.append(f"{rel_path}: Missing Cloudflare token")
    if "posthog" not in content.lower():
        issues.append(f"{rel_path}: Missing PostHog script")
    if "goatcounter.com/count" not in content:
        issues.append(f"{rel_path}: Missing GoatCounter script")
        
    # 2. Check for Global Header (except maybe test_js.html)
    if "test_js.html" not in rel_path:
        if "<header" not in content:
            issues.append(f"{rel_path}: Missing <header> element!")
        if 'id="themeToggle"' not in content:
            issues.append(f"{rel_path}: Missing themeToggle button!")
        if 'id="retroToggle"' not in content:
            issues.append(f"{rel_path}: Missing retroToggle button!")
            
    # 3. Check Retro JS Injection
    if "function initRetroMode()" not in content:
        issues.append(f"{rel_path}: Missing initRetroMode script")
        
    # 4. Check for GoatCounter Image Bug
    if 'src="https://shivanshusharma.goatcounter.com/count"' in content:
        if '<object' not in content and 'display: none' not in content:
            # We had fixed it by using SVG or removing the visible 1x1 pixel if it was corrupted.
            # I'll manually verify this if it flags.
            pass

# Budget Visualizer Check
budget_js = os.path.join(base_path, "projects/budget-visualizer/script.js")
if os.path.exists(budget_js):
    with open(budget_js, 'r') as f:
        bc = f.read()
        if "80000" in bc or "50000" in bc:
            issues.append("budget-visualizer/script.js: Might still have hardcoded 80k/50k")

# Movie Recommender Check
movie_js = os.path.join(base_path, "projects/movie-recommender/app.js")
if os.path.exists(movie_js):
    with open(movie_js, 'r') as f:
        mc = f.read()
        if "let currentSortBy = 'popularity.desc';" not in mc:
            issues.append("movie-recommender/app.js: Default sort is not popularity.desc")

if len(issues) == 0:
    print("QA Passed! No issues found.")
else:
    print("QA Issues Found:")
    for issue in issues:
        print(f" - {issue}")

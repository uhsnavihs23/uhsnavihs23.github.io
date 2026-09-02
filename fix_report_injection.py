import os

def fix_file(filepath, search_str, replacement_str):
    with open(filepath, 'r') as f:
        content = f.read()
    content = content.replace(search_str, replacement_str)
    with open(filepath, 'w') as f:
        f.write(content)

back_btn = '<a href="../../index.html" style="display:inline-flex; align-items:center; color:white; text-decoration:none; margin-bottom:1rem; font-size:0.9rem; opacity:0.8; transition:opacity 0.2s;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.8">&larr; Back to Projects</a>'

# Campus Energy
fix_file("projects/data-analyst-projects/campus-electricity/index.html", 
         '<div class="header-content">', 
         f'<div class="header-content">\n            {back_btn}')

# Food Delivery
fix_file("projects/data-analyst-projects/food-delivery-analytics/index.html", 
         '<div class="dashboard-header">', 
         f'<div class="dashboard-header">\n            {back_btn}')

# Customer Shopping
fix_file("projects/data-analyst-projects/project-1-customer-shopping-trends-analysis/index.html", 
         '<div class=navbar-header>', 
         f'<div class=navbar-header>\n            {back_btn}')


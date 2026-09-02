import re

with open('projects/political-intel/index.html', 'r') as f:
    content = f.read()

# Update the filter line to explicitly exclude Devanagari script
target_line = "allStories = allStories.filter(s => s.section !== 'UP_Focus' && s.report_category !== 'UP_Focus');"
replacement = r"allStories = allStories.filter(s => s.section !== 'UP_Focus' && s.report_category !== 'UP_Focus' && !/[\u0900-\u097F]/.test(s.title));"

content = content.replace(target_line, replacement)

with open('projects/political-intel/index.html', 'w') as f:
    f.write(content)

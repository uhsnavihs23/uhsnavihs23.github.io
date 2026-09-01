import re

with open('./projects/movie-recommender/index.html', 'r') as f:
    content = f.read()

# Fix the multiple main tags
content = re.sub(r'<main class="flex-grow flex justify-center items-center py-12 px-4">\n\n<main', '<main', content)
content = re.sub(r'<main class="flex-grow flex justify-center items-center py-12 px-4">\n\n<div', '<main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">\n<div', content)

# Fix the script and css paths
content = content.replace('<link rel="stylesheet" href="">', '<link rel="stylesheet" href="styles.css">')
content = content.replace('<script src=""></script>', '<script src="app.js"></script>')

# Just to be sure, let's just do a clean replace for the multiple mains
content = re.sub(r'<main.*?</header>', '</header>', content, flags=re.DOTALL) # remove anything between header and the real main
content = content.replace('</header>\n\n<main class="flex-grow flex justify-center items-center py-12 px-4">\n\n<main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">', '</header>\n<main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">')
content = content.replace('</header>\n<main class="flex-grow flex justify-center items-center py-12 px-4">', '</header>\n<main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">')
content = re.sub(r'<main.*?>\s*<main.*?>', '<main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">', content)

with open('./projects/movie-recommender/index.html', 'w') as f:
    f.write(content)


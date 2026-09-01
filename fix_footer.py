from tailwind_redesign import get_footer

with open('./projects/movie-recommender/index.html', 'r') as f:
    content = f.read()

if '</footer>' not in content:
    footer = get_footer(2)
    content = content.replace('</body>', footer + '\n</body>')
    content = content.replace('</html>', '</body>\n</html>')
    
    with open('./projects/movie-recommender/index.html', 'w') as f:
        f.write(content)

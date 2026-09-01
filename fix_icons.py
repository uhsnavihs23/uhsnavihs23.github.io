with open('about.html', 'r') as f:
    content = f.read()

# 1. Fix Jupyter (replace skillicons jupyter with simpleicons jupyter)
content = content.replace(
    '<img src="https://skillicons.dev/icons?i=jupyter" alt="Jupyter" class="h-10 w-10 hover:scale-110 transition-transform hover:shadow-lg rounded-xl" title="Jupyter">',
    '''<div class="h-10 w-10 bg-white rounded-xl shadow-sm border border-gray-100 flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Jupyter">
                        <img src="https://cdn.simpleicons.org/jupyter/F37626" alt="Jupyter" class="h-6 w-6">
                    </div>'''
)

# 2. Fix Microsoft (replace 404 simpleicons with inline SVG)
ms_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-6 w-6"><path fill="#f25022" d="M11.4 0H0v11.4h11.4z"/><path fill="#7fba00" d="M24 0H12.6v11.4H24z"/><path fill="#00a4ef" d="M11.4 12.6H0V24h11.4z"/><path fill="#ffb900" d="M24 12.6H12.6V24H24z"/></svg>'''
content = content.replace(
    '<img src="https://cdn.simpleicons.org/microsoft/5E5E5E" alt="MS Suite" class="h-6 w-6">',
    ms_svg
)

# 3. Fix Power BI (replace 404 simpleicons with inline SVG)
pbi_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-6 w-6"><path fill="#E6AD10" d="M8.644 19.851v-6.315H4.212v6.315h4.432z"/><path fill="#F2C811" d="M15.344 19.851v-12.63h-4.433v12.63h4.433z"/><path fill="#F9E076" d="M22.043 19.851V0h-4.432v19.851h4.432z"/></svg>'''
content = content.replace(
    '<img src="https://cdn.simpleicons.org/powerbi/F2C811" alt="Power BI" class="h-6 w-6">',
    pbi_svg
)

with open('about.html', 'w') as f:
    f.write(content)

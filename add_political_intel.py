with open('projects/index.html', 'r') as f:
    content = f.read()

new_card = """
                <div class="bg-cardBg p-6 rounded-xl border border-borderColor shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Global Intelligence Dashboard</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">A live dashboard aggregating real-time geopolitical developments and strategic intelligence from global news feeds.</p>
                    <a href="./political-intel/index.html" class="text-accent font-medium hover:underline mt-auto">View Dashboard &rarr;</a>
                </div>
"""

# Insert it in the Data Analytics section.
# The Data Analytics section has:
# <h2 class="text-2xl font-bold text-primary">Data Analytics</h2>
# <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
# Let's insert it right after the grid opens!

content = content.replace(
    '<h2 class="text-2xl font-bold text-primary">Data Analytics</h2>\n                <div class="h-px bg-gray-200 flex-grow ml-6"></div>\n            </div>\n            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">',
    '<h2 class="text-2xl font-bold text-primary">Data Analytics</h2>\n                <div class="h-px bg-gray-200 flex-grow ml-6"></div>\n            </div>\n            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">\n' + new_card
)

with open('projects/index.html', 'w') as f:
    f.write(content)


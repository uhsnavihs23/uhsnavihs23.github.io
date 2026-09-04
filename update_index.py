with open('index.html', 'r') as f:
    content = f.read()

import re

# 1. Update Bio
old_bio = "I transform raw data into structured insights, analyze urban governance, and build elegant web applications."
new_bio = "I transform raw data into structured insights, explore public policy, and build elegant web applications."
content = content.replace(old_bio, new_bio)

# 2. Update Featured Work Header
content = content.replace(">Featured Work<", ">Featured Projects<")

# 3. Update the 3 Cards
new_cards = """<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Card 1: Data Analytics -->
                    <a href="./projects/data-analyst-projects/campus-electricity/index.html" class="group block h-full bg-bgColor rounded-lg overflow-hidden border border-borderColor hover:shadow-md transition-all duration-300 transform hover:-translate-y-1">
                        <div class="h-48 bg-gray-200 overflow-hidden relative">
                            <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&q=80&w=800" alt="Campus Electricity" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                            <span class="absolute bottom-4 left-4 px-3 py-1 bg-blue-500 text-white text-xs font-bold rounded-full uppercase tracking-wide">Data Analytics</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-primary mb-2 group-hover:text-accent transition-colors">Campus Electricity Optimization</h3>
                            <p class="text-secondary text-sm leading-relaxed">End-to-end analysis of campus energy data to discover usage patterns and propose efficiency optimizations.</p>
                        </div>
                    </a>

                    <!-- Card 2: Web Applications -->
                    <a href="./projects/ambient-noise/index.html" class="group block h-full bg-bgColor rounded-lg overflow-hidden border border-borderColor hover:shadow-md transition-all duration-300 transform hover:-translate-y-1">
                        <div class="h-48 bg-gray-200 overflow-hidden relative">
                            <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&q=80&w=800" alt="Ambient Noise Mixer" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                            <span class="absolute bottom-4 left-4 px-3 py-1 bg-emerald-500 text-white text-xs font-bold rounded-full uppercase tracking-wide">Web App</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-primary mb-2 group-hover:text-accent transition-colors">Deep Work Ambient Mixer</h3>
                            <p class="text-secondary text-sm leading-relaxed">A sleek audio mixer with customizable ambient soundscapes (Rain, Cafe, Thunder) to aid focus.</p>
                        </div>
                    </a>

                    <!-- Card 3: Policy & Writing -->
                    <a href="./projects/urban-governance.html" class="group block h-full bg-bgColor rounded-lg overflow-hidden border border-borderColor hover:shadow-md transition-all duration-300 transform hover:-translate-y-1">
                        <div class="h-48 bg-gray-200 overflow-hidden relative">
                            <img src="https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&q=80&w=800" alt="Urban Governance" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                            <span class="absolute bottom-4 left-4 px-3 py-1 bg-amber-500 text-white text-xs font-bold rounded-full uppercase tracking-wide">Policy</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-primary mb-2 group-hover:text-accent transition-colors">Urban Governance in India</h3>
                            <p class="text-secondary text-sm leading-relaxed">A structural analysis of what's broken in urban governance and how cities can be fixed from the ground up.</p>
                        </div>
                    </a>
                </div>"""

content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-8">.*?</div>\s*<div class="text-center mt-12">', new_cards + '\n                <div class="text-center mt-12">', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)


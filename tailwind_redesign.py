import os
import glob
import re

# Tailwind Global Config & Header/Footer
def get_tailwind_head(title, depth):
    prefix = '../' * depth if depth > 0 else './'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Shivanshu Sharma</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{ primary: '#0f172a', secondary: '#475569', accent: '#3b82f6' }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }}
    </style>
</head>
<body class="bg-gray-50 text-primary flex flex-col min-h-screen">
'''

def get_header(depth, active='home'):
    prefix = '../' * depth if depth > 0 else './'
    
    def link_class(name):
        base = "text-sm font-medium transition-colors hover:text-accent"
        return f"{base} text-accent" if active == name else f"{base} text-secondary"

    return f'''
    <!-- Navbar -->
    <header class="sticky top-0 z-50 w-full backdrop-blur-md bg-white/80 border-b border-gray-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="{prefix}index.html" class="text-xl font-bold tracking-tight text-primary hover:text-accent transition-colors">Shivanshu Sharma</a>
            <nav class="flex gap-6">
                <a href="{prefix}index.html" class="{link_class('home')}">Home</a>
                <a href="{prefix}projects/index.html" class="{link_class('projects')}">Projects</a>
                <a href="{prefix}about.html" class="{link_class('about')}">About</a>
            </nav>
        </div>
    </header>
'''

def get_footer(depth):
    prefix = '../' * depth if depth > 0 else './'
    return f'''
    <!-- Footer -->
    <footer class="mt-auto border-t border-gray-200 bg-white py-8">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row justify-between items-center gap-4">
            <p class="text-sm text-secondary">© <span id="year"></span> Shivanshu Sharma. All rights reserved.</p>
            <div class="flex gap-4 items-center">
                <a href="https://23022000.goatcounter.com/" target="_blank" rel="noopener" class="opacity-70 hover:opacity-100 transition-opacity mr-2">
                    <img src="https://23022000.goatcounter.com/count?p=/&t=portfolio" width="auto" height="26" alt="Views">
                </a>
                <a href="https://github.com/uhsnavihs23" target="_blank" class="text-secondary hover:text-accent transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                </a>
                <a href="https://linkedin.com/in/shivanshu-sharma-2302" target="_blank" class="text-secondary hover:text-accent transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>
            </div>
        </div>
    </footer>
    <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
    <script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''

# 1. GENERATE INDEX.HTML (Home)
index_html = get_tailwind_head("Portfolio", 0) + get_header(0, 'home') + '''
    <main class="flex-grow">
        <!-- Hero Section -->
        <section class="max-w-5xl mx-auto px-4 sm:px-6 py-20 lg:py-32 flex flex-col-reverse md:flex-row items-center gap-12">
            <div class="flex-1 text-center md:text-left">
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-primary mb-6">
                    Strategy, Data <span class="text-accent">&</span> Policy
                </h1>
                <p class="text-lg text-secondary mb-8 max-w-2xl leading-relaxed">
                    I am a Strategy & Management Consultant and IIT Gandhinagar alumnus. I transform raw data into structured insights, analyze urban governance, and build elegant web applications.
                </p>
                <div class="flex flex-wrap justify-center md:justify-start gap-4">
                    <a href="./projects/index.html" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-accent hover:bg-blue-700 transition-colors shadow-sm">
                        View My Work
                    </a>
                    <a href="./about.html" class="inline-flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-lg text-primary bg-white hover:bg-gray-50 transition-colors shadow-sm">
                        More About Me
                    </a>
                </div>
            </div>
            <div class="flex-shrink-0 relative">
                <div class="absolute inset-0 bg-blue-100 rounded-full blur-3xl opacity-50 -z-10"></div>
                <img src="https://avatars.githubusercontent.com/u/67822353?v=4" alt="Shivanshu Sharma" class="w-48 h-48 sm:w-64 sm:h-64 rounded-full object-cover border-4 border-white shadow-xl">
            </div>
        </section>

        <!-- Featured Projects -->
        <section class="bg-white py-20 border-t border-gray-200">
            <div class="max-w-5xl mx-auto px-4 sm:px-6">
                <h2 class="text-3xl font-bold text-primary mb-2 text-center">Featured Work</h2>
                <div class="w-16 h-1 bg-accent mx-auto rounded mb-12"></div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Card 1 -->
                    <a href="./projects/market-tracker/index.html" class="group block h-full bg-gray-50 rounded-2xl overflow-hidden border border-gray-200 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                        <div class="h-48 bg-gray-200 overflow-hidden relative">
                            <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&q=80&w=800" alt="Market Tracker" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                            <span class="absolute bottom-4 left-4 px-3 py-1 bg-blue-500 text-white text-xs font-bold rounded-full uppercase tracking-wide">Data Analytics</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-primary mb-2 group-hover:text-accent transition-colors">India Market Tracker</h3>
                            <p class="text-secondary text-sm leading-relaxed">Live prices and 7-day trend charts for Nifty 50, Sensex, and Gold. Built without needing any API keys.</p>
                        </div>
                    </a>

                    <!-- Card 2 -->
                    <a href="./projects/urban-governance.html" class="group block h-full bg-gray-50 rounded-2xl overflow-hidden border border-gray-200 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
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

                    <!-- Card 3 -->
                    <a href="./projects/image-filter-app/index.html" class="group block h-full bg-gray-50 rounded-2xl overflow-hidden border border-gray-200 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                        <div class="h-48 bg-gray-200 overflow-hidden relative">
                            <img src="https://images.unsplash.com/photo-1558655146-d09347e92766?auto=format&fit=crop&q=80&w=800" alt="Image Editor" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                            <span class="absolute bottom-4 left-4 px-3 py-1 bg-emerald-500 text-white text-xs font-bold rounded-full uppercase tracking-wide">Web App</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-primary mb-2 group-hover:text-accent transition-colors">Image Editor Studio</h3>
                            <p class="text-secondary text-sm leading-relaxed">Browser-based image editing tool with filters, adjustments, cropping, and multi-format export support.</p>
                        </div>
                    </a>
                </div>
                
                <div class="text-center mt-12">
                    <a href="./projects/index.html" class="inline-flex items-center justify-center font-medium text-accent hover:text-blue-700 group">
                        Explore all projects 
                        <svg class="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
        </section>
    </main>
''' + get_footer(0)
with open('./index.html', 'w') as f: f.write(index_html)


# 2. GENERATE ABOUT.HTML
about_html = get_tailwind_head("About", 0) + get_header(0, 'about') + '''
    <main class="flex-grow max-w-4xl mx-auto px-4 sm:px-6 py-20">
        <h1 class="text-4xl font-extrabold tracking-tight text-primary mb-8 text-center sm:text-left">About Me</h1>
        
        <div class="flex flex-col sm:flex-row gap-12 items-start">
            <div class="sm:w-1/3 w-full flex justify-center sm:justify-start">
                <img src="https://avatars.githubusercontent.com/u/67822353?v=4" alt="Shivanshu Sharma" class="w-48 h-48 rounded-2xl object-cover shadow-lg border border-gray-200">
            </div>
            
            <div class="sm:w-2/3 prose prose-lg prose-blue max-w-none text-secondary">
                <p class="text-xl font-medium text-primary mb-4">Hello, I'm <span class="font-bold">Shivanshu Sharma</span>. I am a Strategy & Management Consultant, and an alumnus of IIT Gandhinagar.</p>
                <p class="mb-4">My work revolves around the intersection of data, policy, and technology. I am passionate about transforming raw data into structured insights, analyzing urban governance, and building functional web applications.</p>
                <p class="mb-6">In my projects, I aim to create simple, effective solutions—whether that means finding actionable insights in a dataset, analyzing complex policy issues, or developing intuitive browser-based tools.</p>
                
                <div class="flex flex-wrap gap-4 mt-8">
                    <a href="mailto:shivanshu.sharma0023@gmail.com" class="px-5 py-2.5 bg-primary text-white font-medium rounded-lg hover:bg-gray-800 transition-colors">Email Me</a>
                    <a href="https://github.com/uhsnavihs23" target="_blank" class="px-5 py-2.5 bg-white border border-gray-300 text-primary font-medium rounded-lg hover:bg-gray-50 transition-colors">GitHub Profile</a>
                    <a href="https://linkedin.com/in/shivanshu-sharma-2302" target="_blank" class="px-5 py-2.5 bg-white border border-gray-300 text-primary font-medium rounded-lg hover:bg-gray-50 transition-colors">LinkedIn</a>
                </div>
            </div>
        </div>
    </main>
''' + get_footer(0)
with open('./about.html', 'w') as f: f.write(about_html)


# 3. GENERATE PROJECTS/INDEX.HTML
proj_idx = get_tailwind_head("Projects", 1) + get_header(1, 'projects') + '''
    <main class="flex-grow max-w-5xl mx-auto px-4 sm:px-6 py-20 w-full">
        <div class="text-center mb-16">
            <h1 class="text-4xl font-extrabold tracking-tight text-primary mb-4">All Projects</h1>
            <p class="text-lg text-secondary max-w-2xl mx-auto">A comprehensive collection of my work spanning Data Analytics, Web Applications, and Policy Research.</p>
        </div>

        <!-- Data Analytics -->
        <section class="mb-20">
            <div class="flex items-center mb-8">
                <h2 class="text-2xl font-bold text-primary">Data Analytics</h2>
                <div class="h-px bg-gray-200 flex-grow ml-6"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Cohort Analysis -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Customer Cohort & Retention</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">End-to-end Python analysis on 25k+ e-commerce transactions to map user retention across cohorts using Plotly.</p>
                    <a href="./data-analyst-projects/cohort-retention/index.html" class="text-accent font-medium hover:underline mt-auto">View Project &rarr;</a>
                </div>
                <!-- Campus Electricity -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Campus Electricity Analysis</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Identified a 10% reduction potential (13 lakh kWh/year) in campus electricity consumption.</p>
                    <a href="./data-analyst-projects/campus-electricity/index.html" class="text-accent font-medium hover:underline mt-auto">View Project &rarr;</a>
                </div>
                <!-- Food Delivery -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Food Delivery Analytics</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">End-to-end analysis of a food delivery dataset exploring customer behaviour and revenue insights.</p>
                    <a href="./data-analyst-projects/food-delivery-analytics/index.html" class="text-accent font-medium hover:underline mt-auto">View Project &rarr;</a>
                </div>
                <!-- Shopping Trends -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Customer Shopping Trends</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Analysis of consumer shopping patterns with actionable segmentation and visual dashboards.</p>
                    <a href="./data-analyst-projects/project-1-customer-shopping-trends-analysis/index.html" class="text-accent font-medium hover:underline mt-auto">View Project &rarr;</a>
                </div>
            </div>
        </section>

        <!-- Web Apps -->
        <section class="mb-20">
            <div class="flex items-center mb-8">
                <h2 class="text-2xl font-bold text-primary">Web Applications & Utilities</h2>
                <div class="h-px bg-gray-200 flex-grow ml-6"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- NEW: Pomodoro Timer -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Pomodoro Focus Room</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">A sleek, distraction-free productivity timer with Pomodoro, short, and long break intervals.</p>
                    <a href="./pomodoro-timer/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
                <!-- NEW: Budget Visualizer -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Personal Budget Visualizer</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Input your income and expenses to instantly generate a breakdown of your cash flow using Chart.js.</p>
                    <a href="./budget-visualizer/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
                <!-- Market Tracker -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">India Market Tracker</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Live prices and 7-day trend charts for Nifty 50, Sensex, and Gold. No API key needed.</p>
                    <a href="./market-tracker/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Image Editor Web App</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Browser-based image editing tool with filters, adjustments, and multi-format export support.</p>
                    <a href="./image-filter-app/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Movie Recommender</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Recommendation engine — search, discover, and explore films by genre and rating.</p>
                    <a href="./movie-recommender/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">GitHub Profile Finder</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Analytics dashboard to search and explore GitHub user profiles, repos, and language breakdowns.</p>
                    <a href="./github-profile-finder/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">News Hub</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Aggregates live news headlines across categories using a stable RSS-to-JSON aggregator.</p>
                    <a href="./news-app/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
            </div>
        </section>

        <!-- Policy -->
        <section>
            <div class="flex items-center mb-8">
                <h2 class="text-2xl font-bold text-primary">Policy & Writing</h2>
                <div class="h-px bg-gray-200 flex-grow ml-6"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Urban Governance in India</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">A structural analysis of what's broken in urban governance and how cities can be fixed from the ground up.</p>
                    <a href="./urban-governance.html" class="text-accent font-medium hover:underline mt-auto">Read Article &rarr;</a>
                </div>
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">India Policy Brief Generator</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Generate structured policy briefs from live Indian news headlines on any topic.</p>
                    <a href="./policy-brief-generator/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>
                </div>
            </div>
        </section>
    </main>
''' + get_footer(1)
with open('./projects/index.html', 'w') as f: f.write(proj_idx)

print("Regenerated core pages with Tailwind CSS.")

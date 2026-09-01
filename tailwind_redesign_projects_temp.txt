from tailwind_redesign import get_tailwind_head, get_header, get_footer

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
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col border-l-4 border-l-accent">
                    <h3 class="text-xl font-bold text-primary mb-2">Customer Cohort & Retention</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">End-to-end Python analysis on 25k+ e-commerce transactions to map user retention across cohorts using Plotly.</p>
                    <a href="./data-analyst-projects/cohort-retention/index.html" class="text-accent font-bold hover:underline mt-auto flex items-center">
                        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                        View Case Study
                    </a>
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
                <h2 class="text-2xl font-bold text-primary">Web Applications</h2>
                <div class="h-px bg-gray-200 flex-grow ml-6"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Market Tracker -->
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">India Market Tracker</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Live prices and 7-day trend charts for Nifty 50, Sensex, and Gold. No API key needed.</p>
                    <a href="./market-tracker/index.html" class="text-accent font-medium hover:underline mt-auto flex items-center"><span class="w-2 h-2 rounded-full bg-emerald-500 mr-2 animate-pulse"></span> View Live Dashboard &rarr;</a>
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
                    <a href="./github-profile-finder/index.html" class="text-accent font-medium hover:underline mt-auto">View Dashboard &rarr;</a>
                </div>
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">News Hub</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Aggregates live news headlines across categories using a stable RSS-to-JSON aggregator.</p>
                    <a href="./news-app/index.html" class="text-accent font-medium hover:underline mt-auto">View Hub &rarr;</a>
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
                    <a href="./policy-brief-generator/index.html" class="text-accent font-medium hover:underline mt-auto">Try Tool &rarr;</a>
                </div>
            </div>
        </section>
    </main>
''' + get_footer(1)

with open('./projects/index.html', 'w') as f:
    f.write(proj_idx)


import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Shivanshu Sharma</title>
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'sans-serif'] },
                    colors: { 
                        primary: 'var(--text-primary)', 
                        secondary: 'var(--text-secondary)', 
                        accent: 'var(--accent-color)',
                        bgColor: 'var(--bg-color)',
                        cardBg: 'var(--card-bg)',
                        borderColor: 'var(--border-color)',
                        navBg: 'var(--nav-bg)'
                    }
                }
            }
        }
    </script>
    <style>
        body { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
        :root {
            --bg-color: #f9fafb;
            --card-bg: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --border-color: #e5e7eb;
            --accent-color: #3b82f6;
            --nav-bg: rgba(255, 255, 255, 0.8);
        }
        html.dark {
            --bg-color: #18181b;
            --card-bg: #27272a;
            --text-primary: #f4f4f5;
            --text-secondary: #d4d4d8;
            --border-color: #3f3f46;
            --accent-color: #2dd4bf;
            --nav-bg: rgba(24, 24, 27, 0.8);
        }
    </style>
</head>
<body class="bg-bgColor text-primary flex flex-col min-h-screen">
    <!-- Header -->
    <header class="sticky top-0 z-50 w-full backdrop-blur-md bg-navBg border-b border-borderColor">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="../index.html" class="text-xl font-bold tracking-tight text-primary hover:text-accent transition-colors">Shivanshu Sharma</a>
            <nav class="flex gap-6 items-center">
                <a href="../index.html" class="text-sm font-medium transition-colors hover:text-accent text-secondary">Home</a>
                <a href="../projects/index.html" class="text-sm font-medium transition-colors hover:text-accent text-accent">Projects</a>
                <a href="../about.html" class="text-sm font-medium transition-colors hover:text-accent text-secondary">About</a>
                <button id="themeToggle" class="ml-4 p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-secondary">
                    <svg id="themeIconLight" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
                    <svg id="themeIconDark" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
                </button>
            </nav>
        </div>
    </header>

    <main class="flex-grow max-w-4xl mx-auto px-4 sm:px-6 py-20 w-full">
        <a href="index.html" class="inline-flex items-center text-sm font-medium text-secondary hover:text-accent mb-8 transition-colors">
            <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>

        <article class="bg-cardBg p-8 rounded-2xl shadow-sm border border-borderColor">
            <header class="mb-10 border-b border-borderColor pb-8">
                <div class="inline-block px-3 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full uppercase tracking-wide mb-4">Policy & Writing</div>
                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-primary mb-4 leading-tight">{title}</h1>
                <p class="text-lg text-secondary">{subtitle}</p>
            </header>
            
            <div class="prose prose-lg prose-blue max-w-none">
                {content}
            </div>
        </article>
    </main>

    <!-- Footer -->
    <footer class="mt-auto border-t border-borderColor bg-cardBg py-8">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row justify-between items-center gap-4">
            <p class="text-sm text-secondary">© <span id="footerYear"></span> Shivanshu Sharma. All rights reserved.</p>
            <div class="flex gap-4 items-center">
                <a href="https://23022000.goatcounter.com/" target="_blank" rel="noopener" class="opacity-70 hover:opacity-100 transition-opacity mr-2">
                    <img src="https://23022000.goatcounter.com/count?p=/&t=portfolio" width="auto" height="26" alt="Views">
                </a>
                <a href="https://github.com/shivanshu-sharma" target="_blank" class="text-secondary hover:text-accent transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                </a>
            </div>
        </div>
    </footer>

    <!-- Theme Script -->
    <script>
        const html = document.documentElement;
        const themeToggle = document.getElementById('themeToggle');
        const themeIconLight = document.getElementById('themeIconLight');
        const themeIconDark = document.getElementById('themeIconDark');
        
        function setTheme(isDark) {
            if (isDark) {
                html.classList.add('dark');
                themeIconLight.classList.remove('hidden');
                themeIconDark.classList.add('hidden');
                localStorage.setItem('theme', 'dark');
            } else {
                html.classList.remove('dark');
                themeIconLight.classList.add('hidden');
                themeIconDark.classList.remove('hidden');
                localStorage.setItem('theme', 'light');
            }
        }
        if (localStorage.getItem('theme') === 'dark') { setTheme(true); } else { setTheme(false); }
        if (themeToggle) { themeToggle.addEventListener('click', () => { setTheme(!html.classList.contains('dark')); }); }
        
        document.getElementById('footerYear').textContent = new Date().getFullYear();
    </script>
    <script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>"""

projects = [
    {
        "file": "projects/esg-strategic-advantage.html",
        "title": "ESG Reporting as a Strategic Advantage",
        "subtitle": "Transforming compliance mandates into long-term corporate value and risk mitigation.",
        "content": """
                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">The Compliance Trap</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">For many organizations, Environmental, Social, and Governance (ESG) metrics are viewed primarily through the lens of compliance. Driven by increasing regulatory pressure—such as the SEC’s climate disclosure rules or the EU’s CSRD—companies often treat ESG reporting as an annual box-ticking exercise. However, restricting ESG to a purely defensive compliance mechanism leaves massive strategic value on the table.</p>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Data-Driven Value Creation</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">Advanced ESG frameworks require the deep integration of operational data. When organizations digitize their supply chains to track Scope 3 emissions, they inadvertently uncover inefficiencies in logistics and procurement. The same data required to appease regulators can be leveraged to streamline operations, reduce resource waste, and lower energy expenditures.</p>

                <div class="border-l-4 border-emerald-500 bg-emerald-50 p-6 my-8 rounded-r-lg text-secondary shadow-sm">
                    <p class="italic text-lg mb-0">"The companies that will lead the next decade are those that weaponize their ESG data to drive operational alpha, rather than just filing it away in an annual report."</p>
                </div>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Access to Capital & Talent</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">Beyond operational efficiency, robust ESG reporting acts as a powerful signal to capital markets. Institutional investors are increasingly weighting ESG maturity as a proxy for management quality and long-term risk resilience. Furthermore, in highly competitive labor markets, authentic corporate governance and demonstrable social commitments have become critical differentiators for attracting top-tier talent.</p>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Strategic Recommendations</h2>
                <ul class="list-disc pl-6 text-lg text-secondary leading-relaxed mb-6 space-y-2">
                    <li><strong>Integrate Financial and ESG Data:</strong> Dissolve the silos between sustainability teams and the CFO’s office.</li>
                    <li><strong>Proactive Materiality Assessments:</strong> Focus reporting strictly on the ESG factors that materially impact your specific business model.</li>
                    <li><strong>Leverage Technology:</strong> Adopt automated data pipelines (like n8n or Power BI) to reduce the manual overhead of data collection and shift focus to analytics.</li>
                </ul>
        """
    },
    {
        "file": "projects/healthcare-infrastructure-stress.html",
        "title": "Healthcare Infrastructure Stress Testing",
        "subtitle": "Analyzing urban vulnerability and hospital bed capacity using demographic density mapping.",
        "content": """
                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">The Urban Vulnerability Equation</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">The rapid urbanization of tier-1 and tier-2 Indian cities has drastically outpaced the development of corresponding public health infrastructure. This structural deficit is rarely visible during normal operational periods but catastrophic during exogenous shocks—as observed during recent global health crises. To prevent systemic failure, civic planners must shift from reactive capacity building to proactive stress testing.</p>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Methodology for Spatial Analysis</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">Effective stress testing requires overlapping geospatial hospital capacity data (ICU beds, oxygen supply lines, trauma centers) with granular demographic density maps. By weighting populations based on age and socio-economic vulnerability indices, we can identify "healthcare deserts"—highly populated zones where the ratio of residents to emergency medical facilities falls below critical thresholds.</p>

                <div class="border-l-4 border-red-500 bg-red-50 p-6 my-8 rounded-r-lg text-secondary shadow-sm">
                    <p class="italic text-lg mb-0">Analysis indicates that merely increasing total bed count is inefficient if the spatial distribution of those beds forces critically ill populations into transport bottlenecks.</p>
                </div>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Policy Interventions</h2>
                <ul class="list-disc pl-6 text-lg text-secondary leading-relaxed mb-6 space-y-2">
                    <li><strong>Decentralized Triage Hubs:</strong> Establish modular, low-acuity care centers in high-density zones to prevent primary hospital overflow.</li>
                    <li><strong>Real-Time Capacity Dashboards:</strong> Mandate API integrations for private and public hospitals to feed live bed availability into a centralized municipal grid.</li>
                    <li><strong>Zoning Reforms:</strong> Fast-track permitting for medical infrastructure development in identified healthcare deserts.</li>
                </ul>
        """
    },
    {
        "file": "projects/urban-mobility-divide.html",
        "title": "The Urban Mobility Divide",
        "subtitle": "How unequal access to public transit restricts economic mobility in metropolitan areas.",
        "content": """
                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Transit as Economic Infrastructure</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">Public transportation is often evaluated purely on operational metrics like farebox recovery ratios or daily ridership. However, this ignores its most critical function: serving as the physical conduit for economic mobility. In major metropolitan areas, the inability to reliably and affordably access employment centers creates a localized poverty trap for populations living on the urban periphery.</p>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">The Last-Mile Penalty</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">While high-capacity transit projects (like metro rails) receive the bulk of capital funding, they frequently fail to address the "last-mile" problem. Lower-income communities often reside outside the immediate catchment area of these premium transit hubs. Consequently, they are forced to rely on fragmented, informal transit networks (shared autos, unregulated mini-buses) which impose a significant "time-tax" and safety risk.</p>

                <div class="border-l-4 border-blue-500 bg-blue-50 p-6 my-8 rounded-r-lg text-secondary shadow-sm">
                    <p class="italic text-lg mb-0">A 30-minute increase in daily commute time correlates strongly with reduced workforce participation, particularly among women in the informal economy.</p>
                </div>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Data-Driven Routing</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">To bridge this divide, civic transport authorities must pivot toward data-driven dynamic routing. By analyzing origin-destination matrices generated from mobile network data and digital ticketing, municipalities can deploy flexible, micro-transit bus routes that adapt to the actual commuting patterns of underserved neighborhoods, rather than forcing populations to adapt to rigid legacy routes.</p>
        """
    },
    {
        "file": "projects/renewable-subsidies.html",
        "title": "The Economics of Renewable Subsidies",
        "subtitle": "Evaluating the efficacy of government incentives in driving solar adoption.",
        "content": """
                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">The Subsidy Paradox</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">In the global push toward decarbonization, direct consumer subsidies and tax incentives have been the primary policy levers used to accelerate the adoption of residential and commercial solar panels. However, an economic analysis of these subsidies often reveals a paradox: they frequently subsidize early adopters who would have purchased the technology regardless, leading to inefficient capital allocation.</p>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Market Distortion vs. Market Making</h2>
                <p class="text-lg text-secondary leading-relaxed mb-6">While subsidies are essential for crossing the "valley of death" in early technology lifecycles, prolonged subsidies can distort local markets. They can artificially inflate hardware costs (as installers absorb the subsidy margin) and delay grid-level investments. The focus must shift from subsidizing the hardware to subsidizing the financing mechanisms—such as green bonds and low-interest transition loans.</p>

                <div class="border-l-4 border-yellow-500 bg-yellow-50 p-6 my-8 rounded-r-lg text-secondary shadow-sm">
                    <p class="italic text-lg mb-0">The most effective policy is not a perpetual discount, but a clearly communicated, phased step-down of incentives that forces the industry to achieve true cost parity.</p>
                </div>

                <h2 class="text-2xl font-bold text-primary mt-12 mb-4">Realigning Policy Focus</h2>
                <ul class="list-disc pl-6 text-lg text-secondary leading-relaxed mb-6 space-y-2">
                    <li><strong>Targeted Incentives:</strong> Shift subsidies away from high-income residential brackets and redirect them toward commercial and industrial (C&I) sectors where scale yields higher carbon reduction per dollar.</li>
                    <li><strong>Grid Infrastructure:</strong> Reallocate subsidy budgets to upgrade grid storage and transmission capacity, which is rapidly becoming the actual bottleneck for renewable integration.</li>
                    <li><strong>Performance-Based Tariffs:</strong> Implement feed-in tariffs that reward actual energy generation and grid-balancing during peak hours, rather than flat installation rebates.</li>
                </ul>
        """
    }
]

for p in projects:
    html = template.replace("{title}", p["title"]).replace("{subtitle}", p["subtitle"]).replace("{content}", p["content"])
    with open(p["file"], 'w') as f:
        f.write(html)
        

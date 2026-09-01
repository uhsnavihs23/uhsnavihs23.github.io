import os
from tailwind_redesign import get_tailwind_head, get_header, get_footer

html = get_tailwind_head("Campus Electricity Consumption Analysis", 3) + get_header(3, 'projects') + '''
    <main class="flex-grow max-w-4xl mx-auto px-4 sm:px-6 py-20 w-full">
        <a href="../../index.html" class="inline-flex items-center text-sm font-medium text-secondary hover:text-accent mb-8 transition-colors">
            <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
        <article class="bg-white p-8 rounded-2xl shadow-sm border border-gray-200">
            <header class="mb-10 border-b border-gray-100 pb-8">
                <div class="inline-block px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase tracking-wide mb-4">Data Analytics</div>
                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-primary mb-4 leading-tight">Campus Electricity Consumption Analysis & Optimization</h1>
            </header>
            <div class="prose prose-lg prose-blue max-w-none text-secondary">
                <p class="text-lg leading-relaxed mb-6">This project presents a comprehensive analysis of campus electricity consumption data at IIT Gandhinagar over a span of 28 months, aiming to identify key consumption drivers and propose actionable strategies for energy optimisation.</p>

                <h2 class="text-2xl font-bold text-primary mt-10 mb-4">📈 Full Analysis Dashboard</h2>
                <p class="mb-6">Explore the interactive energy analysis dashboard detailing consumption anomalies and reduction potential:</p>

                <a href="../../../assets/reports/Campus_energy_analytics-IIT Gandhinagar.html" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-accent hover:bg-blue-700 transition-colors shadow-sm">
                    View Analysis Dashboard
                </a>
            </div>
        </article>
    </main>
''' + get_footer(3)

os.makedirs('./projects/data-analyst-projects/campus-electricity', exist_ok=True)
with open('./projects/data-analyst-projects/campus-electricity/index.html', 'w') as f:
    f.write(html)

print("Generated Campus Electricity Page.")

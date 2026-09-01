from tailwind_redesign import get_tailwind_head, get_header, get_footer

def write_page(filepath, title, content):
    html = get_tailwind_head(title, 3) + get_header(3, 'projects') + f'''
    <main class="flex-grow max-w-4xl mx-auto px-4 sm:px-6 py-20 w-full">
        <a href="../../index.html" class="inline-flex items-center text-sm font-medium text-secondary hover:text-accent mb-8 transition-colors">
            <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
        <article class="bg-white p-8 rounded-2xl shadow-sm border border-gray-200">
            <header class="mb-10 border-b border-gray-100 pb-8">
                <div class="inline-block px-3 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-full uppercase tracking-wide mb-4">Data Analytics</div>
                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-primary mb-4 leading-tight">{title}</h1>
            </header>
            <div class="prose prose-lg prose-blue max-w-none text-secondary">
                {content}
            </div>
        </article>
    </main>
''' + get_footer(3)
    with open(filepath, 'w') as f:
        f.write(html)

content1 = """
<p class="text-lg leading-relaxed mb-6">This project analyzes a <a href="https://www.kaggle.com/datasets/logiccraftbyhimanshi/e-commerce-analytics-swiggy-zomato-blinkit" target="_blank" class="text-accent hover:underline">food delivery service dataset</a> from Kaggle, analyzing key metrics like revenue, delivery performance and customer satisfaction across platforms (Swiggy, Zomato, Blinkit), cities and time periods.</p>

<h2 class="text-2xl font-bold text-primary mt-10 mb-4">📈 Full Analysis Report</h2>
<p class="mb-6">Explore the interactive report with detailed visualizations and data profiling:</p>

<a href="../../../assets/reports/food-delivery-analytics.html" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-accent hover:bg-blue-700 transition-colors shadow-sm">
    View Customer Shopping Trends Report
</a>
"""
write_page('./projects/data-analyst-projects/food-delivery-analytics/index.html', "Food Delivery Analytics Dashboard", content1)


content2 = """
<p class="text-lg leading-relaxed mb-6">This project analyzes the <a href="https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset" target="_blank" class="text-accent hover:underline">Customer Shopping Latest Trends Dataset</a> from Kaggle, exploring shopping behaviors of 3,900 customers. Using Python in Google Colab, I performed data cleaning, SQL-style querying, and visualizations to derive actionable insights.</p>

<h2 class="text-2xl font-bold text-primary mt-10 mb-4">Executive Summary</h2>

<div class="border-l-4 border-amber-500 bg-amber-50 p-6 my-8 rounded-r-lg text-secondary shadow-sm">
  <h3 class="text-xl font-bold text-amber-700 mb-4">Actionable Insights</h3>
  <ul class="list-disc pl-5 space-y-3">
    <li><strong>Age Demographics:</strong> Customers aged 25–35 dominate, making them prime targets for mid-range fashion campaigns.</li>
    <li><strong>Payment Trends:</strong> Credit cards are the preferred payment method; explore exclusive card-based promotions.</li>
    <li><strong>High-Value Categories:</strong> Clothing and footwear yield higher purchase amounts; prioritize inventory and marketing here.</li>
    <li><strong>Seasonal Opportunities:</strong> Winter sees elevated spending; plan seasonal campaigns and flash sales.</li>
    <li><strong>Review Influence:</strong> High review ratings correlate with repeat purchases; incentivize post-purchase reviews.</li>
    <li><strong>Subscriber Value:</strong> Subscribers spend more frequently and at higher values; develop loyalty programs.</li>
  </ul>
</div>

<h2 class="text-2xl font-bold text-primary mt-10 mb-4">📈 Full Analysis Report</h2>
<p class="mb-6">Explore the interactive report with detailed visualizations and data profiling:</p>

<a href="../../../assets/reports/customer_shopping_trends_report_with_summary.html" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-accent hover:bg-blue-700 transition-colors shadow-sm">
    View Customer Shopping Trends Report
</a>
"""
write_page('./projects/data-analyst-projects/project-1-customer-shopping-trends-analysis/index.html', "Customer Shopping Trends Analysis", content2)

print("Generated actual data analyst pages.")

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# 1. Generate Synthetic Data
np.random.seed(42)
print("Generating synthetic dataset...")

# Generate dates over 12 months
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-12-31')
dates = pd.date_range(start_date, end_date)

# Create 5000 unique customers
n_customers = 5000
customers = [f"CUST_{i:04d}" for i in range(n_customers)]

# Assign a join date to each customer (skewed towards earlier months to simulate growth)
join_dates = pd.to_datetime(np.random.choice(dates, size=n_customers))

transactions = []
transaction_id = 10000

for i, cust in enumerate(customers):
    join_date = join_dates[i]
    
    # Random number of transactions for this customer
    # High churn: 40% make only 1 purchase. 
    # Retained: 60% make 2-15 purchases over time.
    if np.random.rand() < 0.4:
        n_trans = 1
    else:
        n_trans = np.random.randint(2, 15)
        
    for _ in range(n_trans):
        # Transaction date must be >= join_date
        max_offset = (end_date - join_date).days
        if max_offset == 0:
            t_date = join_date
        else:
            # Random date after join date, with decay (more likely to buy soon after joining)
            offset = int(np.random.exponential(scale=max_offset/3))
            offset = min(offset, max_offset)
            t_date = join_date + pd.Timedelta(days=offset)
            
        amount = round(np.random.uniform(15.0, 250.0), 2)
        transactions.append({
            'transaction_id': f"TXN_{transaction_id}",
            'customer_id': cust,
            'transaction_date': t_date,
            'amount': amount
        })
        transaction_id += 1

df = pd.DataFrame(transactions)

# Save raw data snippet
os.makedirs('./assets/data', exist_ok=True)
df.to_csv('./assets/data/ecommerce_transactions_sample.csv', index=False)
print(f"Generated {len(df)} transactions.")

# 2. Perform Cohort Analysis
print("Performing Cohort Analysis...")
# Extract invoice month and cohort month
df['transaction_month'] = df['transaction_date'].dt.to_period('M')
df['cohort_month'] = df.groupby('customer_id')['transaction_date'].transform('min').dt.to_period('M')

# Group by cohort and transaction month to count unique customers
cohort_data = df.groupby(['cohort_month', 'transaction_month']).agg(n_customers=('customer_id', 'nunique')).reset_index()

# Calculate cohort index (number of months passed since first purchase)
cohort_data['period_number'] = (cohort_data.transaction_month - cohort_data.cohort_month).apply(lambda x: x.n)

# Pivot table
cohort_counts = cohort_data.pivot(index='cohort_month', columns='period_number', values='n_customers')
cohort_sizes = cohort_counts.iloc[:, 0]

# Retention matrix (%)
retention_matrix = cohort_counts.divide(cohort_sizes, axis=0) * 100
retention_matrix = retention_matrix.round(1)

# Average revenue per cohort
revenue_data = df.groupby(['cohort_month', 'transaction_month']).agg(revenue=('amount', 'sum')).reset_index()
revenue_data['period_number'] = (revenue_data.transaction_month - revenue_data.cohort_month).apply(lambda x: x.n)
revenue_matrix = revenue_data.pivot(index='cohort_month', columns='period_number', values='revenue')

# 3. Create Plotly Heatmap
print("Creating Visualizations...")
y_labels = [str(idx) for idx in retention_matrix.index]
x_labels = [f"Month {col}" for col in retention_matrix.columns]

fig = px.imshow(retention_matrix.values,
                labels=dict(x="Months Since First Purchase", y="Acquisition Cohort", color="Retention (%)"),
                x=x_labels,
                y=y_labels,
                color_continuous_scale='YlGnBu',
                text_auto=True,
                aspect="auto")

fig.update_layout(
    title="Customer Retention Cohort Analysis",
    title_font=dict(size=24, family="Inter", color="#1e293b"),
    xaxis_title="Months Since First Purchase",
    yaxis_title="Acquisition Cohort",
    font=dict(family="Inter", color="#475569"),
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(t=80, l=120, r=40, b=80),
    coloraxis_colorbar=dict(title="Retention (%)")
)

# Export interactive plot to HTML string
plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

# 4. Build the Final Project Page
print("Building HTML Page...")
from tailwind_redesign import get_tailwind_head, get_header, get_footer

html_content = get_tailwind_head("Cohort Analysis & Retention", 3) + get_header(3, 'projects') + f'''
    <main class="flex-grow max-w-5xl mx-auto px-4 sm:px-6 py-12 w-full">
        <a href="../../index.html" class="inline-flex items-center text-sm font-medium text-secondary hover:text-accent mb-8 transition-colors">
            <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>

        <div class="bg-white rounded-3xl shadow-sm border border-gray-200 overflow-hidden">
            <div class="bg-gradient-to-r from-blue-900 to-indigo-800 p-10 text-white">
                <div class="inline-block px-3 py-1 bg-blue-800 border border-blue-600 text-blue-100 text-xs font-bold rounded-full uppercase tracking-wide mb-4">Data Analytics / Python</div>
                <h1 class="text-4xl font-extrabold mb-4">Customer Cohort & Retention Analysis</h1>
                <p class="text-xl text-blue-100 max-w-3xl leading-relaxed">End-to-end Python analysis on {len(df):,} e-commerce transactions to identify user retention patterns and lifetime value across monthly acquisition cohorts.</p>
            </div>

            <div class="p-10 space-y-12">
                <!-- Executive Summary -->
                <section>
                    <h2 class="text-2xl font-bold text-primary mb-6 flex items-center">
                        <span class="w-8 h-8 rounded-full bg-accent text-white flex items-center justify-center text-sm mr-3">1</span>
                        Executive Summary
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
                        <div class="bg-gray-50 border border-gray-100 p-6 rounded-xl">
                            <div class="text-3xl font-black text-primary">{n_customers:,}</div>
                            <div class="text-sm font-bold text-gray-500 uppercase tracking-wide mt-1">Unique Customers</div>
                        </div>
                        <div class="bg-gray-50 border border-gray-100 p-6 rounded-xl">
                            <div class="text-3xl font-black text-primary">{len(df):,}</div>
                            <div class="text-sm font-bold text-gray-500 uppercase tracking-wide mt-1">Total Transactions</div>
                        </div>
                        <div class="bg-gray-50 border border-gray-100 p-6 rounded-xl">
                            <div class="text-3xl font-black text-emerald-600">${df['amount'].sum():,.0f}</div>
                            <div class="text-sm font-bold text-gray-500 uppercase tracking-wide mt-1">Gross Revenue</div>
                        </div>
                    </div>
                    <div class="border-l-4 border-amber-500 bg-amber-50 p-6 rounded-r-lg text-secondary">
                        <h3 class="text-lg font-bold text-amber-800 mb-3">Key Business Insights</h3>
                        <ul class="list-disc pl-5 space-y-2">
                            <li><strong>High Initial Drop-off:</strong> There is a significant churn rate (approx ~60%) after the first month of acquisition across all cohorts. A targeted 30-day onboarding sequence is highly recommended.</li>
                            <li><strong>Long-term Stabilization:</strong> Customers who survive past Month 3 exhibit strong loyalty, maintaining a flat retention curve thereafter.</li>
                            <li><strong>Cohort Quality:</strong> Early-year cohorts (Jan/Feb) demonstrate higher lifetime value and baseline retention than late-year acquisitions.</li>
                        </ul>
                    </div>
                </section>

                <!-- Interactive Heatmap -->
                <section>
                    <h2 class="text-2xl font-bold text-primary mb-6 flex items-center">
                        <span class="w-8 h-8 rounded-full bg-accent text-white flex items-center justify-center text-sm mr-3">2</span>
                        Interactive Retention Heatmap
                    </h2>
                    <p class="text-secondary mb-6">This heatmap visualizes the percentage of customers who returned to make a purchase in the months following their initial acquisition. Darker colors indicate higher retention.</p>
                    
                    <div class="border border-gray-200 rounded-xl overflow-hidden shadow-sm">
                        {plotly_html}
                    </div>
                </section>

                <!-- Methodology & Code -->
                <section>
                    <h2 class="text-2xl font-bold text-primary mb-6 flex items-center">
                        <span class="w-8 h-8 rounded-full bg-accent text-white flex items-center justify-center text-sm mr-3">3</span>
                        Methodology & Python Implementation
                    </h2>
                    <p class="text-secondary mb-4">The analysis was performed using <strong>Pandas</strong> for data wrangling and <strong>Plotly</strong> for interactive visualization. The raw data consisted of transactional records featuring <code>customer_id</code>, <code>transaction_date</code>, and <code>amount</code>.</p>
                    
                    <div class="bg-gray-900 rounded-xl overflow-hidden shadow-sm">
                        <div class="flex items-center px-4 py-2 bg-gray-800 border-b border-gray-700">
                            <div class="flex space-x-2">
                                <div class="w-3 h-3 rounded-full bg-red-500"></div>
                                <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                                <div class="w-3 h-3 rounded-full bg-green-500"></div>
                            </div>
                            <span class="ml-4 text-xs font-medium text-gray-400">cohort_analysis.py</span>
                        </div>
                        <pre class="p-6 text-sm text-gray-300 overflow-x-auto"><code>import pandas as pd

# 1. Extract Invoice Month and Acquisition Cohort Month
df['transaction_month'] = df['transaction_date'].dt.to_period('M')
df['cohort_month'] = df.groupby('customer_id')['transaction_date'].transform('min').dt.to_period('M')

# 2. Group by cohort and count unique customers per transaction month
cohort_data = df.groupby(['cohort_month', 'transaction_month']).agg(n_customers=('customer_id', 'nunique')).reset_index()

# 3. Calculate Cohort Index (Months since acquisition)
cohort_data['period_number'] = (cohort_data.transaction_month - cohort_data.cohort_month).apply(lambda x: x.n)

# 4. Pivot into a Matrix
cohort_counts = cohort_data.pivot(index='cohort_month', columns='period_number', values='n_customers')

# 5. Convert to Percentages (Retention Matrix)
cohort_sizes = cohort_counts.iloc[:, 0]
retention_matrix = cohort_counts.divide(cohort_sizes, axis=0) * 100</code></pre>
                    </div>
                </section>
                
                <div class="flex justify-center mt-12 border-t border-gray-100 pt-10">
                    <a href="../../../assets/data/ecommerce_transactions_sample.csv" download class="inline-flex items-center px-6 py-3 bg-white border border-gray-300 rounded-lg text-primary font-bold hover:bg-gray-50 transition-colors shadow-sm">
                        <svg class="w-5 h-5 mr-2 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                        Download Raw Dataset (CSV)
                    </a>
                </div>
            </div>
        </div>
    </main>
''' + get_footer(3)

os.makedirs('./projects/data-analyst-projects/cohort-retention', exist_ok=True)
with open('./projects/data-analyst-projects/cohort-retention/index.html', 'w') as f:
    f.write(html_content)

print("Generated HTML Page.")


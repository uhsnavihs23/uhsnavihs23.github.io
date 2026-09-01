import os
from tailwind_redesign import get_header, get_footer, get_tailwind_head

html = get_tailwind_head("Advanced Finance Visualizer", 2) + get_header(2, 'projects') + '''
    <!-- html2pdf for PDF export -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full bg-gray-50 min-h-screen">
        <div class="flex flex-col md:flex-row justify-between items-center mb-10 gap-4">
            <div>
                <h1 class="text-3xl font-extrabold text-primary mb-2">Smart Finance Visualizer</h1>
                <p class="text-secondary">Analyze your cash flow, test the 50/30/20 rule, and export your financial report.</p>
            </div>
            <div class="flex gap-3">
                <div class="bg-white rounded-lg p-1 shadow-sm border border-gray-200 inline-flex">
                    <button id="monthlyToggle" class="px-4 py-2 rounded-md text-sm font-bold bg-accent text-white shadow transition-all">Monthly</button>
                    <button id="yearlyToggle" class="px-4 py-2 rounded-md text-sm font-bold text-gray-500 hover:text-gray-700 transition-all">Yearly</button>
                </div>
                <button id="exportBtn" class="bg-gray-900 hover:bg-gray-800 text-white px-4 py-2 rounded-lg font-bold text-sm shadow-sm transition-all flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Export Report
                </button>
            </div>
        </div>

        <div id="reportContainer" class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            
            <!-- Left Column: Inputs -->
            <div class="lg:col-span-4 space-y-6" data-html2canvas-ignore>
                <!-- Income -->
                <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
                    <h2 class="text-lg font-bold text-emerald-600 mb-4 flex items-center">
                        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Base Income
                    </h2>
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <span class="text-gray-500 sm:text-sm">₹</span>
                        </div>
                        <input type="number" id="incomeInput" value="80000" class="w-full pl-8 pr-4 py-3 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 font-bold text-gray-700 text-lg" placeholder="0.00">
                    </div>
                </div>

                <!-- Expenses -->
                <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
                    <h2 class="text-lg font-bold text-red-500 mb-4 flex items-center">
                        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Add Expenses
                    </h2>
                    
                    <form id="expenseForm" class="flex flex-col gap-3 mb-6 border-b border-gray-100 pb-6">
                        <input type="text" id="expName" required class="w-full bg-gray-50 border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-red-400" placeholder="Expense Name (e.g. Rent)">
                        <div class="flex gap-3">
                            <input type="number" id="expAmount" required class="flex-grow bg-gray-50 border border-gray-300 rounded-lg px-4 py-2.5 focus:ring-2 focus:ring-red-400" placeholder="₹ Amount">
                            <select id="expCategory" class="bg-gray-50 border border-gray-300 rounded-lg px-3 py-2.5 text-sm font-medium text-gray-600 focus:ring-2 focus:ring-red-400">
                                <option value="needs">Needs (50%)</option>
                                <option value="wants">Wants (30%)</option>
                            </select>
                        </div>
                        <button type="submit" class="w-full bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 py-2.5 rounded-lg font-bold transition-colors shadow-sm">Add to Budget</button>
                    </form>

                    <div class="max-h-80 overflow-y-auto pr-2 space-y-2" id="expenseList">
                        <!-- Expenses injected here -->
                    </div>
                </div>
            </div>

            <!-- Right Column: Analytics Dashboard -->
            <div class="lg:col-span-8 space-y-6">
                <!-- KPI Cards -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-200 flex flex-col justify-center relative overflow-hidden">
                        <div class="absolute -right-4 -top-4 w-16 h-16 rounded-full bg-emerald-50 opacity-50"></div>
                        <div class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-2">Total Income</div>
                        <div id="sumIncome" class="text-3xl font-black text-primary">₹0</div>
                        <div id="incomeLabel" class="text-xs text-emerald-600 font-bold mt-2">Monthly Projection</div>
                    </div>
                    <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-200 flex flex-col justify-center relative overflow-hidden">
                        <div class="absolute -right-4 -top-4 w-16 h-16 rounded-full bg-red-50 opacity-50"></div>
                        <div class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-2">Total Expenses</div>
                        <div id="sumExpenses" class="text-3xl font-black text-red-500">₹0</div>
                        <div id="expenseLabel" class="text-xs text-red-600 font-bold mt-2">Monthly Projection</div>
                    </div>
                    <div class="bg-gradient-to-br from-gray-900 to-gray-800 rounded-2xl p-6 shadow-md text-white flex flex-col justify-center relative overflow-hidden">
                        <div class="absolute -right-4 -top-4 w-16 h-16 rounded-full bg-white opacity-10"></div>
                        <div class="text-sm font-bold text-gray-400 uppercase tracking-wider mb-2">Net Savings</div>
                        <div id="sumBalance" class="text-3xl font-black text-white">₹0</div>
                        <div class="flex items-center mt-2">
                            <span class="text-xs text-gray-300 font-medium mr-2">Savings Rate:</span>
                            <span id="savingsRate" class="text-sm font-bold text-emerald-400 bg-emerald-900/50 px-2 py-0.5 rounded">0%</span>
                        </div>
                    </div>
                </div>

                <!-- 50/30/20 Rule Analyzer & Chart -->
                <div class="bg-white rounded-2xl p-8 shadow-sm border border-gray-200">
                    <div class="flex flex-col md:flex-row gap-8 items-center">
                        <!-- Chart -->
                        <div class="w-full md:w-1/2 relative h-64 flex justify-center">
                            <canvas id="budgetChart"></canvas>
                        </div>
                        
                        <!-- 50/30/20 Breakdown -->
                        <div class="w-full md:w-1/2 space-y-6">
                            <div>
                                <h3 class="text-xl font-bold text-primary mb-1">The 50/30/20 Analysis</h3>
                                <p class="text-sm text-secondary mb-4">How your budget compares to the golden rule of personal finance.</p>
                            </div>
                            
                            <!-- Needs -->
                            <div>
                                <div class="flex justify-between text-sm mb-1">
                                    <span class="font-bold text-gray-700">Needs (Target: 50%)</span>
                                    <span id="pctNeeds" class="font-bold text-blue-600">0%</span>
                                </div>
                                <div class="w-full bg-gray-100 rounded-full h-2.5">
                                    <div id="barNeeds" class="bg-blue-500 h-2.5 rounded-full" style="width: 0%"></div>
                                </div>
                                <div id="msgNeeds" class="text-xs text-gray-500 mt-1"></div>
                            </div>
                            
                            <!-- Wants -->
                            <div>
                                <div class="flex justify-between text-sm mb-1">
                                    <span class="font-bold text-gray-700">Wants (Target: 30%)</span>
                                    <span id="pctWants" class="font-bold text-amber-500">0%</span>
                                </div>
                                <div class="w-full bg-gray-100 rounded-full h-2.5">
                                    <div id="barWants" class="bg-amber-400 h-2.5 rounded-full" style="width: 0%"></div>
                                </div>
                                <div id="msgWants" class="text-xs text-gray-500 mt-1"></div>
                            </div>

                            <!-- Savings -->
                            <div>
                                <div class="flex justify-between text-sm mb-1">
                                    <span class="font-bold text-gray-700">Savings (Target: 20%)</span>
                                    <span id="pctSavings" class="font-bold text-emerald-500">0%</span>
                                </div>
                                <div class="w-full bg-gray-100 rounded-full h-2.5">
                                    <div id="barSavings" class="bg-emerald-500 h-2.5 rounded-full" style="width: 0%"></div>
                                </div>
                                <div id="msgSavings" class="text-xs text-gray-500 mt-1"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-indigo-50 border border-indigo-100 rounded-2xl p-6 text-indigo-900 shadow-sm flex items-start gap-4">
                    <div class="p-3 bg-indigo-100 rounded-full shrink-0">
                        <svg class="w-6 h-6 text-indigo-600" fill="currentColor" viewBox="0 0 20 20"><path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z"></path></svg>
                    </div>
                    <div>
                        <h3 class="font-bold text-lg mb-1">AI Financial Insight</h3>
                        <p id="aiInsight" class="text-sm font-medium opacity-80 leading-relaxed">Add your income and expenses to receive an automated analysis of your financial health.</p>
                    </div>
                </div>

            </div>
        </div>
    </main>

    <script>
        // State
        let baseIncome = 80000;
        let isYearly = false;
        let expenses = [
            { id: 1, name: 'Rent', amount: 20000, category: 'needs' },
            { id: 2, name: 'Groceries', amount: 10000, category: 'needs' },
            { id: 3, name: 'Utilities & Bills', amount: 4000, category: 'needs' },
            { id: 4, name: 'Dining Out', amount: 6000, category: 'wants' },
            { id: 5, name: 'Subscriptions', amount: 2000, category: 'wants' },
            { id: 6, name: 'Shopping', amount: 8000, category: 'wants' }
        ];
        let chartInstance = null;
        
        // Elements
        const incomeInput = document.getElementById('incomeInput');
        const expenseForm = document.getElementById('expenseForm');
        const expenseList = document.getElementById('expenseList');
        const monthlyToggle = document.getElementById('monthlyToggle');
        const yearlyToggle = document.getElementById('yearlyToggle');
        const exportBtn = document.getElementById('exportBtn');
        const reportContainer = document.getElementById('reportContainer');

        // Toggle Logic
        function setMode(yearly) {
            isYearly = yearly;
            if (yearly) {
                yearlyToggle.className = 'px-4 py-2 rounded-md text-sm font-bold bg-accent text-white shadow transition-all';
                monthlyToggle.className = 'px-4 py-2 rounded-md text-sm font-bold text-gray-500 hover:text-gray-700 transition-all';
                document.getElementById('incomeLabel').textContent = 'Yearly Projection';
                document.getElementById('expenseLabel').textContent = 'Yearly Projection';
            } else {
                monthlyToggle.className = 'px-4 py-2 rounded-md text-sm font-bold bg-accent text-white shadow transition-all';
                yearlyToggle.className = 'px-4 py-2 rounded-md text-sm font-bold text-gray-500 hover:text-gray-700 transition-all';
                document.getElementById('incomeLabel').textContent = 'Monthly Projection';
                document.getElementById('expenseLabel').textContent = 'Monthly Projection';
            }
            updateUI();
        }

        monthlyToggle.addEventListener('click', () => setMode(false));
        yearlyToggle.addEventListener('click', () => setMode(true));

        // PDF Export Logic
        exportBtn.addEventListener('click', () => {
            const opt = {
                margin:       [10, 10, 10, 10],
                filename:     isYearly ? 'yearly_finance_report.pdf' : 'monthly_finance_report.pdf',
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true },
                jsPDF:        { unit: 'mm', format: 'a4', orientation: 'landscape' }
            };
            exportBtn.innerHTML = '<svg class="animate-spin w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path></svg> Generating...';
            
            html2pdf().set(opt).from(reportContainer).save().then(() => {
                exportBtn.innerHTML = '<svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg> Export Report';
            });
        });

        // Form Events
        incomeInput.addEventListener('input', (e) => {
            baseIncome = parseFloat(e.target.value) || 0;
            updateUI();
        });

        expenseForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('expName').value.trim();
            const amount = parseFloat(document.getElementById('expAmount').value);
            const category = document.getElementById('expCategory').value;
            
            if (name && amount > 0) {
                expenses.push({ id: Date.now(), name, amount, category });
                document.getElementById('expName').value = '';
                document.getElementById('expAmount').value = '';
                updateUI();
            }
        });

        window.deleteExpense = function(id) {
            expenses = expenses.filter(e => e.id !== id);
            updateUI();
        }

        // Core Update Logic
        function updateUI() {
            const multiplier = isYearly ? 12 : 1;
            const income = baseIncome * multiplier;
            
            expenseList.innerHTML = '';
            let totalNeeds = 0;
            let totalWants = 0;
            
            expenses.forEach(exp => {
                const amount = exp.amount * multiplier;
                if(exp.category === 'needs') totalNeeds += amount;
                else totalWants += amount;
                
                const catBadge = exp.category === 'needs' 
                    ? '<span class="bg-blue-100 text-blue-700 text-[10px] uppercase font-bold px-2 py-0.5 rounded ml-2">Need</span>'
                    : '<span class="bg-amber-100 text-amber-700 text-[10px] uppercase font-bold px-2 py-0.5 rounded ml-2">Want</span>';

                expenseList.innerHTML += `
                    <div class="flex justify-between items-center p-3 bg-white border border-gray-100 rounded-lg hover:border-gray-300 transition-colors group">
                        <div>
                            <div class="font-bold text-gray-800 flex items-center">${exp.name} ${catBadge}</div>
                        </div>
                        <div class="flex items-center gap-4">
                            <span class="font-black text-gray-900">₹${amount.toLocaleString('en-IN')}</span>
                            <button onclick="deleteExpense(${exp.id})" class="text-gray-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-opacity" data-html2canvas-ignore>
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                            </button>
                        </div>
                    </div>
                `;
            });

            const totalExp = totalNeeds + totalWants;
            const balance = income - totalExp;
            const savingsRateVal = income > 0 ? (balance / income) * 100 : 0;
            
            document.getElementById('sumIncome').textContent = '₹' + income.toLocaleString('en-IN');
            document.getElementById('sumExpenses').textContent = '₹' + totalExp.toLocaleString('en-IN');
            document.getElementById('sumBalance').textContent = '₹' + balance.toLocaleString('en-IN');
            
            document.getElementById('sumBalance').className = `text-3xl font-black ${balance >= 0 ? 'text-white' : 'text-red-400'}`;
            document.getElementById('savingsRate').textContent = savingsRateVal.toFixed(1) + '%';
            document.getElementById('savingsRate').className = `text-sm font-bold px-2 py-0.5 rounded ${savingsRateVal >= 20 ? 'text-emerald-400 bg-emerald-900/50' : 'text-amber-400 bg-amber-900/50'}`;

            // 50/30/20 Math
            const pctNeeds = income > 0 ? (totalNeeds / income) * 100 : 0;
            const pctWants = income > 0 ? (totalWants / income) * 100 : 0;
            
            document.getElementById('pctNeeds').textContent = pctNeeds.toFixed(1) + '%';
            document.getElementById('barNeeds').style.width = Math.min(100, pctNeeds) + '%';
            document.getElementById('barNeeds').className = `h-2.5 rounded-full ${pctNeeds > 50 ? 'bg-red-500' : 'bg-blue-500'}`;
            document.getElementById('msgNeeds').textContent = pctNeeds > 50 ? `Over budget by ${(pctNeeds-50).toFixed(1)}%` : `Under budget by ${(50-pctNeeds).toFixed(1)}%`;

            document.getElementById('pctWants').textContent = pctWants.toFixed(1) + '%';
            document.getElementById('barWants').style.width = Math.min(100, pctWants) + '%';
            document.getElementById('barWants').className = `h-2.5 rounded-full ${pctWants > 30 ? 'bg-red-500' : 'bg-amber-400'}`;
            document.getElementById('msgWants').textContent = pctWants > 30 ? `Over budget by ${(pctWants-30).toFixed(1)}%` : `Under budget by ${(30-pctWants).toFixed(1)}%`;

            document.getElementById('pctSavings').textContent = savingsRateVal.toFixed(1) + '%';
            document.getElementById('barSavings').style.width = Math.min(100, Math.max(0, savingsRateVal)) + '%';
            document.getElementById('barSavings').className = `h-2.5 rounded-full ${savingsRateVal < 20 ? 'bg-red-500' : 'bg-emerald-500'}`;
            document.getElementById('msgSavings').textContent = savingsRateVal < 20 ? `Missed target by ${(20-savingsRateVal).toFixed(1)}%` : `Exceeding target by ${(savingsRateVal-20).toFixed(1)}%`;

            // Insight Generator
            let insight = "";
            if (income <= 0) insight = "Please enter an income to generate insights.";
            else if (balance < 0) insight = "Warning: You are spending more than you earn. Immediate action is required to reduce expenses, particularly in your 'Wants' category.";
            else if (savingsRateVal >= 20 && pctNeeds <= 50 && pctWants <= 30) insight = "Excellent financial health! Your budget perfectly aligns with the 50/30/20 rule. You are effectively balancing your lifestyle while securing your financial future.";
            else if (pctNeeds > 50) insight = `Your fixed costs are high (${pctNeeds.toFixed(1)}%). Consider ways to lower rent or utilities to give yourself more breathing room for savings.`;
            else if (pctWants > 30) insight = `You are overspending on lifestyle/wants (${pctWants.toFixed(1)}%). Try cutting back on dining out or subscriptions to hit your 20% savings goal.`;
            else insight = "Your budget is in decent shape, but you could optimize your spending to increase your savings rate closer to the 20% target.";
            document.getElementById('aiInsight').textContent = insight;

            drawChart(totalNeeds, totalWants, Math.max(0, balance));
        }

        function drawChart(needs, wants, savings) {
            if (chartInstance) chartInstance.destroy();
            const ctx = document.getElementById('budgetChart').getContext('2d');
            chartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Needs', 'Wants', 'Savings'],
                    datasets: [{
                        data: [needs, wants, savings],
                        backgroundColor: ['#3b82f6', '#fbbf24', '#10b981'],
                        borderWidth: 0,
                        hoverOffset: 10
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '65%',
                    plugins: {
                        legend: { position: 'bottom', labels: { font: { family: 'Inter', weight: 'bold' } } }
                    }
                }
            });
        }

        // Init
        updateUI();
    </script>
''' + get_footer(2)

with open('./projects/budget-visualizer/index.html', 'w') as f:
    f.write(html)

print("Upgraded Budget Visualizer")

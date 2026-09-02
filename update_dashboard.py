import re

with open('projects/political-intel/index.html', 'r') as f:
    content = f.read()

# Remove the buttons
# We can just remove the whole div containing the buttons
buttons_div = """<div class="flex flex-col sm:flex-row gap-4 mb-6 justify-end">
                <button onclick="downloadPDF()" class="px-5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-lg transition-colors shadow-sm flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg> Download PDF
                </button>
                
            </div>"""

if buttons_div in content:
    content = content.replace(buttons_div, '')

# If the exact block doesn't match (due to my previous replacement), let's use regex to remove the button container.
content = re.sub(r'<div class="flex flex-col sm:flex-row gap-4 mb-6 justify-end">.*?</div>', '', content, flags=re.DOTALL)

# Also remove html2pdf script from head
content = re.sub(r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/html2pdf\.js/.*?"></script>', '', content)

# Remove downloadPDF function
content = re.sub(r'function downloadPDF\(\) \{.*?\n        \}', '', content, flags=re.DOTALL)

# Replace renderDigest
new_render_digest = """        function renderDigest() {
            const selectedDate = dateFilter.value === 'All' ? allStories[0].date : dateFilter.value;
            const dailyNews = allStories.filter(s => s.date === selectedDate);
            const reportDiv = document.getElementById('pdf-report');
            
            if(dailyNews.length === 0) { 
                reportDiv.innerHTML = "<p class='text-primary py-10 text-center'>No data available for this date.</p>"; 
                return; 
            }

            const intl = dailyNews.filter(s => s.section === 'International').slice(0, 10);
            const natGov = dailyNews.filter(s => s.report_category === 'National_Govt').slice(0, 15);
            const opp = dailyNews.filter(s => s.report_category === 'National_Opposition').slice(0, 5);
            const jud = dailyNews.filter(s => s.report_category === 'National_Judicial').slice(0, 5);
            
            let html = `
                <div class="max-w-5xl mx-auto text-primary">
                    <div class="text-center border-b-2 border-primary pb-6 mb-10">
                        <h2 class="text-3xl font-extrabold uppercase tracking-widest text-primary mb-2">Daily Intelligence Digest</h2>
                        <p class="text-lg font-medium text-secondary">Date: ${formatDate(selectedDate)}</p>
                    </div>
            `;
            
            const generateSection = (title, items) => {
                if(items.length === 0) return '';
                let sectionHtml = `
                    <div class="mb-12">
                        <h3 class="text-xl font-bold uppercase tracking-wide text-accent border-b border-borderColor pb-2 mb-6">${title}</h3>
                        <div class="space-y-8">
                `;
                
                items.forEach(item => {
                    sectionHtml += `
                            <div class="flex flex-col md:flex-row gap-4">
                                <div class="flex-shrink-0 pt-1 hidden sm:block text-accent">
                                    <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><circle cx="10" cy="10" r="8"></circle></svg>
                                </div>
                                <div class="flex-grow">
                                    <h4 class="text-lg font-bold text-primary mb-2 flex items-start gap-2">
                                        <span class="sm:hidden text-accent mt-1.5"><svg class="w-2 h-2" fill="currentColor" viewBox="0 0 20 20"><circle cx="10" cy="10" r="8"></circle></svg></span>
                                        ${item.title}
                                    </h4>
                                    <p class="text-secondary leading-relaxed text-sm text-justify mb-2">${item.summary || ''}</p>
                                </div>
                                <div class="md:w-32 flex-shrink-0 text-left md:text-right pt-1">
                                    <a href="${item.link}" target="_blank" class="inline-flex items-center text-xs font-bold uppercase tracking-wider text-accent hover:text-primary transition-colors bg-blue-50 dark:bg-blue-900/30 px-3 py-1.5 rounded-lg border border-transparent hover:border-accent">
                                        ${item.source || 'Source'}
                                        <svg class="w-3 h-3 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                                    </a>
                                </div>
                            </div>
                    `;
                });
                
                sectionHtml += `
                        </div>
                    </div>
                `;
                return sectionHtml;
            };

            html += generateSection("1. International Updates", intl);
            html += generateSection("2. National: Government Policies & Mandates", natGov);
            html += generateSection("3. Opposition Activity", opp);
            html += generateSection("4. Judicial & Supreme Court Verdicts", jud);
            
            html += `
                    <div class="text-center mt-16 pt-8 border-t border-borderColor">
                        <p class="text-xs font-bold uppercase tracking-widest text-secondary">End of Report</p>
                    </div>
                </div>
            `;
            
            reportDiv.innerHTML = html;
        }"""

content = re.sub(r'function renderDigest\(\) \{.*?\n        \}(?=\n\n        function downloadPDF|\n\n        init)', new_render_digest, content, flags=re.DOTALL)

# Strip out the inline #pdf-report CSS we added earlier because we're using tailwind classes on the html itself now.
content = re.sub(r'/\* PDF specific styling.*?\*/.*?#pdf-report p \{.*?\n', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="pdf-report" class="max-w-4xl mx-auto">', '<div id="pdf-report">', content) # if it still exists

with open('projects/political-intel/index.html', 'w') as f:
    f.write(content)

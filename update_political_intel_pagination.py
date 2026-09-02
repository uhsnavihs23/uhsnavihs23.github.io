import os

with open('projects/political-intel/index.html', 'r') as f:
    content = f.read()

# Replace the Print button
content = content.replace(
    '''<button onclick="window.print()" class="px-5 py-2 bg-gray-600 hover:bg-gray-700 text-white font-bold rounded-lg transition-colors shadow-sm flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg> Print
                </button>''',
    ''
)

# Replace Javascript logic block completely
start_idx = content.find('<!-- App Logic -->')
if start_idx != -1:
    content = content[:start_idx] + """<!-- App Logic -->
    <script>
        let allStories = [];
        let currentMode = 'international';
        let currentPage = 1;
        const itemsPerPage = 30;
        
        const grid = document.getElementById('newsGrid');
        const loading = document.getElementById('loadingState');
        const dateFilter = document.getElementById('dateFilter');
        
        dateFilter.addEventListener('change', () => { currentPage = 1; renderUI(); });

        function formatDate(dateStr) {
            const d = new Date(dateStr);
            if (isNaN(d)) return dateStr;
            const options = { day: 'numeric', month: 'short', year: 'numeric' };
            return d.toLocaleDateString('en-GB', options); 
        }

        async function init() {
            loading.classList.remove('hidden');
            grid.innerHTML = '';
            try {
                const response = await fetch('./data/news.json');
                const data = await response.json();
                
                if (Array.isArray(data)) {
                    allStories = data;
                } else {
                    allStories = data.stories;
                    const date = new Date(data.generated_at);
                    document.getElementById('lastUpdated').textContent = date.toLocaleString();
                }
                
                allStories = allStories.filter(s => s.section !== 'UP_Focus' && s.report_category !== 'UP_Focus');
                
                populateDateDropdown();
                renderUI();
            } catch(e) {
                console.error(e);
                grid.innerHTML = '<p class="col-span-full text-center text-red-500">Failed to fetch intelligence data. The backend might be unreachable.</p>';
            } finally {
                loading.classList.add('hidden');
            }
        }
        
        function setMode(mode) {
            currentMode = mode;
            currentPage = 1;
            document.querySelectorAll('.filter-btn').forEach(btn => {
                if (btn.id === `btn-${mode}`) {
                    btn.className = "filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-accent text-white transition-colors whitespace-nowrap shadow-sm";
                } else {
                    btn.className = "filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-gray-100 dark:bg-gray-800 text-secondary hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors whitespace-nowrap";
                }
            });
            renderUI();
        }
        
        function populateDateDropdown() {
            const dates = [...new Set(allStories.map(s => s.date))].sort().reverse();
            dates.forEach(d => {
                const opt = document.createElement('option');
                opt.value = d;
                opt.textContent = formatDate(d);
                dateFilter.appendChild(opt);
            });
            if(dates.length > 0) dateFilter.value = dates[0];
        }
        
        function renderUI() {
            if(currentMode === 'digest') {
                document.getElementById('grid-view').classList.add('hidden');
                document.getElementById('digest-view').classList.remove('hidden');
                renderDigest();
            } else {
                document.getElementById('digest-view').classList.add('hidden');
                document.getElementById('grid-view').classList.remove('hidden');
                renderGrid();
            }
        }

        function renderGrid() {
            const selectedDate = dateFilter.value;
            let filtered = allStories.filter(s => {
                let matchesMode = false;
                if (currentMode === 'international' && s.section === 'International') matchesMode = true;
                if (currentMode === 'national' && s.section === 'National') matchesMode = true;
                let matchesDate = selectedDate === 'All' || s.date === selectedDate;
                return matchesMode && matchesDate;
            });
            
            grid.innerHTML = '';
            
            // Remove old pagination if exists
            const oldPag = document.getElementById('paginationControls');
            if(oldPag) oldPag.remove();
            
            if (filtered.length === 0) {
                grid.innerHTML = '<p class="col-span-full text-center text-secondary py-10">No intelligence reports found for the selected criteria.</p>';
                return;
            }
            
            const totalPages = Math.ceil(filtered.length / itemsPerPage);
            const paginated = filtered.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
            
            paginated.forEach(story => {
                const card = document.createElement('div');
                card.className = "bg-cardBg rounded-xl border border-borderColor overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col h-full";
                
                card.innerHTML = `
                    <div class="p-6 flex-grow flex flex-col">
                        <div class="flex justify-between items-start mb-3">
                            <span class="text-xs font-bold uppercase tracking-wider text-accent bg-blue-50 dark:bg-blue-900/30 px-2 py-1 rounded">${story.source || 'Intel Source'}</span>
                            <span class="text-xs text-secondary font-medium">${formatDate(story.date)}</span>
                        </div>
                        <h3 class="text-lg font-bold text-primary mb-3 leading-snug"><a href="${story.link}" target="_blank" class="hover:text-accent transition-colors">${story.title}</a></h3>
                        <p class="text-secondary text-sm leading-relaxed flex-grow line-clamp-3">${story.summary || ''}</p>
                    </div>
                    <div class="px-6 py-4 bg-gray-50 dark:bg-gray-800/50 border-t border-borderColor mt-auto">
                        <a href="${story.link}" target="_blank" class="text-sm font-medium text-accent hover:underline flex items-center">
                            Read Full Report
                            <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                `;
                grid.appendChild(card);
            });

            // Add Pagination Controls
            if (totalPages > 1) {
                const pagContainer = document.createElement('div');
                pagContainer.id = 'paginationControls';
                pagContainer.className = "flex justify-center items-center mt-12 gap-4 col-span-full";
                
                const prevBtn = document.createElement('button');
                prevBtn.className = `px-4 py-2 rounded-lg font-medium transition-colors ${currentPage === 1 ? 'bg-gray-100 dark:bg-gray-800 text-gray-400 cursor-not-allowed' : 'bg-cardBg border border-borderColor text-primary hover:bg-gray-100 dark:hover:bg-gray-800 shadow-sm'}`;
                prevBtn.textContent = "Previous";
                prevBtn.disabled = currentPage === 1;
                prevBtn.onclick = () => { if(currentPage > 1) { currentPage--; renderGrid(); window.scrollTo({top: 0, behavior: 'smooth'}); } };
                
                const pageInfo = document.createElement('span');
                pageInfo.className = "text-sm font-medium text-secondary";
                pageInfo.textContent = `Page ${currentPage} of ${totalPages}`;
                
                const nextBtn = document.createElement('button');
                nextBtn.className = `px-4 py-2 rounded-lg font-medium transition-colors ${currentPage === totalPages ? 'bg-gray-100 dark:bg-gray-800 text-gray-400 cursor-not-allowed' : 'bg-cardBg border border-borderColor text-primary hover:bg-gray-100 dark:hover:bg-gray-800 shadow-sm'}`;
                nextBtn.textContent = "Next";
                nextBtn.disabled = currentPage === totalPages;
                nextBtn.onclick = () => { if(currentPage < totalPages) { currentPage++; renderGrid(); window.scrollTo({top: 0, behavior: 'smooth'}); } };
                
                pagContainer.appendChild(prevBtn);
                pagContainer.appendChild(pageInfo);
                pagContainer.appendChild(nextBtn);
                
                // Append after grid
                document.getElementById('grid-view').appendChild(pagContainer);
            }
        }
        
        function renderDigest() {
            const selectedDate = dateFilter.value === 'All' ? allStories[0].date : dateFilter.value;
            const dailyNews = allStories.filter(s => s.date === selectedDate);
            const reportDiv = document.getElementById('pdf-report');
            
            if(dailyNews.length === 0) { 
                reportDiv.innerHTML = "<p style='color:black;'>No data available for this date.</p>"; 
                return; 
            }

            const intl = dailyNews.filter(s => s.section === 'International');
            const nat = dailyNews.filter(s => s.section === 'National');
            
            // Clean, corporate PDF structure
            let html = `
                <div style="padding: 40px; background: white; color: black; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 800px; margin: 0 auto;">
                    
                    <div style="text-align: center; border-bottom: 4px solid #1e3a8a; padding-bottom: 25px; margin-bottom: 35px;">
                        <h2 style="font-size: 36px; font-weight: 800; color: #1e3a8a; margin: 0 0 10px 0; text-transform: uppercase; letter-spacing: 2px;">Daily Intelligence Digest</h2>
                        <div style="display: inline-block; background: #f1f5f9; padding: 6px 16px; border-radius: 20px;">
                            <p style="font-size: 16px; color: #334155; margin: 0; font-weight: 600;">Report Date: ${formatDate(selectedDate)}</p>
                        </div>
                        <p style="font-size: 12px; color: #64748b; margin-top: 15px; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Confidential & Proprietary • Prepared by PoliticalIntel</p>
                    </div>
            `;
            
            if(nat.length > 0) {
                html += `
                    <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 10px 20px; margin-bottom: 25px;">
                        <h3 style="margin: 0; color: #1e293b; font-size: 20px; text-transform: uppercase; letter-spacing: 1px;">National Affairs</h3>
                    </div>
                `;
                nat.slice(0, 15).forEach(s => {
                    html += `
                        <div style="margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid #e2e8f0;">
                            <h4 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a; line-height: 1.4;">${s.title}</h4>
                            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b; font-weight: 600; text-transform: uppercase;">
                                Source: <span style="color: #3b82f6;">${s.source}</span>
                            </p>
                            <p style="margin: 0; font-size: 15px; color: #334155; line-height: 1.6; text-align: justify;">${s.summary}</p>
                        </div>
                    `;
                });
            }
            
            if(intl.length > 0) {
                html += `
                    <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 10px 20px; margin-bottom: 25px; margin-top: 40px;">
                        <h3 style="margin: 0; color: #1e293b; font-size: 20px; text-transform: uppercase; letter-spacing: 1px;">International Developments</h3>
                    </div>
                `;
                intl.slice(0, 15).forEach(s => {
                    html += `
                        <div style="margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid #e2e8f0;">
                            <h4 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a; line-height: 1.4;">${s.title}</h4>
                            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b; font-weight: 600; text-transform: uppercase;">
                                Source: <span style="color: #10b981;">${s.source}</span>
                            </p>
                            <p style="margin: 0; font-size: 15px; color: #334155; line-height: 1.6; text-align: justify;">${s.summary}</p>
                        </div>
                    `;
                });
            }
            
            html += `
                <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 2px solid #e2e8f0;">
                    <p style="font-size: 12px; color: #94a3b8; margin: 0;">END OF REPORT</p>
                    <p style="font-size: 10px; color: #cbd5e1; margin-top: 5px;">Generated autonomously via PoliticalIntel Engine</p>
                </div>
            </div>`; // Close wrapper
            
            reportDiv.innerHTML = html;
        }

        function downloadPDF() {
            const element = document.getElementById('pdf-report');
            const date = dateFilter.value === 'All' ? allStories[0].date : dateFilter.value;
            const opt = {
                margin:       [0.5, 0],
                filename:     `Intelligence-Digest-${date}.pdf`,
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true },
                jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
            };
            html2pdf().set(opt).from(element).save();
        }
        
        init();
    </script>
</body>
</html>
"""

with open('projects/political-intel/index.html', 'w') as f:
    f.write(content)

import re

with open('projects/political-intel/index.html', 'r') as f:
    content = f.read()

# Replace renderDigest and downloadPDF
js_to_replace = """        function renderDigest() {
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
        }"""

new_js = """        function renderDigest() {
            const selectedDate = dateFilter.value === 'All' ? allStories[0].date : dateFilter.value;
            const dailyNews = allStories.filter(s => s.date === selectedDate);
            const reportDiv = document.getElementById('pdf-report');
            
            if(dailyNews.length === 0) { 
                reportDiv.innerHTML = "<p style='color:black; padding: 20px;'>No data available for this date.</p>"; 
                return; 
            }

            const intl = dailyNews.filter(s => s.section === 'International');
            const nat = dailyNews.filter(s => s.section === 'National');
            
            // Client-Ready Corporate PDF Structure
            let html = `
                <div style="width: 100%; background: white; color: black; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">
                    
                    <div style="border-bottom: 2px solid #0f172a; padding-bottom: 15px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: flex-end;">
                        <div>
                            <h2 style="font-size: 24px; font-weight: 800; color: #0f172a; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Global Intelligence Digest</h2>
                            <p style="font-size: 10px; color: #475569; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; font-weight: bold;">Confidential & Proprietary</p>
                        </div>
                        <div style="text-align: right;">
                            <p style="font-size: 12px; color: #0f172a; font-weight: 600; margin: 0;">Date: ${formatDate(selectedDate)}</p>
                        </div>
                    </div>
            `;
            
            if(nat.length > 0) {
                html += `
                    <div style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid #cbd5e1;">
                        <h3 style="margin: 0; color: #1e3a8a; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; font-weight: 800;">National Affairs</h3>
                    </div>
                `;
                nat.slice(0, 15).forEach(s => {
                    html += `
                        <div style="margin-bottom: 16px; page-break-inside: avoid;">
                            <h4 style="margin: 0 0 4px 0; font-size: 14px; color: #0f172a; font-weight: 700; line-height: 1.3;">${s.title}</h4>
                            <p style="margin: 0 0 6px 0; font-size: 10px; color: #64748b; font-weight: 600; text-transform: uppercase;">
                                Source: <a href="${s.link}" target="_blank" style="color: #2563eb; text-decoration: none;">${s.source} &rarr;</a>
                            </p>
                            <p style="margin: 0; font-size: 12px; color: #334155; line-height: 1.5; text-align: justify;">${s.summary}</p>
                        </div>
                    `;
                });
            }
            
            if(intl.length > 0) {
                html += `
                    <div style="margin-bottom: 15px; margin-top: 30px; padding-bottom: 5px; border-bottom: 1px solid #cbd5e1;">
                        <h3 style="margin: 0; color: #047857; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; font-weight: 800;">International Developments</h3>
                    </div>
                `;
                intl.slice(0, 15).forEach(s => {
                    html += `
                        <div style="margin-bottom: 16px; page-break-inside: avoid;">
                            <h4 style="margin: 0 0 4px 0; font-size: 14px; color: #0f172a; font-weight: 700; line-height: 1.3;">${s.title}</h4>
                            <p style="margin: 0 0 6px 0; font-size: 10px; color: #64748b; font-weight: 600; text-transform: uppercase;">
                                Source: <a href="${s.link}" target="_blank" style="color: #059669; text-decoration: none;">${s.source} &rarr;</a>
                            </p>
                            <p style="margin: 0; font-size: 12px; color: #334155; line-height: 1.5; text-align: justify;">${s.summary}</p>
                        </div>
                    `;
                });
            }
            
            html += `
                <div style="text-align: center; margin-top: 40px; padding-top: 15px; border-top: 1px solid #e2e8f0; page-break-inside: avoid;">
                    <p style="font-size: 9px; color: #94a3b8; margin: 0; text-transform: uppercase; letter-spacing: 1px;">End of Report • PoliticalIntel Engine</p>
                </div>
                </div>
            `;
            
            reportDiv.innerHTML = html;
        }

        function downloadPDF() {
            const element = document.getElementById('pdf-report');
            const date = dateFilter.value === 'All' ? allStories[0].date : dateFilter.value;
            const opt = {
                margin:       0.5, // 0.5 inch margins on all sides directly via jsPDF
                filename:     `Intelligence-Digest-${date}.pdf`,
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true, letterRendering: true },
                jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' },
                pagebreak:    { mode: 'css', before: '#nextpage1' }
            };
            html2pdf().set(opt).from(element).save();
        }"""

if js_to_replace in content:
    content = content.replace(js_to_replace, new_js)
else:
    print("Error: Could not find JS string to replace.")

# Also remove the max-width and padding from the UI display wrapper so the screen rendering isn't constrained awkwardly
content = content.replace(
    '<div class="bg-white p-8 sm:p-12 rounded-xl shadow-lg border border-gray-200 overflow-x-auto">\n                <div id="pdf-report" class="max-w-4xl mx-auto">',
    '<div class="bg-white p-8 sm:p-12 rounded-xl shadow-lg border border-gray-200 overflow-x-auto">\n                <div id="pdf-report">'
)

with open('projects/political-intel/index.html', 'w') as f:
    f.write(content)


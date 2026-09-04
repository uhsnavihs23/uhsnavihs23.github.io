import re

with open('about.html', 'r') as f:
    content = f.read()

certificates_html = """
            <!-- Licenses & Certifications -->
            <div class="mt-12">
                <h3 class="text-xl font-bold text-primary mb-6 border-b border-borderColor pb-2 flex justify-between items-end">
                    Licenses & Certifications
                    <div class="flex gap-2">
                        <button id="certScrollLeft" class="p-1 rounded bg-bgColor border border-borderColor text-secondary hover:text-accent transition-colors"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg></button>
                        <button id="certScrollRight" class="p-1 rounded bg-bgColor border border-borderColor text-secondary hover:text-accent transition-colors"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg></button>
                    </div>
                </h3>
                
                <div id="certContainer" class="flex overflow-x-auto pb-6 gap-4 snap-x hide-scrollbar scroll-smooth" style="scrollbar-width: none; -ms-overflow-style: none;">
                    
                    <button onclick="openCertModal('sql')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-blue-100 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">SQL Data Analysis</h4>
                            <p class="text-xs text-secondary mt-1">3 Certificates</p>
                        </div>
                    </button>

                    <button onclick="openCertModal('powerbi')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-yellow-100 dark:bg-yellow-900/30 text-yellow-600 dark:text-yellow-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">Power BI & Excel</h4>
                            <p class="text-xs text-secondary mt-1">2 Certificates</p>
                        </div>
                    </button>

                    <button onclick="openCertModal('sixsigma')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-green-100 dark:bg-green-900/30 text-green-600 dark:text-green-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">Six Sigma Foundations</h4>
                            <p class="text-xs text-secondary mt-1">LinkedIn Learning</p>
                        </div>
                    </button>

                    <button onclick="openCertModal('saperp')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">SAP ERP Training</h4>
                            <p class="text-xs text-secondary mt-1">LinkedIn Learning</p>
                        </div>
                    </button>
                    
                    <button onclick="openCertModal('aiagents')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-red-100 dark:bg-red-900/30 text-red-600 dark:text-red-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">AI Agents & Workflows</h4>
                            <p class="text-xs text-secondary mt-1">n8n Automation</p>
                        </div>
                    </button>

                    <button onclick="openCertModal('statsesg')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-orange-100 dark:bg-orange-900/30 text-orange-600 dark:text-orange-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">Stats & ESG</h4>
                            <p class="text-xs text-secondary mt-1">2 Certificates</p>
                        </div>
                    </button>

                    <button onclick="openCertModal('academic')" class="flex-shrink-0 snap-start bg-cardBg border border-borderColor rounded-xl p-4 hover:shadow-md hover:border-accent/50 transition-all flex items-center gap-4 group w-[280px] text-left">
                        <div class="p-3 bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 rounded-lg group-hover:scale-110 transition-transform">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path></svg>
                        </div>
                        <div>
                            <h4 class="font-bold text-primary text-sm group-hover:text-accent transition-colors">Academic Specializations</h4>
                            <p class="text-xs text-secondary mt-1">MITx, Physiology & more</p>
                        </div>
                    </button>
                    
                </div>
                
                <style>
                    /* Hide scrollbar for Chrome, Safari and Opera */
                    .hide-scrollbar::-webkit-scrollbar { display: none; }
                </style>
                <script>
                    const container = document.getElementById('certContainer');
                    document.getElementById('certScrollLeft').addEventListener('click', () => { container.scrollBy({ left: -300, behavior: 'smooth' }); });
                    document.getElementById('certScrollRight').addEventListener('click', () => { container.scrollBy({ left: 300, behavior: 'smooth' }); });
                </script>
            </div>
"""

# Inject before the <div id="contact-card">
content = content.replace('<!-- Contact Card -->\n        <div id="contact-card"', certificates_html + '\n        <!-- Contact Card -->\n        <div id="contact-card"')


# 2. Add the Modal HTML and JS before </body>
modal_html = """
    <!-- Certifications Modal -->
    <div id="certModal" class="fixed inset-0 z-[100] hidden bg-black/60 backdrop-blur-sm items-center justify-center p-4 opacity-0 transition-opacity duration-300">
        <div class="bg-cardBg border border-borderColor rounded-lg w-full max-w-4xl max-h-[90vh] flex flex-col transform scale-95 transition-transform duration-300 shadow-md" id="certModalContentWrapper">
            
            <div class="flex justify-between items-center p-6 border-b border-borderColor">
                <h3 id="certModalTitle" class="text-2xl font-bold text-primary">Certificate Title</h3>
                <button onclick="closeCertModal()" class="p-2 text-secondary hover:text-primary hover:bg-bgColor rounded-lg transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
            
            <div class="p-6 overflow-y-auto flex-1 flex flex-col gap-6 hide-scrollbar">
                <div class="bg-bgColor border border-borderColor p-4 rounded-xl">
                    <h4 class="font-bold text-primary mb-2 text-sm uppercase tracking-wide">Key Skills Acquired</h4>
                    <p id="certModalSkills" class="text-secondary text-sm leading-relaxed">...</p>
                </div>
                
                <div id="certLinksContainer" class="flex flex-col gap-4">
                    <!-- PDF embeds or buttons injected here -->
                </div>
            </div>
        </div>
    </div>

    <script>
        const certData = {
            'sql': {
                title: 'SQL Data Analysis Track',
                skills: 'Mastered relational database querying, complex table joins (INNER, LEFT, RIGHT), aggregations, subqueries, and advanced data filtering to extract actionable insights from large datasets.',
                files: [
                    { name: 'Introduction to SQL', path: './assets/certificates/sql_intro.pdf' },
                    { name: 'Intermediate SQL', path: './assets/certificates/sql_intermediate.pdf' },
                    { name: 'Joining Data in SQL', path: './assets/certificates/sql_joining.pdf' }
                ]
            },
            'powerbi': {
                title: 'Power BI & Advanced Excel',
                skills: 'Developed proficiency in business intelligence dashboard creation, DAX queries, Power Query data modeling, pivot tables, and advanced spreadsheet automation for enterprise reporting.',
                files: [
                    { name: 'Power BI Essential Training', path: './assets/certificates/powerbi.pdf' },
                    { name: 'Advanced Excel', path: './assets/certificates/advanced_excel.png', type: 'img' }
                ]
            },
            'sixsigma': {
                title: 'Six Sigma Foundations',
                skills: 'Learned the foundational principles of Six Sigma methodology, including DMAIC (Define, Measure, Analyze, Improve, Control) frameworks to reduce process variation and improve quality control.',
                files: [
                    { name: 'Six Sigma Foundations', path: './assets/certificates/six_sigma.pdf' }
                ]
            },
            'saperp': {
                title: 'SAP ERP Essential Training',
                skills: 'Gained comprehensive understanding of Enterprise Resource Planning using SAP, covering master data management, business processes, and system navigation for organizational efficiency.',
                files: [
                    { name: 'SAP ERP Essential Training', path: './assets/certificates/sap_erp.pdf' }
                ]
            },
            'aiagents': {
                title: 'Build AI Agents and Automate Workflows',
                skills: 'Acquired hands-on experience in building autonomous AI agents and deploying complex workflow automations using n8n to streamline operations and enhance productivity.',
                files: [
                    { name: 'AI Agents with n8n', path: './assets/certificates/ai_agents.pdf' }
                ]
            },
            'statsesg': {
                title: 'Statistics & ESG',
                skills: 'Explored core concepts in Statistical Analysis for data-driven decision making, and Environmental, Social, and Governance (ESG) frameworks for sustainable business practices.',
                files: [
                    { name: 'Statistical Analysis', path: './assets/certificates/statistical.pdf' },
                    { name: 'Introduction to ESG', path: './assets/certificates/esg.pdf' }
                ]
            },
            'academic': {
                title: 'Academic Specializations',
                skills: 'Diverse academic pursuits encompassing Differential Equations, Physiology, Collective Leadership frameworks, and rigorous MITx coursework to build a strong analytical foundation.',
                files: [
                    { name: 'Differential Equations', path: './assets/certificates/differential.pdf' },
                    { name: 'Physiology', path: './assets/certificates/physiology.pdf' },
                    { name: 'Collective Leadership', path: './assets/certificates/collective_leadership.pdf' },
                    { name: 'MITx Certificate', path: './assets/certificates/mitx.pdf' }
                ]
            }
        };

        const modal = document.getElementById('certModal');
        const modalWrapper = document.getElementById('certModalContentWrapper');
        
        function openCertModal(key) {
            const data = certData[key];
            if(!data) return;
            
            document.getElementById('certModalTitle').textContent = data.title;
            document.getElementById('certModalSkills').textContent = data.skills;
            
            const linksContainer = document.getElementById('certLinksContainer');
            linksContainer.innerHTML = '';
            
            data.files.forEach(file => {
                const wrapper = document.createElement('div');
                wrapper.className = 'border border-borderColor rounded-xl overflow-hidden bg-white dark:bg-zinc-900 shadow-sm';
                
                const header = document.createElement('div');
                header.className = 'bg-bgColor px-4 py-3 border-b border-borderColor font-bold text-primary text-sm flex justify-between items-center';
                header.innerHTML = `<span>${file.name}</span> <a href="${file.path}" target="_blank" class="text-accent hover:underline text-xs">Open in new tab &rarr;</a>`;
                wrapper.appendChild(header);
                
                if(file.type === 'img') {
                    const img = document.createElement('img');
                    img.src = file.path;
                    img.className = 'w-full h-auto max-h-[500px] object-contain bg-gray-100 dark:bg-zinc-800';
                    wrapper.appendChild(img);
                } else {
                    const iframe = document.createElement('iframe');
                    iframe.src = file.path;
                    iframe.className = 'w-full h-[400px] border-none bg-gray-100 dark:bg-zinc-800';
                    wrapper.appendChild(iframe);
                }
                
                linksContainer.appendChild(wrapper);
            });
            
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            // Trigger animation frame for opacity transition
            requestAnimationFrame(() => {
                modal.classList.remove('opacity-0');
                modalWrapper.classList.remove('scale-95');
            });
            document.body.style.overflow = 'hidden';
        }
        
        function closeCertModal() {
            modal.classList.add('opacity-0');
            modalWrapper.classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
                modal.classList.remove('flex');
                document.body.style.overflow = 'auto';
            }, 300);
        }
        
        // Close on clicking outside
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeCertModal();
        });
    </script>
"""
content = content.replace('<!-- Theme Script -->', modal_html + '\n    <!-- Theme Script -->')

with open('about.html', 'w') as f:
    f.write(content)


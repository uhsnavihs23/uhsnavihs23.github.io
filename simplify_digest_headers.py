import re

with open('projects/political-intel/index.html', 'r') as f:
    content = f.read()

new_logic = """            const intl = dailyNews.filter(s => s.section === 'International').slice(0, 15);
            const nat = dailyNews.filter(s => s.section === 'National').slice(0, 25);
            
            // Rebuilding as a strict A4 Page View
            let html = `
                <div class="max-w-[800px] mx-auto bg-white dark:bg-[#1a1b1e] shadow-2xl border border-gray-200 dark:border-gray-800 rounded-sm my-8" style="min-height: 1122px;">
                    <!-- A4 Inner Padding -->
                    <div class="p-10 sm:p-14 md:p-16">
                        
                        <!-- Header -->
                        <div class="text-center border-b-[3px] border-gray-800 dark:border-gray-200 pb-6 mb-10">
                            <h2 class="text-3xl font-black uppercase tracking-widest text-gray-900 dark:text-white mb-2" style="font-family: Georgia, serif;">Daily Intelligence Digest</h2>
                            <p class="text-lg font-bold text-gray-600 dark:text-gray-400">Date: ${formatDate(selectedDate)}</p>
                            <p class="text-xs font-semibold text-gray-400 dark:text-gray-500 tracking-[0.2em] uppercase mt-4">Confidential & Proprietary</p>
                        </div>
            `;
            
            const generateSection = (title, items) => {
                if(items.length === 0) return '';
                
                let sectionHtml = `
                    <div class="mb-10">
                        <h3 class="text-xl font-bold uppercase tracking-wider text-gray-900 dark:text-white border-b border-gray-300 dark:border-gray-700 pb-2 mb-6" style="font-family: Georgia, serif;">
                            ${title}
                        </h3>
                        <ul class="list-disc pl-5 space-y-6 marker:text-accent">
                `;
                
                items.forEach(item => {
                    sectionHtml += `
                            <li class="pl-2">
                                <div class="flex flex-col">
                                    <h4 class="text-base font-bold text-gray-900 dark:text-gray-100 leading-snug mb-2">
                                        ${item.title}
                                    </h4>
                                    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed text-justify mb-2">
                                        ${item.summary || ''}
                                    </p>
                                    <div>
                                        <a href="${item.link}" target="_blank" class="text-xs font-bold uppercase tracking-wider text-accent hover:underline">
                                            [ Source: ${item.source || 'Intel Link'} ]
                                        </a>
                                    </div>
                                </div>
                            </li>
                    `;
                });
                
                sectionHtml += `
                        </ul>
                    </div>
                `;
                return sectionHtml;
            };

            html += generateSection("Global", intl);
            html += generateSection("National", nat);"""

old_logic_pattern = r'const intl = dailyNews\.filter.*?html \+= generateSection\("4\. Judicial & Supreme Court Verdicts", jud\);'
content = re.sub(old_logic_pattern, new_logic, content, flags=re.DOTALL)

with open('projects/political-intel/index.html', 'w') as f:
    f.write(content)

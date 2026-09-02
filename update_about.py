import re

with open('about.html', 'r') as f:
    content = f.read()

# 1. Update Bio
content = content.replace("analyzing urban governance, and building functional web applications.", "and building functional web applications.")

# 2. Update Email
content = content.replace("shivanshu.sharma0023@gmail.com", "shivanshu.sharma@alumni.iitgn.ac.in")

# 3. Add AI Tools to Tech Stack
ai_tools = """
                    <!-- AI Tools -->
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="ChatGPT">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-6 w-6"><path fill="currentColor" d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.073zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.8956zm16.0993 3.8558L12.5973 8.3829a.0757.0757 0 0 1-.0379-.052V2.7483a4.504 4.504 0 0 1 5.8683 1.637l-.1419.0804-4.783 2.7582a.7948.7948 0 0 0-.3927.6813v6.7369l2.02-1.1686a.071.071 0 0 1 .038-.052v-5.5826a4.504 4.504 0 0 1 5.2536-4.2255zm-1.0264 6.3262l-4.783-2.7582a.7712.7712 0 0 0-.7806 0l-5.8428 3.3685v-2.3324a.0804.0804 0 0 1 .0332-.0615l4.835-2.7913a4.4992 4.4992 0 0 1 6.1408 1.6464V18.0776zm-8.8775-6.8407l-2.02-1.1685a.071.071 0 0 1-.038-.052V4.4338a4.504 4.504 0 0 1 5.2536 4.2255l-.142-.0852-4.783-2.7582a.7948.7948 0 0 0-.3927-.6813v6.7369a.071.071 0 0 1-.038.052l-2.02 1.1686zM12 14.1798l-2.946-1.7011v-3.4022L12 7.3754l2.946 1.7011v3.4022L12 14.1798z"/></svg>
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="GitHub Copilot">
                        <img src="https://cdn.simpleicons.org/githubcopilot/000000" alt="Copilot" class="h-6 w-6 dark:invert">
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Claude">
                        <img src="https://cdn.simpleicons.org/anthropic/000000" alt="Claude" class="h-6 w-6 dark:invert">
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Gemini">
                        <img src="https://cdn.simpleicons.org/googlegemini/4285F4" alt="Gemini" class="h-6 w-6">
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Perplexity">
                        <img src="https://cdn.simpleicons.org/perplexity/222222" alt="Perplexity" class="h-6 w-6 dark:invert">
                    </div>
"""
# inject AI tools at the end of the flex container for tech stack
content = re.sub(r'(<div class="h-10 w-10 bg-cardBg.*?alt="Power BI".*?</div>)', r'\1' + ai_tools, content, flags=re.DOTALL)

# 4. Add new sections below Experience
new_sections = """
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-12">
                <!-- Core Competencies -->
                <div>
                    <h3 class="text-xl font-bold text-primary mb-6 border-b border-borderColor pb-2">Core Competencies</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-bgColor border border-borderColor rounded-lg text-sm text-primary font-medium">Project Management</span>
                        <span class="px-3 py-1 bg-bgColor border border-borderColor rounded-lg text-sm text-primary font-medium">Strategic Planning</span>
                        <span class="px-3 py-1 bg-bgColor border border-borderColor rounded-lg text-sm text-primary font-medium">Client Management</span>
                        <span class="px-3 py-1 bg-bgColor border border-borderColor rounded-lg text-sm text-primary font-medium">Management Consulting</span>
                    </div>
                </div>

                <!-- Volunteering -->
                <div>
                    <h3 class="text-xl font-bold text-primary mb-6 border-b border-borderColor pb-2">Volunteering</h3>
                    <ul class="space-y-3 text-sm text-secondary">
                        <li class="flex items-start gap-2">
                            <svg class="w-4 h-4 text-accent mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                            Teaching Assistant for Prof. Marcos Inácio Severo de Almeida (Federal University of Goiás, Brazil)
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-4 h-4 text-accent mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                            Educating underprivileged children with Nyasa (IITGN)
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-4 h-4 text-accent mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                            Blood Donation Camp in partnership with The Gujarat Cancer & Research Institute (GCRI)
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Achievements & Scholarships -->
            <div class="mt-12">
                <h3 class="text-xl font-bold text-primary mb-6 border-b border-borderColor pb-2">Achievements & Scholarships</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="bg-bgColor border border-borderColor p-4 rounded-xl">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="p-2 bg-yellow-100 dark:bg-yellow-900/30 text-yellow-600 dark:text-yellow-400 rounded-lg">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                            </div>
                            <h4 class="font-bold text-primary text-sm">Pioneer Batch Gold Medal</h4>
                        </div>
                        <p class="text-xs text-secondary">Outstanding Leadership - IITGN (₹25,000)</p>
                    </div>
                    
                    <div class="bg-bgColor border border-borderColor p-4 rounded-xl">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="p-2 bg-blue-100 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 rounded-lg">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path></svg>
                            </div>
                            <h4 class="font-bold text-primary text-sm">Class of 2013 Scholarship</h4>
                        </div>
                        <p class="text-xs text-secondary">₹1,00,000 Award</p>
                    </div>
                    
                    <div class="bg-bgColor border border-borderColor p-4 rounded-xl">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="p-2 bg-green-100 dark:bg-green-900/30 text-green-600 dark:text-green-400 rounded-lg">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                            </div>
                            <h4 class="font-bold text-primary text-sm">Excellence in Social Work & Leadership</h4>
                        </div>
                        <p class="text-xs text-secondary">₹20,000 Scholarship</p>
                    </div>

                    <div class="bg-bgColor border border-borderColor p-4 rounded-xl">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="p-2 bg-orange-100 dark:bg-orange-900/30 text-orange-600 dark:text-orange-400 rounded-lg">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                            </div>
                            <h4 class="font-bold text-primary text-sm">Bronze Medalist</h4>
                        </div>
                        <p class="text-xs text-secondary">Inter-IIT Tech Meet 8.0, IIT Roorkee</p>
                    </div>
                    
                    <div class="bg-bgColor border border-borderColor p-4 rounded-xl sm:col-span-2">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="p-2 bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 rounded-lg">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            </div>
                            <h4 class="font-bold text-primary text-sm">JEE Advanced</h4>
                        </div>
                        <p class="text-xs text-secondary">All India Rank (AIR) 3093</p>
                    </div>
                </div>
            </div>
"""
# we replace the old Pioneer Batch Gold Medal sentence at the bottom of the card with the new sections
old_medal = r'<div class="mt-4 pt-6 border-t border-borderColor text-center">\s*<p class="text-sm text-secondary">Recognized with the <strong>Pioneer Batch Gold Medal for Outstanding Leadership \(2022\)</strong> at IIT Gandhinagar.</p>\s*</div>'
content = re.sub(old_medal, new_sections, content)

with open('about.html', 'w') as f:
    f.write(content)

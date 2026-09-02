import re
import os
import glob
from tailwind_redesign import get_tailwind_head, get_header, get_footer

# 1. Update tailwind_redesign.py footer to include GoatCounter
with open('tailwind_redesign.py', 'r') as f:
    tw_content = f.read()

if 'gc.zgo.at/count.js' not in tw_content:
    new_footer_logic = """
    return f'''
    <!-- Footer -->
    <footer class="mt-auto border-t border-gray-200 bg-white py-8">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row justify-between items-center gap-4">
            <p class="text-sm text-secondary">© <span id="year"></span> Shivanshu Sharma. All rights reserved.</p>
            <div class="flex gap-4 items-center">
                <a href="https://23022000.goatcounter.com/" target="_blank" rel="noopener" class="opacity-70 hover:opacity-100 transition-opacity mr-2">
                    <img src="https://23022000.goatcounter.com/count?p=/&t=portfolio" width="auto" height="26" alt="Views">
                </a>
                <a href="https://github.com/5hivanshu-5harma" target="_blank" class="text-secondary hover:text-accent transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                </a>
                <a href="https://linkedin.com/in/5hivanshu-5harma-2302" target="_blank" class="text-secondary hover:text-accent transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>
            </div>
        </div>
    </footer>
    <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
    <script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''
"""
    tw_content = re.sub(r"return f'''\n    <!-- Footer -->.*?</html>\n'''", new_footer_logic.strip(), tw_content, flags=re.DOTALL)
    
    # We also need to add Campus Electricity back into projects/index.html generation in tailwind_redesign.py
    campus_block = """
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Campus Electricity Analysis</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Identified a 10% reduction potential (13 lakh kWh/year) in campus electricity consumption.</p>
                    <a href="./data-analyst-projects/campus-electricity/index.html" class="text-accent font-medium hover:underline mt-auto">View Project &rarr;</a>
                </div>
"""
    
    # Let's just insert it after the cohort block
    tw_content = tw_content.replace('<span class="text-gray-400 font-medium mt-auto cursor-not-allowed">Migrating soon</span>', '<a href="./data-analyst-projects/campus-electricity/index.html" class="text-accent font-medium hover:underline mt-auto">View Project &rarr;</a>')

    with open('tailwind_redesign.py', 'w') as f:
        f.write(tw_content)

# 2. Re-run tailwind redesign to update Home, About, and Projects pages
os.system('python3 tailwind_redesign.py')

# Also, wait! My tailwind_redesign.py was hardcoded with the OLD four blocks (without cohort retention). I need to make sure cohort is in it, or I just use replace on `projects/index.html` manually! 
# Oh right, my tailwind_redesign.py wasn't updated with the Cohort block!
# Let me just manually edit projects/index.html to add Campus Electricity and GoatCounter, then inject GoatCounter everywhere.


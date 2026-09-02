with open('projects/index.html', 'r') as f:
    content = f.read()

academic_section = """
        <!-- Academic Projects -->
        <section class="mt-16">
            <div class="flex items-center mb-8">
                <h2 class="text-2xl font-bold text-primary">Academic Projects (IIT Gandhinagar)</h2>
                <div class="h-px bg-gray-200 flex-grow ml-6"></div>
            </div>
            
            <div class="space-y-6">
                <!-- Project 1 -->
                <div class="bg-cardBg p-6 sm:p-8 rounded-xl border border-borderColor shadow-sm flex flex-col md:flex-row gap-6 hover:shadow-md transition-shadow">
                    <div class="md:w-1/3 flex-shrink-0 border-r border-transparent md:border-borderColor md:pr-6">
                        <h3 class="text-xl font-bold text-primary mb-2">Face Detection and Image Denoising</h3>
                        <p class="text-sm font-medium text-accent mb-2">Aug 2020 &ndash; Dec 2020</p>
                        <p class="text-xs text-secondary mb-4 uppercase tracking-wider font-semibold">IIT Gandhinagar</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Image Processing</span>
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Computer Vision</span>
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">MATLAB</span>
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Python</span>
                        </div>
                    </div>
                    <div class="md:w-2/3">
                        <p class="text-sm text-secondary font-medium mb-3">Mentored by <span class="text-primary font-semibold">Prof. Shanmuganathan Raman</span> (Dept. of Electrical Engineering)</p>
                        <ul class="list-disc pl-5 space-y-2 text-sm text-secondary leading-relaxed marker:text-accent">
                            <li>Designed and trained a custom XML Haar-cascade model utilizing a dataset of 18,000 samples for precise face detection.</li>
                            <li>Achieved an 80% accuracy rate, demonstrating significant improvements over standard pre-trained models.</li>
                            <li>Focused on enhancing detection performance and applying advanced denoising techniques to improve image clarity and model efficiency.</li>
                        </ul>
                    </div>
                </div>

                <!-- Project 2 -->
                <div class="bg-cardBg p-6 sm:p-8 rounded-xl border border-borderColor shadow-sm flex flex-col md:flex-row gap-6 hover:shadow-md transition-shadow">
                    <div class="md:w-1/3 flex-shrink-0 border-r border-transparent md:border-borderColor md:pr-6">
                        <h3 class="text-xl font-bold text-primary mb-2">Tiling a Floor Using Dominoes</h3>
                        <p class="text-sm font-medium text-accent mb-2">Apr 2019 &ndash; May 2019</p>
                        <p class="text-xs text-secondary mb-4 uppercase tracking-wider font-semibold">IIT Gandhinagar</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Discrete Mathematics</span>
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Logical Reasoning</span>
                        </div>
                    </div>
                    <div class="md:w-2/3">
                        <p class="text-sm text-secondary font-medium mb-3">Mentored by <span class="text-primary font-semibold">Prof. Neeldhara Misra</span> (Dept. of Computer Science)</p>
                        <ul class="list-disc pl-5 space-y-2 text-sm text-secondary leading-relaxed marker:text-accent">
                            <li>Collaborated with a team of five to solve the algorithmic problem of tiling a floor using 2x1 dominoes.</li>
                            <li>Successfully completed the project without prior formal knowledge of Discrete Mathematics, showcasing adaptability and a quick learning curve.</li>
                            <li>Executed as part of the MA201 coursework to leverage advanced problem-solving skills.</li>
                        </ul>
                    </div>
                </div>

                <!-- Project 3 -->
                <div class="bg-cardBg p-6 sm:p-8 rounded-xl border border-borderColor shadow-sm flex flex-col md:flex-row gap-6 hover:shadow-md transition-shadow">
                    <div class="md:w-1/3 flex-shrink-0 border-r border-transparent md:border-borderColor md:pr-6">
                        <h3 class="text-xl font-bold text-primary mb-2">Four-Wheeler Cycle Using 2 Bicycles</h3>
                        <p class="text-sm font-medium text-accent mb-2">Jan 2019 &ndash; Apr 2019</p>
                        <p class="text-xs text-secondary mb-4 uppercase tracking-wider font-semibold">IIT Gandhinagar</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Mechanical Engineering</span>
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Prototyping</span>
                            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-xs rounded-md">Fabrication</span>
                        </div>
                    </div>
                    <div class="md:w-2/3">
                        <p class="text-sm text-secondary font-medium mb-3">Mentored by <span class="text-primary font-semibold">Prof. Madhu Vadali</span> (Dept. of Mechanical Engineering)</p>
                        <ul class="list-disc pl-5 space-y-2 text-sm text-secondary leading-relaxed marker:text-accent">
                            <li>Engineered a rear-wheel-drive quad bike with a 50 kg payload capacity, designed for two riders using the Ackermann steering principle.</li>
                            <li>Collaborated with an 8-member team to design, fabricate, and combine two independent bicycles into a fully functional four-wheeler prototype.</li>
                            <li>Focused on the practical application of core mechanical engineering concepts under real-world constraints.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
"""

# Find where to insert it: right before the closing main tag
if "</main>" in content:
    content = content.replace("</main>", academic_section + "\n    </main>")

with open('projects/index.html', 'w') as f:
    f.write(content)

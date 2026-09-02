with open('projects/breathing-room/index.html', 'r') as f:
    content = f.read()

import re

# 1. Update the Controls UI
new_controls = """<!-- Controls -->
            <div class="flex flex-col items-center gap-6 mt-8">
                <!-- Counter -->
                <div class="bg-gray-800/50 backdrop-blur border border-gray-700 rounded-2xl px-8 py-4 text-center shadow-lg">
                    <p class="text-gray-400 text-sm font-medium uppercase tracking-wider mb-1">Sets Completed</p>
                    <div class="flex items-baseline justify-center gap-2">
                        <span id="setCount" class="text-4xl font-extrabold text-white">0</span>
                        <span class="text-gray-500 font-medium">/ 5 Recommended</span>
                    </div>
                </div>

                <!-- Buttons -->
                <div class="flex gap-4">
                    <button id="toggleBtn" class="flex items-center gap-2 px-6 py-3 rounded-xl bg-white text-gray-900 font-bold hover:bg-gray-200 transition-all shadow-lg hover:scale-105">
                        <svg id="pauseIcon" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
                        <svg id="playIcon" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"/></svg>
                        <span id="toggleText">Pause</span>
                    </button>
                    
                    <button id="resetBtn" class="flex items-center gap-2 px-6 py-3 rounded-xl bg-gray-800 text-white font-bold border border-gray-700 hover:bg-gray-700 transition-all shadow-lg hover:scale-105">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                        Reset
                    </button>
                </div>
            </div>"""

content = re.sub(r'<!-- Controls -->.*?</div>', new_controls, content, flags=re.DOTALL)


# 2. Update the JavaScript
new_js = """<script>
        const wrapper = document.getElementById('breatheWrapper');
        const animatedCircle = wrapper.querySelector('.animate-breathe');
        const btn = document.getElementById('toggleBtn');
        const playIcon = document.getElementById('playIcon');
        const pauseIcon = document.getElementById('pauseIcon');
        const toggleText = document.getElementById('toggleText');
        const resetBtn = document.getElementById('resetBtn');
        const setCountEl = document.getElementById('setCount');
        
        let isPlaying = true;
        let sets = 0;

        // Toggle Play/Pause
        btn.addEventListener('click', () => {
            if(isPlaying) {
                wrapper.classList.add('paused');
                playIcon.classList.remove('hidden');
                pauseIcon.classList.add('hidden');
                toggleText.textContent = "Resume";
            } else {
                wrapper.classList.remove('paused');
                playIcon.classList.add('hidden');
                pauseIcon.classList.remove('hidden');
                toggleText.textContent = "Pause";
            }
            isPlaying = !isPlaying;
        });

        // Reset Animation and Counter
        resetBtn.addEventListener('click', () => {
            // Reset state
            sets = 0;
            setCountEl.textContent = sets;
            setCountEl.classList.remove('text-green-400');
            
            // Force reflow to restart animation from 0%
            animatedCircle.classList.remove('animate-breathe');
            void animatedCircle.offsetWidth; // magic reflow
            animatedCircle.classList.add('animate-breathe');
            
            // If it was paused, resume it
            if(!isPlaying) {
                wrapper.classList.remove('paused');
                playIcon.classList.add('hidden');
                pauseIcon.classList.remove('hidden');
                toggleText.textContent = "Pause";
                isPlaying = true;
            }
        });

        // Track completed sets via animation loop event
        animatedCircle.addEventListener('animationiteration', () => {
            sets++;
            setCountEl.textContent = sets;
            
            // Add a fun success color if they hit the recommendation
            if (sets >= 5) {
                setCountEl.classList.add('text-green-400');
            }
        });
    </script>"""

content = re.sub(r'<script>.*?</script>', new_js, content, flags=re.DOTALL)

with open('projects/breathing-room/index.html', 'w') as f:
    f.write(content)

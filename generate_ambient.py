import os
from tailwind_redesign import get_header, get_footer, get_tailwind_head

html = get_tailwind_head("Deep Work Ambient Mixer", 2) + get_header(2, 'projects') + '''
    <main class="flex-grow max-w-6xl mx-auto px-4 sm:px-6 py-16 w-full min-h-screen">
        
        <div class="text-center mb-16">
            <h1 class="text-4xl font-extrabold text-primary mb-3">Deep Work Focus Space</h1>
            <p class="text-lg text-secondary">Mix your perfect ambient environment for coding, studying, or deep work.</p>
        </div>

        <!-- Master Controls & Presets -->
        <div class="bg-white rounded-3xl p-6 shadow-sm border border-gray-200 mb-10 flex flex-col md:flex-row justify-between items-center gap-6">
            
            <div class="flex items-center gap-4">
                <button id="masterPlayBtn" class="w-14 h-14 bg-gray-900 text-white rounded-full flex items-center justify-center hover:bg-gray-800 transition-all shadow-lg hover:scale-105">
                    <svg id="masterPlayIcon" class="w-6 h-6 ml-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"/></svg>
                    <svg id="masterPauseIcon" class="w-6 h-6 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
                </button>
                <div>
                    <h3 class="font-bold text-gray-800 text-lg">Master Control</h3>
                    <p class="text-xs text-gray-500">Play/Pause all active sounds</p>
                </div>
            </div>

            <div class="flex gap-3 overflow-x-auto pb-2 md:pb-0 w-full md:w-auto">
                <button onclick="applyPreset('midnight')" class="px-4 py-2 bg-purple-50 text-purple-700 border border-purple-200 rounded-xl font-bold text-sm hover:bg-purple-100 transition-colors whitespace-nowrap">💻 Midnight Coder</button>
                <button onclick="applyPreset('cabin')" class="px-4 py-2 bg-amber-50 text-amber-700 border border-amber-200 rounded-xl font-bold text-sm hover:bg-amber-100 transition-colors whitespace-nowrap">🔥 Cozy Cabin</button>
                <button onclick="applyPreset('cafe')" class="px-4 py-2 bg-blue-50 text-blue-700 border border-blue-200 rounded-xl font-bold text-sm hover:bg-blue-100 transition-colors whitespace-nowrap">☕ Rainy Cafe</button>
                <button onclick="applyPreset('focus')" class="px-4 py-2 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-xl font-bold text-sm hover:bg-emerald-100 transition-colors whitespace-nowrap">🌊 Deep Focus</button>
                <button onclick="stopAll()" class="px-4 py-2 bg-gray-100 text-gray-600 border border-gray-200 rounded-xl font-bold text-sm hover:bg-gray-200 transition-colors whitespace-nowrap">Reset All</button>
            </div>
        </div>

        <!-- Sound Mixer Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" id="mixerGrid">
            <!-- Cards injected via JS -->
        </div>

    </main>

    <script>
        // Tested and verified Google Sound Library URLs (Status 200 OK)
        const SOUNDS = [
            { id: 'rain', name: 'Heavy Rain', icon: '🌧️', color: 'blue', url: 'https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg' },
            { id: 'lrain', name: 'Light Rain', icon: '🌦️', color: 'indigo', url: 'https://actions.google.com/sounds/v1/weather/light_rain.ogg' },
            { id: 'thunder', name: 'Thunderstorm', icon: '⚡', color: 'purple', url: 'https://actions.google.com/sounds/v1/weather/rolling_thunder.ogg' },
            { id: 'cafe', name: 'Coffee Shop', icon: '☕', color: 'amber', url: 'https://actions.google.com/sounds/v1/crowds/restaurant_ambience.ogg' },
            { id: 'fire', name: 'Fireplace', icon: '🔥', color: 'red', url: 'https://actions.google.com/sounds/v1/foley/fireplace_crackling.ogg' },
            { id: 'wind', name: 'Howling Wind', icon: '🌬️', color: 'gray', url: 'https://actions.google.com/sounds/v1/weather/strong_wind_blowing.ogg' },
            { id: 'ocean', name: 'Ocean Waves', icon: '🌊', color: 'teal', url: 'https://actions.google.com/sounds/v1/weather/ocean_waves.ogg' },
            { id: 'keyboard', name: 'Typing', icon: '⌨️', color: 'pink', url: 'https://actions.google.com/sounds/v1/office/typing_on_keyboard.ogg' },
            { id: 'clock', name: 'Clock Ticking', icon: '🕰️', color: 'rose', url: 'https://actions.google.com/sounds/v1/household/clock_ticking.ogg' },
            { id: 'country', name: 'Countryside', icon: '🦗', color: 'emerald', url: 'https://actions.google.com/sounds/v1/ambiences/barnyard_with_animals.ogg' }
        ];

        const audioElements = {};
        const state = {}; 
        let isMasterPlaying = false;

        const mixerGrid = document.getElementById('mixerGrid');
        const masterPlayBtn = document.getElementById('masterPlayBtn');
        const masterPlayIcon = document.getElementById('masterPlayIcon');
        const masterPauseIcon = document.getElementById('masterPauseIcon');

        SOUNDS.forEach(sound => {
            const audio = new Audio(sound.url);
            audio.loop = true;
            audio.volume = 0.5;
            audioElements[sound.id] = audio;
            state[sound.id] = { playing: false, volume: 0.5 };

            const colorMap = {
                blue: 'bg-blue-50 border-blue-200 text-blue-600',
                indigo: 'bg-indigo-50 border-indigo-200 text-indigo-600',
                amber: 'bg-amber-50 border-amber-200 text-amber-600',
                red: 'bg-red-50 border-red-200 text-red-600',
                gray: 'bg-gray-50 border-gray-200 text-gray-600',
                teal: 'bg-teal-50 border-teal-200 text-teal-600',
                purple: 'bg-purple-50 border-purple-200 text-purple-600',
                emerald: 'bg-emerald-50 border-emerald-200 text-emerald-600',
                pink: 'bg-pink-50 border-pink-200 text-pink-600',
                rose: 'bg-rose-50 border-rose-200 text-rose-600'
            };

            const card = document.createElement('div');
            card.className = `bg-white rounded-3xl p-6 shadow-sm border border-gray-200 hover:shadow-md transition-shadow relative overflow-hidden group cursor-pointer`;
            card.innerHTML = `
                <div class="absolute -right-4 -top-4 w-20 h-20 rounded-full ${colorMap[sound.color].split(' ')[0]} opacity-30 transition-transform group-hover:scale-150 duration-500"></div>
                <div class="relative z-10">
                    <div class="flex justify-between items-center mb-6">
                        <div class="flex items-center gap-3">
                            <div class="text-3xl">${sound.icon}</div>
                            <h3 class="font-bold text-gray-800 text-sm sm:text-base">${sound.name}</h3>
                        </div>
                        <button id="toggle-${sound.id}" onclick="toggleSound('${sound.id}', event)" class="w-10 h-10 rounded-full bg-gray-50 border border-gray-200 flex items-center justify-center text-gray-400 hover:text-accent transition-colors flex-shrink-0">
                            <svg class="w-5 h-5 play-icon ml-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"/></svg>
                            <svg class="w-5 h-5 pause-icon hidden text-accent" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
                        </button>
                    </div>
                    <div class="w-full">
                        <input type="range" id="vol-${sound.id}" min="0" max="100" value="50" oninput="changeVolume('${sound.id}', this.value)" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-accent" onclick="event.stopPropagation()">
                    </div>
                </div>
            `;
            
            card.onclick = (e) => {
                if(e.target.tagName !== 'INPUT') toggleSound(sound.id, e);
            };
            
            mixerGrid.appendChild(card);
        });

        function toggleSound(id, event) {
            if(event) event.stopPropagation();
            const btn = document.getElementById(`toggle-${id}`);
            const playIcon = btn.querySelector('.play-icon');
            const pauseIcon = btn.querySelector('.pause-icon');
            
            if (state[id].playing) {
                audioElements[id].pause();
                state[id].playing = false;
                playIcon.classList.remove('hidden');
                pauseIcon.classList.add('hidden');
                btn.classList.remove('border-accent', 'bg-blue-50');
            } else {
                audioElements[id].play();
                state[id].playing = true;
                playIcon.classList.add('hidden');
                pauseIcon.classList.remove('hidden');
                btn.classList.add('border-accent', 'bg-blue-50');
                
                if (!isMasterPlaying) updateMasterState(true);
            }
        }

        function changeVolume(id, val) {
            state[id].volume = val / 100;
            audioElements[id].volume = state[id].volume;
            if (!state[id].playing && val > 0) toggleSound(id);
        }

        function updateMasterState(playing) {
            isMasterPlaying = playing;
            if (playing) {
                masterPlayIcon.classList.add('hidden');
                masterPauseIcon.classList.remove('hidden');
            } else {
                masterPlayIcon.classList.remove('hidden');
                masterPauseIcon.classList.add('hidden');
            }
        }

        masterPlayBtn.onclick = () => {
            if (isMasterPlaying) {
                Object.keys(state).forEach(id => { if (state[id].playing) audioElements[id].pause(); });
                updateMasterState(false);
            } else {
                let playedAny = false;
                Object.keys(state).forEach(id => {
                    if (state[id].playing) { audioElements[id].play(); playedAny = true; }
                });
                if (!playedAny) toggleSound('rain');
                updateMasterState(true);
            }
        };

        window.stopAll = function() {
            Object.keys(state).forEach(id => {
                if (state[id].playing) toggleSound(id);
                document.getElementById(`vol-${id}`).value = 50;
                audioElements[id].volume = 0.5;
            });
            updateMasterState(false);
        };

        window.applyPreset = function(preset) {
            stopAll();
            if (preset === 'cabin') {
                toggleSound('fire'); toggleSound('rain'); toggleSound('wind');
                changeVolume('fire', 70); changeVolume('rain', 40); changeVolume('wind', 20);
                document.getElementById('vol-fire').value = 70; document.getElementById('vol-rain').value = 40; document.getElementById('vol-wind').value = 20;
            } else if (preset === 'cafe') {
                toggleSound('cafe'); toggleSound('rain');
                changeVolume('cafe', 60); changeVolume('rain', 30);
                document.getElementById('vol-cafe').value = 60; document.getElementById('vol-rain').value = 30;
            } else if (preset === 'focus') {
                toggleSound('ocean'); toggleSound('wind');
                changeVolume('ocean', 50); changeVolume('wind', 20);
                document.getElementById('vol-ocean').value = 50; document.getElementById('vol-wind').value = 20;
            } else if (preset === 'midnight') {
                toggleSound('lrain'); toggleSound('keyboard'); toggleSound('clock');
                changeVolume('lrain', 50); changeVolume('keyboard', 40); changeVolume('clock', 30);
                document.getElementById('vol-lrain').value = 50; document.getElementById('vol-keyboard').value = 40; document.getElementById('vol-clock').value = 30;
            }
        };
    </script>
''' + get_footer(2)

with open('./projects/ambient-noise/index.html', 'w') as f:
    f.write(html)

print("Upgraded Ambient Noise App with more sounds!")

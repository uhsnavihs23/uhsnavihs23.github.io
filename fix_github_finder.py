import os

from tailwind_redesign import get_header, get_footer, get_tailwind_head

html = get_tailwind_head("GitHub Profile Finder", 2) + get_header(2, 'projects') + '''
    <main class="flex-grow max-w-4xl mx-auto px-4 sm:px-6 py-12 w-full">
        
        <div class="text-center mb-10">
            <h1 class="text-3xl font-extrabold text-primary mb-3">GitHub Profile Finder</h1>
            <p class="text-secondary text-lg">Search for any GitHub user to view their profile, stats, and latest repositories.</p>
        </div>

        <!-- Search Bar -->
        <div class="max-w-xl mx-auto mb-10 relative">
            <div class="relative flex items-center">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </div>
                <input type="text" id="searchInput" class="w-full pl-12 pr-24 py-4 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent text-lg shadow-sm" placeholder="Enter GitHub username (e.g. torvalds)..." autocomplete="off">
                <button id="searchBtn" class="absolute right-2 inset-y-2 bg-accent hover:bg-blue-700 text-white font-medium rounded-lg px-6 transition-colors shadow-sm">
                    Search
                </button>
            </div>
            <p id="errorMsg" class="text-red-500 text-sm font-medium mt-2 hidden text-center"></p>
        </div>

        <!-- Loading State -->
        <div id="loadingState" class="hidden flex justify-center py-10">
            <svg class="animate-spin h-10 w-10 text-accent" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
        </div>

        <!-- Result Container -->
        <div id="profileContainer" class="hidden">
            <!-- Profile Card -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden mb-8">
                <div class="h-32 bg-gradient-to-r from-blue-600 to-indigo-700"></div>
                <div class="px-8 pb-8 relative">
                    <img id="avatar" src="" alt="Avatar" class="w-32 h-32 rounded-full border-4 border-white shadow-lg absolute -top-16 bg-white">
                    <div class="mt-20 flex flex-col md:flex-row justify-between md:items-end gap-4">
                        <div>
                            <h2 id="name" class="text-3xl font-extrabold text-primary"></h2>
                            <a id="usernameLink" href="" target="_blank" class="text-accent hover:underline font-medium text-lg flex items-center mt-1">
                                @<span id="username"></span>
                            </a>
                        </div>
                        <a id="githubBtn" href="" target="_blank" class="inline-flex items-center px-5 py-2.5 bg-gray-900 hover:bg-gray-800 text-white rounded-lg font-medium transition-colors shadow-sm">
                            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                            View on GitHub
                        </a>
                    </div>
                    <p id="bio" class="text-secondary mt-6 text-lg"></p>
                    
                    <div class="mt-6 flex flex-wrap gap-4 text-sm text-secondary font-medium">
                        <div class="flex items-center bg-gray-100 px-3 py-1.5 rounded-lg">
                            <svg class="w-4 h-4 mr-1.5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.243-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            <span id="location">Not provided</span>
                        </div>
                        <div class="flex items-center bg-gray-100 px-3 py-1.5 rounded-lg">
                            <svg class="w-4 h-4 mr-1.5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
                            <a id="blog" href="#" target="_blank" class="hover:text-accent hover:underline truncate max-w-[200px]">Not provided</a>
                        </div>
                        <div class="flex items-center bg-gray-100 px-3 py-1.5 rounded-lg">
                            <svg class="w-4 h-4 mr-1.5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                            Joined <span id="joined" class="ml-1"></span>
                        </div>
                    </div>

                    <div class="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-blue-50 border border-blue-100 p-4 rounded-xl text-center">
                            <div class="text-3xl font-extrabold text-blue-700" id="repos">0</div>
                            <div class="text-sm font-semibold text-blue-600 uppercase tracking-wide mt-1">Repositories</div>
                        </div>
                        <div class="bg-indigo-50 border border-indigo-100 p-4 rounded-xl text-center">
                            <div class="text-3xl font-extrabold text-indigo-700" id="followers">0</div>
                            <div class="text-sm font-semibold text-indigo-600 uppercase tracking-wide mt-1">Followers</div>
                        </div>
                        <div class="bg-emerald-50 border border-emerald-100 p-4 rounded-xl text-center">
                            <div class="text-3xl font-extrabold text-emerald-700" id="following">0</div>
                            <div class="text-sm font-semibold text-emerald-600 uppercase tracking-wide mt-1">Following</div>
                        </div>
                        <div class="bg-amber-50 border border-amber-100 p-4 rounded-xl text-center">
                            <div class="text-3xl font-extrabold text-amber-700" id="gists">0</div>
                            <div class="text-sm font-semibold text-amber-600 uppercase tracking-wide mt-1">Gists</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Repositories List -->
            <div>
                <h3 class="text-2xl font-bold text-primary mb-4 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-secondary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 19a2 2 0 01-2-2V7a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1M5 19h14a2 2 0 002-2v-5a2 2 0 00-2-2H9a2 2 0 00-2 2v5a2 2 0 01-2 2z"></path></svg>
                    Latest Repositories
                </h3>
                <div id="repoList" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Repos will be injected here -->
                </div>
            </div>
        </div>

    </main>

    <script>
        const searchBtn = document.getElementById('searchBtn');
        const searchInput = document.getElementById('searchInput');
        const profileContainer = document.getElementById('profileContainer');
        const loadingState = document.getElementById('loadingState');
        const errorMsg = document.getElementById('errorMsg');

        searchBtn.addEventListener('click', fetchProfile);
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') fetchProfile();
        });

        async function fetchProfile() {
            const username = searchInput.value.trim();
            if (!username) return;

            errorMsg.classList.add('hidden');
            profileContainer.classList.add('hidden');
            loadingState.classList.remove('hidden');

            try {
                const res = await fetch(`https://api.github.com/users/${username}`);
                if (!res.ok) {
                    throw new Error('User not found');
                }
                const data = await res.json();
                
                // Fetch repos
                const repoRes = await fetch(`https://api.github.com/users/${username}/repos?sort=updated&per_page=6`);
                const repos = await repoRes.json();

                renderProfile(data);
                renderRepos(repos);
                
                loadingState.classList.add('hidden');
                profileContainer.classList.remove('hidden');
            } catch (err) {
                loadingState.classList.add('hidden');
                errorMsg.textContent = err.message;
                errorMsg.classList.remove('hidden');
            }
        }

        function renderProfile(data) {
            document.getElementById('avatar').src = data.avatar_url;
            document.getElementById('name').textContent = data.name || data.login;
            document.getElementById('username').textContent = data.login;
            document.getElementById('usernameLink').href = data.html_url;
            document.getElementById('githubBtn').href = data.html_url;
            
            document.getElementById('bio').textContent = data.bio || 'This user has no bio.';
            
            document.getElementById('location').textContent = data.location || 'Not provided';
            
            const blog = document.getElementById('blog');
            if (data.blog) {
                blog.textContent = data.blog.replace(/^https?:\/\//, '');
                blog.href = data.blog.startsWith('http') ? data.blog : 'https://' + data.blog;
            } else {
                blog.textContent = 'Not provided';
                blog.href = '#';
            }

            const joinDate = new Date(data.created_at);
            document.getElementById('joined').textContent = joinDate.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });

            document.getElementById('repos').textContent = data.public_repos;
            document.getElementById('followers').textContent = data.followers;
            document.getElementById('following').textContent = data.following;
            document.getElementById('gists').textContent = data.public_gists;
        }

        function renderRepos(repos) {
            const repoList = document.getElementById('repoList');
            repoList.innerHTML = '';

            if (repos.length === 0) {
                repoList.innerHTML = '<p class="text-secondary col-span-2">No public repositories found.</p>';
                return;
            }

            repos.forEach(repo => {
                const desc = repo.description ? (repo.description.length > 80 ? repo.description.substring(0, 80) + '...' : repo.description) : 'No description provided.';
                const lang = repo.language || 'Unknown';
                const stars = repo.stargazers_count;
                
                repoList.innerHTML += `
                    <a href="${repo.html_url}" target="_blank" class="block bg-white p-6 rounded-xl shadow-sm border border-gray-200 hover:shadow-md hover:border-accent transition-all">
                        <h4 class="text-lg font-bold text-accent mb-2 truncate">${repo.name}</h4>
                        <p class="text-sm text-secondary mb-4 h-10">${desc}</p>
                        <div class="flex items-center justify-between text-xs font-semibold text-gray-500">
                            <span class="flex items-center"><span class="w-3 h-3 rounded-full bg-indigo-500 mr-2"></span>${lang}</span>
                            <span class="flex items-center"><svg class="w-4 h-4 mr-1 text-amber-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>${stars}</span>
                        </div>
                    </a>
                `;
            });
        }
    </script>
''' + get_footer(2)

with open('./projects/github-profile-finder/index.html', 'w') as f:
    f.write(html)

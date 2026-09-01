import re

# 1. UPGRADE NEWS APP
news_html = """
    <main class="flex-grow max-w-6xl mx-auto px-4 sm:px-6 py-12 w-full">
        <div class="flex flex-col md:flex-row justify-between items-end mb-8 border-b border-gray-200 pb-6 gap-4">
            <div>
                <h1 class="text-4xl font-extrabold text-primary mb-2">Global News Hub</h1>
                <p class="text-secondary text-lg">Real-time aggregated headlines from trusted sources worldwide.</p>
            </div>
            <div class="flex gap-4">
                <select id="topicSelect" class="bg-gray-50 border border-gray-300 text-primary text-sm rounded-lg focus:ring-accent focus:border-accent block p-2.5 shadow-sm">
                    <option value="world">World News</option>
                    <option value="technology">Technology</option>
                    <option value="business">Business</option>
                    <option value="science">Science</option>
                    <option value="sports">Sports</option>
                </select>
                <select id="regionSelect" class="bg-gray-50 border border-gray-300 text-primary text-sm rounded-lg focus:ring-accent focus:border-accent block p-2.5 shadow-sm">
                    <option value="us">Global (US)</option>
                    <option value="in">India</option>
                    <option value="uk">United Kingdom</option>
                </select>
                <button id="refreshBtn" class="bg-accent hover:bg-blue-700 text-white font-medium rounded-lg text-sm px-5 py-2.5 transition-colors shadow-sm flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                    Refresh
                </button>
            </div>
        </div>

        <div id="loading" class="hidden flex justify-center py-20">
            <svg class="animate-spin h-10 w-10 text-accent" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
        </div>

        <div id="newsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- News articles injected here -->
        </div>
    </main>

    <script>
        const newsGrid = document.getElementById('newsGrid');
        const loading = document.getElementById('loading');
        const topicSelect = document.getElementById('topicSelect');
        const regionSelect = document.getElementById('regionSelect');
        const refreshBtn = document.getElementById('refreshBtn');

        const RSS_FEEDS = {
            world: {
                us: ['http://feeds.bbci.co.uk/news/world/rss.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml'],
                in: ['https://timesofindia.indiatimes.com/rssfeedstopstories.cms', 'https://www.thehindu.com/news/national/feeder/default.rss'],
                uk: ['http://feeds.bbci.co.uk/news/uk/rss.xml', 'https://www.theguardian.com/uk/rss']
            },
            technology: {
                us: ['https://techcrunch.com/feed/', 'https://www.theverge.com/rss/index.xml'],
                in: ['https://timesofindia.indiatimes.com/rssfeeds/66949542.cms'],
                uk: ['http://feeds.bbci.co.uk/news/technology/rss.xml']
            },
            business: {
                us: ['https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml', 'https://search.cnbc.com/rs/search/combinedcms/view.xml?id=10001147'],
                in: ['https://economictimes.indiatimes.com/rssfeedsdefault.cms'],
                uk: ['http://feeds.bbci.co.uk/news/business/rss.xml']
            },
            science: { default: ['https://www.sciencedaily.com/rss/all.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/Science.xml'] },
            sports: { default: ['http://feeds.bbci.co.uk/sport/rss.xml', 'https://www.espn.com/espn/rss/news'] }
        };

        async function fetchNews() {
            newsGrid.innerHTML = '';
            loading.classList.remove('hidden');
            
            const topic = topicSelect.value;
            const region = regionSelect.value;
            
            let feeds = [];
            if (RSS_FEEDS[topic][region]) {
                feeds = RSS_FEEDS[topic][region];
            } else if (RSS_FEEDS[topic]['default']) {
                feeds = RSS_FEEDS[topic]['default'];
            } else {
                feeds = RSS_FEEDS[topic]['us'];
            }

            let allArticles = [];
            
            for (let feedUrl of feeds) {
                try {
                    const res = await fetch(`https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(feedUrl)}&api_key=`);
                    const data = await res.json();
                    if (data.items) {
                        data.items.forEach(item => {
                            // clean up description
                            let desc = item.description.replace(/<[^>]*>?/gm, '').substring(0, 150) + '...';
                            let image = item.enclosure?.link || item.thumbnail || 'https://images.unsplash.com/photo-1585829365295-ab7cd400c167?w=800&q=80';
                            
                            allArticles.push({
                                title: item.title,
                                link: item.link,
                                pubDate: new Date(item.pubDate.replace(/-/g, '/')),
                                source: data.feed.title,
                                description: desc,
                                image: image
                            });
                        });
                    }
                } catch(e) { console.error("Failed fetching", feedUrl); }
            }

            // Sort by latest
            allArticles.sort((a,b) => b.pubDate - a.pubDate);
            
            loading.classList.add('hidden');
            
            if(allArticles.length === 0) {
                newsGrid.innerHTML = '<div class="col-span-3 text-center text-gray-500 py-10 text-xl">Could not load news at this time. Please try again.</div>';
                return;
            }

            allArticles.forEach(article => {
                const timeStr = article.pubDate.toLocaleTimeString('en-US', {hour: '2-digit', minute:'2-digit'});
                const dateStr = article.pubDate.toLocaleDateString('en-US', {month: 'short', day: 'numeric'});
                
                newsGrid.innerHTML += `
                    <a href="${article.link}" target="_blank" class="flex flex-col bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-xl transition-all duration-300 group">
                        <div class="h-48 overflow-hidden bg-gray-100">
                            <img src="${article.image}" onerror="this.src='https://images.unsplash.com/photo-1585829365295-ab7cd400c167?w=800&q=80'" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="p-6 flex flex-col flex-grow">
                            <div class="flex justify-between items-center mb-3">
                                <span class="text-xs font-bold text-accent uppercase tracking-wider">${article.source}</span>
                                <span class="text-xs font-medium text-gray-500">${dateStr} • ${timeStr}</span>
                            </div>
                            <h3 class="text-xl font-bold text-primary mb-3 group-hover:text-accent transition-colors leading-tight">${article.title}</h3>
                            <p class="text-sm text-secondary flex-grow">${article.description}</p>
                        </div>
                    </a>
                `;
            });
        }

        topicSelect.addEventListener('change', fetchNews);
        regionSelect.addEventListener('change', fetchNews);
        refreshBtn.addEventListener('click', fetchNews);
        
        // Initial fetch
        fetchNews();
    </script>
"""

with open('./projects/news-app/index.html', 'r') as f:
    content = f.read()
    
# Remove raw tags if any
content = content.replace('{% raw %}', '').replace('{% endraw %}', '')
# Replace main block
content = re.sub(r'<main.*?</main>', news_html, content, flags=re.DOTALL)
if 'https://cdn.tailwindcss.com' not in content:
    content = content.replace('</head>', '<script src="https://cdn.tailwindcss.com"></script></head>')

with open('./projects/news-app/index.html', 'w') as f:
    f.write(content)
    
print("News App upgraded.")


# 2. UPGRADE GITHUB PROFILE FINDER
github_html = """
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <main class="flex-grow max-w-6xl mx-auto px-4 sm:px-6 py-12 w-full">
        
        <div class="text-center mb-12">
            <h1 class="text-4xl font-extrabold text-primary mb-3">GitHub Analytics Dashboard</h1>
            <p class="text-secondary text-lg">Comprehensive insights, language breakdown, and repository analysis for any GitHub developer.</p>
        </div>

        <!-- Search Bar -->
        <div class="max-w-2xl mx-auto mb-12 relative">
            <div class="relative flex items-center shadow-lg rounded-2xl overflow-hidden">
                <div class="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none bg-white">
                    <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </div>
                <input type="text" id="searchInput" class="w-full pl-14 pr-32 py-5 border-0 focus:ring-2 focus:ring-accent text-lg" placeholder="Enter GitHub username (e.g. torvalds)..." autocomplete="off">
                <button id="searchBtn" class="absolute right-2 top-2 bottom-2 bg-accent hover:bg-blue-700 text-white font-bold rounded-xl px-8 transition-colors">
                    Analyze
                </button>
            </div>
            <p id="errorMsg" class="text-red-500 text-sm font-medium mt-3 hidden text-center bg-red-50 py-2 rounded-lg"></p>
        </div>

        <!-- Loading State -->
        <div id="loadingState" class="hidden flex flex-col items-center justify-center py-20">
            <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-accent mb-4"></div>
            <p class="text-secondary font-medium animate-pulse">Fetching 100+ data points from GitHub API...</p>
        </div>

        <!-- Result Container -->
        <div id="profileContainer" class="hidden">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Profile Sidebar -->
                <div class="lg:col-span-1 space-y-6">
                    <div class="bg-white rounded-3xl shadow-sm border border-gray-200 p-8 text-center relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-32 bg-gradient-to-br from-gray-900 to-gray-800"></div>
                        <img id="avatar" src="" class="w-40 h-40 rounded-full border-4 border-white shadow-xl mx-auto relative z-10 bg-white object-cover">
                        <h2 id="name" class="text-3xl font-extrabold text-primary mt-4"></h2>
                        <a id="usernameLink" href="" target="_blank" class="text-accent hover:underline font-medium text-lg inline-block mb-4">
                            @<span id="username"></span>
                        </a>
                        <p id="bio" class="text-secondary text-base mb-6 leading-relaxed"></p>
                        
                        <div class="flex flex-col gap-3 text-sm text-left font-medium text-gray-600 bg-gray-50 p-5 rounded-2xl">
                            <div class="flex items-center"><svg class="w-5 h-5 mr-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.243-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg><span id="location" class="truncate"></span></div>
                            <div class="flex items-center"><svg class="w-5 h-5 mr-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg><span id="company" class="truncate"></span></div>
                            <div class="flex items-center"><svg class="w-5 h-5 mr-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg><a id="blog" href="#" target="_blank" class="hover:text-accent truncate"></a></div>
                        </div>
                        <a id="githubBtn" href="" target="_blank" class="mt-6 w-full inline-flex justify-center items-center px-5 py-3 bg-gray-900 hover:bg-gray-800 text-white rounded-xl font-bold transition-colors">
                            View GitHub Profile
                        </a>
                    </div>
                </div>

                <!-- Analytics Main Content -->
                <div class="lg:col-span-2 space-y-8">
                    <!-- Stats Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                        <div class="bg-white border border-gray-200 p-6 rounded-3xl shadow-sm text-center transform hover:-translate-y-1 transition-transform">
                            <div class="text-4xl font-black text-primary" id="repos">0</div>
                            <div class="text-sm font-bold text-gray-400 uppercase tracking-wider mt-2">Repositories</div>
                        </div>
                        <div class="bg-white border border-gray-200 p-6 rounded-3xl shadow-sm text-center transform hover:-translate-y-1 transition-transform">
                            <div class="text-4xl font-black text-accent" id="followers">0</div>
                            <div class="text-sm font-bold text-gray-400 uppercase tracking-wider mt-2">Followers</div>
                        </div>
                        <div class="bg-white border border-gray-200 p-6 rounded-3xl shadow-sm text-center transform hover:-translate-y-1 transition-transform">
                            <div class="text-4xl font-black text-emerald-500" id="stars">0</div>
                            <div class="text-sm font-bold text-gray-400 uppercase tracking-wider mt-2">Total Stars</div>
                        </div>
                        <div class="bg-white border border-gray-200 p-6 rounded-3xl shadow-sm text-center transform hover:-translate-y-1 transition-transform">
                            <div class="text-4xl font-black text-amber-500" id="gists">0</div>
                            <div class="text-sm font-bold text-gray-400 uppercase tracking-wider mt-2">Gists</div>
                        </div>
                    </div>

                    <!-- Chart -->
                    <div class="bg-white border border-gray-200 p-8 rounded-3xl shadow-sm">
                        <h3 class="text-xl font-bold text-primary mb-6 border-b border-gray-100 pb-4">Top Languages Breakdown</h3>
                        <div class="h-64 relative w-full flex justify-center">
                            <canvas id="languageChart"></canvas>
                        </div>
                    </div>

                    <!-- Repositories List -->
                    <div class="bg-white border border-gray-200 p-8 rounded-3xl shadow-sm">
                        <h3 class="text-xl font-bold text-primary mb-6 border-b border-gray-100 pb-4">Top Starred Repositories</h3>
                        <div id="repoList" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <!-- Repos will be injected here -->
                        </div>
                    </div>
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
        let chartInstance = null;

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
                if (!res.ok) throw new Error('User not found on GitHub.');
                const data = await res.json();
                
                // Fetch up to 100 repos to calculate true stats
                const repoRes = await fetch(`https://api.github.com/users/${username}/repos?per_page=100&sort=pushed`);
                const repos = await repoRes.json();

                renderProfile(data);
                renderAnalytics(repos);
                
                loadingState.classList.add('hidden');
                profileContainer.classList.remove('hidden');
            } catch (err) {
                loadingState.classList.add('hidden');
                errorMsg.innerHTML = `<svg class="w-5 h-5 inline mr-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg> ${err.message}`;
                errorMsg.classList.remove('hidden');
            }
        }

        function renderProfile(data) {
            document.getElementById('avatar').src = data.avatar_url;
            document.getElementById('name').textContent = data.name || data.login;
            document.getElementById('username').textContent = data.login;
            document.getElementById('usernameLink').href = data.html_url;
            document.getElementById('githubBtn').href = data.html_url;
            document.getElementById('bio').textContent = data.bio || 'No bio provided.';
            document.getElementById('location').textContent = data.location || 'Unknown location';
            document.getElementById('company').textContent = data.company || 'Independent';
            
            const blog = document.getElementById('blog');
            if (data.blog) {
                blog.textContent = data.blog.replace(/^https?:\\/\\//, '');
                blog.href = data.blog.startsWith('http') ? data.blog : 'https://' + data.blog;
            } else {
                blog.textContent = 'No website';
                blog.href = '#';
            }

            document.getElementById('repos').textContent = data.public_repos;
            document.getElementById('followers').textContent = data.followers;
            document.getElementById('gists').textContent = data.public_gists;
        }

        function renderAnalytics(repos) {
            let totalStars = 0;
            const langCounts = {};

            repos.forEach(repo => {
                totalStars += repo.stargazers_count;
                if(repo.language) {
                    langCounts[repo.language] = (langCounts[repo.language] || 0) + 1;
                }
            });

            document.getElementById('stars').textContent = totalStars;

            // Sort repos by stars
            repos.sort((a,b) => b.stargazers_count - a.stargazers_count);
            const topRepos = repos.slice(0, 6);
            
            const repoList = document.getElementById('repoList');
            repoList.innerHTML = '';
            
            if(topRepos.length === 0) {
                repoList.innerHTML = '<p class="col-span-2 text-gray-500">No public repositories to analyze.</p>';
            } else {
                topRepos.forEach(repo => {
                    const lang = repo.language || '-';
                    repoList.innerHTML += `
                        <a href="${repo.html_url}" target="_blank" class="block bg-gray-50 p-5 rounded-2xl border border-gray-200 hover:border-accent hover:shadow-md transition-all">
                            <h4 class="text-lg font-bold text-primary mb-1 truncate group-hover:text-accent">${repo.name}</h4>
                            <p class="text-sm text-gray-500 mb-4 h-10 overflow-hidden">${repo.description || 'No description'}</p>
                            <div class="flex items-center justify-between text-xs font-bold">
                                <span class="text-accent flex items-center"><div class="w-2 h-2 rounded-full bg-accent mr-2"></div>${lang}</span>
                                <span class="text-gray-500 flex items-center"><svg class="w-4 h-4 mr-1 text-amber-500" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>${repo.stargazers_count}</span>
                            </div>
                        </a>
                    `;
                });
            }

            // Draw Chart
            if(chartInstance) chartInstance.destroy();
            
            const labels = Object.keys(langCounts).sort((a,b) => langCounts[b] - langCounts[a]).slice(0, 5);
            const data = labels.map(l => langCounts[l]);
            
            if(labels.length > 0) {
                const ctx = document.getElementById('languageChart').getContext('2d');
                chartInstance = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: labels,
                        datasets: [{
                            data: data,
                            backgroundColor: ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444'],
                            borderWidth: 0,
                            hoverOffset: 10
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { position: 'right', labels: { font: { family: 'Inter', weight: 'bold' } } } },
                        cutout: '70%'
                    }
                });
            }
        }
    </script>
"""

with open('./projects/github-profile-finder/index.html', 'r') as f:
    content = f.read()

content = re.sub(r'<main.*?</main>', github_html, content, flags=re.DOTALL)
with open('./projects/github-profile-finder/index.html', 'w') as f:
    f.write(content)

print("GitHub Finder upgraded.")


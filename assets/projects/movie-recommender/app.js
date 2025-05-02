const apiKey = '456f76c1c99182904cde62e39869240e'; // Replace with your TMDB API key

const movieContainer = document.getElementById('movies');
const genreSelect = document.getElementById('genre');
const languageSelect = document.getElementById('language');
const yearSelect = document.getElementById('year');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const pageInfo = document.getElementById('page-info');
const modal = document.getElementById('movie-modal');
const modalContent = document.getElementById('modal-content');
const closeModal = document.getElementById('close-modal');
let currentPage = 1;
let currentGenre = '';
let currentLanguage = '';
let currentYear = '';

// Fetch and populate genres
async function fetchGenres() {
    const response = await fetch(`https://api.themoviedb.org/3/genre/movie/list?api_key=${apiKey}`);
    const data = await response.json();
    genreSelect.innerHTML = '<option value="">All Genres</option>';
    data.genres.forEach(genre => {
        const option = document.createElement('option');
        option.value = genre.id;
        option.textContent = genre.name;
        genreSelect.appendChild(option);
    });
}

// Fetch and populate languages
async function fetchLanguages() {
    const response = await fetch(`https://api.themoviedb.org/3/configuration/languages?api_key=${apiKey}`);
    const data = await response.json();
    languageSelect.innerHTML = '<option value="">All Languages</option>';
    const commonLanguages = data.filter(lang => ['en', 'hi', 'es', 'fr', 'de', 'ja', 'zh'].includes(lang.iso_639_1));
    commonLanguages.forEach(lang => {
        const option = document.createElement('option');
        option.value = lang.iso_639_1;
        option.textContent = lang.english_name;
        languageSelect.appendChild(option);
    });
}

// Populate years
function populateYears() {
    yearSelect.innerHTML = '<option value="">All Years</option>';
    for (let year = 2025; year >= 1980; year--) {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        yearSelect.appendChild(option);
    }
}

// Fetch movies
async function fetchMovies(genreId, language, year, page = 1) {
    let url = `https://api.themoviedb.org/3/discover/movie?api_key=${apiKey}&page=${page}`;
    if (genreId) url += `&with_genres=${genreId}`;
    if (language) url += `&with_original_language=${language}`;
    if (year) url += `&primary_release_year=${year}`;
    const response = await fetch(url);
    const data = await response.json();
    movieContainer.innerHTML = '';
    data.results.slice(0, 25).forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.className = 'bg-white rounded shadow p-4 cursor-pointer';
        movieCard.dataset.movieId = movie.id;
        movieCard.innerHTML = `
         <img src="https://image.tmdb.org/t/p/w400${movie.poster_path}" alt="${movie.title}" class="w-full h-auto object-contain rounded">
         <h2 class="text-lg font-bold text-black text-center mt-2">${movie.title}</h2>
       `;
        movieCard.addEventListener('click', () => showMovieDetails(movie.id));
        movieContainer.appendChild(movieCard);
    });
    pageInfo.textContent = `Page ${page}`;
    prevBtn.disabled = page === 1;
    nextBtn.disabled = page >= data.total_pages;
}

// Fetch and show movie details
async function showMovieDetails(movieId) {
    const response = await fetch(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${apiKey}&append_to_response=videos,credits`);
    const movie = await response.json();
    const trailer = movie.videos.results.find(video => video.type === 'Trailer' && video.site === 'YouTube');
    modalContent.innerHTML = `
       <div class="flex flex-col md:flex-row gap-6">
         <div class="w-full md:w-1/3 flex-shrink-0">
           <img src="https://image.tmdb.org/t/p/w400${movie.poster_path}" alt="${movie.title}" class="w-full h-auto object-contain rounded">
         </div>
         <div class="flex-1 text-gray-800">
           <h2 class="text-3xl font-bold text-blue-800 mb-2">${movie.title}</h2>
           <p class="text-lg italic text-blue-600 mb-4">${movie.tagline || ''}</p>
           <div class="space-y-3">
             <p><span class="font-semibold text-blue-700">Overview:</span> ${movie.overview}</p>
             <p><span class="font-semibold text-blue-700">Genres:</span> ${movie.genres.map(g => g.name).join(', ')}</p>
             <p><span class="font-semibold text-blue-700">Runtime:</span> ${movie.runtime} minutes</p>
             <p><span class="font-semibold text-blue-700">Release Date:</span> ${movie.release_date}</p>
             <p><span class="font-semibold text-blue-700">Cast:</span> ${movie.credits.cast.slice(0, 10).map(c => c.name).join(', ')}</p>
             <p><span class="font-semibold text-blue-700">Budget:</span> $${movie.budget.toLocaleString() || 'N/A'}</p>
             <p><span class="font-semibold text-blue-700">Revenue:</span> $${movie.revenue.toLocaleString() || 'N/A'}</p>
             <p><span class="font-semibold text-blue-700">Production:</span> ${movie.production_companies.map(c => c.name).join(', ') || 'N/A'}</p>
             <p><span class="font-semibold text-blue-700">Status:</span> ${movie.status}</p>
             ${trailer ? `<p class="font-semibold text-blue-700">Trailer:</p><div class="relative pt-[56.25%]"><iframe class="absolute top-0 left-0 w-full h-full rounded" src="https://www.youtube.com/embed/${trailer.key}" frameborder="0" allowfullscreen></iframe></div>` : ''}
           </div>
         </div>
       </div>
     `;
    modal.classList.remove('hidden');
    modalContent.focus();
}

// Event listeners
genreSelect.addEventListener('change', (e) => {
    currentGenre = e.target.value;
    currentPage = 1;
    fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);
});

languageSelect.addEventListener('change', (e) => {
    currentLanguage = e.target.value;
    currentPage = 1;
    fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);
});

yearSelect.addEventListener('change', (e) => {
    currentYear = e.target.value;
    currentPage = 1;
    fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);
});

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);
    }
});

nextBtn.addEventListener('click', () => {
    currentPage++;
    fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);
});

closeModal.addEventListener('click', () => {
    modal.classList.add('hidden');
});

window.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.add('hidden');
});

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        modal.classList.add('hidden');
    }
});

// Initialize
fetchGenres();
fetchLanguages();
populateYears();
fetchMovies(currentGenre, currentLanguage, currentYear, currentPage);
const apiKey = '456f76c1c99182904cde62e39869240e'; // Replace with your TMDB API key

const movieContainer = document.getElementById('movies');
const genreSelect = document.getElementById('genre');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const pageInfo = document.getElementById('page-info');
let currentPage = 1;
let currentGenre = 28;

async function fetchMovies(genreId, page = 1) {
    const response = await fetch(`https://api.themoviedb.org/3/discover/movie?api_key=${apiKey}&with_genres=${genreId}&page=${page}`);
    const data = await response.json();
    movieContainer.innerHTML = '';
    data.results.slice(0,).forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.className = 'bg-white rounded shadow p-4';
        movieCard.innerHTML = `
         <a href="https://www.themoviedb.org/movie/${movie.id}" target="_blank">
           <img src="https://image.tmdb.org/t/p/w400${movie.poster_path}" alt="${movie.title}" class="w-full h-64 object-cover rounded">
           <h2 class="text-xl font-semibold mt-2">${movie.title}</h2>
           <p class="text-gray-600">${movie.overview.substring(0, 100)}...</p>
         </a>
       `;
        movieContainer.appendChild(movieCard);
    });
    pageInfo.textContent = `Page ${page}`;
    prevBtn.disabled = page === 1;
    nextBtn.disabled = page >= data.total_pages;
}

genreSelect.addEventListener('change', (e) => {
    currentGenre = e.target.value;
    currentPage = 1;
    fetchMovies(currentGenre, currentPage);
});

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        fetchMovies(currentGenre, currentPage);
    }
});

nextBtn.addEventListener('click', () => {
    currentPage++;
    fetchMovies(currentGenre, currentPage);
});

fetchMovies(currentGenre, currentPage); // Default to Action

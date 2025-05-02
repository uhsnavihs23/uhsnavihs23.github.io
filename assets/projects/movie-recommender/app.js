const apiKey = '456f76c1c99182904cde62e39869240e'; // Replace with your TMDB API key
const movieContainer = document.getElementById('movies');
const genreSelect = document.getElementById('genre');

async function fetchMovies(genreId) {
    const response = await fetch(`https://api.themoviedb.org/3/discover/movie?api_key=${apiKey}&with_genres=${genreId}`);
    const data = await response.json();
    movieContainer.innerHTML = '';
    data.results.slice(0, 6).forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.className = 'bg-white rounded shadow p-4';
        movieCard.innerHTML = `
           <img src="https://image.tmdb.org/t/p/w200${movie.poster_path}" alt="${movie.title}" class="w-full h-64 object-cover rounded">
           <h2 class="text-xl font-semibold mt-2">${movie.title}</h2>
           <p class="text-gray-600">${movie.overview.substring(0, 100)}...</p>
         `;
        movieContainer.appendChild(movieCard);
    });
}

genreSelect.addEventListener('change', (e) => fetchMovies(e.target.value));
fetchMovies(28); // Default to Action
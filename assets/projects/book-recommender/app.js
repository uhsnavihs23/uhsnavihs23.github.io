const bookContainer = document.getElementById('books');
const categorySelect = document.getElementById('category');
const languageSelect = document.getElementById('language');
const yearSelect = document.getElementById('year');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const pageInfo = document.getElementById('page-info');
const modal = document.getElementById('book-modal');
const modalContent = document.getElementById('modal-content');
const closeModal = document.getElementById('close-modal');
let currentPage = 1;
let currentCategory = '';
let currentLanguage = '';
let currentYear = '';

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

// Fetch books
async function fetchBooks(category, language, year, page = 1) {
    let query = '';
    if (category) query += `+subject:${category}`;
    if (year) query += `+from:${year}`;
    const startIndex = (page - 1) * 25;
    let url = `https://www.googleapis.com/books/v1/volumes?q=${query}&startIndex=${startIndex}&maxResults=25`;
    if (language) url += `&langRestrict=${language}`;
    const response = await fetch(url);
    const data = await response.json();
    bookContainer.innerHTML = '';
    if (data.items) {
        data.items.slice(0, 25).forEach(book => {
            const bookCard = document.createElement('div');
            bookCard.className = 'bg-white rounded shadow p-4 cursor-pointer';
            bookCard.dataset.bookId = book.id;
            bookCard.innerHTML = `
             <img src="${book.volumeInfo.imageLinks?.thumbnail || 'https://via.placeholder.com/128x192'}" alt="${book.volumeInfo.title}" class="w-full h-auto object-contain rounded">
             <h2 class="text-lg font-bold text-black text-center mt-2">${book.volumeInfo.title}</h2>
           `;
            bookCard.addEventListener('click', () => showBookDetails(book.id));
            bookContainer.appendChild(bookCard);
        });
    }
    pageInfo.textContent = `Page ${page}`;
    prevBtn.disabled = page === 1;
    nextBtn.disabled = !data.items || data.items.length < 25;
}

// Show book details
async function showBookDetails(bookId) {
    const response = await fetch(`https://www.googleapis.com/books/v1/volumes/${bookId}`);
    const book = await response.json();
    modalContent.innerHTML = `
         <div class="flex flex-col md:flex-row gap-6">
           <div class="w-full md:w-1/3 flex-shrink-0">
             <img src="${book.volumeInfo.imageLinks?.thumbnail || 'https://via.placeholder.com/128x192'}" alt="${book.volumeInfo.title}" class="w-full h-auto object-contain rounded">
           </div>
           <div class="flex-1 text-gray-800">
             <h2 class="text-3xl font-bold text-blue-800 mb-2">${book.volumeInfo.title}</h2>
             <p class="text-lg italic text-blue-600 mb-4">${book.volumeInfo.subtitle || ''}</p>
             <div class="space-y-3">
               <p><span class="font-semibold text-blue-700">Description:</span> ${book.volumeInfo.description || 'N/A'}</p>
               <p><span class="font-semibold text-blue-700">Authors:</span> ${book.volumeInfo.authors?.join(', ') || 'N/A'}</p>
               <p><span class="font-semibold text-blue-700">Publisher:</span> ${book.volumeInfo.publisher || 'N/A'}</p>
               <p><span class="font-semibold text-blue-700">Published:</span> ${book.volumeInfo.publishedDate || 'N/A'}</p>
               <p><span class="font-semibold text-blue-700">Categories:</span> ${book.volumeInfo.categories?.join(', ') || 'N/A'}</p>
               <p><span class="font-semibold text-blue-700">Pages:</span> ${book.volumeInfo.pageCount || 'N/A'}</p>
               <p><span class="font-semibold text-blue-700">Language:</span> ${book.volumeInfo.language?.toUpperCase() || 'N/A'}</p>
             </div>
           </div>
         </div>
       `;
    modal.classList.remove('hidden');
    modalContent.focus();
}

// Event listeners
categorySelect.addEventListener('change', (e) => {
    currentCategory = e.target.value;
    currentPage = 1;
    fetchBooks(currentCategory, currentLanguage, currentYear, currentPage);
});

languageSelect.addEventListener('change', (e) => {
    currentLanguage = e.target.value;
    currentPage = 1;
    fetchBooks(currentCategory, currentLanguage, currentYear, currentPage);
});

yearSelect.addEventListener('change', (e) => {
    currentYear = e.target.value;
    currentPage = 1;
    fetchBooks(currentCategory, currentLanguage, currentYear, currentPage);
});

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        fetchBooks(currentCategory, currentLanguage, currentYear, currentPage);
    }
});

nextBtn.addEventListener('click', () => {
    currentPage++;
    fetchBooks(currentCategory, currentLanguage, currentYear, currentPage);
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
populateYears();
fetchBooks(currentCategory, currentLanguage, currentYear, currentPage);
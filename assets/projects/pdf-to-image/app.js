const pdfUpload = document.getElementById('pdf-upload');
const compressionSelect = document.getElementById('compression');
const thumbnailsContainer = document.getElementById('thumbnails');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const pageInfo = document.getElementById('page-info');
const modal = document.getElementById('image-modal');
const modalContent = document.getElementById('modal-content');
const closeModal = document.getElementById('close-modal');
let currentPage = 1;
let totalPages = 0;
let pdfDoc = null;
const itemsPerPage = 25;

// Compression settings
const compressionSettings = {
    high: { quality: 0.9, scale: 1.5 },
    medium: { quality: 0.6, scale: 1.0 },
    low: { quality: 0.3, scale: 0.7 }
};

// Handle PDF upload
pdfUpload.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/pdf') {
        const reader = new FileReader();
        reader.onload = async () => {
            const typedArray = new Uint8Array(reader.result);
            pdfDoc = await pdfjsLib.getDocument(typedArray).promise;
            totalPages = pdfDoc.numPages;
            currentPage = 1;
            renderThumbnails();
        };
        reader.readAsArrayBuffer(file);
    } else {
        alert('Please upload a valid PDF file.');
    }
});

// Render thumbnails
async function renderThumbnails() {
    thumbnailsContainer.innerHTML = '';
    const start = (currentPage - 1) * itemsPerPage + 1;
    const end = Math.min(start + itemsPerPage - 1, totalPages);

    for (let i = start; i <= end; i++) {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        const page = await pdfDoc.getPage(i);
        const viewport = page.getViewport({ scale: 0.5 });
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        await page.render({ canvasContext: context, viewport }).promise;
        const thumbnail = document.createElement('div');
        thumbnail.className = 'bg-white rounded shadow p-4 cursor-pointer';
        thumbnail.dataset.page = i;
        thumbnail.appendChild(canvas);
        thumbnail.addEventListener('click', () => showFullImage(i));
        thumbnailsContainer.appendChild(thumbnail);
    }

    pageInfo.textContent = `Page ${currentPage} of ${Math.ceil(totalPages / itemsPerPage)}`;
    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = end >= totalPages;
}

// Show full-size image in modal
async function showFullImage(pageNum) {
    const compression = compressionSelect.value;
    const { quality, scale } = compressionSettings[compression];
    const page = await pdfDoc.getPage(pageNum);
    const viewport = page.getViewport({ scale });
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.height = viewport.height;
    canvas.width = viewport.width;
    await page.render({ canvasContext: context, viewport }).promise;

    // Convert canvas to image with compression
    const imgData = canvas.toDataURL('image/jpeg', quality);
    modalContent.innerHTML = `
         <div class="flex flex-col md:flex-row gap-6">
           <div class="w-full md:w-1/3 flex-shrink-0">
             <img src="${imgData}" alt="Page ${pageNum}" class="w-full h-auto object-contain rounded">
           </div>
           <div class="flex-1 text-gray-800">
             <h2 class="text-3xl font-bold text-blue-800 mb-2">Page ${pageNum}</h2>
             <p class="text-lg italic text-blue-600 mb-4">Compression: ${compression.charAt(0).toUpperCase() + compression.slice(1)}</p>
             <div class="space-y-3">
               <p><span class="font-semibold text-blue-700">Resolution:</span> ${canvas.width}x${canvas.height}</p>
               <p><span class="font-semibold text-blue-700">Quality:</span> ${quality * 100}%</p>
               <p><a href="${imgData}" download="page-${pageNum}.jpg" class="text-blue-600 hover:underline">Download Image</a></p>
             </div>
           </div>
         </div>
       `;
    modal.classList.remove('hidden');
    modalContent.focus();
}

// Pagination
prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        renderThumbnails();
    }
});

nextBtn.addEventListener('click', () => {
    if (currentPage < Math.ceil(totalPages / itemsPerPage)) {
        currentPage++;
        renderThumbnails();
    }
});

// Modal controls
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
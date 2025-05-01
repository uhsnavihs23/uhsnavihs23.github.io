document.addEventListener('DOMContentLoaded', function () {
    // Get or initialize visit count
    let visitCount = localStorage.getItem('siteVisitCount') || 0;
    visitCount = parseInt(visitCount) + 1;
    localStorage.setItem('siteVisitCount', visitCount);

    // Create counter element
    const counter = document.createElement('div');
    counter.id = 'visit-counter';
    counter.style.position = 'fixed';
    counter.style.bottom = '20px';
    counter.style.right = '20px';
    counter.style.backgroundColor = '#333';
    counter.style.color = '#fff';
    counter.style.padding = '5px 10px';
    counter.style.borderRadius = '5px';
    counter.style.fontSize = '14px';
    counter.style.zIndex = '1000';
    counter.textContent = `Visits: ${visitCount}`;

    // Append to body
    document.body.appendChild(counter);
});
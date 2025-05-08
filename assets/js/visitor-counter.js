document.addEventListener('DOMContentLoaded', () => {
    console.log('Counter script loaded');
    const counter = document.getElementById('visitor-counter');
    if (counter) {
        counter.textContent = 'Visits: 42'; // Replace with actual count from https://23022000.goatcounter.com/
    } else {
        console.error('Visitor counter element not found');
    }
});
document.addEventListener('DOMContentLoaded', () => {
    console.log('GoatCounter API script loaded');
    const counter = document.getElementById('visitor-counter');
    if (!counter) {
        console.error('Visitor counter element not found');
        return;
    }

    fetch('https://23022000.goatcounter.com/api/v0/count?totals=1', {
        headers: {
            'Authorization': 'ae60gn9pimrkt9zd2ea18pf56qzloy416r6g9u51o27yayhj' // Replace with your API key
        }
    })
        .then(response => {
            if (!response.ok) throw new Error('API request failed: ' + response.status);
            return response.json();
        })
        .then(data => {
            const total = data.count || 0;
            counter.textContent = `Visits: ${total}`;
        })
        .catch(error => {
            console.error('Error fetching GoatCounter stats:', error);
            counter.textContent = 'Visits: Error';
        });
});
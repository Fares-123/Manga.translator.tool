// Event listeners for the start and stop mining buttons
document.getElementById('start-button').addEventListener('click', function() {
    fetch('/start-mining', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status-message').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('stop-button').addEventListener('click', function() {
    fetch('/stop-mining', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status-message').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Load server status when the page loads
window.addEventListener('load', function() {
    fetch('/status')
    .then(response => response.json())
    .then(data => {
        document.getElementById('status-message').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

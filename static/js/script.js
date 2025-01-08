// Load server status when the page loads and update it every 5 seconds
function fetchMiningStatus() {
    fetch('/status')
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById('status-message').innerText = data.message;
        } else if (data.error) {
            document.getElementById('status-message').innerText = "Error fetching mining status.";
        }
    })
    .catch(error => {
        document.getElementById('status-message').innerText = "Error fetching mining status.";
        console.error('Error:', error);
    });
}

// Fetch status every 5 seconds
window.addEventListener('load', function() {
    fetchMiningStatus();
    setInterval(fetchMiningStatus, 5000); // Update every 5 seconds
});

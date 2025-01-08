document.getElementById('start-mining-btn').addEventListener('click', function() {
    fetch('/start-mining')
        .then(response => response.json())
        .then(data => {
            if (data.message === "Mining started") {
                updateStatus();
            }
        });
});

function updateStatus() {
    setInterval(function() {
        fetch('/mining-status')
            .then(response => response.json())
            .then(data => {
                document.getElementById('mining-status').innerText = data.status;
            });
    }, 5000);
}

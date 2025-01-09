setInterval(function() {
    fetch('/latest-block')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hash').innerText = 'Hash: ' + data.hash;
            document.getElementById('nonce').innerText = 'Nonce: ' + data.nonce;
            document.getElementById('time').innerText = 'Time Taken: ' + data.time_taken + ' seconds';
        });
}, 1000);

setInterval(function() {
    fetch('/latest-block')
    .then(response => response.json())
    .then(data => {
        document.getElementById("nonce").textContent = data.nonce;
        document.getElementById("hash").textContent = data.hash;
        document.getElementById("timeTaken").textContent = data.time_taken + " ثواني";
    });
}, 2500);  // تحديث البيانات كل ثانيتين ونصف

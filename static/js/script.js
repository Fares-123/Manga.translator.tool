// جلب حالة الخادم وعرضها
fetch('/status')
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('status').innerHTML = 'Error loading status';
    });

// إضافة تفاعل زر Start Mining
document.getElementById('start-mining').addEventListener('click', function() {
    fetch('/start-mining', { method: 'POST' })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => {
            console.error('Error:', error);
            alert('Error starting mining');
        });
});

// إضافة تفاعل زر Stop Mining
document.getElementById('stop-mining').addEventListener('click', function() {
    fetch('/stop-mining', { method: 'POST' })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => {
            console.error('Error:', error);
            alert('Error stopping mining');
        });
});

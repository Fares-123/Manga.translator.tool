async function getStatus() {
    const response = await fetch('/status');
    const data = await response.json();
    document.getElementById('status').innerText = JSON.stringify(data, null, 2);
}

async function startMining() {
    const wallet = document.getElementById('wallet').value;
    if (!wallet) {
        alert("Please enter a wallet address!");
        return;
    }

    const response = await fetch('/start-mining', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ wallet: wallet })
    });
    const data = await response.json();
    if (data.error) {
        alert(`Error: ${data.error}`);
    } else {
        alert(data.message);
    }
    getStatus();
}

async function stopMining() {
    const response = await fetch('/stop-mining', { method: 'POST' });
    const data = await response.json();
    if (data.error) {
        alert(`Error: ${data.error}`);
    } else {
        alert(data.message);
    }
    getStatus();
}

// استدعاء حالة التعدين عند فتح الصفحة
getStatus();

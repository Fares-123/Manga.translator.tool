function startMining() {
    fetch('/mine', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: 'data=miningData'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('balance').innerText = data.balance;
        alert("Mining Successful!");
    });
}

document.getElementById('transferForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const address = document.getElementById('address').value;
    const amount = document.getElementById('amount').value;

    fetch('/transfer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `address=${address}&amount=${amount}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('transferMessage').innerText = data.message;
            document.getElementById('balance').innerText = data.balance;
        } else {
            document.getElementById('transferMessage').innerText = data.message;
        }
    });
});

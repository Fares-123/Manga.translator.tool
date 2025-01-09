// main.js
function fetchLatestBlock() {
    $.get("/latest-block", function(data) {
        $('#nonce').text(data.nonce);
        $('#hash').text(data.hash);
        $('#time_taken').text(data.time_taken);
    });
}

setInterval(fetchLatestBlock, 5000); // Update every 5 seconds

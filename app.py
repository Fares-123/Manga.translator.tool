from flask import Flask, render_template, jsonify
from Crypto.Hash import SHA256
import time
import threading
import os

app = Flask(__name__)

block_data = {}

def mine_block(previous_hash):
    nonce = 0
    while True:
        data = f"{previous_hash}{nonce}".encode()
        hash_result = SHA256.new(data).hexdigest()
        if hash_result.startswith("000"): 
            return {"nonce": nonce, "hash": hash_result}
        nonce += 1

def start_mining():
    previous_hash = "00000000000000000000000000000000"
    while True:
        start_time = time.time()
        block = mine_block(previous_hash)
        elapsed_time = time.time() - start_time
        block_data['block'] = block
        block_data['time_taken'] = elapsed_time

@app.route('/')
def home():
    block = block_data.get('block', {'nonce': '0', 'hash': '00000000000000000000000000000000'})
    return render_template('index.html', block=block)

@app.route('/latest-block')
def latest_block():
    block = block_data.get('block', {'nonce': '0', 'hash': '00000000000000000000000000000000'})
    time_taken = block_data.get('time_taken', 0)
    return jsonify({'nonce': block['nonce'], 'hash': block['hash'], 'time_taken': time_taken})

if __name__ == '__main__':
    mining_thread = threading.Thread(target=start_mining, daemon=True)
    mining_thread.start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

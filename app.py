from flask import Flask, render_template, jsonify
from Crypto.Hash import SHA256
import time
import threading
import os

app = Flask(__name__)

# بيانات البلوك والمبالغ المعدنة
block_data = {
    'current_mining_amount': 0,  # المبلغ المعدن في الدورة الحالية
    'total_mining_amount': 0,    # المجموع الكلي للمبالغ منذ تشغيل الخادم
    'mining_reward': 50,         # المكافأة لكل بلوك
}

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

        # تحديث المبالغ عند العثور على بلوك جديد
        block_data['current_mining_amount'] = block_data['mining_reward']
        block_data['total_mining_amount'] += block_data['mining_reward']

@app.route('/')
def home():
    return render_template('index.html', 
                           current_mining_amount=block_data['current_mining_amount'],
                           total_mining_amount=block_data['total_mining_amount'],
                           block=block_data.get('block', {'nonce': '0', 'hash': '00000000000000000000000000000000'}),
                           time_taken=block_data.get('time_taken', 0))

@app.route('/latest-block')
def latest_block():
    block = block_data.get('block', {'nonce': '0', 'hash': '00000000000000000000000000000000'})
    time_taken = block_data.get('time_taken', 0)
    return jsonify({
        'nonce': block['nonce'],
        'hash': block['hash'],
        'time_taken': time_taken,
        'current_mining_amount': block_data['current_mining_amount'],
        'total_mining_amount': block_data['total_mining_amount']
    })

if __name__ == '__main__':
    mining_thread = threading.Thread(target=start_mining, daemon=True)
    mining_thread.start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

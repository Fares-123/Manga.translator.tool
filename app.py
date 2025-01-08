from flask import Flask, render_template, request, jsonify
from Crypto.Hash import SHA256
import time

app = Flask(__name__)

# قيمة بداية التعدين
mining_rate = 0.01  # المبلغ المبدئي للعملة لكل عملية تعدين
balance = 0.0  # رصيد المستخدم من العملة
transactions = []  # سجل المعاملات

# وظيفة تعدين
def mine_block(data, nonce):
    h = SHA256.new()
    h.update((data + str(nonce)).encode('utf-8'))
    return h.hexdigest()

@app.route('/')
def index():
    global balance
    return render_template('index.html', balance=balance, transactions=transactions)

@app.route('/mine', methods=['POST'])
def mine():
    global balance
    data = request.form['data']
    nonce = 0
    while True:
        result = mine_block(data, nonce)
        if result.startswith('0000'):  # تحقق من التحدي (4 أصفار في بداية الهاش)
            balance += mining_rate  # إضافة قيمة التعدين
            transactions.append(f"Successfully mined: {mining_rate} coins")
            break
        nonce += 1
    return jsonify({'status': 'mining successful', 'balance': balance})

@app.route('/transfer', methods=['POST'])
def transfer():
    global balance
    address = request.form['address']
    if not address:
        return jsonify({'status': 'error', 'message': 'Please provide a wallet address'})
    amount = float(request.form['amount'])
    if amount > balance:
        return jsonify({'status': 'error', 'message': 'Insufficient funds'})
    balance -= amount
    transactions.append(f"Transferred {amount} coins to wallet {address}")
    return jsonify({'status': 'success', 'balance': balance, 'message': f"Transferred {amount} coins to {address}"})

if __name__ == '__main__':
    app.run(debug=True)

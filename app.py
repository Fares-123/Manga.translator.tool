from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# إعداد بيانات الاتصال بـ Mining Pool API
POOL_URL = "https://miningpool.com/api"  # قم بتغيير الرابط إلى رابط الـ API الخاص بك
API_KEY = "YOUR_API_KEY"  # ضع مفتاح API الخاص بك هنا

# وظيفة للحصول على حالة التعدين
@app.route('/status', methods=['GET'])
def get_mining_status():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{POOL_URL}/status", headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch mining status", "status_code": response.status_code})

# الوظيفة الرئيسية
@app.route('/')
def home():
    return jsonify({"message": "Mining Server is running. Use /status to check mining status."})

if __name__ == '__main__':
    app.run(debug=True)

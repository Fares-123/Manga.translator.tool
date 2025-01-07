from flask import Flask, render_template, jsonify, request
from Crypto.PublicKey import RSA
import requests

app = Flask(__name__)

# الصفحة الرئيسية - تعرض index.html
@app.route("/")
def home():
    return render_template("index.html")

# API لتوليد مفتاح RSA باستخدام PyCryptodome
@app.route("/generate-key", methods=["GET"])
def generate_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return jsonify({"private_key": private_key.decode(), "public_key": public_key.decode()})

# API لإجراء طلب خارجي باستخدام requests
@app.route("/fetch-data", methods=["GET"])
def fetch_data():
    try:
        response = requests.get("https://api.example.com")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

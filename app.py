from flask import Flask, render_template, jsonify, request
import os
from mining import start_xmrig, get_mining_status

app = Flask(__name__)

# إعدادات التعدين الافتراضية
WALLET_ADDRESS = "YOUR_MONERO_WALLET_ADDRESS"
POOL_URL = "pool.supportxmr.com:3333"  # استبدل بمجمع التعدين الذي تفضله
CPU_THREADS = 2
process = None  # حفظ العملية التي يتم تشغيلها

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start-mining", methods=["GET"])
def start_mining():
    global process
    if not os.path.exists("./xmrig"):
        return jsonify({"error": "XMRig not found. Please install it."}), 500
    
    process = start_xmrig(WALLET_ADDRESS, POOL_URL, CPU_THREADS)
    if isinstance(process, str):  # إذا كان هناك خطأ في بدء العملية
        return jsonify({"error": process}), 500
    return jsonify({"message": "Mining started"}), 200

@app.route("/mining-status", methods=["GET"])
def mining_status():
    if process:
        status = get_mining_status(process)
        if status:
            return jsonify({"status": status})
        else:
            return jsonify({"status": "Mining finished or error occurred."})
    return jsonify({"status": "Mining process not started."})

if __name__ == "__main__":
    app.run(debug=True)

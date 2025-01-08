from flask import Flask, render_template
from Crypto.Hash import SHA256
import time

app = Flask(__name__)

def mine_block(previous_hash):
    """وظيفة تعدين تقوم بإنشاء كتلة جديدة"""
    nonce = 0
    while True:
        # بيانات الكتلة
        data = f"{previous_hash}{nonce}".encode()
        # تجزئة الكتلة
        hash_result = SHA256.new(data).hexdigest()
        # التحقق من أن التجزئة تبدأ بعدد معين من الأصفار
        if hash_result.startswith("0000"):
            return {"nonce": nonce, "hash": hash_result}
        nonce += 1

@app.route('/')
def home():
    """المسار لعرض البيانات في الصفحة الرئيسية"""
    previous_hash = "00000000000000000000000000000000"  # قيمة ثابتة لبدء التعدين
    start_time = time.time()
    block = mine_block(previous_hash)
    elapsed_time = time.time() - start_time
    
    # إرسال البيانات إلى قالب HTML
    return render_template('index.html', block=block, time_taken=elapsed_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

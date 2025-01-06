# app.py
from fastapi import FastAPI
import httpx
from Crypto.PublicKey import RSA

app = FastAPI()

# مثال على تكوين مفتاح RSA باستخدام PyCryptodome
@app.get("/generate-key")
def generate_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return {"private_key": private_key.decode(), "public_key": public_key.decode()}

# مثال على استخدام httpx لإجراء طلب خارجي
@app.get("/fetch-data")
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com")
        return response.json()

# نقطة الدخول الأساسية
@app.get("/")
def read_root():
    return {"message": "Hello, World"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# Cliente de Groq (compatible con OpenAI)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

class ComparacionRequest(BaseModel):
    producto1: str
    producto2: str

@app.get("/")
def home():
    return {"message": "API de T-HardIA (Groq) activa ✅"}

@app.post("/comparar")
def comparar(req: ComparacionRequest):
    try:
        prompt = f"Compara los productos de hardware:\n1️⃣ {req.producto1}\n2️⃣ {req.producto2}\nEn rendimiento, consumo, precio y mejor opción general."
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
        )
        return {"comparacion": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

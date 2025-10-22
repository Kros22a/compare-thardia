from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# Cliente de Groq (API 100% compatible con OpenAI)
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
        prompt = (
            f"Compara los siguientes productos de hardware:\n"
            f"1️⃣ {req.producto1}\n"
            f"2️⃣ {req.producto2}\n\n"
            f"Evalúa rendimiento, eficiencia energética, temperatura, precio y cuál conviene más para un usuario gamer o profesional."
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # 🔥 Modelo activo y recomendado por Groq
            messages=[{"role": "user", "content": prompt}],
        )

        return {"comparacion": response.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

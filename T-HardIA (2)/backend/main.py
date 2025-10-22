from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

# Configurar CORS (para permitir peticiones desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cliente de OpenAI (usa la nueva API oficial)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CompareRequest(BaseModel):
    producto1: str
    producto2: str

@app.get("/")
def root():
    return {"message": "API de T-HardIA activa ✅"}

@app.post("/comparar")
def comparar_productos(data: CompareRequest):
    prompt = f"""
    Compara estos dos productos de hardware y genera un análisis técnico breve y objetivo:
    1. {data.producto1}
    2. {data.producto2}
    Incluye rendimiento, eficiencia, calidad, ventajas y desventajas.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        result = response.choices[0].message.content
        return {"comparacion": result}
    except Exception as e:
        return {"error": str(e)}

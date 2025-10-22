from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI()

# Permitir CORS para tu frontend
origins = [
    "*",  # Puedes restringirlo a tu dominio más adelante
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # permite GET, POST, etc.
    allow_headers=["*"],
)

# Tu API key de Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/v1/completions"  # o la URL actual que uses

@app.get("/")
async def root():
    return {"message": "API de T-HardIA (Groq) activa ✅"}

@app.post("/comparar")
async def comparar_hardware(request: Request):
    data = await request.json()
    producto1 = data.get("producto1")
    producto2 = data.get("producto2")

    if not producto1 or not producto2:
        return {"error": "Debes enviar producto1 y producto2"}

    prompt = f"Comparar los siguientes productos de hardware y generar un análisis detallado: {producto1} vs {producto2}"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-mini",  # Asegúrate de usar un modelo activo
        "prompt": prompt,
        "max_tokens": 1000
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return {"error": response.json()}

    result = response.json()
    # Ajusta según el JSON que Groq devuelva
    comparacion = result.get("completion", "No se obtuvo respuesta del modelo")

    return {"comparacion": comparacion}

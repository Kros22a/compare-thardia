# main.py
import os
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Configurar CORS para que tu frontend pueda acceder al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URL de Groq
GROQ_URL = "https://api.groq.com/v1/llama-3.1-mini/completions"

# Tu clave se toma de variable de entorno
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ La variable de entorno GROQ_API_KEY no está configurada.")

@app.get("/")
async def root():
    return {"message": "API de T-HardIA (Groq) activa ✅"}

@app.post("/comparar")
async def comparar(request: Request):
    """
    Endpoint que recibe JSON con 'hardware1' y 'hardware2'
    y devuelve la comparación en texto formateado.
    """
    try:
        data = await request.json()
        hardware1 = data.get("hardware1")
        hardware2 = data.get("hardware2")

        if not hardware1 or not hardware2:
            return {"error": "Faltan los campos 'hardware1' o 'hardware2'."}

        # Payload para Groq
        payload = {
            "prompt": f"Compara estos dos productos de hardware: {hardware1} vs {hardware2}. Genera un análisis detallado en español, incluyendo rendimiento, eficiencia energética, temperatura y precio, y concluye con recomendaciones.",
            "max_tokens": 500,  # ajusta según tus necesidades
            "temperature": 0.7,
        }

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        # Llamada a Groq
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        response.raise_for_status()  # levanta error si status != 200
        result = response.json()

        # Extraer el texto de la respuesta
        comparacion = result.get("completions", [{}])[0].get("text", "No se obtuvo resultado.")

        return {"comparacion": comparacion}

    except requests.exceptions.RequestException as e:
        # Captura errores de la API de Groq
        return {"error": f"Error en la API de Groq: {str(e)}"}

    except Exception as e:
        # Captura errores generales
        return {"error": f"Error interno del servidor: {str(e)}"}

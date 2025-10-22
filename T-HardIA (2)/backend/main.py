from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("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")

class CompareRequest(BaseModel):
    producto1: str
    producto2: str

@app.post("/comparar")
async def comparar_productos(data: CompareRequest):
    prompt = f"""
    Compara estos dos productos de hardware y genera un análisis técnico breve y objetivo:
    1. {data.producto1}
    2. {data.producto2}
    Incluye rendimiento, eficiencia, calidad, ventajas y desventajas.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        result = response.choices[0].message["content"]
        return {"comparacion": result}
    except Exception as e:
        return {"error": str(e)}

import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/v1/completions"

@app.route("/comparar", methods=["POST"])
def comparar():
    data = request.json
    hardware1 = data.get("hardware1")
    hardware2 = data.get("hardware2")

    if not hardware1 or not hardware2:
        return jsonify({"error": "Debes enviar ambos hardware"}), 400

    prompt = f"Comparar estos dos productos de hardware: {hardware1} vs {hardware2} y dar un análisis detallado de rendimiento, eficiencia energética, temperatura y precio."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-7b",  # Modelo activo recomendado por Groq
        "prompt": prompt,
        "max_tokens": 800
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        result = response.json()

        # Suponiendo que Groq devuelve 'completion' en la respuesta
        comparacion = result.get("completion", "No se pudo generar la comparación")

        return jsonify({"comparacion": comparacion})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Para ejecutar localmente
if __name__ == "__main__":
    app.run(debug=True)

# 🧠 T-HardIA

Comparador de hardware con inteligencia artificial (OpenAI + FastAPI).

## 🚀 Estructura
- **backend/** → API con FastAPI + OpenAI
- **frontend/** → HTML + JS + CSS

## 🧩 Despliegue
1. Crea tu API key de OpenAI y guárdala como variable de entorno:
   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```
2. Sube el backend a Vercel (o Render).
3. Sube el frontend a Vercel (directamente desde la carpeta `frontend`).
4. En `frontend/js/api.js` actualiza `API_URL` con la URL del backend.

---
Hecho con 💙 por Santiago y T-HardIA.

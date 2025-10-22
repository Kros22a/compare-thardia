const API_URL = "https://t-hardia-backend.vercel.app"; // tu URL de backend

document.getElementById("btnComparar").addEventListener("click", async () => {
    const prod1 = document.getElementById("producto1").value;
    const prod2 = document.getElementById("producto2").value;

    if (!prod1 || !prod2) {
        alert("Debes ingresar ambos productos");
        return;
    }

    const resultadoDiv = document.getElementById("resultado");
    resultadoDiv.innerHTML = "Cargando comparación...";

    try {
        const response = await fetch(`${API_URL}/comparar`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ producto1: prod1, producto2: prod2 })
        });

        const data = await response.json();

        if (data.error) {
            resultadoDiv.innerHTML = `<p style="color:red;">Error: ${JSON.stringify(data.error)}</p>`;
        } else {
            resultadoDiv.innerHTML = `<pre>${data.comparacion}</pre>`;
        }
    } catch (err) {
        resultadoDiv.innerHTML = `<p style="color:red;">Error de conexión: ${err}</p>`;
    }
});

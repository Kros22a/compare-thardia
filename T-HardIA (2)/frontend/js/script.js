const API_URL = "https://t-hardia-backend.vercel.app"; // URL de tu backend

const hardware1Input = document.getElementById("hardware1");
const hardware2Input = document.getElementById("hardware2");
const compararBtn = document.getElementById("compararBtn");
const resultadoPre = document.getElementById("resultado");

compararBtn.addEventListener("click", async () => {
    const hardware1 = hardware1Input.value.trim();
    const hardware2 = hardware2Input.value.trim();

    if (!hardware1 || !hardware2) {
        alert("Por favor ingresa ambos hardware.");
        return;
    }

    resultadoPre.textContent = "Generando comparación...";

    try {
        const response = await fetch(`${API_URL}/comparar`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ hardware1, hardware2 })
        });

        const data = await response.json();

        if (data.error) {
            resultadoPre.textContent = "Error: " + data.error;
        } else {
            resultadoPre.textContent = data.comparacion;
        }
    } catch (err) {
        resultadoPre.textContent = "Error al conectar con el servidor: " + err;
    }
});

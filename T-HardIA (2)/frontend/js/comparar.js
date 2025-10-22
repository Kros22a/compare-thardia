// comparar.js

const API_URL = "https://t-hardia-backend.vercel.app/comparar"; // Endpoint correcto

// Función para obtener la comparación de hardware
async function obtenerComparacion(producto1, producto2) {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ producto1, producto2 })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`${response.status} - ${JSON.stringify(errorData)}`);
        }

        const data = await response.json();
        mostrarComparacion(data.comparacion);
    } catch (error) {
        console.error("Error al obtener comparativa:", error);
        mostrarComparacion("Ocurrió un error al generar la comparativa. Revisa la consola.");
    }
}

// Función para mostrar la comparativa en el HTML
function mostrarComparacion(texto) {
    const contenedor = document.getElementById("resultadoComparacion");
    contenedor.innerHTML = texto; // Puedes usar innerHTML si tu comparativa contiene HTML
}

// Escuchar el submit del formulario
document.getElementById("formComparar").addEventListener("submit", (e) => {
    e.preventDefault();

    const producto1 = document.getElementById("producto1").value;
    const producto2 = document.getElementById("producto2").value;

    if (producto1 && producto2) {
        obtenerComparacion(producto1, producto2);
    } else {
        mostrarComparacion("Por favor, ingresa ambos productos para comparar.");
    }
});

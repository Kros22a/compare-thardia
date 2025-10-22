async function comparar() {
  const producto1 = document.getElementById("producto1").value.trim();
  const producto2 = document.getElementById("producto2").value.trim();
  const resultado = document.getElementById("resultado");

  if (!producto1 || !producto2) {
    resultado.innerHTML = "<p>Por favor ingresa ambos productos.</p>";
    return;
  }

  resultado.innerHTML = "<p>Comparando con IA... ⏳</p>";

  try {
    const res = await fetch(`${API_URL}/comparar`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ producto1, producto2 }),
    });

    const data = await res.json();
    if (data.comparacion) {
      resultado.innerHTML = `<h3>Resultado:</h3><p>${data.comparacion}</p>`;
    } else {
      resultado.innerHTML = `<p>Error: ${data.error}</p>`;
    }
  } catch (err) {
    resultado.innerHTML = "<p>Error al conectar con el servidor.</p>";
  }
}

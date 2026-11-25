import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

function App(){
  const [estado, setEstado] = useState("Comprobando...");

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then((res) => res.json())
      .then((data) => setEstado(`API conectada: ${data.status}`))
      .catch(() => setEstado("No se puede conectar con la API"));
  }, []);

  return (
    <main>
      <h1>Agenda de eventos de Jerez</h1>
      <p>{estado}</p>
    </main>
  );
}

export default App;
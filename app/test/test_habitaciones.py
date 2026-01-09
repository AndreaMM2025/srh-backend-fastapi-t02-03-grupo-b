from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_habitacion_1():
    habitacion = {
        "numero": "101",
        "tipo": "Simple",
        "tarifa": 50.0,
        "estado": "Disponible"
    }

    response = client.post("/api/habitaciones/", json=habitacion)

    # Si falla, esto te muestra el detalle exacto del 422
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["numero"] == "101"
    assert data["tipo"] == "Simple"
    assert data["tarifa"] == 50.0
    assert data["estado"] == "Disponible"


def test_listar_habitaciones():
    response = client.get("/api/habitaciones/")
    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)

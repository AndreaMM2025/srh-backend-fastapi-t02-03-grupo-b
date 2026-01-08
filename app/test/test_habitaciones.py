from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_habitacion_1():
    habitacion = {
        "ID_HABITACION": 1,
        "NUMERO": "101",
        "TIPO": "Simple",
        "TARIFA": 50.0,
        "ESTADO": "Disponible"
    }

    response = client.post("/api/habitaciones/", json=habitacion)
    assert response.status_code == 200

    data = response.json()
    assert data["ID_HABITACION"] == 1
    assert data["NUMERO"] == "101"
    assert data["ESTADO"] == "Disponible"


def test_listar_habitaciones():
    response = client.get("/api/habitaciones/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

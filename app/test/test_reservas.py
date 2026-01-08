from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_reserva_1():
    reserva = {
        "ID_RESERVA": 1,
        "ID_CLIENTE": 1,
        "ID_HABITACION": 1,
        "FECHA_INICIO": "2025-01-01",
        "FECHA_FIN": "2025-01-05",
        "ESTADO": "pendiente"
    }

    response = client.post("/api/reservas/", json=reserva)
    assert response.status_code == 200

    data = response.json()
    assert data["ID_RESERVA"] == 1
    assert data["ESTADO"] == "pendiente"
    assert data["FECHA_FIN"] == "2025-01-05"


def test_listar_reservas():
    response = client.get("/api/reservas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

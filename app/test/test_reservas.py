from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_reserva_1():
    reserva = {
        "cliente_id": 1,
        "habitacion_id": 1,
        "fecha_inicio": "2025-01-01",
        "fecha_fin": "2025-01-05"
    }

    response = client.post("/api/reservas/", json=reserva)
    assert response.status_code == 200

    data = response.json()
    assert data["cliente_id"] == 1
    assert data["habitacion_id"] == 1
    assert "id" in data
    assert "estado" in data

def test_listar_reservas():
    response = client.get("/api/reservas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

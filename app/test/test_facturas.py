from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_factura_1():
    factura = {
        "reserva_id": 1,
        "subtotal": 100.0,
        "impuestos": 20.0,
        "total": 120.0
    }

    response = client.post("/api/facturas/", json=factura)

    # Si falla, esto te muestra el detalle exacto del 422
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["reserva_id"] == 1
    assert data["subtotal"] == 100.0
    assert data["impuestos"] == 20.0
    assert data["total"] == 120.0


def test_listar_facturas():
    response = client.get("/api/facturas/")
    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)

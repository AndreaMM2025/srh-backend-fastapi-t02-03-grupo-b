from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_pago_1():
    pago = {
        "ID_PAGO": 1,
        "ID_FACTURA": 1,
        "FECHA": "2026-01-02",
        "MONTO": 120.0,
        "METODO": "tarjeta"
    }

    response = client.post("/api/pagos/", json=pago)
    assert response.status_code == 200

    data = response.json()
    assert data["ID_PAGO"] == 1
    assert data["MONTO"] == 120.0


def test_listar_pagos():
    response = client.get("/api/pagos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

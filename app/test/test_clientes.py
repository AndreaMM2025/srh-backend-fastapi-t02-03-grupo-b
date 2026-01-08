from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_cliente_1():
    cliente = {
        "ID_CLIENTE": 1,
        "NOMBRE": "Andrea Murillo",
        "IDENTIFICACION": "0954769287",
        "TELEFONO": "0992319870",
        "CORREO": "amurillom3@est.ups.edu.ec",
        "NACIONALIDAD": "Ecuatoriana"
    }

    response = client.post("/api/clientes/", json=cliente)
    assert response.status_code == 200

    data = response.json()
    assert data["ID_CLIENTE"] == 1
    assert data["NOMBRE"] == "Andrea Murillo"
    assert data["CORREO"] == "amurillom3@est.ups.edu.ec"


def test_listar_clientes():
    response = client.get("/api/clientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

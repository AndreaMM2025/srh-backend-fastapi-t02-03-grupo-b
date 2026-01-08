from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_usuario_1():
    usuario = {
        "ID_USUARIO": 1,
        "NOMBRE": "Admin",
        "ROL": "administrador",
        "ESTADO": True
    }

    response = client.post("/api/usuarios/", json=usuario)
    assert response.status_code == 200

    data = response.json()
    assert data["ID_USUARIO"] == 1
    assert data["NOMBRE"] == "Admin"
    assert data["ROL"] == "administrador"


def test_listar_usuarios():
    response = client.get("/api/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
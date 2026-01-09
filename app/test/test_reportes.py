from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_reportes():
    response = client.get("/api/reportes/ingresos")
    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)

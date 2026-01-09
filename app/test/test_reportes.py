from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_reportes():
    # En Swagger: GET /api/reportes/ingresos
    response = client.get("/api/reportes/ingresos")
    assert response.status_code == 200, response.text

    data = response.json()

    assert isinstance(data, (list, dict))

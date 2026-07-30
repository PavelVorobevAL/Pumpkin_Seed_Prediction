from fastapi.testclient import TestClient as TestClient
from app.main import app

def test_missing_values():
    with TestClient(app) as client:
        data = {
            "Area": 50000
        }

        response = client.post("/predict", json=data)

        assert response.status_code == 422
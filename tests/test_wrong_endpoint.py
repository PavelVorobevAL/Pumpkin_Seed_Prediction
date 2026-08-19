from fastapi.testclient import TestClient as TestClient
from app.main import app

def test_unknown_endpoint():

    with TestClient(app) as client:

        response = client.get("/wrong_endpoint")

        assert response.status_code == 404
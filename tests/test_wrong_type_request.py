from fastapi.testclient import TestClient as TestClient
from app.main import app

def test_predict_get_not_allowed():

    with TestClient(app) as client:

        response = client.get("/predict")

        assert response.status_code == 405
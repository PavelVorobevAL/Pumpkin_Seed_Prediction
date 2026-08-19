from fastapi.testclient import TestClient as TestClient
from app.main import app

def test_predict():

    with TestClient(app) as client:
        data = {
            "Area": -50000,
            "Perimeter": 800,
            "Major_Axis_Length": 100,
            "Minor_Axis_Length": 100,
            "Convex_Area": 51500,
            "Equiv_Diameter": 456,
            "Eccentricity": 0.4,
            "Solidity": 0.6,
            "Extent": 0.5,
            "Roundness": 0.3,
            "Aspect_Ration": 1.2,
            "Compactness": 0.5
        }

    response = client.post("/predict", json=data)

    assert response.status_code == 422
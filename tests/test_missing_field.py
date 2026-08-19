from fastapi.testclient import TestClient as TestClient
from app.main import app

def test_predict_missing_field():
    with TestClient(app) as client:

        data = {
            "Area": 50000,
            "Perimeter": 800,
            "Major_Axis_Length": 300,
            "Minor_Axis_Length": 200,
            #Convex_Area
            "Equiv_Diameter": 250,
            "Eccentricity": 0.7,
            "Solidity": 0.98,
            "Extent": 0.75,
            "Roundness": 0.8,
            "Aspect_Ration": 1.5,
            "Compactness": 0.8
        }

        response = client.post("/predict", json=data)

        assert response.status_code == 422
from fastapi.testclient import TestClient as TestClient
from app.main import app


def test_prediction_str():

    with TestClient(app) as client:

        data = {
                    "Area": 90,
                    "Perimeter": 900,
                    "Major_Axis_Length": 350,
                    "Minor_Axis_Length": 180,
                    "Convex_Area": 50500,
                    "Equiv_Diameter": 250,
                    "Eccentricity": 0.8,
                    "Solidity": 0.99,
                    "Extent": 0.75,
                    "Roundness": 0.78,
                    "Aspect_Ration": 1.9,
                    "Compactness": 0.72
                }

        response = client.post("/predict", json=data)

        result = response.json()

        assert isinstance(result["prediction"], str)
# Pumpkin Seed Prediction API

A production-style REST API for pumpkin seed classification built with Python and FastAPI. The project combines a trained machine-learning model with input validation, automated testing, logging, and Docker containerization.

The API receives morphological measurements of a pumpkin seed and predicts its seed variety using a trained machine-learning model.

The project was built to practice the software-engineering skills required to turn an ML model into a usable and testable backend service.

## Main workflow

Client (POST /predict) -> FastAPI Router -> Pydantic Validation -> Prediction Service (ML Model, Label Encoder) -> JSON Response

## Technologies

Python, FastAPI, Pydantic, Scikit-learn, Pandas, Joblib, Pytest, Pytest-cov, Docker, GitHub Actions

## Testing

Testing

The project includes automated tests using Pytest:

      Valid prediction requests
      Invalid input
      Missing required fields
      Incorrect data types
      Zero and negative values
      API response structure
      HTTP error responses
      Prediction service logic
      Model failures

Running Tests:

      python -m pytest
      
Run tests with coverage:

      pytest --cov=app --cov-report=term-missing

Generate an HTML coverage report:

      pytest --cov=app --cov-report=html

## Docker

The application is containerized with Docker to provide a reproducible runtime environment.

Running with Docker:

      Build the image:
      
      docker build -t pumpkin-api .
      
      Run the container:
      
      docker run -p 8000:8000 pumpkin-api
      
      Open:
      
      http://localhost:8000/docs


## Example:

POST /predict -> Predicts the pumpkin seed variety ->

    -> Example request:
    
      {
          "Area": 50000,
          "Perimeter": 800.0,
          "Major_Axis_Length": 300.0,
          "Minor_Axis_Length": 200.0,
          "Convex_Area": 51000,
          "Equiv_Diameter": 250.0,
          "Eccentricity": 0.7,
          "Solidity": 0.98,
          "Extent": 0.75,
          "Roundness": 0.8,
          "Aspect_Ration": 1.5,
          "Compactness": 0.8
      }
      
      Example response:
      
      {
          "message": "Data received",
          "prediction": "ÜRGÜP"
    }

    

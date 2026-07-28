from fastapi import FastAPI

from app.models.seed_model import SeedInputModel
from app.services.predictor import predict_seed


from contextlib import asynccontextmanager
from fastapi import Request

import joblib
import pickle
import pandas as pd

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Loading model...")

    app.state.model = joblib.load("model.joblib")
    app.state.encoder = joblib.load("label_encoder.joblib")

    yield

    print("Application stopped")


app = FastAPI(
            title="Pumpkin Seed API",
            lifespan=lifespan
            )


@app.get("/")
async def root():
    return {"text" : "Hello"}

@app.post("/predict")
async def seed_entry(data: SeedInputModel, request: Request):

    prediction = predict_seed(data, request.app.state.model, request.app.state.encoder)


    return {
        "message": "Data received",
        "prediction": prediction

    }


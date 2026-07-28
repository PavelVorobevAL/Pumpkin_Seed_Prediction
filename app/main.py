from fastapi import FastAPI
from app.models.seed_model import SeedInputModel
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

    model = request.app.state.model
    encoder = request.app.state.encoder

    data_dict = data.model_dump() # converts the Pydantic object into a normal Python dictionary
    X_new = pd.DataFrame([data_dict])

    prediction = model.predict(X_new)
    seed_name = encoder.inverse_transform(prediction)
    



    return {
        "message": "Data received",
        "received_data": data_dict,
        "prediction": seed_name[0]

    }


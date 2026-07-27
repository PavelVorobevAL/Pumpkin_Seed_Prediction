from fastapi import FastAPI
from app.models.seed_model import SeedInputModel
import joblib
import pickle


app = FastAPI(title="Pumpkin Seed API")

@app.get("/")
async def root():
    return {"text" : "Hello"}

@app.post("/predict")
async def seed_entry(data: SeedInputModel):
    data_dict = data.model_dump()

    return {
        "message": "Data received",
        "received_data": data_dict
    }


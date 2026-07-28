from fastapi import FastAPI
from app.models.seed_model import SeedInputModel
import joblib
import pickle
import pandas as pd


app = FastAPI(title="Pumpkin Seed API")

model = joblib.load("model.joblib")
encoder = joblib.load("label_encoder.joblib")

@app.get("/")
async def root():
    return {"text" : "Hello"}

@app.post("/predict")
async def seed_entry(data: SeedInputModel):
    data_dict = data.model_dump() # converts the Pydantic object into a normal Python dictionary
    #X_new = pd.DataFrame([data_dict])

    #prediction = model.predict(X_new)


    return {
        "message": "Data received",
        "received_data": data_dict,
        #"prediction": prediction

    }


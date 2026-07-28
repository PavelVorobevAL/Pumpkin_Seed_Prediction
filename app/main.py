from fastapi import FastAPI

from app.routes import predict

from contextlib import asynccontextmanager

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


app.include_router(predict.router)




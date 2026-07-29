from fastapi import APIRouter
from app.models.seed_model import SeedInputModel, PredictionResponse
from fastapi import Request
from app.services.predictor import predict_seed

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def seed_entry(data: SeedInputModel, request: Request):

    prediction = predict_seed(data, request.app.state.model, request.app.state.encoder)

    return PredictionResponse(
        message="Data received",
        prediction=prediction
    )
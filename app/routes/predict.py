from fastapi import APIRouter, HTTPException, Request
from app.models.seed_model import SeedInputModel, PredictionResponse
from app.services.predictor import predict_seed

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def seed_entry(data: SeedInputModel, request: Request):

    try:

        prediction = predict_seed(
            data, 
            request.app.state.model, 
            request.app.state.encoder
            )

        return PredictionResponse(
            message="Data received",
            prediction=prediction
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed."
        )

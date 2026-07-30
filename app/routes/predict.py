from fastapi import APIRouter, HTTPException, Request
from app.models.seed_model import SeedInputModel, PredictionResponse
from app.services.predictor import predict_seed
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/predict", response_model=PredictionResponse)
async def seed_entry(data: SeedInputModel, request: Request):

    logger.info("Prediction request received.")

    try:

        prediction = predict_seed(
            data, 
            request.app.state.model, 
            request.app.state.encoder
            )

        logger.info(f"Prediction successful: {prediction}")

        return PredictionResponse(
            message="Data received",
            prediction=prediction
        )

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed."
        )

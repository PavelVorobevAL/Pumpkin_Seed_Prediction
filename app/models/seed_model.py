from pydantic import BaseModel, Field

class SeedInputModel(BaseModel):
    Area: int = Field(gt=0, description="Seed area")
    Perimeter: float = Field(gt=0)
    Major_Axis_Length: float = Field(gt=0)
    Minor_Axis_Length: float = Field(gt=0)
    Convex_Area: int = Field(gt=0)
    Equiv_Diameter: float = Field(gt=0)
    Eccentricity: float = Field(gt=0, le=1)
    Solidity: float = Field(gt=0, le=1)
    Extent: float = Field(gt=0, le=1)
    Roundness: float = Field(gt=0, le=1)
    Aspect_Ration: float = Field(gt=0)
    Compactness: float = Field(gt=0, le=1)

class PredictionResponse(BaseModel):
    message: str
    prediction: str
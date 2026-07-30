from pydantic import BaseModel, Field

class SeedInputModel(BaseModel):
    Area: int = Field(gt=0)
    Perimeter: float = Field(gt=0)
    Major_Axis_Length: float = Field(gt=0)
    Minor_Axis_Length: float = Field(gt=0)
    Convex_Area: int = Field(gt=0)
    Equiv_Diameter: float = Field(gt=0)
    Eccentricity: float = Field(gt=0)
    Solidity: float = Field(gt=0)
    Extent: float = Field(gt=0)
    Roundness: float = Field(gt=0)
    Aspect_Ration: float = Field(gt=0)
    Compactness: float = Field(gt=0)

class PredictionResponse(BaseModel):
    message: str
    prediction: str
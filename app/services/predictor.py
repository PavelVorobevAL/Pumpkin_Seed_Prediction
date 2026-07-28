import pandas as pd
from app.models.seed_model import SeedInputModel


def predict_seed(data: SeedInputModel, model, encoder):

    data_dict = data.model_dump() # converts the Pydantic object into a normal Python dictionary
    X_new = pd.DataFrame([data_dict])

    prediction = model.predict(X_new)
    seed_name = encoder.inverse_transform(prediction)

    return seed_name[0]
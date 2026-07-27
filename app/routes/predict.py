import joblib
import pandas as pd

model = joblib.load("model.joblib")

encoder = joblib.load("label_encoder.joblib")

X_new = pd.DataFrame([
    {
        "Area": 500,
        "Perimeter": 90,
        "Major_Axis_Length": 30,
        "Minor_Axis_Length": 20,
        "Convex_Area": 510,
        "Equiv_Diameter": 25,
        "Eccentricity": 0.75,
        "Solidity": 0.98,
        "Extent": 0.82,
        "Roundness": 0.77,
        "Aspect_Ration": 1.50,
        "Compactness": 0.81
    }
])

prediction = model.predict(X_new)

print(prediction)

label = encoder.inverse_transform(prediction)
print(label)
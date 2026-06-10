

import joblib
import numpy as np

scaler = joblib.load(
    "models/scaler.pkl"
)

def preprocess_input(
    income,
    spending_score
):
    data = np.array([
        [income, spending_score]
    ])

    return scaler.transform(data)
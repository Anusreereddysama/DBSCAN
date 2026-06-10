import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

df = pd.read_csv(
    "data/processed/cleaned_data.csv"
)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(df)

model = DBSCAN(
    eps=0.5,
    min_samples=5
)

model.fit(X_scaled)

joblib.dump(
    model,
    "models/dbscan_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

print("Model trained successfully!")
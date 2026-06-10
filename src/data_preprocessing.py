import pandas as pd

df = pd.read_csv("data/raw/Mall_Customers.csv")

# Select useful columns
df = df[[
    "Annual Income (k$)",
    "Spending Score (1-100)"
]]

df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False
)

print("Data cleaned successfully!")
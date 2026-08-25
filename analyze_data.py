import pandas as pd

# Load the dataset
df = pd.read_csv("data/credit_risk.csv")

# Display basic information
print("Dataset shape:")
print(df.shape)

print("\nFirst rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nDefault rate:")
print(df["default"].mean())

import pandas as pd

# Load the dataset
df = pd.read_csv("data/credit_risk.csv")
df["loan_to_income"] = df["loan_amount"] / df["income"]

# Display basic information
print("Dataset shape:")
print(df.shape)

print("\nFirst rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nDefault rate:")
print(df["default"].mean())
print("\nLoan-to-income ratio:")
print(df[["income", "loan_amount", "loan_to_income", "default"]])

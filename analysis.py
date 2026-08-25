import pandas as pd

data = {
    "income": [25000, 40000, 55000, 30000, 70000],
    "loan_amount": [10000, 15000, 20000, 12000, 25000],
    "default": [1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

print(df)
print("\nDefault rate:")
print(df["default"].mean())

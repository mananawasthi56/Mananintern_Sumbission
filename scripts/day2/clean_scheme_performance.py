import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Rows:", len(df))

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nMissing Return Values:")
print(df[return_columns].isnull().sum())

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio:", len(invalid_expense))

# Flag abnormal returns (>100% or <-100%)
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("Return Anomalies:", len(anomalies))

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nScheme Performance cleaned successfully.")
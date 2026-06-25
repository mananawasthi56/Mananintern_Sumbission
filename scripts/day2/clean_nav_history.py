import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Rows:", len(df))

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

df = df.drop_duplicates()

# Missing NAV before fill
print("Missing NAV Before:", df["nav"].isnull().sum())

# Forward fill within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

print("Missing NAV After:", df["nav"].isnull().sum())

# Keep only valid NAV
df = df[df["nav"] > 0]

print("Final Rows:", len(df))

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV History cleaned successfully.")
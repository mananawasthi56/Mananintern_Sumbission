import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Rows:", len(df))

# Convert date column
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]

invalid = df[~df["transaction_type"].isin(valid_types)]

print("Invalid Transaction Types:", len(invalid))

# Keep only valid transaction types
df = df[df["transaction_type"].isin(valid_types)]

# Check amount
invalid_amount = (df["amount_inr"] <= 0).sum()

print("Invalid Amounts:", invalid_amount)

df = df[df["amount_inr"] > 0]

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("\nFinal Rows:", len(df))

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nInvestor Transactions cleaned successfully.")
import pandas as pd

files = {
    "01_fund_master.csv": "fund_master_clean.csv",
    "03_aum_by_fund_house.csv": "aum_by_fund_house_clean.csv",
    "04_monthly_sip_inflows.csv": "monthly_sip_inflows_clean.csv",
    "05_category_inflows.csv": "category_inflows_clean.csv",
    "06_industry_folio_count.csv": "industry_folio_count_clean.csv",
    "09_portfolio_holdings.csv": "portfolio_holdings_clean.csv",
    "10_benchmark_indices.csv": "benchmark_indices_clean.csv"
}

for source, output in files.items():

    print(f"\nCleaning {source}")

    # Read dataset
    df = pd.read_csv(f"data/raw/{source}")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows where all values are missing
    df = df.dropna(how="all")

    # Convert date columns (only if they exist)
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Save cleaned dataset
    df.to_csv(f"data/processed/{output}", index=False)

    print(f"Saved -> {output}")

print("\nAll remaining datasets cleaned successfully.")
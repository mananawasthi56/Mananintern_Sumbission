import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 50)
print("FUND MASTER ANALYSIS")
print("=" * 50)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].nunique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].nunique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].nunique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

print("\n" + "=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\nTotal AMFI Codes in Fund Master:")
print(len(master_codes))

print("\nTotal AMFI Codes in NAV History:")
print(len(nav_codes))

print("\nMissing Codes:")
print(len(missing_codes))

if len(missing_codes) > 0:
    print(missing_codes)

coverage = (
    len(master_codes.intersection(nav_codes))
    / len(master_codes)
) * 100

print(f"\nCoverage: {coverage:.2f}%")
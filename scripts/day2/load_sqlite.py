import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///database/bluestock_mf.db")

# Load cleaned datasets
fund_master = pd.read_csv("data/processed/fund_master_clean.csv")
nav = pd.read_csv("data/processed/nav_history_clean.csv")
transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")
aum = pd.read_csv("data/processed/aum_by_fund_house_clean.csv")
monthly_sip = pd.read_csv("data/processed/monthly_sip_inflows_clean.csv")
category_inflows = pd.read_csv("data/processed/category_inflows_clean.csv")
industry_folio = pd.read_csv("data/processed/industry_folio_count_clean.csv")
portfolio = pd.read_csv("data/processed/portfolio_holdings_clean.csv")
benchmark = pd.read_csv("data/processed/benchmark_indices_clean.csv")

# Load into SQLite
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

monthly_sip.to_sql("monthly_sip_inflows", engine, if_exists="replace", index=False)
category_inflows.to_sql("category_inflows", engine, if_exists="replace", index=False)
industry_folio.to_sql("industry_folio_count", engine, if_exists="replace", index=False)
portfolio.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("benchmark_indices", engine, if_exists="replace", index=False)

print("SQLite Database Created Successfully!")

print("\nRow Counts")
print("Fund Master:", len(fund_master))
print("NAV:", len(nav))
print("Transactions:", len(transactions))
print("Performance:", len(performance))
print("AUM:", len(aum))
print("Monthly SIP:", len(monthly_sip))
print("Category Inflows:", len(category_inflows))
print("Industry Folio:", len(industry_folio))
print("Portfolio Holdings:", len(portfolio))
print("Benchmark Indices:", len(benchmark))
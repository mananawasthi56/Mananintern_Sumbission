# Mutual Fund Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company name |
| scheme_name | Text | Name of the mutual fund scheme |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Regular or Direct plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio (%) |
| exit_load_pct | Float | Exit load (%) |
| min_sip_amount | Integer | Minimum SIP investment |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk level |
| sebi_category_code | Text | SEBI category code |

---

## 2. NAV History (02_nav_history.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 3. AUM by Fund House (03_aum_by_fund_house.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| date | Date | Reporting date |
| fund_house | Text | Mutual fund company |
| aum_lakh_crore | Float | AUM in lakh crore |
| aum_crore | Integer | Assets Under Management |
| num_schemes | Integer | Total schemes |

---

## 4. Monthly SIP Inflows (04_monthly_sip_inflows.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| month | Text | Month |
| sip_inflow_crore | Integer | SIP inflow |
| active_sip_accounts_crore | Float | Active SIP accounts |
| new_sip_accounts_lakh | Float | New SIP accounts |
| sip_aum_lakh_crore | Float | SIP AUM |
| yoy_growth_pct | Float | Year-over-year growth |

---

## 5. Category Inflows (05_category_inflows.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| month | Text | Month |
| category | Text | Fund category |
| net_inflow_crore | Float | Net inflow |

---

## 6. Industry Folio Count (06_industry_folio_count.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| month | Text | Month |
| total_folios_crore | Float | Total folios |
| equity_folios_crore | Float | Equity folios |
| debt_folios_crore | Float | Debt folios |
| hybrid_folios_crore | Float | Hybrid folios |
| others_folios_crore | Float | Other folios |

---

## 7. Scheme Performance (07_scheme_performance.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | Integer | AMFI code |
| scheme_name | Text | Scheme name |
| fund_house | Text | Fund house |
| category | Text | Fund category |
| plan | Text | Plan type |
| return_1yr_pct | Float | 1-Year Return |
| return_3yr_pct | Float | 3-Year Return |
| return_5yr_pct | Float | 5-Year Return |
| benchmark_3yr_pct | Float | Benchmark return |
| alpha | Float | Alpha |
| beta | Float | Beta |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Standard deviation |
| max_drawdown_pct | Float | Maximum drawdown |
| aum_crore | Integer | AUM |
| expense_ratio_pct | Float | Expense ratio |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Text | Risk grade |

---

## 8. Investor Transactions (08_investor_transactions.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | AMFI code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Integer | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier classification |
| age_group | Text | Investor age group |
| gender | Text | Gender |
| annual_income_lakh | Float | Annual income |
| payment_mode | Text | Payment mode |
| kyc_status | Text | KYC status |

---

## 9. Portfolio Holdings (09_portfolio_holdings.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | Integer | AMFI code |
| stock_symbol | Text | Stock symbol |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio weight |
| market_value_cr | Float | Market value |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio date |

---

## 10. Benchmark Indices (10_benchmark_indices.csv)

| Column | Data Type | Description |
|---------|----------|-------------|
| date | Date | Trading date |
| index_name | Text | Index name |
| close_value | Float | Closing index value |

---

## Source

All datasets were provided as part of the Bluestock Mutual Fund Capstone Project. Live NAV data was fetched using the MFAPI API.
```sql
-- Query 1: Find the top 5 mutual funds based on Assets Under Management (AUM)

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- Query 2: Calculate the average NAV for each month

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- Query 3: Display monthly SIP inflows along with year-over-year growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- Query 4: Check transaction count and total investment amount for each state

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- Query 5: List all funds where the expense ratio is less than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Query 6: Calculate the average 1-year return for each fund category

SELECT
    category,
    ROUND(AVG(return_1yr_pct), 2) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;


-- Query 7: Find the top 10 investors based on their total investment amount

SELECT
    investor_id,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_investment DESC
LIMIT 10;


-- Query 8: Count how many transactions were made using each payment mode

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;


-- Query 9: Check the distribution of investors based on KYC status

SELECT
    kyc_status,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status
ORDER BY total_investors DESC;


-- Query 10: Find the average expense ratio for each fund house

SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_expense_ratio;
```

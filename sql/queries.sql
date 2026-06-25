-- ==========================================
-- Mutual Fund Analytics - Analytical Queries
-- ==========================================

------------------------------------------------
-- 1. Top 5 Funds by AUM
------------------------------------------------
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

------------------------------------------------
-- 2. Average NAV Per Month
------------------------------------------------
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

------------------------------------------------
-- 3. SIP Year-over-Year Growth
------------------------------------------------
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

------------------------------------------------
-- 4. Transactions by State
------------------------------------------------
SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

------------------------------------------------
-- 5. Funds with Expense Ratio Less Than 1%
------------------------------------------------
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

------------------------------------------------
-- 6. Average 1-Year Return by Category
------------------------------------------------
SELECT
    category,
    ROUND(AVG(return_1yr_pct), 2) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;

------------------------------------------------
-- 7. Top 10 Investors by Investment Amount
------------------------------------------------
SELECT
    investor_id,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_investment DESC
LIMIT 10;

------------------------------------------------
-- 8. Transactions by Payment Mode
------------------------------------------------
SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;

------------------------------------------------
-- 9. KYC Status Distribution
------------------------------------------------
SELECT
    kyc_status,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status
ORDER BY total_investors DESC;

------------------------------------------------
-- 10. Average Expense Ratio by Fund House
------------------------------------------------
SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_expense_ratio;
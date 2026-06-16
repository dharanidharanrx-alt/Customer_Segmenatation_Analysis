-- ============================================================
-- PRDA-05 | Retail Customer Sales Analysis – Shopping Malls
-- SQL Analysis: All 9 Business Questions
-- Author  : Dharanidharan
-- Dataset : customer_transactions (1,000 rows)
-- ============================================================

-- ────────────────────────────────────────────────────────────
-- Query 1 – Shopping Distribution by Gender
-- Business Question: How is the shopping distribution by gender?
-- ────────────────────────────────────────────────────────────
SELECT 
    gender,
    COUNT(*)                                                            AS transaction_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_transactions), 2) AS pct_share
FROM customer_transactions
GROUP BY gender
ORDER BY transaction_count DESC;


-- ────────────────────────────────────────────────────────────
-- Query 2 – Products Sold by Gender
-- Business Question: Which gender did we sell more products to?
-- ────────────────────────────────────────────────────────────
SELECT 
    gender,
    SUM(quantity)   AS total_units_sold,
    COUNT(*)        AS transaction_count,
    ROUND(AVG(quantity), 2) AS avg_units_per_txn
FROM customer_transactions
GROUP BY gender
ORDER BY total_units_sold DESC;


-- ────────────────────────────────────────────────────────────
-- Query 3 – Revenue by Gender
-- Business Question: Which gender generated more revenue?
-- ────────────────────────────────────────────────────────────
SELECT 
    gender,
    ROUND(SUM(price), 2)   AS total_revenue,
    ROUND(AVG(price), 2)   AS avg_order_value,
    COUNT(*)               AS transactions
FROM customer_transactions
GROUP BY gender
ORDER BY total_revenue DESC;


-- ────────────────────────────────────────────────────────────
-- Query 4 – Category Distribution by Gender & Other Columns
-- Business Question: Distribution of purchase categories relative to other columns?
-- ────────────────────────────────────────────────────────────
SELECT 
    gender,
    category,
    COUNT(*)               AS transactions,
    SUM(quantity)          AS units_sold,
    ROUND(SUM(price), 2)   AS revenue,
    ROUND(AVG(price), 2)   AS avg_order_value
FROM customer_transactions
GROUP BY gender, category
ORDER BY gender, revenue DESC;


-- ────────────────────────────────────────────────────────────
-- Query 5 – Shopping Distribution by Age Group
-- Business Question: How is the shopping distribution according to age?
-- ────────────────────────────────────────────────────────────
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '55+'
    END AS age_group,
    COUNT(*)                                                            AS transaction_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_transactions), 2) AS pct_share
FROM customer_transactions
GROUP BY age_group
ORDER BY 
    CASE age_group
        WHEN '18-25' THEN 1 WHEN '26-35' THEN 2 WHEN '36-45' THEN 3
        WHEN '46-55' THEN 4 ELSE 5
    END;


-- ────────────────────────────────────────────────────────────
-- Query 6 – Products Sold by Age Group
-- Business Question: Which age category did we sell more products to?
-- ────────────────────────────────────────────────────────────
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '55+'
    END AS age_group,
    SUM(quantity)          AS total_units_sold,
    COUNT(*)               AS transaction_count,
    ROUND(SUM(price), 2)   AS total_revenue
FROM customer_transactions
GROUP BY age_group
ORDER BY total_revenue DESC;


-- ────────────────────────────────────────────────────────────
-- Query 7 – Revenue by Age Group
-- Business Question: Which age category generated more revenue?
-- ────────────────────────────────────────────────────────────
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '55+'
    END AS age_group,
    COUNT(*)               AS transactions,
    SUM(quantity)          AS units_sold,
    ROUND(SUM(price), 2)   AS total_revenue,
    ROUND(AVG(price), 2)   AS avg_order_value,
    ROUND(SUM(price) * 100.0 / (SELECT SUM(price) FROM customer_transactions), 2) AS pct_of_total_revenue
FROM customer_transactions
GROUP BY age_group
ORDER BY total_revenue DESC;


-- ────────────────────────────────────────────────────────────
-- Query 8 – Payment Method vs Other Columns
-- Business Question: Does the payment method have a relation with other columns?
-- ────────────────────────────────────────────────────────────
SELECT 
    payment_method,
    category,
    COUNT(*)               AS transactions,
    SUM(quantity)          AS units_sold,
    ROUND(SUM(price), 2)   AS revenue,
    ROUND(AVG(price), 2)   AS avg_order_value
FROM customer_transactions
GROUP BY payment_method, category
ORDER BY payment_method, revenue DESC;


-- ────────────────────────────────────────────────────────────
-- Query 9 – Payment Method Distribution
-- Business Question: How is the distribution of the payment method?
-- ────────────────────────────────────────────────────────────
SELECT 
    payment_method,
    COUNT(*)                                                            AS transaction_count,
    SUM(quantity)                                                       AS units_sold,
    ROUND(SUM(price), 2)                                                AS total_revenue,
    ROUND(AVG(price), 2)                                                AS avg_order_value,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_transactions), 2) AS pct_share
FROM customer_transactions
GROUP BY payment_method
ORDER BY transaction_count DESC;


-- ────────────────────────────────────────────────────────────
-- BONUS: Mall Performance Summary
-- ────────────────────────────────────────────────────────────
SELECT 
    shopping_mall,
    COUNT(*)               AS transactions,
    SUM(quantity)          AS units_sold,
    ROUND(SUM(price), 2)   AS total_revenue,
    ROUND(AVG(price), 2)   AS avg_order_value,
    ROUND(SUM(price) * 100.0 / (SELECT SUM(price) FROM customer_transactions), 2) AS revenue_share_pct
FROM customer_transactions
GROUP BY shopping_mall
ORDER BY total_revenue DESC;


-- ────────────────────────────────────────────────────────────
-- BONUS: Monthly Revenue Trend
-- ────────────────────────────────────────────────────────────
SELECT 
    strftime('%Y-%m', invoice_date)  AS year_month,
    COUNT(*)                         AS transactions,
    ROUND(SUM(price), 2)             AS monthly_revenue,
    ROUND(AVG(price), 2)             AS avg_order_value
FROM customer_transactions
GROUP BY year_month
ORDER BY year_month;

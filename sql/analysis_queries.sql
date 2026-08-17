------------------------
-- Overall sales summary
------------------------

SELECT
    COUNT(DISTINCT i.invoice_id) AS total_invoices,
    SUM(ii.quantity) AS total_units_sold,
    ROUND(SUM(ii.quantity * ii.price), 2) AS total_revenue
FROM invoice_items ii
JOIN invoices i
    ON ii.invoice_id = i.invoice_id;

------------------------
-- Monthly sales
------------------------

SELECT
    DATE_TRUNC('month', i.invoice_date) AS month,
    COUNT(DISTINCT i.invoice_id) AS total_invoices,
    SUM(ii.quantity) AS total_units_sold,
    ROUND(SUM(ii.quantity * ii.price), 2) AS total_revenue
FROM invoice_items ii
JOIN invoices i
    ON ii.invoice_id = i.invoice_id
GROUP BY DATE_TRUNC('month', i.invoice_date)
ORDER BY month;

------------------------
-- Top products by revenue
------------------------

SELECT
    p.stock_code,
    p.description,
    SUM(ii.quantity) AS total_units_sold,
    ROUND(SUM(ii.quantity * ii.price), 2) AS total_revenue
FROM invoice_items ii
JOIN products p
    ON ii.stock_code = p.stock_code
GROUP BY
    p.stock_code,
    p.description
ORDER BY total_revenue DESC
LIMIT 10;

------------------------
-- Sales by country
------------------------

SELECT
    i.country,
    COUNT(DISTINCT i.invoice_id) AS total_invoices,
    SUM(ii.quantity) AS total_units_sold,
    ROUND(SUM(ii.quantity * ii.price), 2) AS total_revenue
FROM invoice_items ii
JOIN invoices i
    ON ii.invoice_id = i.invoice_id
GROUP BY i.country
ORDER BY total_revenue DESC;

------------------------
-- Top customers by revenue
------------------------

SELECT
    i.customer_id,
    COUNT(DISTINCT i.invoice_id) AS total_invoices,
    ROUND(SUM(ii.quantity * ii.price), 2) AS total_revenue
FROM invoices i
JOIN invoice_items ii
    ON i.invoice_id = ii.invoice_id
WHERE i.customer_id IS NOT NULL
GROUP BY i.customer_id
ORDER BY total_revenue DESC
LIMIT 10;

------------------------
-- Monthly revenue with month-over-month change
------------------------

WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', i.invoice_date) AS month,
        SUM(ii.quantity * ii.price) AS revenue
    FROM invoices i
    JOIN invoice_items ii
        ON i.invoice_id = ii.invoice_id
    GROUP BY DATE_TRUNC('month', i.invoice_date)
)

SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(
        100 * (revenue - LAG(revenue) OVER (ORDER BY month))
        / LAG(revenue) OVER (ORDER BY month),
        2
    ) AS revenue_change_percent
FROM monthly_sales
ORDER BY month;

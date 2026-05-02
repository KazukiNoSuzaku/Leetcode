"""
SQL problem — Customers With Strictly Increasing Purchases.

Table: Orders(order_id, customer_id, order_date, price)

Return each customer whose total purchase amount is strictly greater every year
compared to the previous year they appeared. Order by customer_id.

WITH yearly AS (
    SELECT customer_id,
           YEAR(order_date) AS yr,
           SUM(price)       AS total
    FROM Orders
    GROUP BY customer_id, YEAR(order_date)
),
lagged AS (
    SELECT customer_id, yr, total,
           LAG(total) OVER (PARTITION BY customer_id ORDER BY yr) AS prev_total
    FROM yearly
)
SELECT customer_id
FROM lagged
GROUP BY customer_id
HAVING SUM(CASE WHEN prev_total IS NOT NULL AND total <= prev_total THEN 1 ELSE 0 END) = 0
ORDER BY customer_id;
"""

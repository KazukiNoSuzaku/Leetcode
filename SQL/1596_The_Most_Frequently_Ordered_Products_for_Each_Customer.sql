-- Author: Kaustav Ghosh
-- Problem: The Most Frequently Ordered Products for Each Customer
-- Approach: Counting orders per customer and product is a plain grouping, but picking the busiest product per customer needs a per-customer comparison, which is what a window function gives: RANK over partitions by customer, ordered by that count descending. RANK rather than ROW_NUMBER matters here because ties must all be reported, and RANK hands every tied product the same value of 1 while ROW_NUMBER would arbitrarily keep only one of them. Customers who never ordered simply never appear in Orders, so they drop out without any extra filtering.

WITH product_counts AS (
    SELECT customer_id,
           product_id,
           RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS placing
    FROM Orders
    GROUP BY customer_id, product_id
)
SELECT pc.customer_id,
       pc.product_id,
       p.product_name
FROM product_counts pc
JOIN Products p ON pc.product_id = p.product_id
WHERE pc.placing = 1;

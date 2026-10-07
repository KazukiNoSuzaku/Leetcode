-- Author: Kaustav Ghosh
-- Problem: The Most Recent Three Orders
-- Approach: Number each customer's orders from newest to oldest with ROW_NUMBER over a per-customer partition, which is unambiguous because a customer places at most one order per day, then keep the first three and sort as the question asks

SELECT customer_name, customer_id, order_id, order_date
FROM (
    SELECT c.name AS customer_name,
           c.customer_id,
           o.order_id,
           o.order_date,
           ROW_NUMBER() OVER (PARTITION BY c.customer_id ORDER BY o.order_date DESC) AS recency
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
) ranked
WHERE recency <= 3
ORDER BY customer_name ASC, customer_id ASC, order_date DESC;

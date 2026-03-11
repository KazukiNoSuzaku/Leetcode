-- Find the customer who has placed the largest number of orders.
-- Author: Kaustav Ghosh

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

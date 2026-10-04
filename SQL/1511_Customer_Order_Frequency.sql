-- Author: Kaustav Ghosh
-- Problem: Customer Order Frequency
-- Approach: Join each order to its product price and total quantity * price per customer, splitting June and July 2020 with conditional sums, then keep only customers whose both monthly totals reach 100

SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Product p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING SUM(CASE WHEN o.order_date BETWEEN '2020-06-01' AND '2020-06-30'
                THEN o.quantity * p.price ELSE 0 END) >= 100
   AND SUM(CASE WHEN o.order_date BETWEEN '2020-07-01' AND '2020-07-31'
                THEN o.quantity * p.price ELSE 0 END) >= 100;

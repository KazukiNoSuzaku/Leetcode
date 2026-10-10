-- Author: Kaustav Ghosh
-- Problem: Unique Orders and Customers Per Month
-- Approach: Filter to invoices above 20 first so that a month whose every order is cheap drops out of the result entirely rather than appearing with a count of zero, then collapse each date to its year and month before grouping, since grouping the raw date would split a single month across its individual days; order_id is unique so a plain COUNT counts distinct orders, while a customer can order several times in a month and therefore needs COUNT(DISTINCT ...)

SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       COUNT(order_id) AS order_count,
       COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY DATE_FORMAT(order_date, '%Y-%m');

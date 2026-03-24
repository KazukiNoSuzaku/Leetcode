-- Author: Kaustav Ghosh
-- Problem 2082: The Number of Rich Customers

SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500;

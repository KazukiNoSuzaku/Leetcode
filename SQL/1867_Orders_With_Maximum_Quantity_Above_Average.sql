-- Author: Kaustav Ghosh
-- Problem: Orders With Maximum Quantity Above Average
-- Approach: Each order is summarised once into its largest single quantity and its average quantity, which is what grouping by order_id over the detail rows gives directly; the average is per distinct product, and since order and product together are unique that is exactly the row count. An order is imbalanced when its largest quantity beats the average of every order, which is the same as beating the largest of those averages, so the comparison is against a single scalar taken from that same summary rather than a correlated check against each order in turn.

WITH PerOrder AS (
    SELECT
        order_id,
        MAX(quantity) AS largest,
        AVG(quantity) AS mean
    FROM OrdersDetails
    GROUP BY order_id
)
SELECT order_id
FROM PerOrder
WHERE largest > (SELECT MAX(mean) FROM PerOrder);

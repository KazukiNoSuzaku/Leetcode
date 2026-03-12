-- Author: Kaustav Ghosh
-- 1084. Sales Analysis III
-- https://leetcode.com/problems/sales-analysis-iii/

SELECT p.product_id, p.product_name
FROM Product p
WHERE p.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)
AND p.product_id IN (
    SELECT product_id FROM Sales
);

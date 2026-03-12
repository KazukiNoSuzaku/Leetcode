-- Author: Kaustav Ghosh
-- 1082. Sales Analysis I
-- https://leetcode.com/problems/sales-analysis-i/

SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (
    SELECT MAX(total)
    FROM (
        SELECT SUM(price) AS total
        FROM Sales
        GROUP BY seller_id
    ) t
);

-- Author: Kaustav Ghosh
-- Problem: Group Sold Products By The Date
-- Approach: GROUP BY date, GROUP_CONCAT distinct product names

SELECT sell_date,
       COUNT(DISTINCT product) AS num_sold,
       GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;

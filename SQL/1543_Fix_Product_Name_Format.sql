-- Author: Kaustav Ghosh
-- Problem: Fix Product Name Format
-- Approach: Normalise first, group second: trim and lowercase the name and cut the date down to its month, then group by those cleaned expressions rather than the raw columns, since grouping by the bare column would keep names differing only by stray spaces apart

SELECT LOWER(TRIM(product_name)) AS product_name,
       DATE_FORMAT(sale_date, '%Y-%m') AS sale_date,
       COUNT(*) AS total
FROM Sales
GROUP BY LOWER(TRIM(product_name)), DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY product_name ASC, sale_date ASC;

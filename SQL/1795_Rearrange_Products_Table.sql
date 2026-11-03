-- Author: Kaustav Ghosh
-- Problem: Rearrange Products Table
-- Approach: The table is wide, one column per store, and the answer wants it long, one row per product and store, so each store column is selected separately with its name supplied as a literal and the three results stacked. Filtering out the null prices in each branch drops the product and store combinations that do not exist, which is what the problem asks for, and UNION ALL is used because the branches cannot overlap and no duplicate check is needed.

SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price FROM Products WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price FROM Products WHERE store3 IS NOT NULL;

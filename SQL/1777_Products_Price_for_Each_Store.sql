-- Author: Kaustav Ghosh
-- Problem: Product's Price for Each Store
-- Approach: The rows hold one store per record and the answer wants one record per product with a column per store, so this is a pivot. Grouping by product_id collapses the records, and a conditional expression per store picks out the matching price while yielding nothing for the other stores. MAX over a group that contains no row for a store returns NULL, which is exactly the required output for a product that store does not sell.

SELECT
    product_id,
    MAX(CASE WHEN store = 'store1' THEN price END) AS store1,
    MAX(CASE WHEN store = 'store2' THEN price END) AS store2,
    MAX(CASE WHEN store = 'store3' THEN price END) AS store3
FROM Products
GROUP BY product_id;

-- Author: Kaustav Ghosh
-- Problem: Sellers With No Sales
-- Approach: This is an anti-join: keep the sellers for whom no 2020 order exists. I write it as NOT EXISTS rather than NOT IN deliberately, because NOT IN against a subquery that yields even a single NULL seller_id evaluates to UNKNOWN for every row and would silently return nothing at all, whereas NOT EXISTS is immune to that. Filtering the year inside the correlated subquery rather than outside it matters too: a seller with orders only in 2019 must still be reported, so the year test belongs to the existence check and not to the outer query.

SELECT s.seller_name
FROM Seller s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.seller_id = s.seller_id
      AND YEAR(o.sale_date) = 2020
)
ORDER BY s.seller_name ASC;

-- Author: Kaustav Ghosh
-- Problem: Find Customers With Positive Revenue this Year
-- Approach: Customer and year together are unique, so each customer has at most one row for 2021 and no grouping or aggregation is needed: the two conditions on that row, the right year and a revenue above zero, are a plain filter. A customer with no 2021 row simply has nothing to match, which is already the required behaviour, and revenue being allowed to go negative is why the comparison has to be strictly greater than zero rather than merely non-zero.

SELECT customer_id
FROM Customers
WHERE year = 2021
  AND revenue > 0;

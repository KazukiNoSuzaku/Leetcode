-- Author: Kaustav Ghosh
-- Problem: Recyclable and Low Fat Products
-- Approach: Both flags are enumerations holding only 'Y' or 'N', so the requirement is a straight conjunction on the two columns with no joins, grouping or aggregation involved. Comparing against the literal 'Y' rather than testing for not-'N' keeps it correct even if a column were ever to admit another value.

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';

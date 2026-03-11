-- Find the largest number that appears only once in MyNumbers; return null if none exists.
-- Author: Kaustav Ghosh

SELECT MAX(num) AS num
FROM (
    SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1
) t;

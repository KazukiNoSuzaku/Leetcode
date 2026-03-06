-- Table: Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- Write a solution to report all the duplicate emails.

-- Author: Kaustav Ghosh

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;

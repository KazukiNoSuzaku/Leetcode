-- Table: Customers
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- Table: Orders
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | customerId  | int  |
-- +-------------+------+
-- Write a solution to find all customers who never order anything.

-- Author: Kaustav Ghosh

SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);

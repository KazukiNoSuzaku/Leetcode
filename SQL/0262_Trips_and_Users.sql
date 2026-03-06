-- Table: Trips
-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | id          | int      |
-- | client_id   | int      |
-- | driver_id   | int      |
-- | city_id     | int      |
-- | status      | enum     |
-- | request_at  | varchar  |
-- +-------------+----------+
-- Table: Users
-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | users_id    | int      |
-- | banned      | enum     |
-- | role        | enum     |
-- +-------------+----------+
-- Write a solution to find the cancellation rate of requests with unbanned users each day between
-- "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

-- Author: Kaustav Ghosh

SELECT request_at AS Day,
       ROUND(SUM(status != 'completed') / COUNT(*), 2) AS `Cancellation Rate`
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;

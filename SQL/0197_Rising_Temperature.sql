-- Table: Weather
-- +---------------+------+
-- | Column Name   | Type |
-- +---------------+------+
-- | id            | int  |
-- | recordDate    | date |
-- | temperature   | int  |
-- +---------------+------+
-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Author: Kaustav Ghosh

SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;

-- Author: Kaustav Ghosh
-- Problem: Users That Actively Request Confirmation Messages
-- Approach: A user qualifies as soon as some pair of their own requests lies within 24 hours of each other, so I join Confirmations to itself on the user and keep the pairs whose timestamps are at most 86400 seconds apart. Requiring the second timestamp to be strictly later than the first both orders each pair one way and rules out matching a row with itself, and comparing in whole seconds makes the stated boundary case of exactly 24 hours count as inside the window. The Signups table is not needed because every user_id in Confirmations already references it, and DISTINCT collapses a user who has many such pairs to a single row.

SELECT DISTINCT c1.user_id
FROM Confirmations AS c1
JOIN Confirmations AS c2
    ON c2.user_id = c1.user_id
    AND c2.time_stamp > c1.time_stamp
    AND TIMESTAMPDIFF(SECOND, c1.time_stamp, c2.time_stamp) <= 24 * 60 * 60;

-- Author: Kaustav Ghosh
-- Problem: First and Last Call On the Same Day
-- Approach: Calls count whether the user placed or received them, so the first step is to turn each stored row into two directed rows, one from each participant's point of view, giving a plain user-and-other-party log. Within each user and each calendar day the earliest and latest call are then read off with FIRST_VALUE over the same partition ordered forwards and backwards, which avoids having to join the day's minimum and maximum times back against the log. A user qualifies when those two other parties are the same on at least one day, which also covers a day holding a single call since then the earliest and latest row are one and the same, and DISTINCT collapses a user who qualifies on several days to one row.

WITH Directed AS (
    SELECT caller_id AS user_id, recipient_id AS other_id, call_time FROM Calls
    UNION ALL
    SELECT recipient_id AS user_id, caller_id AS other_id, call_time FROM Calls
),
Edges AS (
    SELECT
        user_id,
        FIRST_VALUE(other_id) OVER (
            PARTITION BY user_id, DATE(call_time) ORDER BY call_time ASC
        ) AS earliest,
        FIRST_VALUE(other_id) OVER (
            PARTITION BY user_id, DATE(call_time) ORDER BY call_time DESC
        ) AS latest
    FROM Directed
)
SELECT DISTINCT user_id
FROM Edges
WHERE earliest = latest;

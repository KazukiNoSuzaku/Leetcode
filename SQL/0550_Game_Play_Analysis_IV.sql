-- Report the fraction of players that logged in again on the day after the day they
-- first logged in, rounded to 2 decimal places.
-- Author: Kaustav Ghosh

SELECT ROUND(
    COUNT(DISTINCT a2.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
) AS fraction
FROM Activity a1
JOIN Activity a2 ON a1.player_id = a2.player_id
    AND DATEDIFF(a2.event_date, a1.event_date) = 1
WHERE (a1.player_id, a1.event_date) IN (
    SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id
);

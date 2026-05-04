"""
SQL problem — Merge Overlapping Events in the Same Hall.

Table: HallEvents(hall_id, start_day, end_day)

For each hall, merge all overlapping or touching events into the minimum set of
non-overlapping intervals. Two events overlap if one starts on or before the other ends.

WITH sorted_events AS (
    SELECT hall_id, start_day, end_day,
           MAX(end_day) OVER (
               PARTITION BY hall_id
               ORDER BY start_day
               ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
           ) AS prev_max_end
    FROM HallEvents
),
groups AS (
    SELECT hall_id, start_day, end_day,
           SUM(CASE WHEN start_day > prev_max_end OR prev_max_end IS NULL THEN 1 ELSE 0 END)
               OVER (PARTITION BY hall_id ORDER BY start_day) AS grp
    FROM sorted_events
)
SELECT hall_id, MIN(start_day) AS start_day, MAX(end_day) AS end_day
FROM groups
GROUP BY hall_id, grp
ORDER BY hall_id, start_day;
"""

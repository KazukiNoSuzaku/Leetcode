-- Author: Kaustav Ghosh
-- Problem: Ad-Free Sessions
-- Approach: A session is reported exactly when no ad exists for that same customer at a moment inside the session's inclusive window, which is a question about absence rather than about matching rows, so a correlated NOT EXISTS expresses it directly. Phrasing it that way also sidesteps the trap in a join-based version: joining Playback to Ads and filtering would both duplicate sessions that saw several ads and, under an anti-join written with NOT IN, silently drop everything if any timestamp were null.

SELECT p.session_id
FROM Playback AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM Ads AS a
    WHERE a.customer_id = p.customer_id
      AND a.timestamp BETWEEN p.start_time AND p.end_time
);

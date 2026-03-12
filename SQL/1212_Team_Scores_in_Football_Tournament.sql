-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Calculate points per team based on match results

SELECT t.team_id, t.team_name,
       IFNULL(SUM(
           CASE
               WHEN t.team_id = m.host_team AND m.host_goals > m.guest_goals THEN 3
               WHEN t.team_id = m.guest_team AND m.guest_goals > m.host_goals THEN 3
               WHEN m.host_goals = m.guest_goals THEN 1
               ELSE 0
           END
       ), 0) AS num_points
FROM Teams t
LEFT JOIN Matches m ON t.team_id = m.host_team OR t.team_id = m.guest_team
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC, t.team_id ASC;

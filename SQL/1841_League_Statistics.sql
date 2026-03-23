-- Author: Kaustav Ghosh
-- Problem 1841: League Statistics (Premium)
-- This is a premium problem

SELECT
    team_name,
    SUM(matches_played) AS matches_played,
    SUM(points) AS points,
    SUM(goal_for) AS goal_for,
    SUM(goal_against) AS goal_against,
    SUM(goal_for) - SUM(goal_against) AS goal_diff
FROM (
    SELECT
        t.team_name,
        COUNT(*) AS matches_played,
        SUM(CASE
            WHEN m.home_team_goals > m.away_team_goals THEN 3
            WHEN m.home_team_goals = m.away_team_goals THEN 1
            ELSE 0
        END) AS points,
        SUM(m.home_team_goals) AS goal_for,
        SUM(m.away_team_goals) AS goal_against
    FROM Teams t
    JOIN Matches m ON t.team_id = m.home_team_id
    GROUP BY t.team_name
    UNION ALL
    SELECT
        t.team_name,
        COUNT(*) AS matches_played,
        SUM(CASE
            WHEN m.away_team_goals > m.home_team_goals THEN 3
            WHEN m.away_team_goals = m.home_team_goals THEN 1
            ELSE 0
        END) AS points,
        SUM(m.away_team_goals) AS goal_for,
        SUM(m.home_team_goals) AS goal_against
    FROM Teams t
    JOIN Matches m ON t.team_id = m.away_team_id
    GROUP BY t.team_name
) combined
GROUP BY team_name
ORDER BY points DESC, goal_diff DESC, team_name;

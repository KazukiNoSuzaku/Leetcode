-- Author: Kaustav Ghosh
-- Problem: League Statistics
-- Approach: Every match contributes to two teams, so the fixtures are first unfolded into one row per team per match, with that team's goals and its opponent's the right way round in each branch. Points are decided inside the same expression, three for more goals, one for equal and none otherwise, which means a single grouped pass then yields every column including the goal difference. The join to Teams is an inner one, so a team that has not played does not appear, and the ordering applies the three stated tie-breaks in turn.

WITH Appearances AS (
    SELECT
        home_team_id AS team_id,
        home_team_goals AS scored,
        away_team_goals AS conceded,
        CASE
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals = away_team_goals THEN 1
            ELSE 0
        END AS earned
    FROM Matches
    UNION ALL
    SELECT
        away_team_id AS team_id,
        away_team_goals AS scored,
        home_team_goals AS conceded,
        CASE
            WHEN away_team_goals > home_team_goals THEN 3
            WHEN away_team_goals = home_team_goals THEN 1
            ELSE 0
        END AS earned
    FROM Matches
)
SELECT
    t.team_name,
    COUNT(*) AS matches_played,
    SUM(a.earned) AS points,
    SUM(a.scored) AS goal_for,
    SUM(a.conceded) AS goal_against,
    SUM(a.scored) - SUM(a.conceded) AS goal_diff
FROM Appearances AS a
JOIN Teams AS t
    ON t.team_id = a.team_id
GROUP BY t.team_id, t.team_name
ORDER BY points DESC, goal_diff DESC, t.team_name;

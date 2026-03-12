-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Sum scores per player per group, find max scorer in each group

SELECT group_id, player_id
FROM (
    SELECT p.group_id, ps.player_id, ps.total_score,
           ROW_NUMBER() OVER (PARTITION BY p.group_id ORDER BY ps.total_score DESC, ps.player_id ASC) AS rn
    FROM (
        SELECT player_id, SUM(score) AS total_score
        FROM (
            SELECT first_player AS player_id, first_score AS score FROM Matches
            UNION ALL
            SELECT second_player AS player_id, second_score AS score FROM Matches
        ) scores
        GROUP BY player_id
    ) ps
    JOIN Players p ON ps.player_id = p.player_id
) ranked
WHERE rn = 1;

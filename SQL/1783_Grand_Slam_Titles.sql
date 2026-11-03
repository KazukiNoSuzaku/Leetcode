-- Author: Kaustav Ghosh
-- Problem: Grand Slam Titles
-- Approach: Each year's four winners sit in four separate columns, so the table has to be unpivoted before the titles can be counted: stacking the four columns with UNION ALL turns every championship win into its own row. Joining those rows to Players and grouping then counts titles per player, and because the join is an inner one the players who never won are dropped automatically, which is what the problem asks for.

SELECT
    p.player_id,
    p.player_name,
    COUNT(*) AS grand_slams_count
FROM Players AS p
JOIN (
    SELECT Wimbledon AS player_id FROM Championships
    UNION ALL
    SELECT Fr_open FROM Championships
    UNION ALL
    SELECT US_open FROM Championships
    UNION ALL
    SELECT Au_open FROM Championships
) AS wins
    ON wins.player_id = p.player_id
GROUP BY p.player_id, p.player_name;

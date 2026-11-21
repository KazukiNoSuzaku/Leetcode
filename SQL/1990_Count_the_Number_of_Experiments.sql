-- Author: Kaustav Ghosh
-- Problem: Count the Number of Experiments
-- Approach: Every platform and experiment pairing must appear even when no experiment was run, so the row set cannot come from the data; it has to be built. I spell out the three platforms and the three experiment names as literal rows and cross join them to get all nine pairings, then attach the recorded experiments with a left join so unmatched pairings survive. Counting the experiment_id column rather than the rows is what makes an empty pairing report zero instead of one, since COUNT over a column ignores the NULL that the left join leaves behind.

WITH Platforms AS (
    SELECT 'Android' AS platform
    UNION ALL SELECT 'IOS'
    UNION ALL SELECT 'Web'
),
Names AS (
    SELECT 'Reading' AS experiment_name
    UNION ALL SELECT 'Sports'
    UNION ALL SELECT 'Programming'
)
SELECT
    p.platform,
    n.experiment_name,
    COUNT(e.experiment_id) AS num_experiments
FROM Platforms AS p
CROSS JOIN Names AS n
LEFT JOIN Experiments AS e
    ON e.platform = p.platform
    AND e.experiment_name = n.experiment_name
GROUP BY p.platform, n.experiment_name;

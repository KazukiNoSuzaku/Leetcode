-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Group by (value - row_number) to find continuous ranges

SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM (
    SELECT log_id,
           log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
    FROM Logs
) t
GROUP BY grp;

-- Pivot the student geography table to show America, Asia, Europe columns.
-- Author: Kaustav Ghosh

SELECT
    MAX(CASE WHEN continent = 'America' THEN name END) AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rn
    FROM Student
) t
GROUP BY rn;

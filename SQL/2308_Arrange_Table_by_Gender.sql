-- Author: Kaustav Ghosh
-- Premium Problem
SELECT user_id, gender
FROM (
    SELECT
        user_id,
        gender,
        ROW_NUMBER() OVER (PARTITION BY gender ORDER BY user_id) AS rn,
        CASE gender WHEN 'female' THEN 1 WHEN 'other' THEN 2 WHEN 'male' THEN 3 END AS ord
    FROM Genders
) t
ORDER BY rn, ord;

-- Author: Kaustav Ghosh
-- 1076. Project Employees II
-- https://leetcode.com/problems/project-employees-ii/

SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) AS cnt
        FROM Project
        GROUP BY project_id
    ) t
);

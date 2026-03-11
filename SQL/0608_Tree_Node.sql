-- Given a table Tree, each row includes id and parent_id.
-- Write a query to output the type of each node.
-- Author: Kaustav Ghosh

SELECT id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;

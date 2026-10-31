-- Author: Kaustav Ghosh
-- Problem: Find the Subtasks That Did Not Execute
-- Approach: Tasks only stores how many subtasks exist, not their IDs, so the rows 1..subtasks_count have to be produced before they can be compared with Executed. A recursive term counts down from subtasks_count to 1 for every task, giving one row per subtask that should have run. Left joining that against Executed on both columns and keeping the rows with no match leaves exactly the subtasks that never executed.

WITH RECURSIVE Subtasks (task_id, subtask_id) AS (
    SELECT task_id, subtasks_count FROM Tasks
    UNION ALL
    SELECT task_id, subtask_id - 1 FROM Subtasks WHERE subtask_id > 1
)
SELECT s.task_id, s.subtask_id
FROM Subtasks AS s
LEFT JOIN Executed AS e
    ON e.task_id = s.task_id AND e.subtask_id = s.subtask_id
WHERE e.subtask_id IS NULL;

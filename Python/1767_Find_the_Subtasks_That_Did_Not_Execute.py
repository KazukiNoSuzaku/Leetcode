# Author: Kaustav Ghosh
# Premium problem - Find the Subtasks That Did Not Execute
# SQL: Use recursive CTE to generate all subtask ids, then LEFT JOIN
# WITH RECURSIVE Sub AS (
#     SELECT task_id, subtasks_count AS subtask_id FROM Tasks
#     UNION ALL
#     SELECT task_id, subtask_id - 1 FROM Sub WHERE subtask_id > 1
# )
# SELECT s.task_id, s.subtask_id
# FROM Sub s LEFT JOIN Executed e
# ON s.task_id = e.task_id AND s.subtask_id = e.subtask_id
# WHERE e.task_id IS NULL;

class Solution(object):
    pass

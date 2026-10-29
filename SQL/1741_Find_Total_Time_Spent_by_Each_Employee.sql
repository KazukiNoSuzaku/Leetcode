-- Author: Kaustav Ghosh
-- Problem: Find Total Time Spent by Each Employee
-- Approach: Each row already holds a complete visit, and the problem guarantees that visits on the same day never overlap, so the minutes can be added up directly with no interval merging: the time for one visit is the difference of its two stamps and a day's total is the sum of those differences. Grouping by the day together with the employee gives one row per employee per day, which is the requested granularity, and the day column has to be aliased since the output names it differently from the source column.

SELECT event_day AS day,
       emp_id,
       SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;

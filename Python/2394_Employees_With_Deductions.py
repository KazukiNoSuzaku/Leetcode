# Premium SQL problem
# Find employees whose total deduction hours exceed their allowed hours.
#
# SELECT e.employee_id
# FROM Employees e
# LEFT JOIN (
#     SELECT employee_id,
#            SUM(CEIL(TIMESTAMPDIFF(SECOND, in_time, out_time) / 3600.0)) AS worked
#     FROM Logs
#     GROUP BY employee_id
# ) l ON e.employee_id = l.employee_id
# WHERE COALESCE(l.worked, 0) < e.needed_hours

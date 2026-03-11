-- A university uses 2 data tables, Department and Student, to keep data.
-- Return all departments in the university and the count of students.
-- Author: Kaustav Ghosh

SELECT d.dept_name, COUNT(s.student_id) AS student_number
FROM Department d
LEFT JOIN Student s ON d.dept_id = s.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY student_number DESC, d.dept_name;

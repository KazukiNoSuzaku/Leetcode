# Author: Kaustav Ghosh
# SQL problem - Primary Department for Each Employee
# SELECT employee_id, department_id
# FROM Employee
# WHERE primary_flag = 'Y'
# UNION
# SELECT employee_id, department_id
# FROM Employee
# GROUP BY employee_id
# HAVING COUNT(*) = 1;

class Solution(object):
    pass

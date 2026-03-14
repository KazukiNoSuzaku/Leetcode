# Premium problem - Find the team size for each employee.
# Join employee_id with team_id to count team members.

# Author: Kaustav Ghosh

# SQL solution:
# SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size
# FROM Employee;

class Solution(object):
    pass

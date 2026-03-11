# Return total importance of an employee including all subordinates.

# Author: Kaustav Ghosh

class Solution(object):
    def getImportance(self, employees, id):
        emp_map = {e.id: e for e in employees}
        total = 0
        stack = [id]
        while stack:
            eid = stack.pop()
            emp = emp_map[eid]
            total += emp.importance
            stack.extend(emp.subordinates)
        return total

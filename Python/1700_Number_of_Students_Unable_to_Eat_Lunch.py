# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = Counter(students)
        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
            else:
                return count[0] + count[1]
        return 0

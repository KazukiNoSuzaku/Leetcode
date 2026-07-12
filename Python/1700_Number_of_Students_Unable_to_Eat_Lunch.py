# Author: Kaustav Ghosh
# Problem: Number of Students Unable to Eat Lunch
# Approach: Rotation makes order irrelevant, so just count preferences; a sandwich is eaten while someone still wants that type. The first sandwich nobody wants blocks all remaining students

from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        want = Counter(students)
        for i, s in enumerate(sandwiches):
            if want[s] == 0:
                return len(sandwiches) - i
            want[s] -= 1
        return 0

# Author: Kaustav Ghosh
# Problem: Number of Students Unable to Eat Lunch
# Approach: The students at the back of the queue are irrelevant to whether the front one eats, since anyone who does not want the top sandwich simply rejoins the queue without changing anything else; what matters is only whether any remaining student at all wants it. So the queue collapses to two tallies, one per preference, and the sandwiches are walked in order: each is taken if some student still prefers it, and the first sandwich nobody wants halts the process permanently. Whatever tallies remain at that point are the students left hungry.

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        wanting = [0, 0]
        for preference in students:
            wanting[preference] += 1
        for sandwich in sandwiches:
            if wanting[sandwich] == 0:
                break
            wanting[sandwich] -= 1
        return wanting[0] + wanting[1]

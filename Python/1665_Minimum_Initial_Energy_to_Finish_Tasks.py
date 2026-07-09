# Author: Kaustav Ghosh
# Problem: Minimum Initial Energy to Finish Tasks
# Approach: Do the tasks with the biggest (minimum - actual) buffer last; sweep keeping energy = max(energy + actual, minimum)

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        energy = 0
        for actual, minimum in tasks:
            energy = max(energy + actual, minimum)
        return energy

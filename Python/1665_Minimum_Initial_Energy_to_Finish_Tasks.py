# Author: Kaustav Ghosh
# Problem: Minimum Initial Energy to Finish Tasks
# Approach: Sort by (minimum - actual) ascending; sweeping energy = max(energy + actual, minimum) then yields the minimum start energy (it effectively schedules the largest-buffer tasks first)

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda t: t[1] - t[0])
        energy = 0
        for actual, minimum in tasks:
            energy = max(energy + actual, minimum)
        return energy

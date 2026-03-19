# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort by (minimum - actual) descending, i.e., surplus descending
        tasks.sort(key=lambda x: x[0] - x[1])
        energy = 0
        current = 0
        for actual, minimum in tasks:
            if current < minimum:
                energy += minimum - current
                current = minimum
            current -= actual
        return energy

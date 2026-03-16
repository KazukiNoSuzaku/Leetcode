# Author: Kaustav Ghosh
# Problem: Reducing Dishes
# Approach: Sort desc, greedily accumulate while running sum is positive

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        total = 0
        running_sum = 0
        for s in satisfaction:
            running_sum += s
            if running_sum <= 0:
                break
            total += running_sum
        return total

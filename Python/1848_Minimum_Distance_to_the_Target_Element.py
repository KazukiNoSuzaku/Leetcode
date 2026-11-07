# Author: Kaustav Ghosh
# Problem: Minimum Distance to the Target Element
# Approach: The target is guaranteed to be present, so the answer is simply the smallest distance from the start index to any position holding it. One pass over the array, taking the distance only at the matching positions, settles it without sorting or collecting the indices first.

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        return min(abs(index - start) for index, value in enumerate(nums) if value == target)

# Author: Kaustav Ghosh
# Problem: Minimum Distance to the Target Element
# Approach: Scan once and keep the smallest |i - start| among indices whose value equals target

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        best = float('inf')
        for i, x in enumerate(nums):
            if x == target:
                best = min(best, abs(i - start))
        return best

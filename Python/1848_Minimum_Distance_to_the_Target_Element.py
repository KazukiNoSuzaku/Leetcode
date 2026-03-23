# Author: Kaustav Ghosh
# Problem 1848: Minimum Distance to the Target Element

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                min_dist = min(min_dist, abs(i - start))
        return min_dist

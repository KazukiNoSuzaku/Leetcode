# Author: Kaustav Ghosh
# Problem: Minimum Value to Get Positive Step by Step Sum
# Approach: Track minimum prefix sum, start value = 1 - min_prefix

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_prefix = 0
        prefix = 0
        for n in nums:
            prefix += n
            min_prefix = min(min_prefix, prefix)
        return max(1, 1 - min_prefix)

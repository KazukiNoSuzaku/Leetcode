# Author: Kaustav Ghosh

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        min_sum = 0
        cur_max = 0
        cur_min = 0
        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        return max(max_sum, -min_sum)

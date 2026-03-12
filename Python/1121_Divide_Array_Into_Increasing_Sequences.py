# Author: Kaustav Ghosh
# 1121. Divide Array Into Increasing Sequences
# https://leetcode.com/problems/divide-array-into-increasing-sequences/

from collections import Counter

class Solution(object):
    def canDivideIntoSubsequences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        max_freq = max(Counter(nums).values())
        return max_freq * k <= len(nums)

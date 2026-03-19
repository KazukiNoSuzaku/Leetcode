# Author: Kaustav Ghosh
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = Counter(nums)
        ops = 0
        for num in list(count.keys()):
            comp = k - num
            if comp == num:
                ops += count[num] // 2
            elif comp in count:
                pairs = min(count[num], count[comp])
                ops += pairs
                count[num] -= pairs
                count[comp] -= pairs
        return ops

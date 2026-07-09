# Author: Kaustav Ghosh
# Problem: Max Number of K-Sum Pairs
# Approach: One pass with a counter of unpaired values; if the complement k-x is available, consume it as a pair, otherwise stash x

from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        available = Counter()
        operations = 0
        for x in nums:
            need = k - x
            if available[need] > 0:
                available[need] -= 1
                operations += 1
            else:
                available[x] += 1
        return operations

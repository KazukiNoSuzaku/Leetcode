# Author: Kaustav Ghosh
# Problem: Number of Good Pairs
# Approach: Count frequency of each number; pairs for k occurrences = k*(k-1)/2

from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(v * (v - 1) // 2 for v in Counter(nums).values())

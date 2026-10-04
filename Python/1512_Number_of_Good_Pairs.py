# Author: Kaustav Ghosh
# Problem: Number of Good Pairs
# Approach: A good pair is any two positions holding the same value, so count the occurrences of each value and add c * (c - 1) / 2 for every count

from collections import Counter


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(c * (c - 1) // 2 for c in Counter(nums).values())

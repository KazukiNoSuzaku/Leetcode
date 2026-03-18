# Author: Kaustav Ghosh
# Problem: 1569 - Number of Ways to Reorder Array to Get Same BST
# Approach: Combinatorics with recursion: C(n-1, left_size) * ways(left) * ways(right)

from math import comb
from functools import lru_cache

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def count_ways(arr):
            if len(arr) <= 1:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return comb(len(arr) - 1, len(left)) * count_ways(left) * count_ways(right)

        return (count_ways(nums) - 1) % MOD

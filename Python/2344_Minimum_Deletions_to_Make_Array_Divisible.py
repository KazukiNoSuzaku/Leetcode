# Author: Kaustav Ghosh
# 2344. Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
# Difficulty: Hard
#
# Find GCD of all elements in nums; then find the smallest element in divisors
# that is divisible by that GCD; count how many numElements must be deleted
# from the front of sorted nums before we find one that divides that divisors element.

from math import gcd
from functools import reduce

class Solution(object):
    def minOperations(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        g = reduce(gcd, nums)
        # find smallest divisor element divisible by g
        valid = [d for d in divisors if d % g == 0]
        if not valid:
            return -1
        target = min(valid)
        nums_sorted = sorted(nums)
        for i, n in enumerate(nums_sorted):
            if target % n == 0:
                return i
        return -1

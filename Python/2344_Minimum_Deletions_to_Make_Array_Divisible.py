# Author: Kaustav Ghosh
# Problem: Minimum Deletions to Make Array Divisible
# Approach: A number divides every element of numsDivide exactly when it divides their gcd. Sort nums and find the first value that divides the gcd; every element before it is smaller and must be deleted, so its index is the answer, or -1 if no value divides the gcd

from functools import reduce
from math import gcd


class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        g = reduce(gcd, numsDivide)
        for i, x in enumerate(sorted(nums)):
            if g % x == 0:
                return i
        return -1

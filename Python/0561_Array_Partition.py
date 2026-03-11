# Given an integer array nums of 2n integers, group these integers into n pairs such that
# the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Author: Kaustav Ghosh

class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

# Author: Kaustav Ghosh
# Problem: 2221. Find Triangular Sum of an Array
# URL: https://leetcode.com/problems/find-triangular-sum-of-an-array/
# Difficulty: Medium
#
# Approach:
# Repeatedly reduce the array by replacing each element with the sum of
# consecutive pairs modulo 10, until only one element remains.

class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        return nums[0]

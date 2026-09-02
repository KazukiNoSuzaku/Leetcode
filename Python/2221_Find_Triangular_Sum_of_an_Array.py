# Author: Kaustav Ghosh
# Problem: Find Triangular Sum of an Array
# Approach: Repeatedly replace the array with the digit-wise sums (mod 10) of adjacent pairs, shrinking the length by one each round, until a single value remains

class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        return nums[0]

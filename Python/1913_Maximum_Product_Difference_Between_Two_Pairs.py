# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

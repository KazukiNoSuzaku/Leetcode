# Find the maximum product of three numbers in an integer array.

# Author: Kaustav Ghosh

class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

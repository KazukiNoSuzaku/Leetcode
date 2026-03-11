# Given an integer array, negate any element k times to maximize the array sum.

# Author: Kaustav Ghosh

class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)

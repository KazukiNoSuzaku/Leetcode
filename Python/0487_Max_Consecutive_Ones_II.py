# Given a binary array nums, return the maximum number of consecutive 1's in the array
# if you can flip at most one 0.

# Author: Kaustav Ghosh

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        left = zeros = res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# Given a binary array, return the maximum number of consecutive 1s
# if you can flip at most k 0s.

# Author: Kaustav Ghosh

class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

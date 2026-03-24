# Author: Kaustav Ghosh
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def isStrictlyIncreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True

        for i in range(len(nums)):
            if isStrictlyIncreasing(nums[:i] + nums[i + 1:]):
                return True
        return False

# Author: Kaustav Ghosh
# Problem: Longest Subarray of 1's After Deleting One Element
# Approach: Sliding window with at most one zero budget

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeros = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            result = max(result, right - left)
        return result

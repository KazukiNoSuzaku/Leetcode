# Author: Kaustav Ghosh
# Problem: Largest Subarray Length K (Premium)
# Approach: Elements are distinct, so the largest length-k subarray is the one starting at the maximum element among the first n-k+1 positions

class Solution(object):
    def largestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        best_start = 0
        for i in range(1, len(nums) - k + 1):
            if nums[i] > nums[best_start]:
                best_start = i
        return nums[best_start:best_start + k]

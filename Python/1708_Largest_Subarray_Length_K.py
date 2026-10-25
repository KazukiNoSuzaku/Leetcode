# Author: Kaustav Ghosh
# Problem: Largest Subarray Length K
# Approach: Comparison is decided at the first differing position, and because the values are all distinct no two candidate subarrays can share a first element, so the largest one is simply whichever starts with the biggest value. Only starts up to the point where k elements still fit are eligible, so a single scan over that prefix locates the winner and the answer is the slice beginning there. Were the values allowed to repeat, as the follow-up asks, ties on the first element would have to be broken by comparing the subarrays onward from there.

class Solution(object):
    def largestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        last_start = len(nums) - k
        best = 0
        for i in range(1, last_start + 1):
            if nums[i] > nums[best]:
                best = i
        return nums[best:best + k]

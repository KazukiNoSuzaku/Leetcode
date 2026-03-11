# Find the contiguous subarray of length k with the maximum average.

# Author: Kaustav Ghosh

class Solution(object):
    def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        best = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            best = max(best, window)
        return best / float(k)

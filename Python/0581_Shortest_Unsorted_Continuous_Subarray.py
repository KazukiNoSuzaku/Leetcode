# Given an integer array nums, find the shortest subarray that if sorted makes the whole array sorted.
# Return its length. If already sorted return 0.

# Author: Kaustav Ghosh

class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        max_seen = float('-inf')
        right = -1
        for i in range(n):
            if nums[i] < max_seen: right = i
            max_seen = max(max_seen, nums[i])
        min_seen = float('inf')
        left = 0
        for i in range(n-1, -1, -1):
            if nums[i] > min_seen: left = i
            min_seen = min(min_seen, nums[i])
        return right - left + 1 if right != -1 else 0

# Author: Kaustav Ghosh
# Problem: Subarray With Elements Greater Than Varying Threshold
# Approach: A subarray of length k works when its minimum exceeds threshold / k. For each element, find the widest window where it is the minimum (bounded by the previous strictly smaller and next smaller-or-equal elements) with a monotonic stack; a longer window only lowers the bar, so if nums[i] * length > threshold that length is a valid answer

class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] >= x:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        for i, x in enumerate(nums):
            length = right[i] - left[i] - 1
            if x * length > threshold:
                return length
        return -1

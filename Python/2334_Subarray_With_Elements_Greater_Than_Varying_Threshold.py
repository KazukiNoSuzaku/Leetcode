# Author: Kaustav Ghosh
# 2334. Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
# Monotonic stack to find range where min > threshold/length

class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        # For each element as the minimum, find the widest subarray where it is minimum
        # using monotonic stack to find left and right boundaries
        left = [-1] * n   # index of nearest smaller element to the left
        right = [n] * n   # index of nearest smaller element to the right

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            # subarray length where nums[i] is minimum
            length = right[i] - left[i] - 1
            if nums[i] > threshold // length:
                # check exact condition: nums[i] > threshold / length
                if nums[i] * length > threshold:
                    return length

        return -1

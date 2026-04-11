# Author: Kaustav Ghosh
# Problem: 2289. Steps to Make Array Non-decreasing
# URL: https://leetcode.com/problems/steps-to-make-array-non-decreasing/
# Difficulty: Medium
#
# Approach:
# Use a stack tracking (value, steps_to_remove). Process right to left.
# For each element, it will eventually remove elements to its right that are
# smaller. The time for element i to eat all smaller elements to its right
# is the max of accumulated steps.

class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []  # (value, steps)
        result = 0
        for i in range(len(nums) - 1, -1, -1):
            steps = 0
            while stack and nums[i] > stack[-1][0]:
                steps = max(steps + 1, stack[-1][1])
                stack.pop()
            stack.append((nums[i], steps))
            result = max(result, steps)
        return result

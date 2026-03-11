# Given an array of n integers nums, a 132 pattern is a subsequence of three integers
# nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise return false.

# Author: Kaustav Ghosh

class Solution(object):
    def find132pattern(self, nums):
        stack = []
        k = float('-inf')  # the "2" in 132 pattern (third element)
        for n in reversed(nums):
            if n < k:
                return True
            while stack and stack[-1] < n:
                k = stack.pop()
            stack.append(n)
        return False

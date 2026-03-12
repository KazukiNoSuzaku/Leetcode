# Author: Kaustav Ghosh
# 1063. Number of Valid Subarrays
# https://leetcode.com/problems/number-of-valid-subarrays/

class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                result += i - stack.pop()
            stack.append(i)
        n = len(nums)
        while stack:
            result += n - stack.pop()
        return result

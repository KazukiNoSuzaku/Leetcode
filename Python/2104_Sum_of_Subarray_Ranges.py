# Author: Kaustav Ghosh
# https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = 0

        # Sum of subarray maximums - Sum of subarray minimums
        # For min contributions
        stack = []
        sum_min = 0
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] >= nums[i]):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                sum_min += nums[j] * left * right
            stack.append(i)

        # For max contributions
        stack = []
        sum_max = 0
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] <= nums[i]):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                sum_max += nums[j] * left * right
            stack.append(i)

        result = sum_max - sum_min
        return result

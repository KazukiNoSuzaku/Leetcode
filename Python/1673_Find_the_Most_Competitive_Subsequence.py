# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + (n - i) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack

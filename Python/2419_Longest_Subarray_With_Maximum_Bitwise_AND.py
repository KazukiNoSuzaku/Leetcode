# Author: Kaustav Ghosh
# Problem: Longest Subarray With Maximum Bitwise AND
# Approach: An AND never exceeds any of its operands, so the largest possible value is the array maximum and only subarrays made entirely of that value reach it. The answer is therefore the longest run of the maximum value

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = max(nums)
        best = run = 0
        for x in nums:
            run = run + 1 if x == target else 0
            best = max(best, run)
        return best

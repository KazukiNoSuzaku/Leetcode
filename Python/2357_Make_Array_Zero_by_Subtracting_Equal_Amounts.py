# Author: Kaustav Ghosh
# Problem: Make Array Zero by Subtracting Equal Amounts
# Approach: The best move is always to subtract the smallest positive value from every positive element, which zeroes exactly one distinct positive value and keeps the rest distinct, so the answer is the count of distinct non-zero values

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(set(nums) - {0})

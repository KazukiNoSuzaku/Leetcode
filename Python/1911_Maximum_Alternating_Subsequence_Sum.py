# Author: Kaustav Ghosh
# Problem: Maximum Alternating Subsequence Sum
# Approach: Track two running bests as we scan - the best alternating sum of a subsequence of even length (last element subtracted) and of odd length (last element added). Each new element either extends one parity or is skipped

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even, odd = 0, 0   # best sum for even-length / odd-length subsequences
        for x in nums:
            even, odd = max(even, odd - x), max(odd, even + x)
        return odd

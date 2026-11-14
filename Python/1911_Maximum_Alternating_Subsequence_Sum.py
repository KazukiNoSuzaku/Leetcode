# Author: Kaustav Ghosh
# Problem: Maximum Alternating Subsequence Sum
# Approach: Whether the next chosen element is added or subtracted depends only on how many have been chosen so far, so two running totals suffice: the best sum of a subsequence of even length and the best of odd length. Each element either extends the other total, flipping the parity, or is skipped, and both totals are updated together from their previous values so a single element cannot be used twice. The answer is the even-length total, since a subsequence ending on a subtracted element can always be improved by dropping it.

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        added = subtracted = 0
        for value in nums:
            added, subtracted = max(added, subtracted + value), max(subtracted, added - value)
        return added

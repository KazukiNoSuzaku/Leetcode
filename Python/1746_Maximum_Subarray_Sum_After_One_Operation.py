# Author: Kaustav Ghosh
# Problem: Maximum Subarray Sum After One Operation (Premium)
# Approach: Kadane with two states per index — best sum ending here with the square still unused, and with it already spent. Exactly one square is required, so the answer reads off the used state

class Solution(object):
    def maxSumAfterOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unused = 0   # best sum ending here, square not yet applied
        used = 0     # best sum ending here, square already applied
        best = float('-inf')

        for x in nums:
            new_unused = max(x, unused + x)
            new_used = max(x * x, unused + x * x, used + x)
            unused, used = new_unused, new_used
            best = max(best, used)

        return best

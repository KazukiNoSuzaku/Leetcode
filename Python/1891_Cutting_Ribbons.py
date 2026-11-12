# Author: Kaustav Ghosh
# Problem: Cutting Ribbons
# Approach: A ribbon of length L yields L divided by x pieces of length x with the remainder discarded, so for a candidate length the total number of pieces is a sum of integer divisions. That total only falls as the candidate grows, which makes the feasibility of a length monotone and the answer the largest length still producing k pieces, found by binary search between one and the longest ribbon. Nothing is ever cut; the counting is arithmetic, so each probe is one pass over the ribbons.

class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, max(ribbons)
        while low < high:
            middle = (low + high + 1) // 2
            if sum(length // middle for length in ribbons) >= k:
                low = middle
            else:
                high = middle - 1
        return low

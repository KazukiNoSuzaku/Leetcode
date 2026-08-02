# Author: Kaustav Ghosh
# Problem: Cutting Ribbons (Premium)
# Approach: The number of equal-length pieces decreases as the length grows, so binary search the largest length that still yields at least k pieces

class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        lo, hi = 1, max(ribbons)
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            pieces = sum(r // mid for r in ribbons)
            if pieces >= k:
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best

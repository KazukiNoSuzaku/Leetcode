# Author: Kaustav Ghosh
# Problem: Maximum Value at a Given Index in a Bounded Array
# Approach: Binary search the peak value; for a candidate the minimal total is a descending staircase on each side (clamped at 1), so check that its sum fits within maxSum

class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def side_sum(peak, length):
            # sum of peak-1, peak-2, ... over `length` cells, floored at 1
            if peak > length:
                # values peak-1 .. peak-length, all >= 1
                top = peak - 1
                bottom = peak - length
                return (top + bottom) * length // 2
            # values peak-1..1 then 1's for the rest
            descending = peak * (peak - 1) // 2
            return descending + (length - (peak - 1))

        def feasible(peak):
            left = side_sum(peak, index)
            right = side_sum(peak, n - index - 1)
            return peak + left + right <= maxSum

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

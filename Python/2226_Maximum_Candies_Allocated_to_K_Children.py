# Author: Kaustav Ghosh
# Problem: Maximum Candies Allocated to K Children
# Approach: The number of children that can each receive x candies is a non-increasing function of x, so binary search for the largest x where the total sub-piles of size x (sum of pile//x) still reaches k

class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k:
            return 0
        lo, hi = 1, max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if sum(c // mid for c in candies) >= k:
                lo = mid
            else:
                hi = mid - 1
        return lo

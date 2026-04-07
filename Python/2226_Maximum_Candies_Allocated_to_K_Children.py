# Author: Kaustav Ghosh
# Problem: 2226. Maximum Candies Allocated to K Children
# URL: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
# Difficulty: Medium
#
# Approach:
# Binary search on the number of candies per child. For a given amount x,
# each pile of size p can serve p // x children. Check if the total children
# served >= k. Find the maximum x satisfying this condition.

class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def can_give(x):
            if x == 0:
                return True
            return sum(c // x for c in candies) >= k

        lo, hi = 0, max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_give(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

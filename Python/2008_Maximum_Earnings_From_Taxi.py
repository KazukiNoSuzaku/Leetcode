# Author: Kaustav Ghosh
# Problem 2008: Maximum Earnings From Taxi

from collections import defaultdict

class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        # Group rides by end point
        rides_by_end = defaultdict(list)
        for s, e, t in rides:
            rides_by_end[e].append((s, e - s + t))

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for start, earn in rides_by_end[i]:
                dp[i] = max(dp[i], dp[start] + earn)
        return dp[n]

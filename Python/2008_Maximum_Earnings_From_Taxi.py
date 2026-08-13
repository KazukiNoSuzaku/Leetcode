# Author: Kaustav Ghosh
# Problem: Maximum Earnings From Taxi
# Approach: DP along the road. dp[i] is the best earnings reachable at point i. Either skip point i (dp[i-1]) or take a ride ending at i, adding dp[start] + (end-start+tip). Group rides by their end point

from collections import defaultdict

class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        by_end = defaultdict(list)
        for start, end, tip in rides:
            by_end[end].append((start, tip))

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for start, tip in by_end[i]:
                dp[i] = max(dp[i], dp[start] + (i - start + tip))
        return dp[n]

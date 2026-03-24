# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

import math

class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        n = len(dist)
        # dp[j] = minimum time * speed using j skips (keep in integer domain)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            new_dp = [INF] * (n + 1)
            for j in range(n + 1):
                if dp[j] == INF:
                    continue
                # Don't skip rest after road i (ceil up), unless last road
                if i < n - 1:
                    ceil_val = ((dp[j] + dist[i] + speed - 1) // speed) * speed
                    new_dp[j] = min(new_dp[j], ceil_val)
                else:
                    new_dp[j] = min(new_dp[j], dp[j] + dist[i])
                # Skip rest after road i
                if j + 1 <= n:
                    new_dp[j + 1] = min(new_dp[j + 1], dp[j] + dist[i])
            dp = new_dp
        for j in range(n + 1):
            if dp[j] <= hoursBefore * speed:
                return j
        return -1

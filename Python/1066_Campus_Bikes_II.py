# Author: Kaustav Ghosh
# 1066. Campus Bikes II
# https://leetcode.com/problems/campus-bikes-ii/

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        m, n = len(workers), len(bikes)
        # dp[mask] = min total dist when bikes in mask are assigned
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            w = bin(mask).count('1')
            if w >= m:
                continue
            wx, wy = workers[w]
            for b in range(n):
                if mask & (1 << b):
                    continue
                new_mask = mask | (1 << b)
                dist = abs(wx - bikes[b][0]) + abs(wy - bikes[b][1])
                dp[new_mask] = min(dp[new_mask], dp[mask] + dist)
        return min(dp[mask] for mask in range(1 << n) if bin(mask).count('1') == m)

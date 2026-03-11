# Find minimum number of moves to determine critical floor with k eggs and n floors.

# Author: Kaustav Ghosh

class Solution(object):
    def superEggDrop(self, k, n):
        m = 0
        dp = [0] * (k + 1)
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] += dp[i-1] + 1
        return m

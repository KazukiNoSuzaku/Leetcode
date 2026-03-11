# Find max number of 'A's on screen in n keystrokes using A, Ctrl+A, Ctrl+C, Ctrl+V.

# Author: Kaustav Ghosh

class Solution(object):
    def maxA(self, n):
        dp = list(range(n + 1))
        for i in range(3, n + 1):
            for j in range(i - 2, 0, -1):
                dp[i] = max(dp[i], dp[j - 1] * (i - j + 1))
        return dp[n]

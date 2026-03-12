# Author: Kaustav Ghosh
# DP[steps][pos] with position bounded by min(steps, arrLen-1)

class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        max_pos = min(steps // 2 + 1, arrLen)
        dp = [0] * max_pos
        dp[0] = 1

        for _ in range(steps):
            new_dp = [0] * max_pos
            for pos in range(max_pos):
                new_dp[pos] = dp[pos]
                if pos > 0:
                    new_dp[pos] = (new_dp[pos] + dp[pos - 1]) % MOD
                if pos < max_pos - 1:
                    new_dp[pos] = (new_dp[pos] + dp[pos + 1]) % MOD
            dp = new_dp
        return dp[0]

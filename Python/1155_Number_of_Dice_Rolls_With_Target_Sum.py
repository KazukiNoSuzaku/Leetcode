# Author: Kaustav Ghosh
# DP[dice][target] counting ways to reach target with given dice and faces

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(n):
            new_dp = [0] * (target + 1)
            for j in range(1, target + 1):
                for face in range(1, k + 1):
                    if j - face >= 0:
                        new_dp[j] = (new_dp[j] + dp[j - face]) % MOD
            dp = new_dp
        return dp[target]

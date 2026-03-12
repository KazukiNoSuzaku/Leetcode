# Author: Kaustav Ghosh
# DP tracking count of strings ending with each vowel

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # a=0, e=1, i=2, o=3, u=4
        dp = [1, 1, 1, 1, 1]
        for _ in range(n - 1):
            new_dp = [0] * 5
            new_dp[0] = (dp[1] + dp[2] + dp[4]) % MOD  # a follows e, i, u
            new_dp[1] = (dp[0] + dp[2]) % MOD            # e follows a, i
            new_dp[2] = (dp[1] + dp[3]) % MOD            # i follows e, o
            new_dp[3] = dp[2] % MOD                       # o follows i
            new_dp[4] = (dp[2] + dp[3]) % MOD            # u follows i, o
            dp = new_dp
        return sum(dp) % MOD

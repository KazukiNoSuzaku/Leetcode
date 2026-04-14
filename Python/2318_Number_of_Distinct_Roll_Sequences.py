# Author: Kaustav Ghosh
# 2318. Number of Distinct Roll Sequences
# DP with last two dice values and gcd constraint (consecutive rolls must have gcd=1)

from math import gcd

class Solution(object):
    def distinctSequences(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        if n == 1:
            return 6

        # dp[prev2][prev1] = number of sequences ending with (prev2, prev1)
        # dice values are 1-indexed (1 to 6), use 0 as "no previous"
        dp = [[0] * 7 for _ in range(7)]

        # Initialize for length 2
        for d1 in range(1, 7):
            for d2 in range(1, 7):
                if d1 != d2 and gcd(d1, d2) == 1:
                    dp[d1][d2] = 1

        for _ in range(n - 2):
            new_dp = [[0] * 7 for _ in range(7)]
            for prev2 in range(1, 7):
                for prev1 in range(1, 7):
                    if dp[prev2][prev1] == 0:
                        continue
                    for curr in range(1, 7):
                        if curr != prev1 and curr != prev2 and gcd(curr, prev1) == 1:
                            new_dp[prev1][curr] = (new_dp[prev1][curr] + dp[prev2][prev1]) % MOD
            dp = new_dp

        return sum(dp[i][j] for i in range(7) for j in range(7)) % MOD

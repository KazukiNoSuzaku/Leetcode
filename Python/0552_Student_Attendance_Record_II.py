# Given an integer n, return the number of strings of length n that will be rewarded.
# A string is eligible if: at most 1 'A' and no 3+ consecutive 'L's. Answer mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def checkRecord(self, n):
        MOD = 10**9 + 7
        # dp[a][l]: count of valid strings of current length with a A's and ending with l L's
        dp = [[0]*3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            ndp = [[0]*3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    if dp[a][l] == 0: continue
                    # Add 'P'
                    ndp[a][0] = (ndp[a][0] + dp[a][l]) % MOD
                    # Add 'A' (only if no A yet)
                    if a == 0:
                        ndp[1][0] = (ndp[1][0] + dp[a][l]) % MOD
                    # Add 'L' (only if < 2 consecutive L's)
                    if l < 2:
                        ndp[a][l+1] = (ndp[a][l+1] + dp[a][l]) % MOD
            dp = ndp
        return sum(dp[a][l] for a in range(2) for l in range(3)) % MOD

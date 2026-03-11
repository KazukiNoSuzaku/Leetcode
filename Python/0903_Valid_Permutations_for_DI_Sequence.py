# Count permutations of 0..n matching the DI sequence.

# Author: Kaustav Ghosh

class Solution(object):
    def numPermsDISequence(self, s):
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)
        for c in s:
            if c == 'D':
                dp = list(dp)
                for j in range(len(dp) - 2, -1, -1):
                    dp[j] = (dp[j] + dp[j+1]) % MOD
            else:
                for j in range(1, len(dp)):
                    dp[j] = (dp[j] + dp[j-1]) % MOD
            dp.pop()
        return dp[0]

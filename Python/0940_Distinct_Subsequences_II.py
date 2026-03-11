# Count distinct non-empty subsequences of a string mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        dp = {}
        total = 0
        for c in s:
            new = (total + 1) % MOD
            total = (total + 1 - dp.get(c, 0)) % MOD
            dp[c] = new
        return total

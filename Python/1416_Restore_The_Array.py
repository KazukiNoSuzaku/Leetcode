# Author: Kaustav Ghosh
# Problem: Restore The Array (Premium)
# Approach: DP counting ways to split string into valid numbers 1..k

class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                substr = s[j - 1:i]
                if substr[0] == '0':
                    continue
                num = int(substr)
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j - 1]) % MOD
        return dp[n]

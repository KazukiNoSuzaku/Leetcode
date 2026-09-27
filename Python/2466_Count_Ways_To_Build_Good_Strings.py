# Author: Kaustav Ghosh
# Problem: Count Ways To Build Good Strings
# Approach: Only the length built so far matters, since each step appends a fixed block of zeros or of ones. dp[length] counts the ways to reach that length, coming from length - zero and from length - one, and the answer sums the counts for every length in the allowed range

class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]
            if length >= one:
                dp[length] += dp[length - one]
            dp[length] %= MOD
        return sum(dp[low:high + 1]) % MOD

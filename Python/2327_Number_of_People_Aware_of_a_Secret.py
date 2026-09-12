# Author: Kaustav Ghosh
# Problem: Number of People Aware of a Secret
# Approach: Let dp[i] be the number of people who first learn the secret on day i. A person who learned on day j shares during days [j+delay, j+forget-1], so dp[i] sums dp[j] over that sharing window. Use prefix sums to update in O(1). At day n, everyone who learned after day n-forget still remembers; sum those

class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        pref = [0] * (n + 2)
        pref[1] = 0
        pref[2] = 1  # prefix sum of dp[1..1]
        for i in range(2, n + 1):
            lo = max(1, i - forget + 1)
            hi = i - delay
            if hi >= lo:
                dp[i] = (pref[hi + 1] - pref[lo]) % MOD
            pref[i + 1] = (pref[i] + dp[i]) % MOD

        # people who still know on day n: learned on day j with j > n - forget
        start = max(1, n - forget + 1)
        total = (pref[n + 1] - pref[start]) % MOD
        return total % MOD

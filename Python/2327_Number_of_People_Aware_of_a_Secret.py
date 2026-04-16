# Author: Kaustav Ghosh
# Problem: 2327. Number of People Aware of a Secret
# URL: https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# Difficulty: Medium
#
# Approach:
# dp[i] = number of people who first learn the secret on day i.
# A person who learns on day i can share from day i+delay to day i+forget-1.
# Use a prefix sum (sliding window) to efficiently compute how many new people
# learn the secret each day. On day n, sum up all who learned but haven't forgotten.

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

        # prefix[i] = sum of dp[1..i]
        prefix = [0] * (n + 2)
        prefix[1] = 1

        for i in range(2, n + 1):
            # People who can share on day i: learned on days [i-forget+1, i-delay]
            lo = max(1, i - forget + 1)
            hi = max(0, i - delay)
            if lo <= hi:
                dp[i] = (prefix[hi] - prefix[lo - 1]) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

        # People still alive on day n: learned on days [n-forget+1, n]
        lo = max(1, n - forget + 1)
        ans = (prefix[n] - prefix[lo - 1]) % MOD
        return ans

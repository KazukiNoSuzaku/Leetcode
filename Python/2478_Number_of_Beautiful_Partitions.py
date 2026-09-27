# Author: Kaustav Ghosh
# Problem: Number of Beautiful Partitions
# Approach: A piece is valid when it starts on a prime digit, ends on a non-prime digit and is long enough, so dp[j][i] counts ways to cut the first i digits into j pieces. For a fixed j the eligible cut points only grow as i advances, so a running total of dp[j - 1] over them replaces an inner loop and keeps the whole thing linear per piece count

class Solution(object):
    def beautifulPartitions(self, s, k, minLength):
        """
        :type s: str
        :type k: int
        :type minLength: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        primes = set('2357')
        n = len(s)
        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0
        dp = [1] + [0] * n
        for _ in range(k):
            nxt = [0] * (n + 1)
            running = 0
            for i in range(1, n + 1):
                start = i - minLength
                if start >= 0 and s[start] in primes:
                    running = (running + dp[start]) % MOD
                if s[i - 1] not in primes:
                    nxt[i] = running
            dp = nxt
        return dp[n]

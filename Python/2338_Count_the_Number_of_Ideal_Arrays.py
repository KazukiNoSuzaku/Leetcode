# Author: Kaustav Ghosh
# 2338. Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/
# Combinatorics + DP: count strictly increasing divisor chains, distribute positions with stars and bars

MOD = 10 ** 9 + 7

class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        # dp[v][k] = number of strictly increasing chains of length k ending at value v
        # where each element divides the next
        # Then for a chain of length k ending at v, we can place it in an array of length n
        # using C(n-1, k-1) ways (stars and bars: choose k-1 positions to increment)

        MAX_K = 14  # max chain length (2^14 > 10000)

        # Precompute dp: dp[v] = list of counts by chain length
        # dp[v][k] = number of chains of length k ending at v
        dp = [[0] * (MAX_K + 1) for _ in range(maxValue + 1)]
        for v in range(1, maxValue + 1):
            dp[v][1] = 1

        for k in range(1, MAX_K):
            for v in range(1, maxValue + 1):
                if dp[v][k] == 0:
                    continue
                # Extend chain: find multiples of v
                mult = 2 * v
                while mult <= maxValue:
                    dp[mult][k + 1] = (dp[mult][k + 1] + dp[v][k]) % MOD
                    mult += v

        # Precompute combinations C(n-1, k-1) for k from 1 to MAX_K
        # Using Pascal's triangle or direct computation
        # C(n-1, j) for j = 0..MAX_K-1
        comb = [0] * MAX_K
        comb[0] = 1
        # Compute C(n-1, j) iteratively
        val = 1
        for j in range(1, MAX_K):
            val = val * (n - j) % MOD * pow(j, MOD - 2, MOD) % MOD
            comb[j] = val

        ans = 0
        for v in range(1, maxValue + 1):
            for k in range(1, MAX_K + 1):
                if dp[v][k] == 0:
                    continue
                # C(n-1, k-1) ways to place chain of length k into array of length n
                ans = (ans + dp[v][k] * comb[k - 1]) % MOD

        return ans

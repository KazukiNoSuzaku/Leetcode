# Author: Kaustav Ghosh
# Problem: Count Ways to Make Array With Product
# Approach: Each prime's exponent is distributed independently across the n slots (stars and bars), so the answer is the product of C(e + n - 1, n - 1) over the prime factorization of k

from math import comb

class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        LIMIT = 10001

        # smallest prime factor sieve for fast factorization
        spf = list(range(LIMIT))
        i = 2
        while i * i < LIMIT:
            if spf[i] == i:
                for j in range(i * i, LIMIT, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        res = []
        for n, k in queries:
            ways = 1
            while k > 1:
                p = spf[k]
                e = 0
                while k % p == 0:
                    k //= p
                    e += 1
                ways = ways * comb(e + n - 1, n - 1) % MOD
            res.append(ways)
        return res

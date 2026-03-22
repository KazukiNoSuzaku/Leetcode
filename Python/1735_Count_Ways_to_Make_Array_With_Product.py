# Author: Kaustav Ghosh

class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        # Precompute factorials and inverse factorials
        MAX = 10013 + 14
        fact = [1] * MAX
        for i in range(1, MAX):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * MAX
        inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
        for i in range(MAX - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        def factorize(k):
            factors = {}
            d = 2
            while d * d <= k:
                while k % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    k //= d
                d += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors

        res = []
        for n, k in queries:
            factors = factorize(k)
            ways = 1
            for p, cnt in factors.items():
                # Distribute cnt copies among n slots: C(cnt + n - 1, n - 1)
                ways = ways * comb(cnt + n - 1, n - 1) % MOD
            res.append(ways)
        return res

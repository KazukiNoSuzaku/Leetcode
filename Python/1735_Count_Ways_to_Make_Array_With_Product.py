# Author: Kaustav Ghosh
# Problem: Count Ways to Make Array With Product
# Approach: Filling an array with a given product means distributing that product's prime factors among the slots, and the primes are independent of one another, so the count is the product over primes of the ways to spread that prime's exponent across the slots. Spreading e identical copies among n slots, with empty slots allowed, is the standard stars-and-bars count of e + n - 1 choose n - 1. Factorials are precomputed once up to the largest slot count plus a small margin for the exponents, and factorisation is made constant-time per prime by sieving the smallest prime factor up to the largest product, so each query costs only its number of distinct primes.

class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        top_n = max(n for n, _k in queries)
        top_k = max(k for _n, k in queries)

        # Smallest prime factor, so factorising k is one division per prime.
        smallest = list(range(top_k + 1))
        p = 2
        while p * p <= top_k:
            if smallest[p] == p:
                for multiple in range(p * p, top_k + 1, p):
                    if smallest[multiple] == multiple:
                        smallest[multiple] = p
            p += 1

        limit = top_n + 32
        factorial = [1] * (limit + 1)
        for i in range(1, limit + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        inverse = [1] * (limit + 1)
        inverse[limit] = pow(factorial[limit], MOD - 2, MOD)
        for i in range(limit, 0, -1):
            inverse[i - 1] = inverse[i] * i % MOD

        def choose(a, b):
            if b < 0 or b > a:
                return 0
            return factorial[a] * inverse[b] % MOD * inverse[a - b] % MOD

        answers = []
        for n, k in queries:
            ways = 1
            while k > 1:
                prime = smallest[k]
                exponent = 0
                while k % prime == 0:
                    k //= prime
                    exponent += 1
                ways = ways * choose(exponent + n - 1, n - 1) % MOD
            answers.append(ways)
        return answers

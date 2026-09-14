# Author: Kaustav Ghosh
# Problem: Count the Number of Ideal Arrays
# Approach: An ideal array ending at v is fixed by its ratios arr[0], arr[1]/arr[0], ..., arr[n-1]/arr[n-2]: n positive integers whose product is v. Each prime power p^e in v splits its e factors of p across the n slots independently in C(n - 1 + e, e) ways. Sum the product of these over every v up to maxValue, factoring with a smallest-prime-factor sieve and precomputed binomials (e is at most log2(maxValue))

class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        max_exp = maxValue.bit_length()
        comb = [1] * (max_exp + 1)
        for e in range(1, max_exp + 1):
            comb[e] = comb[e - 1] * (n - 1 + e) % MOD * pow(e, MOD - 2, MOD) % MOD
        spf = list(range(maxValue + 1))
        i = 2
        while i * i <= maxValue:
            if spf[i] == i:
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1
        total = 0
        for v in range(1, maxValue + 1):
            ways = 1
            x = v
            while x > 1:
                p = spf[x]
                e = 0
                while x % p == 0:
                    x //= p
                    e += 1
                ways = ways * comb[e] % MOD
            total = (total + ways) % MOD
        return total

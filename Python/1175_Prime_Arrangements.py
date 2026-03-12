# Author: Kaustav Ghosh
# Count primes up to n, multiply factorial(primes) * factorial(non-primes)

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def count_primes(n):
            if n < 2:
                return 0
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, n + 1, i):
                        sieve[j] = False
            return sum(sieve)

        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result

        primes = count_primes(n)
        return (factorial(primes) * factorial(n - primes)) % MOD

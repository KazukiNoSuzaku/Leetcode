class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        # Factorize each element and collect all distinct primes across the array.
        primes = set()
        for n in nums:
            d = 2
            while d * d <= n:
                if n % d == 0:
                    primes.add(d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                primes.add(n)
        return len(primes)

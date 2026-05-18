from bisect import bisect_left

class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        limit = 1001
        sieve = [True] * limit
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit, i):
                    sieve[j] = False
        primes = [i for i in range(limit) if sieve[i]]

        prev = 0
        for x in nums:
            # Find largest prime p < (x - prev) so that x - p > prev
            idx = bisect_left(primes, x - prev) - 1
            if idx >= 0:
                x -= primes[idx]
            if x <= prev:
                return False
            prev = x
        return True

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # Collect primes in [left, right]; consecutive primes always give the minimum gap.
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n < 4:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        primes = [p for p in range(left, right + 1) if is_prime(p)]
        if len(primes) < 2:
            return [-1, -1]
        best = min(range(1, len(primes)), key=lambda i: primes[i] - primes[i - 1])
        return [primes[best - 1], primes[best]]

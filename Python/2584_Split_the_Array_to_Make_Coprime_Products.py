from math import gcd

class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        # Track how many numbers contribute each prime factor; a split is valid
        # only when no prime spans both halves (open_primes == 0).
        prime_last = {}   # prime -> index of last occurrence
        open_primes = 0   # primes whose last occurrence is strictly right of current index

        def factorize(x, idx):
            nonlocal open_primes
            d = 2
            while d * d <= x:
                if x % d == 0:
                    if d not in prime_last:
                        open_primes += 1
                    prime_last[d] = idx
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                if x not in prime_last:
                    open_primes += 1
                prime_last[x] = idx

        for i, v in enumerate(nums):
            factorize(v, i)

        # Now sweep left to right; whenever we pass the last occurrence of a prime, close it.
        open_primes = 0
        prime_last2 = {}

        def factorize2(x, idx):
            nonlocal open_primes
            d = 2
            while d * d <= x:
                if x % d == 0:
                    if d not in prime_last2:
                        prime_last2[d] = prime_last[d]
                        open_primes += 1
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                if x not in prime_last2:
                    prime_last2[x] = prime_last[x]
                    open_primes += 1

        for i, v in enumerate(nums[:-1]):
            factorize2(v, i)
            # close primes whose last occurrence is exactly i
            for p in list(prime_last2):
                if prime_last2[p] == i:
                    open_primes -= 1
            if open_primes == 0:
                return i
        return -1

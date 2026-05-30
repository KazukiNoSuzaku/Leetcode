class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [[x, n - x] for x in range(2, n // 2 + 1) if sieve[x] and sieve[n - x]]

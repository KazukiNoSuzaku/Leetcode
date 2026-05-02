class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10 ** 9 + 7
        primes = set('2357')
        n = len(s)

        # A partition is valid only if s[0] is prime and s[-1] is non-prime
        if s[0] not in primes or s[-1] in primes:
            return 0

        # dp[i] = ways to form j complete parts using first i characters.
        # Rolling: prev = dp for j-1 parts, curr = dp for j parts.
        # Transition: curr[i] += prev[l] for all valid cut points l where:
        #   s[l] is prime (start of new part), s[i-1] is non-prime (end of part), i-l >= minLength
        prev = [0] * (n + 1)
        prev[0] = 1

        for _ in range(k):
            curr = [0] * (n + 1)
            prefix = 0  # prefix sum of prev[l] for valid starts s[l] in primes
            for i in range(1, n + 1):
                # Position l = i - minLength may become a valid start to accumulate
                l = i - minLength
                if l >= 0 and s[l] in primes:
                    prefix = (prefix + prev[l]) % MOD
                # Can only end part at i if s[i-1] is non-prime
                if s[i - 1] not in primes:
                    curr[i] = prefix
            prev = curr

        return prev[n]

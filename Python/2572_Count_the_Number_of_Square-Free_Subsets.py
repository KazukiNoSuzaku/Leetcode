class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        # Bitmask DP over 10 primes ≤ 30; skip numbers with a squared prime factor.
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_mask(x):
            mask = 0
            for i, p in enumerate(primes):
                if x % p == 0:
                    if x % (p * p) == 0:
                        return -1
                    mask |= (1 << i)
            return mask

        dp = [0] * (1 << 10)
        dp[0] = 1
        for x in nums:
            m = get_mask(x)
            if m < 0:
                continue
            for s in range((1 << 10) - 1, -1, -1):
                if dp[s] and not (s & m):
                    dp[s | m] = (dp[s | m] + dp[s]) % MOD
        return (sum(dp) - 1) % MOD

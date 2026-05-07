class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        # Premium: answer = 2^n - 2*(subsets with sum < k).
        # If total < 2k it's impossible; otherwise subtract bad partitions by symmetry.
        MOD = 10**9 + 7
        if sum(nums) < 2 * k:
            return 0
        n = len(nums)
        dp = [0] * k
        dp[0] = 1
        for x in nums:
            for s in range(k - 1, -1, -1):
                if s + x < k:
                    dp[s + x] = (dp[s + x] + dp[s]) % MOD
        less_than_k = sum(dp) % MOD
        return (pow(2, n, MOD) - 2 * less_than_k + MOD) % MOD

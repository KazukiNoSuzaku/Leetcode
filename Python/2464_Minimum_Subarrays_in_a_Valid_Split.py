from math import gcd

class Solution:
    def minimumSubarrays(self, nums: list[int]) -> int:
        # Premium: split into minimum subarrays where gcd(first, last) > 1 for each.
        # DP: dp[i] = min splits for nums[0..i].
        n = len(nums)
        INF = float('inf')
        dp = [INF] * n
        for i in range(n):
            for j in range(i, -1, -1):
                if gcd(nums[j], nums[i]) > 1:
                    prev = dp[j - 1] if j > 0 else 0
                    if prev + 1 < dp[i]:
                        dp[i] = prev + 1
        return dp[-1] if dp[-1] < INF else -1

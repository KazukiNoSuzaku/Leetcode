from collections import defaultdict

class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        # DP: dp[i] = min cost for nums[0..i-1]; trimmed = subarray length minus count of unique elements.
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            freq = defaultdict(int)
            unique = 0
            for j in range(i, n):
                x = nums[j]
                if freq[x] == 0:
                    unique += 1
                elif freq[x] == 1:
                    unique -= 1
                freq[x] += 1
                trimmed = (j - i + 1) - unique
                dp[j + 1] = min(dp[j + 1], dp[i] + k + trimmed)
        return dp[n]

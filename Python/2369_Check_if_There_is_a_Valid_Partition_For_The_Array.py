class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        # dp[i] = can we validly partition nums[:i]
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            if dp[i - 2] and nums[i - 1] == nums[i - 2]:
                dp[i] = True
            if i >= 3:
                a, b, c = nums[i - 3], nums[i - 2], nums[i - 1]
                if dp[i - 3] and (a == b == c or (c == b + 1 == a + 2)):
                    dp[i] = True
        return dp[n]

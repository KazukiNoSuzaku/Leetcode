from typing import List

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = [max(0, k - x) for x in nums]
        for i in range(3, len(nums)):
            dp[i] += min(dp[i - 3], dp[i - 2], dp[i - 1])
        return min(dp[-1], dp[-2], dp[-3])

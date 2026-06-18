from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        # dp[v] = length of longest consecutive sequence ending at value v
        # For each x, it can contribute as x (extends seq ending at x-1)
        # or as x+1 (extends seq ending at x).
        # Update dp[x+1] BEFORE dp[x] to avoid using this element twice.
        dp = {}
        for x in nums:
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1
        return max(dp.values())

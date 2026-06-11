from typing import List
import bisect

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0] * (n + 1)
        last = [0] * (n + 1)
        val = [0] * (n + 1)  # val[j] = prefix[j] + last[j], non-decreasing

        for i in range(1, n + 1):
            j = bisect.bisect_right(val, prefix[i], 0, i) - 1
            dp[i] = dp[j] + 1
            last[i] = prefix[i] - prefix[j]
            val[i] = prefix[i] + last[i]

        return dp[n]

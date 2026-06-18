from typing import List
from functools import lru_cache

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(target):
            @lru_cache(maxsize=None)
            def dp(i, j):
                if j - i < 1:
                    return 0
                res = 0
                if nums[i] + nums[i + 1] == target:
                    res = max(res, 1 + dp(i + 2, j))
                if nums[j - 1] + nums[j] == target:
                    res = max(res, 1 + dp(i, j - 2))
                if nums[i] + nums[j] == target:
                    res = max(res, 1 + dp(i + 1, j - 1))
                return res
            result = dp(0, n - 1)
            dp.cache_clear()
            return result

        return max(
            solve(nums[0] + nums[1]),
            solve(nums[-2] + nums[-1]),
            solve(nums[0] + nums[-1]),
        )

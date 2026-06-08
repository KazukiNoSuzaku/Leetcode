from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for m in range(1, n + 1):
            if nums[m - 1] < m and (m == n or nums[m] > m):
                res += 1
        return res

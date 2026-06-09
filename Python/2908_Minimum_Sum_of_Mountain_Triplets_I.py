from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        for j in range(1, n - 1):
            left_min = min((nums[i] for i in range(j) if nums[i] < nums[j]), default=float('inf'))
            right_min = min((nums[k] for k in range(j + 1, n) if nums[k] < nums[j]), default=float('inf'))
            if left_min < float('inf') and right_min < float('inf'):
                res = min(res, left_min + nums[j] + right_min)
        return -1 if res == float('inf') else res

from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        full_repeats = target // total
        remaining = target % total

        if remaining == 0:
            return full_repeats * n

        double = nums + nums
        min_len = float('inf')
        window_sum = left = 0
        for right in range(2 * n):
            window_sum += double[right]
            while window_sum > remaining:
                window_sum -= double[left]
                left += 1
            if window_sum == remaining:
                min_len = min(min_len, right - left + 1)

        return -1 if min_len == float('inf') else full_repeats * n + min_len

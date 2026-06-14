from typing import List
import itertools

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        def cost(l: int, r: int) -> int:
            mid = (l + r) // 2
            left_sum = nums[mid] * (mid - l) - (prefix[mid] - prefix[l])
            right_sum = (prefix[r + 1] - prefix[mid + 1]) - nums[mid] * (r - mid)
            return left_sum + right_sum

        ans = left = 0
        for right in range(n):
            while cost(left, right) > k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans

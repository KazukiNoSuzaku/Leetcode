from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur |= nums[j]
                if cur >= k:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != float('inf') else -1

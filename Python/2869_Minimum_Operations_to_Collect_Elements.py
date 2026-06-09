from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        needed = set(range(1, k + 1))
        for i in range(len(nums) - 1, -1, -1):
            needed.discard(nums[i])
            if not needed:
                return len(nums) - i
        return len(nums)

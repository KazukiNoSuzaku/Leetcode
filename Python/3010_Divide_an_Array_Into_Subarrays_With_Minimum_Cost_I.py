from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        rest = sorted(nums[1:])
        return first + rest[0] + rest[1]

from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for bit in range(32):
            if sum(1 for x in nums if x >> bit & 1) >= k:
                res |= 1 << bit
        return res

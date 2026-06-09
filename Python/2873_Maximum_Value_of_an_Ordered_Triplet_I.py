from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = max_i = max_diff = 0
        for x in nums:
            res = max(res, max_diff * x)
            max_diff = max(max_diff, max_i - x)
            max_i = max(max_i, x)
        return res

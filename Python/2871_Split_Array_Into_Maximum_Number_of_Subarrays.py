from typing import List
from functools import reduce
from operator import and_

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total = reduce(and_, nums)
        if total > 0:
            return 1
        res, cur = 0, ~0
        for x in nums:
            cur &= x
            if cur == 0:
                res += 1
                cur = ~0
        return res

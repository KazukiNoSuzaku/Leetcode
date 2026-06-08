from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        res = 0
        for x in nums:
            if x % modulo == k:
                prefix += 1
            need = (prefix % modulo - k + modulo) % modulo
            res += count[need]
            count[prefix % modulo] += 1
        return res

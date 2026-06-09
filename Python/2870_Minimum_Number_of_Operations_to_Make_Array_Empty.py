import math
from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for c in Counter(nums).values():
            if c == 1:
                return -1
        return sum(math.ceil(c / 3) for c in Counter(nums).values())

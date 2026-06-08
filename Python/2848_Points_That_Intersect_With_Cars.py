from typing import List
from itertools import accumulate

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        diff = [0] * 102
        for start, end in nums:
            diff[start] += 1
            diff[end + 1] -= 1
        return sum(1 for x in accumulate(diff) if x > 0)

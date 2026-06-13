from typing import List
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = Counter(x for row in grid for x in row)
        repeated = next(k for k, v in count.items() if v == 2)
        missing = next(k for k in range(1, n * n + 1) if count[k] == 0)
        return [repeated, missing]

from typing import List
from collections import Counter

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = max(Counter(nums).values())
        pairs = min(n // 2, n - max_count)
        return n - 2 * pairs

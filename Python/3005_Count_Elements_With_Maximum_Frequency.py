from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        return sum(v for v in cnt.values() if v == max_freq)

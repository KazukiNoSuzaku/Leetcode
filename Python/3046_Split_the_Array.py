from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # Possible iff no element appears more than twice
        # (each copy goes to one of the two halves; both halves need distinct elements)
        return max(Counter(nums).values()) <= 2

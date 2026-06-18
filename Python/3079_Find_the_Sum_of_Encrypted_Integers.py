from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            s = str(n)
            total += int(max(s) * len(s))
        return total

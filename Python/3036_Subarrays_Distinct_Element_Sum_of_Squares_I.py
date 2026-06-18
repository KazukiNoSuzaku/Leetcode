from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                total += len(s) * len(s)
        return total

from typing import List

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        last = {x: i for i, x in enumerate(nums)}
        cuts = end = 0
        for i, x in enumerate(nums):
            end = max(end, last[x])
            if i == end < len(nums) - 1:
                cuts += 1
        return pow(2, cuts, MOD)

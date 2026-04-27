import math

class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        # Can shift excess leftward; minimum possible max = max ceil(prefix_avg) over all prefixes
        ans = prefix = 0
        for i, x in enumerate(nums):
            prefix += x
            ans = max(ans, math.ceil(prefix / (i + 1)))
        return ans

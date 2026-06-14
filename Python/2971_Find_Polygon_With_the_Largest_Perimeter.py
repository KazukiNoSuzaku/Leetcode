from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix = 0
        ans = -1
        for x in nums:
            if x < prefix:
                ans = prefix + x
            prefix += x
        return ans

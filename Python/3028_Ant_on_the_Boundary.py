from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # Count how many times the running position sum returns to 0
        pos = 0
        count = 0
        for x in nums:
            pos += x
            if pos == 0:
                count += 1
        return count

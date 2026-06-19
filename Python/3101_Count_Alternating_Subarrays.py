from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = run = 1
        for i in range(1, len(nums)):
            run = run + 1 if nums[i] != nums[i - 1] else 1
            ans += run
        return ans

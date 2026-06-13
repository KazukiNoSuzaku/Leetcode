from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        ans = count = left = 0
        for right, x in enumerate(nums):
            if x == max_val:
                count += 1
            while count >= k:
                if nums[left] == max_val:
                    count -= 1
                left += 1
            ans += left
        return ans

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find length of sequential prefix (each element = previous + 1)
        k = 1
        while k < len(nums) and nums[k] == nums[k - 1] + 1:
            k += 1
        prefix_sum = sum(nums[:k])
        num_set = set(nums)
        ans = prefix_sum
        while ans in num_set:
            ans += 1
        return ans

import math

class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        limit = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= limit:
                limit = nums[i]
            else:
                parts = math.ceil(nums[i] / limit)
                ans += parts - 1
                limit = nums[i] // parts
        return ans

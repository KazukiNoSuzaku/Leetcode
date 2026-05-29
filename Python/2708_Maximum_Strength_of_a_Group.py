class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        res = 1
        i = 0
        while i + 1 < len(nums) and nums[i] < 0 and nums[i + 1] < 0:
            res *= nums[i] * nums[i + 1]
            i += 2
        while i < len(nums) and nums[i] <= 0:
            i += 1
        for j in range(i, len(nums)):
            res *= nums[j]
        return res if res != 1 else max(nums)
